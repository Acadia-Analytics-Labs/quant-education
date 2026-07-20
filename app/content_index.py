"""content_index.py — the catalog of articles and how they map to content files."""
from __future__ import annotations

from pathlib import Path

CONTENT_DIR = Path(__file__).parent / "content"

# Display metadata for each category (folder name -> label / emoji / one-liner).
CATEGORIES = {
    "probability-statistics": ("Probability & Statistics", "🎲",
                               "The mathematics of uncertainty — the language of markets."),
    "quantitative-finance": ("Quantitative Finance", "📈",
                             "Systematic strategies that turn rules into returns."),
    "trading": ("Trading & Risk", "💼",
                "Sizing bets and surviving to trade another day."),
    "economics": ("Economics & Markets", "🏛️",
                  "The forces that move prices and generations."),
    "machine-learning": ("Machine Learning", "🤖",
                         "Teaching machines to find signal in the noise."),
}

TIERS = {
    "kid": ("🧒 Explain like I'm 11", "A comic-strip story with simple pictures."),
    "standard": ("📘 Standard", "The full article, with charts and diagrams."),
    "quant": ("🎓 Jim Simons level", "Rigorous math, derivations, and references."),
}

# Ordered so the sidebar reads like a learning path.
ARTICLES = [
    dict(category="probability-statistics", slug="bayesian-thinking",
         title="Probability & Bayesian Thinking", difficulty="Beginner",
         tags=["Bayesian", "Frequentist", "Uncertainty"],
         blurb="What probability even means — and two ways to think about it."),
    dict(category="probability-statistics", slug="conditional-probability",
         title="Conditional Probability & Bayes' Theorem", difficulty="Intermediate",
         tags=["Bayes", "Updating", "Decision Making"],
         blurb="How to update your beliefs when new information arrives."),
    dict(category="probability-statistics", slug="distributions",
         title="Probability Distributions in Trading", difficulty="Intermediate",
         tags=["Normal", "Fat Tails", "Risk"],
         blurb="Normal, binomial, Poisson, Pareto — and why tails matter."),
    dict(category="quantitative-finance", slug="trend-following",
         title="Trend Following Systems", difficulty="Intermediate",
         tags=["Systematic", "Turtles", "Position Sizing"],
         blurb="Lose small often, win big rarely — the Turtle Traders' edge."),
    dict(category="trading", slug="position-sizing",
         title="Position Sizing & Risk Management", difficulty="Beginner",
         tags=["Kelly", "Risk", "Portfolio Heat"],
         blurb="How much to bet — the most underrated skill in trading."),
    dict(category="trading", slug="esg-investing",
         title="Understanding ESG Investing", difficulty="Intermediate",
         tags=["ESG", "Sustainable", "Governance"],
         blurb="Environmental, Social & Governance factors in investing."),
    dict(category="economics", slug="day-trading-affordability-crisis",
         title="Day Trading & the Affordability Crisis", difficulty="Beginner",
         tags=["Day Trading", "Crypto", "Prediction Markets"],
         blurb="Why a priced-out generation is turning to high-risk trading."),
    dict(category="economics", slug="calculus-of-value",
         title="The Calculus of Value (Howard Marks)", difficulty="Intermediate",
         tags=["Valuation", "P/E", "Cycles"],
         blurb="Price vs. value, sentiment, and Howard Marks' INVESTCON."),
    dict(category="machine-learning", slug="intro-ml-trading",
         title="Introduction to Machine Learning in Trading", difficulty="Beginner",
         tags=["ML", "Features", "Backtesting"],
         blurb="How ML learns patterns — and the traps that fool beginners."),
]

DIFFICULTY_COLOR = {"Beginner": "#16a34a", "Intermediate": "#d97706", "Advanced": "#dc2626"}


def article_dir(article: dict) -> Path:
    return CONTENT_DIR / article["category"] / article["slug"]


def load_tier(article: dict, tier: str) -> str | None:
    path = article_dir(article) / f"{tier}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return None


def articles_by_category():
    grouped: dict[str, list[dict]] = {}
    for a in ARTICLES:
        grouped.setdefault(a["category"], []).append(a)
    return grouped
