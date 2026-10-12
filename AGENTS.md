# Agent Docs Maintainer 维护入口

- 先读 MIGRATION.md 确认建仓后的剩余工作，用户指定任务优先；不自动发布或切换日常安装。
- 插件位于仓库根目录，身份、版本和分发元数据只维护 plugin-catalog.json；manifest 与两端 marketplace 通过 python3 scripts/sync_plugin_metadata.py --write 生成。
- 文档技能只编辑 sources/project-docs/，运行 python3 scripts/build_project_docs.py --write 生成 skills/；安装资料必须自包含。
- 修改对外说明时保持 README.md 和 docs/README.cn.md 对齐；解释性注释使用中文，代码标识符、日志和配置键使用英文。
- 修改后运行 README 中相关的现有检查；未经用户明确要求，不新增测试、不提交、不推送、不使用 subagents。
- 使用说明、历史设计或技能审查先读 [docs/index.md](docs/index.md)；活动状态只维护 MIGRATION.md。
