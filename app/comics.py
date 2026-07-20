"""
comics.py — turn a compact JSON ``comic`` spec into a meme-style comic strip.

Authors write a fenced ```comic block containing JSON like:

    {
      "title": "The $100 Lemonade Stand",
      "panels": [
        {"emoji": "🍋", "caption": "You have $100 for a lemonade stand.", "bubble": "Let's go!"},
        {"emoji": "💸", "caption": "You spend ALL $100 on lemons. One bad day = broke."}
      ]
    }

The renderer lays the panels out as numbered comic cards (4–10 frames), so
non-artists can produce a consistent, friendly, meme-like story for kids.
"""
from __future__ import annotations

import html
import json

# A cheerful, high-contrast palette cycled across the panels.
_PALETTES = [
    ("#FDE68A", "#F59E0B", "#7C2D12"),  # amber
    ("#BBF7D0", "#22C55E", "#14532D"),  # green
    ("#BFDBFE", "#3B82F6", "#1E3A8A"),  # blue
    ("#FBCFE8", "#EC4899", "#831843"),  # pink
    ("#DDD6FE", "#8B5CF6", "#4C1D95"),  # violet
    ("#FED7AA", "#FB923C", "#7C2D12"),  # orange
    ("#A5F3FC", "#06B6D4", "#164E63"),  # cyan
    ("#FECACA", "#EF4444", "#7F1D1D"),  # red
    ("#D9F99D", "#84CC16", "#365314"),  # lime
    ("#E5E7EB", "#6B7280", "#111827"),  # gray
]


def _columns(n: int) -> int:
    if n <= 3:
        return n
    if n == 4:
        return 2
    return 3


def render_comic(spec: dict) -> tuple[str, int]:
    """Return (html, iframe_height_px) for a comic spec dict."""
    title = spec.get("title", "")
    panels = spec.get("panels", [])
    n = len(panels)
    cols = _columns(n) or 1
    rows = (n + cols - 1) // cols

    cards = []
    for i, panel in enumerate(panels):
        base, accent, ink = _PALETTES[i % len(_PALETTES)]
        emoji = panel.get("emoji", "✨")
        caption = html.escape(panel.get("caption", ""))
        bubble = panel.get("bubble")
        bubble_html = ""
        if bubble:
            bubble_html = (
                f'<div class="bubble" style="border-color:{accent};color:{ink}">'
                f"{html.escape(bubble)}</div>"
            )
        cards.append(
            f"""
            <div class="panel" style="background:linear-gradient(160deg,{base},#ffffff 85%);border-color:{accent}">
              <div class="badge" style="background:{accent}">{i + 1}</div>
              <div class="emoji">{emoji}</div>
              {bubble_html}
              <div class="caption" style="color:{ink}">{caption}</div>
            </div>
            """
        )

    title_html = (
        f'<div class="comic-title">🎬 {html.escape(title)}</div>' if title else ""
    )

    doc = f"""
    <div class="comic-wrap">
      {title_html}
      <div class="grid" style="grid-template-columns:repeat({cols}, 1fr)">
        {''.join(cards)}
      </div>
    </div>
    <style>
      * {{ box-sizing: border-box; }}
      .comic-wrap {{
        font-family: -apple-system, "Segoe UI", Roboto, sans-serif;
        padding: 4px 2px 10px;
      }}
      .comic-title {{
        display: inline-block; font-size: 19px; font-weight: 800;
        margin: 4px 0 16px; padding: 7px 15px; border-radius: 11px;
        background: #0f172a; color: #ffffff; letter-spacing: -0.01em;
        box-shadow: 0 3px 8px rgba(15,23,42,0.18);
      }}
      .grid {{ display: grid; gap: 14px; }}
      .panel {{
        position: relative; border: 3px solid; border-radius: 18px;
        padding: 18px 16px 16px; min-height: 190px;
        display: flex; flex-direction: column; align-items: center;
        text-align: center; box-shadow: 0 6px 16px rgba(15,23,42,0.10);
      }}
      .badge {{
        position: absolute; top: -12px; left: -12px; width: 30px; height: 30px;
        border-radius: 50%; color: #fff; font-weight: 800; font-size: 15px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
      }}
      .emoji {{ font-size: 54px; line-height: 1; margin: 6px 0 10px; }}
      .bubble {{
        background: #fff; border: 2px solid; border-radius: 14px;
        padding: 6px 12px; font-size: 14px; font-weight: 700; margin-bottom: 10px;
        max-width: 95%; box-shadow: 0 2px 5px rgba(0,0,0,0.08);
      }}
      .caption {{ font-size: 15px; line-height: 1.35; font-weight: 600; }}
    </style>
    """
    height = 62 * bool(title) + rows * 250 + 20
    return doc, height


def render_comic_from_text(text: str) -> tuple[str, int]:
    """Parse the raw text inside a ```comic fence and render it."""
    try:
        spec = json.loads(text)
    except json.JSONDecodeError as exc:  # pragma: no cover - surfaced in UI
        msg = html.escape(f"Invalid comic JSON: {exc}")
        return f'<pre style="color:#b91c1c">{msg}</pre>', 120
    return render_comic(spec)
