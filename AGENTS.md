# Agent Docs Maintainer 维护入口

- 先读 MIGRATION.md 确认建仓后的剩余工作，用户指定任务优先；不自动发布或切换日常安装。
- 插件位于仓库根目录，身份、版本和分发元数据只维护 plugin-catalog.json；manifest 与两端 marketplace 通过 python3 scripts/sync_plugin_metadata.py --write 生成。
- 文档技能只编辑 sources/project-docs/，运行 python3 scripts/build_project_docs.py --write 生成 skills/；安装资料必须自包含。
- 修改公开内容导致与 README 已有内容产生冲突时，仅同步修正 README.md 和 docs/README.cn.md 中受影响的已有内容，使其与公共事实对齐；无冲突不顺带修改。未经用户明确授权，不新增内容；删除任何 README 现有内容前须征得用户同意。
- 本次改动产生值得补充或调整的 README 内容时，主动沿用现有章节、格式和语气提出具体修改草案，说明位置与理由，并询问是否同步更新双语 README；确认前不写入，不仅等待用户提出要求。
- 解释性注释使用中文，代码标识符、日志和配置键使用英文。
- 修改后运行 README 中相关的现有检查；未经用户明确要求，不新增测试、不提交、不推送、不使用 subagents。
- 使用说明、历史设计或技能审查先读 [docs/index.md](docs/index.md)；活动状态只维护 MIGRATION.md。
