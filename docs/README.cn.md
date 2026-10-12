# Agent Docs Maintainer

[English](../README.md)

本仓库维护面向 Codex 和 Claude Code 的独立插件 `agent-docs-maintainer`。客户端安装验证与发布准备尚未完成，剩余工作见[迁移后待办](../MIGRATION.md)。

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

GitHub 仓库为 `Laxpud/agent-docs-maintainer`。下方命令说明预期安装流程，两端客户端的真实安装与执行尚未验证；若地址变更，同步修改 plugin-catalog.json 的 publisher.homepage、publisher.repository 和中英文安装命令，再重新生成元数据。

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

安装后新建任务或会话。最小提示词：

~~~text
Use $agent-docs-maintainer:project-docs-bootstrap to initialize a minimal documentation baseline for this repository.
~~~

## 维护

从[文档入口](index.md)查看从 Vibekits 迁入的使用说明、历史设计或审查资料。

plugin-catalog.json 是元数据维护入口；两端 manifest 和用于独立调试的 marketplace 均由脚本生成，指向本仓库根目录。从仓库根目录运行检查：

~~~bash
python3 scripts/build_project_docs.py
python3 scripts/sync_plugin_metadata.py --write
python3 scripts/sync_plugin_metadata.py
python3 scripts/check_codex_install.py --all
python3 scripts/check_markdown_links.py
~~~

以上只检查本地元数据和文件，不代表两端客户端安装或实际执行已通过。客户端安装验证与发布准备保留为 MIGRATION.md 中的待办；npx skills 分发尚未验证。

## 许可证

[MIT](../LICENSE)
