"""
renderer.py — a small block renderer for the Quant Education app.

Markdown is rendered by Streamlit (LaTeX via KaTeX works out of the box).
Four fenced block types get special handling:

    ```mermaid            -> Mermaid.js diagram (flowcharts, trees, timelines)
    ```comic              -> JSON comic strip (see comics.py)
    ```chart              -> a call into charts.CHARTS, shown with st.pyplot
    ```ascii              -> monospace ASCII diagram

Any other fenced block (```python, ```text, …) stays inline in the markdown.
"""
from __future__ import annotations

import ast
import html
import re

import streamlit as st
import streamlit.components.v1 as components

from charts import CHARTS
from comics import render_comic_from_text

SPECIAL = {"mermaid", "comic", "chart", "ascii"}


# Operators that mark a ``$…`` span as maths when they follow the leading number
# *across a space*: ``$1 - 2\varepsilon$``, ``$0 < 1$``.  A real price puts an
# ordinary word there instead ("$100 to enter").
_MATH_AFTER_SPACE = set("+-*/^_=<>\\(){}[]|&~")


def _closes_on_same_line(md: str, start: int) -> bool:
    """True if an unescaped ``$`` appears before the end of this line."""
    i, n = start, len(md)
    while i < n and md[i] != "\n":
        if md[i] == "$" and (i == 0 or md[i - 1] != "\\"):
            return True
        i += 1
    return False


def escape_currency(md: str) -> str:
    """Escape currency dollar signs (``$100``) so KaTeX doesn't eat them as math.

    A ``$`` that precedes a digit is money unless the span looks like maths and
    closes on the same line.  It looks like maths when the number runs straight
    into another token (``$0.5$``, ``$2N$``, ``$1/(1-c)$``) or is followed,
    across a space, by an operator (``$1 - 2\\varepsilon$``).  A real price is
    followed by ordinary prose instead ("$100 to enter", "near $125K in
    October").  ``$$`` display math and already-escaped ``\\$`` are left
    untouched.  This lets authors write real math and real dollar amounts in the
    same paragraph without hand-escaping every price.
    """
    out: list[str] = []
    i, n = 0, len(md)
    while i < n:
        ch = md[i]
        if ch == "$":
            if i > 0 and md[i - 1] == "\\":  # already escaped
                out.append(ch); i += 1; continue
            if i + 1 < n and md[i + 1] == "$":  # display math $$
                out.append("$$"); i += 2; continue
            if i + 1 < n and md[i + 1].isdigit():  # candidate currency
                j = i + 1
                while j < n and (md[j].isdigit() or md[j] in ",."):
                    j += 1
                if j < n and md[j] == "$":  # inline math like $0.5$
                    out.append(md[i:j]); i = j; continue
                # The number runs into another token ($2N$, $1/(1-c)$), or an
                # operator follows across a space ($1 - 2\varepsilon$).
                k = j
                while k < n and md[k] == " ":
                    k += 1
                looks_mathy = (j < n and md[j] != " ") or (
                    k < n and md[k] in _MATH_AFTER_SPACE
                )
                if looks_mathy and _closes_on_same_line(md, j):
                    out.append(ch); i += 1; continue  # inline math
                out.append("\\$"); i += 1; continue  # currency
        out.append(ch)
        i += 1
    return "".join(out)


def _parse_info(info: str):
    """Split a fence info string like 'mermaid height=520' -> (lang, opts)."""
    parts = info.split()
    lang = parts[0].lower() if parts else ""
    opts = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            opts[k] = v
    return lang, opts


def parse_blocks(text: str):
    lines = text.split("\n")
    blocks: list[tuple] = []
    buf: list[str] = []

    def flush_md():
        nonlocal buf
        if any(ln.strip() for ln in buf):
            blocks.append(("markdown", "\n".join(buf), {}))
        buf = []

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith("```"):
            lang, opts = _parse_info(stripped[3:].strip())
            # find closing fence
            j = i + 1
            body: list[str] = []
            while j < len(lines) and not lines[j].lstrip().startswith("```"):
                body.append(lines[j])
                j += 1
            if lang in SPECIAL:
                flush_md()
                blocks.append((lang, "\n".join(body), opts))
            else:
                # keep normal code block verbatim inside the markdown stream
                buf.append(line)
                buf.extend(body)
                if j < len(lines):
                    buf.append(lines[j])
            i = j + 1
            continue
        buf.append(line)
        i += 1
    flush_md()
    return blocks


def _render_mermaid(code: str, opts: dict):
    n_lines = max(1, len([ln for ln in code.splitlines() if ln.strip()]))
    height = int(opts.get("height", min(900, max(220, 140 + 30 * n_lines))))
    safe = html.escape(code)
    doc = f"""
    <div style="background:#ffffff;border-radius:12px;padding:10px 6px;">
      <pre class="mermaid" style="text-align:center;">{safe}</pre>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
    <script>
      mermaid.initialize({{ startOnLoad: true, theme: 'neutral',
                            securityLevel: 'loose',
                            flowchart: {{ curve: 'basis', useMaxWidth: true }} }});
    </script>
    """
    components.html(doc, height=height, scrolling=True)


def _render_comic(code: str):
    doc, height = render_comic_from_text(code)
    components.html(doc, height=height, scrolling=False)


def _eval_chart(call: str):
    """Safely evaluate a `func(a=1, b=2)` call against the CHARTS registry."""
    call = call.strip()
    if not call:
        return None, "empty chart call"
    tree = ast.parse(call, mode="eval")
    if not isinstance(tree.body, ast.Call) or not isinstance(tree.body.func, ast.Name):
        return None, f"not a simple function call: {call!r}"
    name = tree.body.func.id
    if name not in CHARTS:
        return None, f"unknown chart '{name}'. Available: {', '.join(sorted(CHARTS))}"
    args = [ast.literal_eval(a) for a in tree.body.args]
    kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in tree.body.keywords}
    return CHARTS[name](*args, **kwargs), None


def _render_chart(code: str):
    # allow multiple chart calls in one block (one per non-empty line)
    for call in [ln for ln in code.splitlines() if ln.strip() and not ln.strip().startswith("#")]:
        try:
            fig, err = _eval_chart(call)
            if err:
                st.warning(f"⚠️ {err}")
                continue
            st.pyplot(fig, use_container_width=True)
            import matplotlib.pyplot as plt

            plt.close(fig)
        except Exception as exc:  # pragma: no cover - surfaced in UI
            st.error(f"Chart error in `{call}`: {exc}")


def _render_ascii(code: str):
    st.code(code, language="text")


def render_markdown(text: str):
    """Render a full article body (mixed markdown + special blocks)."""
    for kind, payload, opts in parse_blocks(text):
        if kind == "markdown":
            # Content escapes currency as ``\$`` (see SPEC.md), so every bare ``$``
            # is a genuine LaTeX delimiter — render as-is and let KaTeX handle it.
            st.markdown(payload, unsafe_allow_html=False)
        elif kind == "mermaid":
            _render_mermaid(payload, opts)
        elif kind == "comic":
            _render_comic(payload)
        elif kind == "chart":
            _render_chart(payload)
        elif kind == "ascii":
            _render_ascii(payload)
