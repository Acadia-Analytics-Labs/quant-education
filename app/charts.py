"""
charts.py — reproducible matplotlib chart catalog for the Quant Education app.

Content authors reference a chart from markdown with a fenced block:

    ```chart
    kelly_curve(p=0.6, b=1)
    ```

The renderer evaluates the call against ``CHARTS`` (below) and displays the
returned Figure with ``st.pyplot``.  Every function is deterministic (seeded)
so the app renders identically on every run.  Pure numpy + stdlib math — no
scipy dependency.
"""
from __future__ import annotations

import math

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------------
# House style
# ----------------------------------------------------------------------------
INK = "#0f172a"
GRID = "#e2e8f0"
BLUE = "#2563eb"
GREEN = "#16a34a"
RED = "#dc2626"
AMBER = "#d97706"
VIOLET = "#7c3aed"
SLATE = "#64748b"
CYAN = "#0891b2"

plt.rcParams.update(
    {
        "figure.dpi": 130,
        "savefig.dpi": 130,
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.labelcolor": INK,
        "axes.edgecolor": "#cbd5e1",
        "axes.labelweight": "medium",
        "text.color": INK,
        "xtick.color": SLATE,
        "ytick.color": SLATE,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.autolayout": True,
    }
)


def _fig(w=7.0, h=4.1):
    fig, ax = plt.subplots(figsize=(w, h))
    return fig, ax


# ----------------------------------------------------------------------------
# Probability distributions
# ----------------------------------------------------------------------------
def _normal_pdf(x, mu=0.0, sd=1.0):
    return np.exp(-0.5 * ((x - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))


def _t_pdf(x, nu=2.0):
    c = math.gamma((nu + 1) / 2) / (math.sqrt(nu * math.pi) * math.gamma(nu / 2))
    return c * (1 + x**2 / nu) ** (-(nu + 1) / 2)


def normal_vs_fat_tail(nu=2.0):
    """Normal bell vs a fat-tailed (Student-t) distribution: crashes live in the tails."""
    fig, ax = _fig()
    x = np.linspace(-6, 6, 800)
    ax.plot(x, _normal_pdf(x), color=BLUE, lw=2.4, label="Normal (textbook)")
    ax.plot(x, _t_pdf(x, nu), color=RED, lw=2.4, label=f"Fat-tailed (Student-t, ν={nu:g})")
    tail = x[np.abs(x) >= 3]
    ax.fill_between(tail, 0, _t_pdf(tail, nu), color=RED, alpha=0.25)
    ax.axvline(3, color=SLATE, ls=":", lw=1)
    ax.axvline(-3, color=SLATE, ls=":", lw=1)
    ax.annotate(
        "extreme events\n(crashes / melt-ups)\nfar more likely",
        xy=(4.1, _t_pdf(4.1, nu)), xytext=(3.2, 0.12),
        fontsize=9, color=RED, fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=RED),
    )
    ax.set_title("Why 'once-in-a-century' crashes happen every decade")
    ax.set_xlabel("Standardized return (σ)")
    ax.set_ylabel("Probability density")
    ax.set_ylim(0, 0.45)
    ax.legend(frameon=False)
    return fig


def binomial_pmf(n=10, p=0.55):
    """Binomial distribution of wins out of n trades."""
    fig, ax = _fig()
    ks = np.arange(0, n + 1)
    pmf = np.array([math.comb(n, int(k)) * p**k * (1 - p) ** (n - k) for k in ks])
    colors = [GREEN if k >= n * p else BLUE for k in ks]
    ax.bar(ks, pmf, color=colors, edgecolor="white", width=0.85)
    ax.axvline(n * p, color=RED, ls="--", lw=1.6, label=f"expected wins = {n*p:g}")
    ax.set_title(f"Wins out of {n} trades  (win rate p = {p:g})")
    ax.set_xlabel("Number of winning trades")
    ax.set_ylabel("Probability")
    ax.legend(frameon=False)
    return fig


def poisson_pmf(lam=3.0, kmax=12):
    """Poisson distribution: number of events (e.g. news jumps) in a window."""
    fig, ax = _fig()
    ks = np.arange(0, kmax + 1)
    pmf = np.array([lam**k * math.exp(-lam) / math.factorial(int(k)) for k in ks])
    ax.bar(ks, pmf, color=VIOLET, edgecolor="white", width=0.85)
    ax.axvline(lam, color=RED, ls="--", lw=1.6, label=f"E[X] = Var(X) = λ = {lam:g}")
    ax.set_title(f"Poisson: count of events per window (λ = {lam:g})")
    ax.set_xlabel("Number of events k")
    ax.set_ylabel("Probability")
    ax.legend(frameon=False)
    return fig


def pareto_pdf(alpha=1.5, xm=1.0):
    """Pareto heavy tail: a few extreme outcomes dominate."""
    fig, ax = _fig()
    x = np.linspace(xm, 8, 600)
    pdf = alpha * xm**alpha / x ** (alpha + 1)
    ax.plot(x, pdf, color=AMBER, lw=2.6)
    ax.fill_between(x, 0, pdf, color=AMBER, alpha=0.15)
    big = x[x >= 4]
    ax.fill_between(big, 0, alpha * xm**alpha / big ** (alpha + 1), color=RED, alpha=0.3,
                    label="rare, giant outcomes")
    ax.set_title(f"Pareto distribution (α = {alpha:g}): the 80/20 tail")
    ax.set_xlabel("Outcome size x")
    ax.set_ylabel("Probability density")
    ax.legend(frameon=False)
    return fig


def frequentist_convergence(flips=1500, seed=7):
    """Law of large numbers: running frequency of heads converges to 0.5."""
    rng = np.random.default_rng(seed)
    fig, ax = _fig()
    for s in range(3):
        r = np.random.default_rng(seed + s)
        tosses = r.integers(0, 2, flips)
        running = np.cumsum(tosses) / np.arange(1, flips + 1)
        ax.plot(running, lw=1.4, alpha=0.85)
    ax.axhline(0.5, color=RED, ls="--", lw=1.8, label="true probability = 0.5")
    ax.set_xscale("log")
    ax.set_ylim(0, 1)
    ax.set_title("Frequentist view: long-run frequency settles down")
    ax.set_xlabel("Number of flips (log scale)")
    ax.set_ylabel("Fraction that were heads")
    ax.legend(frameon=False)
    return fig


def bayes_update(prior=(0.5, 0.5), likelihood=(0.5, 0.7), labels=("Bag 1", "Bag 2")):
    """Prior vs posterior after evidence (the two-bags-of-marbles example)."""
    prior = np.array(prior, float)
    like = np.array(likelihood, float)
    post = prior * like
    post = post / post.sum()
    fig, ax = _fig()
    x = np.arange(len(labels))
    w = 0.38
    ax.bar(x - w / 2, prior, w, label="Prior belief", color=SLATE)
    ax.bar(x + w / 2, post, w, label="Posterior (after green marble)", color=GREEN)
    for xi, (a, b) in enumerate(zip(prior, post)):
        ax.text(xi - w / 2, a + 0.01, f"{a:.0%}", ha="center", fontsize=9)
        ax.text(xi + w / 2, b + 0.01, f"{b:.0%}", ha="center", fontsize=9, fontweight="bold")
    ax.set_xticks(x, labels)
    ax.set_ylim(0, 1)
    ax.set_title("Bayes' theorem updates belief with evidence")
    ax.set_ylabel("Probability")
    ax.legend(frameon=False)
    return fig


def beta_update(prior_a=2, prior_b=2, heads=8, tails=2):
    """Beta-Binomial belief update over an unknown win probability θ."""
    theta = np.linspace(0, 1, 500)

    def beta_pdf(t, a, b):
        # normalize numerically to avoid a Beta-function import
        raw = t ** (a - 1) * (1 - t) ** (b - 1)
        return raw / np.trapz(raw, t)

    fig, ax = _fig()
    ax.plot(theta, beta_pdf(theta, prior_a, prior_b), color=SLATE, lw=2.2,
            label=f"Prior  Beta({prior_a},{prior_b})")
    ax.plot(theta, beta_pdf(theta, prior_a + heads, prior_b + tails), color=BLUE, lw=2.6,
            label=f"Posterior  Beta({prior_a+heads},{prior_b+tails})")
    ax.fill_between(theta, 0, beta_pdf(theta, prior_a + heads, prior_b + tails),
                    color=BLUE, alpha=0.12)
    ax.set_title(f"Updating belief about a win rate after {heads}W / {tails}L")
    ax.set_xlabel("θ  (true probability of winning)")
    ax.set_ylabel("Belief density")
    ax.legend(frameon=False)
    return fig


# ----------------------------------------------------------------------------
# Position sizing / Kelly
# ----------------------------------------------------------------------------
def kelly_curve(p=0.6, b=1.0):
    """Long-run growth rate vs bet fraction; marks the Kelly-optimal fraction."""
    q = 1 - p
    f = np.linspace(0.0001, 0.9999, 600)
    g = p * np.log(1 + b * f) + q * np.log(1 - f)
    f_star = (b * p - q) / b
    fig, ax = _fig()
    ax.plot(f, g, color=BLUE, lw=2.6)
    ax.axhline(0, color=SLATE, lw=1)
    ax.axvline(f_star, color=GREEN, ls="--", lw=1.8, label=f"Kelly f* = {f_star:.0%}")
    ax.axvline(min(2 * f_star, 0.999), color=RED, ls=":", lw=1.8,
               label="double Kelly → 0 growth")
    ax.fill_between(f, g, 0, where=(g > 0), color=GREEN, alpha=0.10)
    ax.fill_between(f, g, 0, where=(g < 0), color=RED, alpha=0.10)
    ax.scatter([f_star], [p * np.log(1 + b * f_star) + q * np.log(1 - f_star)],
               color=GREEN, zorder=5, s=45)
    ax.set_title(f"Kelly criterion (p={p:g}, b={b:g}): bet too big and you go backwards")
    ax.set_xlabel("Fraction of capital bet per trade  f")
    ax.set_ylabel("Long-run growth rate  g(f)")
    ax.legend(frameon=False, loc="lower left")
    return fig


def kelly_wealth_paths(p=0.6, b=1.0, rounds=200, seed=3):
    """Median wealth trajectories for half / full / double Kelly (log scale)."""
    q = 1 - p
    f_star = (b * p - q) / b
    fig, ax = _fig()
    specs = [(0.5 * f_star, "Half Kelly", GREEN),
             (f_star, "Full Kelly", BLUE),
             (2 * f_star, "Double Kelly (over-bet)", RED)]
    for frac, label, color in specs:
        paths = []
        for s in range(200):
            r = np.random.default_rng(seed + s)
            wins = r.random(rounds) < p
            mult = np.where(wins, 1 + b * frac, 1 - frac)
            paths.append(np.concatenate([[1.0], np.cumprod(mult)]))
        median = np.median(np.array(paths), axis=0)
        ax.plot(median, color=color, lw=2.4, label=f"{label} (f={frac:.0%})")
    ax.set_yscale("log")
    ax.axhline(1, color=SLATE, lw=1, ls=":")
    ax.set_title("Median wealth over 200 bets: over-betting destroys compounding")
    ax.set_xlabel("Bet number")
    ax.set_ylabel("Wealth (× starting, log scale)")
    ax.legend(frameon=False, loc="upper left")
    return fig


def portfolio_heat(risks=(1.0, 1.5, 0.8, 1.2, 2.0), limit=8.0):
    """Stacked per-position risk vs a portfolio-heat ceiling."""
    fig, ax = _fig(7, 3.4)
    bottom = 0.0
    colors = [BLUE, GREEN, VIOLET, AMBER, CYAN, RED]
    for i, r in enumerate(risks):
        ax.barh(0, r, left=bottom, color=colors[i % len(colors)], edgecolor="white",
                label=f"Position {i+1}: {r:g}%")
        bottom += r
    ax.axvline(limit, color=RED, ls="--", lw=2, label=f"heat ceiling {limit:g}%")
    ax.set_xlim(0, max(limit + 2, bottom + 1))
    ax.set_yticks([])
    ax.set_title(f"Portfolio heat = Σ position risk = {sum(risks):g}%")
    ax.set_xlabel("Percent of capital at risk")
    ax.legend(frameon=False, fontsize=8, ncol=2, loc="lower right")
    return fig


# ----------------------------------------------------------------------------
# Trend following
# ----------------------------------------------------------------------------
def _gbm_price(n=600, mu=0.0004, sigma=0.011, seed=11, s0=100.0):
    r = np.random.default_rng(seed)
    shocks = r.normal(mu, sigma, n)
    # inject a couple of sustained trends
    shocks[120:220] += 0.0016
    shocks[350:470] -= 0.0018
    return s0 * np.exp(np.cumsum(shocks))


def ema_crossover(fast=50, slow=200, seed=11):
    """Synthetic price with fast/slow moving averages and golden/death crosses."""
    price = _gbm_price(seed=seed)
    n = len(price)
    t = np.arange(n)

    def sma(a, w):
        out = np.full_like(a, np.nan)
        c = np.cumsum(np.insert(a, 0, 0))
        out[w - 1:] = (c[w:] - c[:-w]) / w
        return out

    mf, ms = sma(price, fast), sma(price, slow)
    fig, ax = _fig(7.4, 4.2)
    ax.plot(t, price, color="#94a3b8", lw=1.0, label="Price")
    ax.plot(t, mf, color=BLUE, lw=2.0, label=f"{fast}-day MA")
    ax.plot(t, ms, color=AMBER, lw=2.0, label=f"{slow}-day MA")
    cross = np.sign(mf - ms)
    for i in range(1, n):
        if np.isnan(cross[i]) or np.isnan(cross[i - 1]):
            continue
        if cross[i] > 0 and cross[i - 1] <= 0:
            ax.scatter(i, price[i], marker="^", color=GREEN, s=110, zorder=5)
        elif cross[i] < 0 and cross[i - 1] >= 0:
            ax.scatter(i, price[i], marker="v", color=RED, s=110, zorder=5)
    ax.scatter([], [], marker="^", color=GREEN, s=90, label="Golden cross (go long)")
    ax.scatter([], [], marker="v", color=RED, s=90, label="Death cross (exit/short)")
    ax.set_title("Moving-average crossover: the trend filter in action")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Price")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    return fig


def trend_equity_curve(n_trades=120, seed=5):
    """Many small losses + a few big wins → a rising, jagged equity curve."""
    r = np.random.default_rng(seed)
    wins = r.random(n_trades) < 0.35
    pnl = np.where(wins, r.uniform(2, 7, n_trades), -r.uniform(0.5, 1.5, n_trades))
    equity = 100 + np.cumsum(pnl)
    peak = np.maximum.accumulate(equity)
    fig, ax = _fig()
    ax.plot(equity, color=GREEN, lw=2.2, label="Equity")
    ax.fill_between(range(n_trades), equity, peak, color=RED, alpha=0.18,
                    label="Drawdown")
    ax.plot(peak, color=SLATE, lw=1.0, ls=":")
    ax.set_title("Trend-following equity: lose small often, win big rarely")
    ax.set_xlabel("Trade number")
    ax.set_ylabel("Account value")
    ax.legend(frameon=False, loc="upper left")
    return fig


def win_loss_hist(n_trades=400, seed=8):
    """Distribution of trade P&L: cluster of small losses, thin fat right tail."""
    r = np.random.default_rng(seed)
    wins = r.random(n_trades) < 0.35
    pnl = np.where(wins, r.uniform(1, 9, n_trades), -r.uniform(0.3, 1.6, n_trades))
    fig, ax = _fig()
    ax.hist(pnl[pnl < 0], bins=20, color=RED, alpha=0.75, label="Losses (frequent, small)")
    ax.hist(pnl[pnl >= 0], bins=25, color=GREEN, alpha=0.75, label="Wins (rare, large)")
    ax.axvline(pnl.mean(), color=INK, ls="--", lw=1.8, label=f"mean = +{pnl.mean():.2f} (edge)")
    ax.set_title("Asymmetric payoff: the math behind trend following")
    ax.set_xlabel("Profit / loss per trade (R)")
    ax.set_ylabel("Number of trades")
    ax.legend(frameon=False)
    return fig


def diversification_smoothing(seed=4):
    """One market vs a 20-market portfolio: same edge, far smoother ride."""
    r = np.random.default_rng(seed)
    steps = 250

    def curve(k):
        rets = r.normal(0.05, 1.0, (k, steps))
        port = rets.mean(axis=0)
        return 100 + np.cumsum(port)

    fig, ax = _fig()
    ax.plot(curve(1), color=RED, lw=1.4, alpha=0.9, label="1 market (jagged)")
    ax.plot(curve(5), color=AMBER, lw=1.7, alpha=0.9, label="5 markets")
    ax.plot(curve(20), color=GREEN, lw=2.4, label="20 uncorrelated markets (smooth)")
    ax.set_title("Diversification smooths the equity curve")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Account value")
    ax.legend(frameon=False, loc="upper left")
    return fig


# ----------------------------------------------------------------------------
# Economics / valuation
# ----------------------------------------------------------------------------
def pe_vs_forward_return(seed=2):
    """Stylized: high starting P/E → low subsequent 10-yr returns."""
    r = np.random.default_rng(seed)
    pe = r.uniform(8, 32, 120)
    ret = 18 - 0.55 * pe + r.normal(0, 2.2, 120)
    fig, ax = _fig()
    ax.scatter(pe, ret, color=BLUE, alpha=0.6, edgecolor="white", s=42)
    coef = np.polyfit(pe, ret, 1)
    xs = np.linspace(8, 32, 50)
    ax.plot(xs, np.polyval(coef, xs), color=RED, lw=2.4, label="best-fit trend")
    ax.axhline(0, color=SLATE, lw=1)
    ax.axvline(23, color=AMBER, ls="--", lw=1.6, label="S&P 500 ≈ 23 (rich)")
    ax.set_title("Starting valuation predicts long-run return")
    ax.set_xlabel("Starting P/E ratio")
    ax.set_ylabel("Next 10-yr annual return (%)")
    ax.legend(frameon=False)
    return fig


def price_value_convergence(seed=1):
    """Intrinsic value as a magnet: price oscillates around it (bubbles & crashes)."""
    n = 240
    t = np.arange(n)
    value = 100 * np.exp(0.0025 * t)
    r = np.random.default_rng(seed)
    sentiment = 30 * np.sin(t / 22) + np.cumsum(r.normal(0, 1.1, n))
    price = value + sentiment
    fig, ax = _fig()
    ax.plot(t, value, color=GREEN, lw=2.6, label="Intrinsic value (fundamentals)")
    ax.plot(t, price, color=BLUE, lw=1.6, label="Price (sentiment-driven)")
    ax.fill_between(t, value, price, where=(price >= value), color=RED, alpha=0.15)
    ax.fill_between(t, value, price, where=(price < value), color=GREEN, alpha=0.15)
    i_hi = int(np.argmax(price - value))
    i_lo = int(np.argmin(price - value))
    ax.annotate("bubble", xy=(i_hi, price[i_hi]), xytext=(i_hi - 30, price[i_hi] + 18),
                color=RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.annotate("bargain", xy=(i_lo, price[i_lo]), xytext=(i_lo - 5, price[i_lo] - 32),
                color=GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.set_title("Value is a magnet — price wanders, then reverts")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price / value")
    ax.legend(frameon=False, loc="upper left")
    return fig


def affordability_gap():
    """Stylized home-price index vs wage index diverging over decades."""
    years = np.arange(1985, 2026)
    t = years - 1985
    homes = 100 * np.exp(0.045 * t)
    wages = 100 * np.exp(0.021 * t)
    fig, ax = _fig()
    ax.plot(years, homes, color=RED, lw=2.6, label="Home prices")
    ax.plot(years, wages, color=BLUE, lw=2.6, label="Wages")
    ax.fill_between(years, wages, homes, color=RED, alpha=0.12)
    ax.annotate("affordability gap", xy=(2018, (homes[-8] + wages[-8]) / 2),
                fontsize=11, color=RED, fontweight="bold")
    ax.set_title("Why a generation feels priced out (stylized index)")
    ax.set_xlabel("Year")
    ax.set_ylabel("Index (1985 = 100)")
    ax.legend(frameon=False, loc="upper left")
    return fig


# ----------------------------------------------------------------------------
# Machine learning
# ----------------------------------------------------------------------------
def overfitting_curve():
    """Train vs validation error as model complexity grows: the bias–variance U."""
    c = np.linspace(1, 12, 200)
    train = 1.6 * np.exp(-0.35 * c) + 0.05
    val = 1.6 * np.exp(-0.55 * c) + 0.04 * (c - 4) ** 2 * (c > 4) + 0.18
    fig, ax = _fig()
    ax.plot(c, train, color=BLUE, lw=2.4, label="Training error")
    ax.plot(c, val, color=RED, lw=2.4, label="Validation error")
    sweet = c[np.argmin(val)]
    ax.axvline(sweet, color=GREEN, ls="--", lw=1.8, label="sweet spot")
    ax.annotate("underfit", xy=(2, 1.0), color=SLATE, fontweight="bold")
    ax.annotate("overfit", xy=(10, 1.0), color=SLATE, fontweight="bold")
    ax.set_title("Overfitting: the enemy of every trading model")
    ax.set_xlabel("Model complexity →")
    ax.set_ylabel("Error")
    ax.set_yticks([])
    ax.legend(frameon=False, loc="upper center")
    return fig


def walk_forward_cv(folds=5):
    """Schematic of walk-forward validation: train windows precede test windows."""
    fig, ax = _fig(7.2, 3.8)
    for i in range(folds):
        y = folds - i
        train_end = 3 + i * 1.6
        ax.barh(y, train_end, left=0, color=BLUE, edgecolor="white", height=0.6)
        ax.barh(y, 1.4, left=train_end, color=AMBER, edgecolor="white", height=0.6)
    ax.barh([], [], color=BLUE, label="Train (past)")
    ax.barh([], [], color=AMBER, label="Test (future)")
    ax.set_title("Walk-forward validation: never train on the future")
    ax.set_xlabel("Time →")
    ax.set_yticks([])
    ax.set_ylim(0.3, folds + 0.8)
    ax.legend(frameon=False, loc="lower right")
    ax.grid(False)
    return fig


def confusion_matrix_demo(tp=38, fp=22, fn=17, tn=43):
    """A 2×2 confusion matrix for an up/down market classifier."""
    m = np.array([[tp, fp], [fn, tn]])
    fig, ax = _fig(5.2, 4.4)
    ax.imshow(m, cmap="Blues")
    labels = [["True Up\n(correct)", "False Up\n(costly)"],
              ["False Down\n(missed)", "True Down\n(correct)"]]
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{labels[i][j]}\n{m[i, j]}", ha="center", va="center",
                    fontsize=11, fontweight="bold",
                    color="white" if m[i, j] > m.max() / 2 else INK)
    ax.set_xticks([0, 1], ["Predicted Up", "Predicted Down"])
    ax.set_yticks([0, 1], ["Actual Up", "Actual Down"])
    ax.set_title("Confusion matrix: not all errors cost the same")
    ax.grid(False)
    return fig


# ----------------------------------------------------------------------------
# ESG
# ----------------------------------------------------------------------------
def esg_rating_divergence():
    """The same company scored very differently by three ESG agencies."""
    companies = ["MegaOil", "TechCorp", "AutoInc", "BankCo"]
    a = [22, 78, 55, 61]
    b = [48, 65, 40, 72]
    c = [35, 88, 67, 50]
    x = np.arange(len(companies))
    w = 0.26
    fig, ax = _fig()
    ax.bar(x - w, a, w, label="Agency A", color=BLUE)
    ax.bar(x, b, w, label="Agency B", color=AMBER)
    ax.bar(x + w, c, w, label="Agency C", color=GREEN)
    ax.set_xticks(x, companies)
    ax.set_title("Same company, three ESG scores — ratings disagree")
    ax.set_ylabel("ESG score (0–100)")
    ax.set_ylim(0, 100)
    ax.legend(frameon=False, ncol=3)
    return fig


def esg_aum_growth():
    """Stylized growth of ESG assets under management toward ~$35T."""
    years = np.arange(2004, 2025, 2)
    aum = np.array([2, 4, 7, 11, 14, 18, 23, 30, 33, 35, 34])[: len(years)]
    fig, ax = _fig()
    ax.fill_between(years, 0, aum, color=GREEN, alpha=0.25)
    ax.plot(years, aum, color=GREEN, lw=2.8, marker="o")
    ax.set_title("ESG assets under management (stylized, $ trillions)")
    ax.set_xlabel("Year")
    ax.set_ylabel("AUM ($T)")
    return fig


# ----------------------------------------------------------------------------
# Registry exposed to the renderer
# ----------------------------------------------------------------------------
CHARTS = {
    name: obj
    for name, obj in list(globals().items())
    if callable(obj) and not name.startswith("_") and name not in {"CHARTS"}
}
