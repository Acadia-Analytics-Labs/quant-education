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

    # --- Probability & Statistics ---
    dict(category="probability-statistics", slug="expected-value",
         title="Expected Value (E[X])", difficulty="Beginner",
         tags=["Expected Value", "Edge", "Decisions"],
         blurb="The average outcome — the number every strategy lives or dies by."),
    dict(category="probability-statistics", slug="monte-carlo-risk-forecasting",
         title="Monte Carlo Risk Forecasting", difficulty="Intermediate",
         tags=["Monte Carlo", "Simulation", "VaR"],
         blurb="Simulate thousands of possible futures to see the range of outcomes."),
    dict(category="probability-statistics", slug="state-space-kalman",
         title="State-Space Models & Kalman Filters", difficulty="Advanced",
         tags=["Kalman", "Filtering", "Signal"],
         blurb="Track a hidden 'true' value through noisy market data."),

    # --- Quantitative Finance ---
    dict(category="quantitative-finance", slug="intro-quant-trading",
         title="Introduction to Quantitative Trading", difficulty="Beginner",
         tags=["Systematic", "Backtesting", "Edge"],
         blurb="What quants actually do — turning ideas into tested rules."),
    dict(category="quantitative-finance", slug="intro-dcf",
         title="The Discounted Cash Flow Model", difficulty="Intermediate",
         tags=["DCF", "Valuation", "WACC"],
         blurb="Value a company by discounting its future cash back to today."),
    dict(category="quantitative-finance", slug="hmm-market-regimes",
         title="Hidden Markov Models for Market Regimes", difficulty="Advanced",
         tags=["HMM", "Regimes", "Bull/Bear"],
         blurb="Detect the hidden bull, bear, and choppy states behind prices."),

    # --- Machine Learning ---
    dict(category="machine-learning", slug="model-types",
         title="Machine Learning Model Types", difficulty="Beginner",
         tags=["Supervised", "Unsupervised", "Models"],
         blurb="A map of the main model families and when to reach for each."),
    dict(category="machine-learning", slug="linear-and-logistic-regression",
         title="Linear & Logistic Regression", difficulty="Intermediate",
         tags=["Regression", "Classification", "OLS"],
         blurb="Two workhorses: predict a number, or predict a yes/no."),
    dict(category="machine-learning", slug="neural-networks-foundations",
         title="Neural Networks in Trading (Foundations)", difficulty="Intermediate",
         tags=["Neural Nets", "Activation", "Deep Learning"],
         blurb="How layered 'neurons' learn nonlinear patterns."),
    dict(category="machine-learning", slug="curse-of-dimensionality",
         title="The Curse of Dimensionality", difficulty="Advanced",
         tags=["Dimensions", "Overfitting", "Features"],
         blurb="Why more features can make a model worse, not better."),
    dict(category="machine-learning", slug="manifold-hypothesis",
         title="The Manifold Hypothesis", difficulty="Advanced",
         tags=["Manifolds", "Structure", "Deep Learning"],
         blurb="Why high-dimensional data secretly lives on a low-dimensional surface."),
    dict(category="machine-learning", slug="rl-trading-agents-foundations",
         title="Reinforcement-Learning Trading Agents", difficulty="Advanced",
         tags=["Reinforcement Learning", "Agents", "Reward"],
         blurb="Agents that learn to trade by trial, error, and reward."),

    # --- Trading & Risk ---
    dict(category="trading", slug="thorp-edge-principle",
         title="The Thorp Edge Principle", difficulty="Beginner",
         tags=["Edge", "Frequency", "Kelly"],
         blurb="Ed Thorp's lesson: make more small edge-bets, not bigger ones."),
    dict(category="trading", slug="etfs",
         title="Exchange-Traded Funds (ETFs)", difficulty="Beginner",
         tags=["ETFs", "Diversification", "Index"],
         blurb="Buy a whole basket of assets in a single ticker."),
    dict(category="trading", slug="backtesting-basics",
         title="Backtesting Basics", difficulty="Beginner",
         tags=["Backtesting", "Overfitting", "Validation"],
         blurb="Test a strategy on history — without fooling yourself."),
    dict(category="trading", slug="orders-slippage-costs",
         title="Orders, Slippage & Transaction Costs", difficulty="Beginner",
         tags=["Orders", "Slippage", "Costs"],
         blurb="The hidden frictions that quietly eat your returns."),
    dict(category="trading", slug="indicator-cheatsheet",
         title="Trading Indicators Cheat Sheet", difficulty="Beginner",
         tags=["Indicators", "RSI", "MACD"],
         blurb="A quick tour of the most common technical indicators."),
    dict(category="trading", slug="volatility",
         title="Measuring Market Risk", difficulty="Beginner",
         tags=["Volatility", "VIX", "Beta"],
         blurb="Volatility, the VIX and beta — three lenses on market risk."),

    # --- Economics & Markets ---
    dict(category="economics", slug="fundamental-vs-technical-analysis",
         title="Fundamental vs Technical Analysis", difficulty="Beginner",
         tags=["Fundamental", "Technical", "Analysis"],
         blurb="Two lenses for a trade: the business vs the chart."),
    dict(category="economics", slug="macro-econ-intro",
         title="Introduction to Macroeconomics", difficulty="Beginner",
         tags=["Macro", "GDP", "Inflation"],
         blurb="The big-picture forces: growth, inflation, and jobs."),
    dict(category="economics", slug="micro-econ-intro",
         title="Introduction to Microeconomics", difficulty="Beginner",
         tags=["Micro", "Supply & Demand", "Utility"],
         blurb="How people and firms make choices under scarcity."),
    dict(category="economics", slug="monetary-economics",
         title="Monetary Economics", difficulty="Intermediate",
         tags=["Money", "Central Banks", "Rates"],
         blurb="How central banks and the money supply steer the economy."),
    dict(category="economics", slug="understanding-treasury-rates",
         title="Understanding Treasury Rates", difficulty="Intermediate",
         tags=["Treasuries", "Yield Curve", "Rates"],
         blurb="What bond yields and the yield curve signal about the economy."),
    dict(category="economics", slug="tips",
         title="Treasury Inflation-Protected Securities (TIPS)", difficulty="Intermediate",
         tags=["TIPS", "Inflation", "Bonds"],
         blurb="Bonds that adjust with inflation to protect real returns."),
    dict(category="economics", slug="sovereign-wealth-funds",
         title="Sovereign Wealth Funds", difficulty="Intermediate",
         tags=["SWF", "Reserves", "Investing"],
         blurb="How nations invest their surplus wealth."),
    dict(category="economics", slug="economic-theories",
         title="The History of Economic Thought", difficulty="Intermediate",
         tags=["Economics", "Theory", "Schools"],
         blurb="From Smith to Keynes — the big ideas that shaped markets."),
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
