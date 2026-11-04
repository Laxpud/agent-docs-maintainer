"""生成 DSH 分发入口；技能正文和调用策略仍以 SKILL.md 为准。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from scripts.plugin_catalog import CatalogError, PluginCatalog, PluginSpec


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def skill_summary(root: Path, skill) -> dict[str, Any]:
    """解析仓库使用的单行标量 frontmatter；未知 YAML 写法拒绝生成，不放宽调用权限。

    这里不是通用 YAML 解析器。当前技能只使用名称、描述和两个调用开关；
    若以后引入折行、嵌套 metadata 或转义语法，应先扩展构建器再更新源格式。
    """
    relative = Path(skill.path.as_posix()) / "SKILL.md"
    text = (root / relative).read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        raise CatalogError(f"{relative}: missing frontmatter")
    fields: dict[str, Any] = {}
    for line in match[1].splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        entry = re.fullmatch(r"([a-zA-Z-]+):\s+(.+)", line)
        if not entry or entry[1] in fields:
            raise CatalogError(f"{relative}: unsupported or duplicate frontmatter: {line!r}")
        key, value = entry.groups()
        if key in {"disable-model-invocation", "user-invocable"}:
            if value not in {"true", "false"}:
                raise CatalogError(f"{relative}: {key} must be true or false")
            fields[key] = value == "true"
        elif key in {"name", "description", "whenToUse"}:
            # 双引号只接受 JSON 字符串子集；单引号遵循 YAML 的双写转义。
            if value.startswith('"'):
                value = json.loads(value)
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1].replace("''", "'")
            elif value.startswith(tuple("|>!&*{[")) or " #" in value or ": " in value:
                raise CatalogError(f"{relative}: quote this scalar as a JSON string: {key}")
            if not isinstance(value, str) or not value.strip():
                raise CatalogError(f"{relative}: {key} must be a non-empty string")
            fields[key] = value
        else:
            raise CatalogError(f"{relative}: unsupported frontmatter key: {key}")
    if fields.get("name") != skill.id or not fields.get("description"):
        raise CatalogError(f"{relative}: name must match catalog and description is required")
    summary = {
        "name": skill.id,
        "description": fields["description"],
        "invocation": {
            "modelInvocable": not fields.get("disable-model-invocation", False),
            "userInvocable": fields.get("user-invocable", True),
        },
        "file": relative.as_posix(),
        # 加载正文前核对头部，防止本地编辑后沿用已过期的权限或名称。
        "frontmatter": match[0],
    }
    if "whenToUse" in fields:
        summary["whenToUse"] = fields["whenToUse"]
    return summary


def generated_dsh_files(root: Path, catalog: PluginCatalog, plugin: PluginSpec) -> dict[Path, str]:
    """生成可独立安装的 npm 包、Cordis patch、展示资源及按需加载索引。"""
    adapter = plugin.dsh
    manifest = {
        "name": adapter["packageName"],
        "version": plugin.version,
        "description": adapter["description"],
        "type": "module",
        "license": catalog.publisher["license"],
        "author": {"name": catalog.publisher["name"], "url": catalog.publisher["url"]},
        "homepage": catalog.publisher["homepage"],
        "repository": {"type": "git", "url": catalog.publisher["repository"]},
        "keywords": list(plugin.keywords),
        "engines": {"node": ">=22", "dsh": adapter["engine"]},
        "exports": {
            ".": "./dsh/index.js",
            "./locale/*.json": "./dsh/locale/*.json",
            "./icon": "./dsh/icon.svg",
        },
        "files": [
            "dsh/", "cordis.patch.yml", "skills/", "docs/", "MIGRATION.md",
            "!**/__pycache__/**", "!**/*.pyc",
        ],
        "dsh": {"bundle": {"patch": "./cordis.patch.yml"}},
    }
    # JSON 是 YAML 子集；序列化字符串而非拼接裸值，避免包名或标点改变 patch 语义。
    patch = (
        "# 由 scripts/sync_plugin_metadata.py 生成；仅新增本插件，不替换 preset。\n"
        "- insert:\n"
        f"    - id: {json.dumps(plugin.id)}\n"
        f"      name: {json.dumps(adapter['packageName'])}\n"
    )
    result = {
        Path("package.json"): _json(manifest),
        Path("cordis.patch.yml"): patch,
        Path("dsh/skills.json"): _json([skill_summary(root, skill) for skill in plugin.skills]),
    }
    for locale, suffix in (("en", ""), ("zh", "Zh")):
        result[Path(f"dsh/locale/{locale}.json")] = _json({"meta": {
            "title": adapter[f"title{suffix}"],
            "description": adapter[f"description{suffix}"],
        }})
    return result
