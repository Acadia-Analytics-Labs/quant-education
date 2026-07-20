"""
Quant Education — an interactive, three-audiences learning app.

Every article can be read at three levels:
    🧒 Explain like I'm 11   — a comic-strip story
    📘 Standard              — the full article with charts, mermaid & ascii diagrams
    🎓 Jim Simons level      — rigorous math, derivations and references

Run:  streamlit run app.py
"""
from __future__ import annotations

import streamlit as st

from content_index import (
    ARTICLES,
    CATEGORIES,
    DIFFICULTY_COLOR,
    TIERS,
    articles_by_category,
    load_tier,
)
from renderer import render_markdown

st.set_page_config(page_title="Quant Education", page_icon="📈", layout="wide")

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
      .block-container { max-width: 960px; padding-top: 1.6rem; }
      .qe-hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #2563eb 100%);
        border-radius: 18px; padding: 26px 30px; color: #fff; margin-bottom: 8px;
      }
      .qe-hero h1 { margin: 0 0 6px; font-size: 30px; letter-spacing: -0.02em; }
      .qe-hero p  { margin: 0; opacity: 0.9; font-size: 15px; }
      .pill {
        display:inline-block; padding: 2px 10px; border-radius: 999px;
        font-size: 12px; font-weight: 700; color:#fff; margin-right:6px;
      }
      .tag {
        display:inline-block; padding: 2px 10px; border-radius: 999px;
        font-size: 12px; font-weight:600; color:#334155; background:#f1f5f9;
        margin: 0 6px 6px 0; border:1px solid #e2e8f0;
      }
      div[data-testid="stSidebarNav"] { display:none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
if "article_key" not in st.session_state:
    st.session_state.article_key = ARTICLES[0]["slug"]

with st.sidebar:
    st.markdown("### 📚 Quant Education")
    st.caption("by Acadia Analytics · read at your level")
    st.divider()

    grouped = articles_by_category()
    slug_to_article = {a["slug"]: a for a in ARTICLES}

    for cat_key, articles in grouped.items():
        label, emoji, _ = CATEGORIES[cat_key]
        st.markdown(f"**{emoji} {label}**")
        for a in articles:
            selected = st.session_state.article_key == a["slug"]
            if st.button(
                a["title"],
                key=f"nav_{a['slug']}",
                use_container_width=True,
                type="primary" if selected else "secondary",
            ):
                st.session_state.article_key = a["slug"]
                st.rerun()
        st.write("")

    st.divider()
    st.caption("Tip: switch the reading level with the tabs at the top of each article.")

article = slug_to_article[st.session_state.article_key]
cat_label, cat_emoji, _cat_blurb = CATEGORIES[article["category"]]

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="qe-hero">
      <h1>{article['title']}</h1>
      <p>{cat_emoji} {cat_label} &nbsp;·&nbsp; {article['blurb']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

diff = article["difficulty"]
tag_html = "".join(f'<span class="tag">{t}</span>' for t in article["tags"])
st.markdown(
    f'<span class="pill" style="background:{DIFFICULTY_COLOR.get(diff, "#64748b")}">'
    f"{diff}</span> {tag_html}",
    unsafe_allow_html=True,
)
st.write("")

# ---------------------------------------------------------------------------
# Tier selector + body
# ---------------------------------------------------------------------------
tier_labels = [TIERS[t][0] for t in TIERS]
tier_keys = list(TIERS.keys())
choice = st.radio(
    "Reading level",
    tier_labels,
    horizontal=True,
    label_visibility="collapsed",
)
tier = tier_keys[tier_labels.index(choice)]
st.caption(TIERS[tier][1])
st.divider()

body = load_tier(article, tier)
if body is None:
    st.info(
        f"The **{TIERS[tier][0]}** version of this article is coming soon. "
        "Try another reading level above."
    )
else:
    render_markdown(body)

st.divider()
st.caption(
    "Educational content only — not investment advice. "
    "© 2025 Acadia Analytics · enhanced local build."
)
