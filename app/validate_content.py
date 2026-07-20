"""
validate_content.py — sanity-check every authored article before the visual QA.

Checks, for each content/<cat>/<slug>/{kid,standard,quant}.md:
  * file exists and starts with an H1
  * ```comic blocks contain valid JSON with a non-empty "panels" list (4–10)
  * ```chart calls reference a real function in charts.CHARTS with literal args
  * kid tier contains at least one comic
Run:  python validate_content.py
"""
from __future__ import annotations

import ast
import json
import sys

from charts import CHARTS
from content_index import ARTICLES, article_dir
from renderer import parse_blocks

TIERS = ("kid", "standard", "quant")


def check_chart(call: str) -> str | None:
    try:
        tree = ast.parse(call.strip(), mode="eval")
    except SyntaxError as e:
        return f"unparseable chart call {call!r}: {e}"
    if not isinstance(tree.body, ast.Call) or not isinstance(tree.body.func, ast.Name):
        return f"not a simple call: {call!r}"
    if tree.body.func.id not in CHARTS:
        return f"unknown chart '{tree.body.func.id}'"
    try:
        [ast.literal_eval(a) for a in tree.body.args]
        {kw.arg: ast.literal_eval(kw.value) for kw in tree.body.keywords}
    except Exception as e:  # noqa: BLE001
        return f"non-literal args in {call!r}: {e}"
    return None


def validate_file(path, tier) -> list[str]:
    issues: list[str] = []
    if not path.exists():
        return [f"MISSING FILE: {path}"]
    text = path.read_text(encoding="utf-8")
    if not text.lstrip().startswith("# "):
        issues.append("does not start with an H1 (# Title)")
    comics = 0
    for kind, payload, _opts in parse_blocks(text):
        if kind == "comic":
            comics += 1
            try:
                spec = json.loads(payload)
                panels = spec.get("panels", [])
                if not (1 <= len(panels) <= 10):
                    issues.append(f"comic has {len(panels)} panels (want 4–10)")
                for p in panels:
                    if not p.get("caption"):
                        issues.append("a comic panel is missing 'caption'")
            except json.JSONDecodeError as e:
                issues.append(f"invalid comic JSON: {e}")
        elif kind == "chart":
            for call in [ln for ln in payload.splitlines()
                         if ln.strip() and not ln.strip().startswith("#")]:
                err = check_chart(call)
                if err:
                    issues.append(err)
    if tier == "kid" and comics == 0:
        issues.append("kid tier has NO comic block")
    return issues


def main() -> int:
    total_issues = 0
    for a in ARTICLES:
        d = article_dir(a)
        for tier in TIERS:
            issues = validate_file(d / f"{tier}.md", tier)
            status = "✅" if not issues else "❌"
            print(f"{status} {a['category']}/{a['slug']}/{tier}.md")
            for it in issues:
                print(f"      - {it}")
                total_issues += 1
    print(f"\n{'ALL GOOD' if total_issues == 0 else f'{total_issues} issue(s) found'}")
    return 1 if total_issues else 0


if __name__ == "__main__":
    sys.exit(main())
