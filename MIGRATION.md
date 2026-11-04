# Agent Docs Maintainer 迁移后待办

- 核对调用配置与外部校验器的兼容限制，完成两端隔离安装检查。
- Vibekits 两端市场已引用本独立仓库；发布版本、日常安装更新和 `npx skills` 支持仍分别验证。
- [x] 从 Vibekits 迁入使用说明、改造设计、ADR 与历史审查，入口见 [docs/index.md](docs/index.md)。

- [x] 已增加 DSH bundle、保留调用策略的按需技能 provider、中英文展示资源及自包含分发入口；安装入口见 [README](README.md)。
- [x] 本轮通过元数据同步、原有安装文件检查、Markdown 链接、JavaScript 语法与模块导入、SVG XML、npm 打包清单和 diff 空白检查；这些检查不证明 DSH 实际挂载。
- [ ] DSH 实际安装、挂载、显式／自动调用、卸载与图标渲染待授权验证；本轮仅修改仓库，不切换当前 profile。
