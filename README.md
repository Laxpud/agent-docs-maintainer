# Agent Docs Maintainer

[简体中文](docs/README.cn.md)

Minimal project progress and plan/spec storage, with shared document rules for explicit README, planning, architecture, guidance, and organization workflows.

This repository maintains the standalone plugin named `agent-docs-maintainer` for Codex and Claude Code. Client installation validation and release preparation remain pending; see [remaining migration work](MIGRATION.md).

## Skills

- [project-docs-bootstrap](skills/project-docs-bootstrap/SKILL.md)
- [project-docs-refactor](skills/project-docs-refactor/SKILL.md)
- [project-docs-readme](skills/project-docs-readme/SKILL.md)
- [project-docs-planning](skills/project-docs-planning/SKILL.md)
- [project-docs-architecture](skills/project-docs-architecture/SKILL.md)
- [project-docs-guidance](skills/project-docs-guidance/SKILL.md)
- [project-docs-progress](skills/project-docs-progress/SKILL.md)

Edit sources/project-docs/ and run python3 scripts/build_project_docs.py --write. Root skills/ is generated; each installed skill includes its own referenced resources.

## Installation

The GitHub repository is `Laxpud/agent-docs-maintainer`. The commands below describe the intended installation flow; actual installation and execution in both clients remain unverified. If the repository address changes, update publisher.homepage and publisher.repository in plugin-catalog.json and both README files, then regenerate metadata with --write.

Codex, in a terminal:

~~~bash
codex plugin marketplace add Laxpud/agent-docs-maintainer
~~~

Then open the plugin picker and install `agent-docs-maintainer`:

~~~text
/plugins
~~~

Claude Code, in the client input area:

~~~text
/plugin marketplace add Laxpud/agent-docs-maintainer
/plugin install agent-docs-maintainer@laxpud-agent-docs-maintainer
~~~

Start a new task or session after installation. Example prompt:

~~~text
Use $agent-docs-maintainer:project-docs-bootstrap to initialize a minimal documentation baseline for this repository.
~~~

## Maintenance

plugin-catalog.json is the metadata source. Generated manifests and local authoring marketplaces point to this repository root. Run these commands from the repository root:

~~~bash
python3 scripts/build_project_docs.py
python3 scripts/sync_plugin_metadata.py --write
python3 scripts/sync_plugin_metadata.py
python3 scripts/check_codex_install.py --all
python3 scripts/check_markdown_links.py
~~~

These checks verify local metadata and files; they do not prove installation or execution in either client. Client installation validation and release preparation remain pending in MIGRATION.md. Direct npx skills distribution is not verified.

## License

[MIT](LICENSE)
