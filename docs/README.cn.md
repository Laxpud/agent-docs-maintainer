# Agent Docs Maintainer

[English](../README.md)

本仓库维护面向 Codex、Claude Code 和 DSH 的独立插件 `agent-docs-maintainer`。

## 技能

- [project-docs-bootstrap](../skills/project-docs-bootstrap/SKILL.md)
- [project-docs-refactor](../skills/project-docs-refactor/SKILL.md)
- [project-docs-readme](../skills/project-docs-readme/SKILL.md)
- [project-docs-planning](../skills/project-docs-planning/SKILL.md)
- [project-docs-architecture](../skills/project-docs-architecture/SKILL.md)
- [project-docs-guidance](../skills/project-docs-guidance/SKILL.md)
- [project-docs-progress](../skills/project-docs-progress/SKILL.md)

维护源位于 sources/project-docs/；修改后运行 python3 scripts/build_project_docs.py --write。根目录 skills/ 为生成物，每个安装技能包含自身引用的资料。

## 安装

使用下方命令从 `Laxpud/agent-docs-maintainer` 安装。

在终端添加 Codex marketplace：

~~~bash
codex plugin marketplace add Laxpud/agent-docs-maintainer
~~~

在 Codex 输入区打开列表，安装 `agent-docs-maintainer`：

~~~text
/plugins
~~~

在 Claude Code 输入区依次执行：

~~~text
/plugin marketplace add Laxpud/agent-docs-maintainer
/plugin install agent-docs-maintainer@laxpud-agent-docs-maintainer
~~~

在终端安装 DSH 插件，将 `<profile>` 替换为使用的 profile 名称：

~~~bash
dsh plugin --profile <profile> add github:Laxpud/agent-docs-maintainer
~~~

## 维护

从[文档入口](index.md)查看使用说明、设计和审查资料。

plugin-catalog.json 是元数据维护入口；Codex／Claude manifest、独立调试 marketplace 和 DSH manifest、patch、locale、技能索引均由脚本生成，指向本仓库根目录。从仓库根目录运行检查：

~~~bash
python3 scripts/build_project_docs.py
python3 scripts/sync_plugin_metadata.py --write
python3 scripts/sync_plugin_metadata.py
python3 scripts/check_codex_install.py --all
python3 scripts/check_markdown_links.py
node --check dsh/index.js
npm pack --dry-run --ignore-scripts
~~~

## 许可证

[MIT](../LICENSE)
