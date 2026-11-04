import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import manifest from '../package.json' with { type: 'json' };
import summaries from './skills.json' with { type: 'json' };

export const name = manifest.name;
export const inject = ['skills'];

/**
 * 向宿主注册包内技能目录；不替换 preset，不注册工具，也不启动调度器。
 * 摘要来自构建索引，正文仅在用户或模型实际加载技能时读取。
 * @param {object} ctx - 提供 skills 服务和 effect 生命周期的 Cordis 上下文。
 */
export function apply(ctx) {
  // 1. 以安装包而不是工作目录定位资源，目录安装和 tarball 安装使用同一套路径。
  const entries = new Map(summaries.map(({ file, frontmatter, ...summary }) => {
    const url = new URL(`../${file}`, import.meta.url);
    const candidate = {
      ...summary,
      path: fileURLToPath(url),
      resourceBase: { kind: 'directory', path: fileURLToPath(new URL('./', url)) },
      source: 'bundled',
      provider: name,
      rank: 300,
      locator: summary.name,
    };
    return [summary.name, { candidate, url, frontmatter }];
  }));

  // 2. effect 同时持有 provider 的移除器；禁用或卸载后目录和缓存由宿主一并失效。
  ctx.effect(() => ctx.skills.registerProvider(control => ({
    name,
    async list({ signal } = {}) {
      control.signal.throwIfAborted();
      signal?.throwIfAborted();
      return [...entries.values()].map(entry => entry.candidate);
    },
    async get(candidate, { signal } = {}) {
      control.signal.throwIfAborted();
      signal?.throwIfAborted();
      const entry = entries.get(candidate.locator);
      if (!entry || entry.candidate.name !== candidate.name) return undefined;
      // 3. 读取可取消；头部漂移时拒绝加载，避免旧目录悄悄放宽新的调用限制。
      const text = (await readFile(entry.url, {
        encoding: 'utf8',
        signal: signal ? AbortSignal.any([control.signal, signal]) : control.signal,
      })).replace(/\r\n/g, '\n');
      if (!text.startsWith(entry.frontmatter)) {
        throw new Error(`Skill metadata changed: ${entry.candidate.name}; regenerate metadata and reload the bundle`);
      }
      const { rank, locator, ...definition } = entry.candidate;
      return { ...definition, content: text.slice(entry.frontmatter.length).trim() };
    },
  })));
}
