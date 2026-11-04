# Agent Docs Maintainer

[简体中文](docs/README.cn.md)

Minimal project progress and plan/spec storage, with shared document rules for explicit README, planning, architecture, guidance, and organization workflows.

This repository maintains the standalone plugin `agent-docs-maintainer` for Codex, Claude Code, and DSH.

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

Install from `Laxpud/agent-docs-maintainer` using the commands below.

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

DSH, in a terminal; replace `<profile>` with your profile name:

~~~bash
dsh plugin --profile <profile> add github:Laxpud/agent-docs-maintainer
~~~

## Maintenance

See the [documentation index](docs/index.md) for usage, design, and review material.

plugin-catalog.json is the metadata source. Generated Codex/Claude manifests, local authoring marketplaces, and DSH manifest, patch, locales, and skill index point to this repository root. Run these commands from the repository root:

~~~bash
python3 scripts/build_project_docs.py
python3 scripts/sync_plugin_metadata.py --write
python3 scripts/sync_plugin_metadata.py
python3 scripts/check_codex_install.py --all
python3 scripts/check_markdown_links.py
node --check dsh/index.js
npm pack --dry-run --ignore-scripts
~~~

## License

[MIT](LICENSE)
