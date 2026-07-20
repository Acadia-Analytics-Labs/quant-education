# Quant Education — interactive three-audiences app

An interactive Streamlit app that wraps the `articles/` content and lets you read
every topic at **three levels**:

| Tier | Audience | What you get |
|------|----------|--------------|
| 🧒 **Explain like I'm 11** | a curious kid | a colorful **comic strip** + everyday analogies |
| 📘 **Standard** | a motivated adult / undergrad | the full article with **charts, Mermaid diagrams & ASCII sketches** |
| 🎓 **Jim Simons level** | a PhD quant | **rigorous math, derivations/proofs & references** |

## Run it

```bash
cd app
./run.sh                 # uses the pyenv "aa_research" env (streamlit + matplotlib + numpy)
# or:  streamlit run app.py
```

Then open http://localhost:8501 (or the port it prints). Pick an article in the
sidebar, switch the reading level with the tabs at the top.

## What's inside

```
app/
  app.py              # Streamlit UI: sidebar learning-path nav + tier selector
  renderer.py         # block renderer: markdown+LaTeX / mermaid / comic / chart / ascii
                      #   + currency-vs-LaTeX $ disambiguation
  charts.py           # 22 reproducible matplotlib charts (the CHARTS registry)
  comics.py           # compact JSON comic-spec -> meme-style comic strip
  content_index.py    # the catalog: categories, articles, difficulty, tags
  content/<cat>/<slug>/{kid,standard,quant}.md   # the 3-tier content
  SPEC.md             # authoring spec (how the content is written)
  validate_content.py # sanity-checks comics + chart references
```

## Authoring

Content is plain Markdown + LaTeX with four special fenced blocks:
`` ```comic `` (JSON), `` ```mermaid ``, `` ```chart `` (calls into `charts.py`),
and `` ```ascii ``. See [SPEC.md](SPEC.md) for the full grammar and the chart catalog.
Run `python validate_content.py` to check all articles.

*Educational content only — not investment advice.*
