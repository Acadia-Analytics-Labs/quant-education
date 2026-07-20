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

    _trapz = getattr(np, "trapezoid", np.trapz)  # numpy 2.x renamed trapz

    def beta_pdf(t, a, b):
        # normalize numerically to avoid a Beta-function import
        raw = t ** (a - 1) * (1 - t) ** (b - 1)
        return raw / _trapz(raw, t)

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
# Expected value / betting (thorp, expected-value)
# ----------------------------------------------------------------------------
def expected_value_bars(outcomes=(-100, 150), probs=(0.55, 0.45)):
    """Probability-weighted outcomes and the resulting expected value."""
    outcomes = np.array(outcomes, float)
    probs = np.array(probs, float)
    ev = float((outcomes * probs).sum())
    fig, ax = _fig()
    colors = [GREEN if o >= 0 else RED for o in outcomes]
    ax.bar(range(len(outcomes)), outcomes * probs, color=colors, edgecolor="white")
    for i, (o, p) in enumerate(zip(outcomes, probs)):
        ax.text(i, o * p + (3 if o > 0 else -3), f"{o:+g} × {p:.0%}",
                ha="center", va="bottom" if o > 0 else "top", fontsize=9)
    ax.axhline(ev, color=INK, ls="--", lw=2, label=f"E[X] = {ev:+.1f}")
    ax.axhline(0, color=SLATE, lw=1)
    ax.set_title("Expected value = the probability-weighted average outcome")
    ax.set_xticks(range(len(outcomes)), [f"Outcome {i+1}" for i in range(len(outcomes))])
    ax.set_ylabel("Contribution to E[X]")
    ax.legend(frameon=False)
    return fig


def many_small_bets(edge=0.02, sd=1.0):
    """Probability of finishing ahead rises with the NUMBER of small-edge bets."""
    from math import erf, sqrt
    ns = np.arange(1, 401)
    # P(sum>0) ≈ Phi(edge*sqrt(N)/sd) via the normal CDF
    z = edge * np.sqrt(ns) / sd
    p = 0.5 * (1 + np.array([erf(zi / sqrt(2)) for zi in z]))
    fig, ax = _fig()
    ax.plot(ns, p, color=BLUE, lw=2.6)
    ax.axhline(0.5, color=SLATE, ls=":", lw=1)
    for n in (10, 100, 400):
        ax.scatter([n], [p[n - 1]], color=GREEN, zorder=5)
        ax.annotate(f"{p[n-1]:.0%}", (n, p[n - 1]), textcoords="offset points",
                    xytext=(4, -12), fontsize=9)
    ax.set_title(f"Thorp's edge: a tiny {edge:.0%} edge becomes near-certain over many bets")
    ax.set_xlabel("Number of independent bets")
    ax.set_ylabel("Probability of finishing profitable")
    ax.set_ylim(0.4, 1.0)
    return fig


# ----------------------------------------------------------------------------
# Monte Carlo / Kalman (monte-carlo, state-space-kalman)
# ----------------------------------------------------------------------------
def monte_carlo_paths(n_paths=250, days=252, seed=6):
    """Fan of simulated price paths with a percentile cone and a VaR marker."""
    r = np.random.default_rng(seed)
    shocks = r.normal(0.0003, 0.012, (n_paths, days))
    paths = 100 * np.exp(np.cumsum(shocks, axis=1))
    fig, ax = _fig()
    for i in range(min(60, n_paths)):
        ax.plot(paths[i], color=BLUE, lw=0.5, alpha=0.18)
    p5, p50, p95 = np.percentile(paths, [5, 50, 95], axis=0)
    ax.plot(p50, color=INK, lw=2.2, label="median")
    ax.fill_between(range(days), p5, p95, color=AMBER, alpha=0.25, label="5–95% cone")
    var5 = np.percentile(paths[:, -1], 5)
    ax.axhline(var5, color=RED, ls="--", lw=1.6, label=f"5% VaR ≈ {var5:.0f}")
    ax.set_title(f"Monte Carlo: {n_paths} simulated futures → a distribution of outcomes")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Simulated price")
    ax.legend(frameon=False, loc="upper left")
    return fig


def kalman_filter_demo(n=120, seed=9):
    """Hidden true level, noisy observations, and the Kalman-filtered estimate."""
    r = np.random.default_rng(seed)
    true = np.cumsum(r.normal(0, 0.3, n)) + 10
    obs = true + r.normal(0, 1.6, n)
    # scalar Kalman filter
    est, P, Q, R = [obs[0]], 1.0, 0.05, 2.5
    x = obs[0]
    for z in obs[1:]:
        P += Q
        K = P / (P + R)
        x = x + K * (z - x)
        P *= (1 - K)
        est.append(x)
    fig, ax = _fig()
    ax.scatter(range(n), obs, s=14, color=SLATE, alpha=0.6, label="Noisy observations")
    ax.plot(true, color=GREEN, lw=2.4, label="Hidden true level")
    ax.plot(est, color=BLUE, lw=2.2, label="Kalman estimate")
    ax.set_title("Kalman filter: recover the signal from the noise")
    ax.set_xlabel("Time")
    ax.set_ylabel("Level")
    ax.legend(frameon=False, loc="upper left")
    return fig


def hmm_regimes(n=400, seed=12):
    """Price path shaded by hidden regime (bull / bear / choppy)."""
    r = np.random.default_rng(seed)
    regimes, mus, sds = [], [0.0012, -0.0014, 0.0], [0.008, 0.014, 0.006]
    state, out = 0, []
    for _ in range(n):
        if r.random() < 0.03:
            state = int(r.integers(0, 3))
        out.append(state)
    rets = np.array([r.normal(mus[s], sds[s]) for s in out])
    price = 100 * np.exp(np.cumsum(rets))
    fig, ax = _fig()
    names = ["Bull", "Bear", "Choppy"]
    cols = [GREEN, RED, SLATE]
    ax.plot(price, color=INK, lw=1.2)
    for s in range(3):
        mask = np.array(out) == s
        ax.fill_between(range(n), price.min(), price.max(), where=mask,
                        color=cols[s], alpha=0.12)
        ax.plot([], [], color=cols[s], lw=8, alpha=0.4, label=names[s])
    ax.set_title("Hidden Markov regimes: one price, three hidden states")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Price")
    ax.legend(frameon=False, loc="upper left", ncol=3)
    return fig


# ----------------------------------------------------------------------------
# Machine learning (regression, activations, curse, manifold, backtest)
# ----------------------------------------------------------------------------
def linear_regression_fit(seed=1):
    """Scatter with an OLS best-fit line and residual segments."""
    r = np.random.default_rng(seed)
    x = np.linspace(0, 10, 40)
    y = 2 + 1.3 * x + r.normal(0, 2.2, x.size)
    b, a = np.polyfit(x, y, 1)
    yhat = a + b * x
    fig, ax = _fig()
    for xi, yi, yh in zip(x, y, yhat):
        ax.plot([xi, xi], [yi, yh], color=SLATE, lw=0.8, alpha=0.6)
    ax.scatter(x, y, color=BLUE, s=32, zorder=4, label="data")
    ax.plot(x, yhat, color=RED, lw=2.6, label=f"ŷ = {a:.1f} + {b:.2f}x")
    ax.set_title("Linear regression: the line that minimizes squared residuals")
    ax.set_xlabel("Feature x")
    ax.set_ylabel("Target y")
    ax.legend(frameon=False)
    return fig


def logistic_sigmoid(seed=2):
    """The logistic curve mapping a score to a probability, with a 0.5 threshold."""
    r = np.random.default_rng(seed)
    x = np.linspace(-6, 6, 400)
    s = 1 / (1 + np.exp(-x))
    fig, ax = _fig()
    ax.plot(x, s, color=BLUE, lw=2.8)
    ax.axhline(0.5, color=SLATE, ls=":", lw=1)
    ax.axvline(0, color=SLATE, ls=":", lw=1)
    pos = r.normal(2.2, 1.2, 25); neg = r.normal(-2.2, 1.2, 25)
    ax.scatter(pos, 1 / (1 + np.exp(-pos)), color=GREEN, s=22, label="class 1 (up)")
    ax.scatter(neg, 1 / (1 + np.exp(-neg)), color=RED, s=22, label="class 0 (down)")
    ax.annotate("decision threshold 0.5", (0.2, 0.55), fontsize=9, color=SLATE)
    ax.set_title("Logistic regression squashes any score into a probability")
    ax.set_xlabel("Linear score  w·x + b")
    ax.set_ylabel("P(class = 1)")
    ax.legend(frameon=False, loc="upper left")
    return fig


def activation_functions():
    """Common neural-network activation functions."""
    x = np.linspace(-5, 5, 400)
    fig, ax = _fig()
    ax.plot(x, 1 / (1 + np.exp(-x)), color=BLUE, lw=2.2, label="sigmoid")
    ax.plot(x, np.tanh(x), color=GREEN, lw=2.2, label="tanh")
    ax.plot(x, np.maximum(0, x), color=RED, lw=2.2, label="ReLU")
    ax.plot(x, np.where(x > 0, x, 0.1 * x), color=AMBER, lw=1.8, ls="--", label="LeakyReLU")
    ax.axhline(0, color=SLATE, lw=0.8); ax.axvline(0, color=SLATE, lw=0.8)
    ax.set_title("Activation functions: where neural nets get their nonlinearity")
    ax.set_xlabel("input")
    ax.set_ylabel("output")
    ax.set_ylim(-1.5, 5)
    ax.legend(frameon=False, loc="upper left")
    return fig


def curse_of_dimensionality():
    """Share of a hypercube's volume that sits in its outer shell vs dimension."""
    d = np.arange(1, 26)
    shell = 1 - 0.9**d  # fraction of volume within 10% of the boundary
    fig, ax = _fig()
    ax.plot(d, shell, color=VIOLET, lw=2.8, marker="o", ms=4)
    ax.fill_between(d, 0, shell, color=VIOLET, alpha=0.12)
    ax.axhline(1.0, color=SLATE, ls=":", lw=1)
    ax.set_title("Curse of dimensionality: in high-D, (almost) everything is on the edge")
    ax.set_xlabel("Number of dimensions (features)")
    ax.set_ylabel("Fraction of volume near the surface")
    ax.set_ylim(0, 1.05)
    return fig


def manifold_swiss_roll(n=1200, seed=3):
    """A 2-D 'swiss roll' manifold embedded in 3-D — structure hides in low dimensions."""
    r = np.random.default_rng(seed)
    t = 1.5 * np.pi * (1 + 2 * r.random(n))
    h = 21 * r.random(n)
    x, y, z = t * np.cos(t), h, t * np.sin(t)
    fig = plt.figure(figsize=(6.6, 4.4))
    ax = fig.add_subplot(projection="3d")
    ax.scatter(x, y, z, c=t, cmap="viridis", s=8)
    ax.set_title("The manifold hypothesis: data lives on a low-D surface in high-D space")
    ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")
    ax.grid(False)
    return fig


def backtest_overfit(seed=5):
    """In-sample curve that looks great, out-of-sample that doesn't — overfitting."""
    r = np.random.default_rng(seed)
    n = 250
    ins = 100 + np.cumsum(r.normal(0.25, 1.0, n))
    oos = np.concatenate([ins[:n // 2], ins[n // 2] + np.cumsum(r.normal(-0.05, 1.1, n - n // 2))])
    fig, ax = _fig()
    ax.axvspan(0, n // 2, color=GREEN, alpha=0.06)
    ax.axvspan(n // 2, n, color=RED, alpha=0.06)
    ax.plot(ins, color=BLUE, lw=2.2, label="overfit backtest (in-sample)")
    ax.plot(range(n // 2, n), oos[n // 2:], color=RED, lw=2.4, label="live / out-of-sample")
    ax.axvline(n // 2, color=INK, ls="--", lw=1.4)
    ax.text(n // 4, ins.max(), "in-sample", ha="center", color=GREEN, fontweight="bold")
    ax.text(3 * n // 4, ins.max(), "out-of-sample", ha="center", color=RED, fontweight="bold")
    ax.set_title("Backtest overfitting: the curve that falls apart out-of-sample")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Equity")
    ax.legend(frameon=False, loc="upper left")
    return fig


def rl_reward_curve(episodes=300, seed=7):
    """A reinforcement-learning agent's reward improving over training, with variance."""
    r = np.random.default_rng(seed)
    runs = np.array([np.clip(np.cumsum(r.normal(0.03, 1, episodes)) / np.arange(1, episodes + 1)
                             * np.arange(1, episodes + 1) ** 0.0, -5, None) for _ in range(20)])
    curve = 1 - np.exp(-np.arange(episodes) / 60)
    band = runs.std(0) * 0.15 + 0.05
    fig, ax = _fig()
    ax.plot(curve, color=GREEN, lw=2.6, label="mean reward")
    ax.fill_between(range(episodes), curve - band, curve + band, color=GREEN, alpha=0.18,
                    label="±1 std across seeds")
    ax.set_title("Reinforcement learning: reward climbs as the agent learns")
    ax.set_xlabel("Training episode")
    ax.set_ylabel("Average reward (normalized)")
    ax.legend(frameon=False, loc="lower right")
    return fig


# ----------------------------------------------------------------------------
# Valuation / DCF (intro-dcf, intro-quant-trading)
# ----------------------------------------------------------------------------
def dcf_discounting(r=0.10, g=0.05, years=6, fcf0=100.0):
    """Projected free cash flows vs their present value after discounting."""
    t = np.arange(1, years + 1)
    fcf = fcf0 * (1 + g) ** t
    pv = fcf / (1 + r) ** t
    fig, ax = _fig()
    w = 0.4
    ax.bar(t - w / 2, fcf, w, color=SLATE, label="Projected FCF (future $)")
    ax.bar(t + w / 2, pv, w, color=GREEN, label="Present value (today's $)")
    for ti, f, p in zip(t, fcf, pv):
        ax.text(ti + w / 2, p + 2, f"{p:.0f}", ha="center", fontsize=8)
    ax.set_title(f"DCF: discounting future cash to today (r={r:.0%}, g={g:.0%})")
    ax.set_xlabel("Year")
    ax.set_ylabel("Cash flow")
    ax.legend(frameon=False)
    return fig


# ----------------------------------------------------------------------------
# Economics (yield curve, bonds, TIPS, micro, macro, monetary, SWF)
# ----------------------------------------------------------------------------
def yield_curve():
    """Normal, flat, and inverted Treasury yield curves."""
    mats = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30])
    fig, ax = _fig()
    ax.plot(mats, 2.0 + 1.8 * (1 - np.exp(-mats / 6)), color=GREEN, lw=2.6, marker="o", label="Normal (healthy)")
    ax.plot(mats, 4.0 + 0.05 * mats, color=SLATE, lw=2.2, marker="o", label="Flat (uncertain)")
    ax.plot(mats, 4.8 - 1.4 * (1 - np.exp(-mats / 6)), color=RED, lw=2.6, marker="o", label="Inverted (recession signal)")
    ax.set_xscale("log")
    ax.set_xticks([0.25, 1, 2, 5, 10, 30], ["3M", "1Y", "2Y", "5Y", "10Y", "30Y"])
    ax.set_title("The yield curve: shape signals the economy's outlook")
    ax.set_xlabel("Maturity")
    ax.set_ylabel("Yield (%)")
    ax.legend(frameon=False)
    return fig


def bond_price_yield():
    """The inverse relationship between a bond's price and its yield."""
    y = np.linspace(0.01, 0.12, 200)
    coupon, face, n = 5.0, 100.0, 10
    price = coupon * (1 - (1 + y) ** -n) / y + face * (1 + y) ** -n
    fig, ax = _fig()
    ax.plot(y * 100, price, color=BLUE, lw=2.8)
    ax.axhline(face, color=SLATE, ls=":", lw=1)
    ax.annotate("yields ↑  →  price ↓", (8, 80), fontsize=11, color=RED, fontweight="bold")
    ax.set_title("Bond prices move opposite to yields")
    ax.set_xlabel("Yield to maturity (%)")
    ax.set_ylabel("Bond price ($)")
    return fig


def tips_vs_nominal():
    """Real return of a nominal bond vs TIPS across inflation scenarios."""
    infl = np.linspace(0, 8, 100)
    nominal_yield = 4.0
    fig, ax = _fig()
    ax.plot(infl, nominal_yield - infl, color=RED, lw=2.6, label="Nominal bond (real return)")
    ax.plot(infl, np.full_like(infl, 1.5), color=GREEN, lw=2.6, label="TIPS (real return, protected)")
    ax.axhline(0, color=SLATE, lw=1)
    ax.fill_between(infl, nominal_yield - infl, 1.5, where=(infl > 2.5), color=GREEN, alpha=0.12)
    ax.set_title("TIPS protect real returns when inflation rises")
    ax.set_xlabel("Inflation rate (%)")
    ax.set_ylabel("Real (after-inflation) return (%)")
    ax.legend(frameon=False)
    return fig


def supply_demand():
    """Supply and demand curves, equilibrium, and a demand shift."""
    q = np.linspace(1, 10, 100)
    demand = 12 - q
    supply = 2 + 0.9 * q
    demand2 = 15 - q
    fig, ax = _fig()
    ax.plot(q, demand, color=BLUE, lw=2.6, label="Demand")
    ax.plot(q, supply, color=GREEN, lw=2.6, label="Supply")
    ax.plot(q, demand2, color=BLUE, lw=1.8, ls="--", alpha=0.7, label="Demand ↑ (shift)")
    qe = (12 - 2) / (1 + 0.9); pe = 2 + 0.9 * qe
    ax.scatter([qe], [pe], color=RED, zorder=5, s=55)
    ax.annotate("equilibrium", (qe, pe), textcoords="offset points", xytext=(8, 8), color=RED)
    ax.set_title("Supply & demand set the market-clearing price")
    ax.set_xlabel("Quantity")
    ax.set_ylabel("Price")
    ax.legend(frameon=False)
    return fig


def business_cycle():
    """Real GDP trend with cyclical expansions and recessions."""
    t = np.linspace(0, 24, 400)
    trend = 100 + 2.2 * t
    cycle = 6 * np.sin(t / 1.9)
    gdp = trend + cycle
    fig, ax = _fig()
    ax.plot(t, gdp, color=BLUE, lw=2.2, label="Real GDP")
    ax.plot(t, trend, color=SLATE, lw=1.6, ls="--", label="Long-run trend")
    ax.fill_between(t, gdp, trend, where=(cycle < 0), color=RED, alpha=0.18, label="Recession")
    ax.fill_between(t, gdp, trend, where=(cycle >= 0), color=GREEN, alpha=0.12, label="Expansion")
    ax.set_title("The business cycle: expansions and recessions around trend")
    ax.set_xlabel("Time (quarters)")
    ax.set_ylabel("Output")
    ax.legend(frameon=False, loc="upper left", ncol=2)
    return fig


def money_supply_inflation(seed=4):
    """Stylized link between money-supply growth and inflation."""
    r = np.random.default_rng(seed)
    m = np.linspace(0, 15, 60)
    infl = 0.8 * m + r.normal(0, 1.4, m.size)
    fig, ax = _fig()
    ax.scatter(m, infl, color=AMBER, alpha=0.7, edgecolor="white", s=36)
    coef = np.polyfit(m, infl, 1)
    ax.plot(m, np.polyval(coef, m), color=RED, lw=2.4, label="trend")
    ax.set_title("Over the long run, more money growth → more inflation")
    ax.set_xlabel("Money-supply growth (%)")
    ax.set_ylabel("Inflation (%)")
    ax.legend(frameon=False)
    return fig


def swf_sizes():
    """Approximate assets of the largest sovereign wealth funds."""
    funds = ["Norway\nGPFG", "China\nCIC", "Abu Dhabi\nADIA", "Kuwait\nKIA",
             "Saudi\nPIF", "Singapore\nGIC", "Qatar\nQIA"]
    aum = [1600, 1350, 1000, 920, 900, 800, 520]
    fig, ax = _fig(7, 4.2)
    ax.barh(funds[::-1], aum[::-1], color=CYAN, edgecolor="white")
    for i, v in enumerate(aum[::-1]):
        ax.text(v + 15, i, f"${v}B", va="center", fontsize=9)
    ax.set_title("Largest sovereign wealth funds (approx. AUM)")
    ax.set_xlabel("Assets under management ($B)")
    ax.grid(axis="y", visible=False)
    return fig


# ----------------------------------------------------------------------------
# Trading mechanics (ETFs, slippage, indicators)
# ----------------------------------------------------------------------------
def expense_ratio_drag(years=30, gross=0.07):
    """How a small annual fee compounds into a big gap over decades."""
    t = np.arange(0, years + 1)
    fig, ax = _fig()
    for fee, label, color in [(0.0003, "ETF (0.03% fee)", GREEN),
                              (0.005, "fund (0.50% fee)", AMBER),
                              (0.01, "fund (1.00% fee)", RED)]:
        ax.plot(t, 10000 * (1 + gross - fee) ** t, lw=2.4, color=color, label=label)
    ax.set_title("Fee drag: small expense ratios compound into large gaps")
    ax.set_xlabel("Years")
    ax.set_ylabel("Value of $10,000")
    ax.legend(frameon=False, loc="upper left")
    return fig


def slippage_costs():
    """Waterfall from gross edge to net after costs."""
    labels = ["Gross\nedge", "Commission", "Spread", "Slippage", "Net\nedge"]
    vals = [10.0, -1.5, -2.5, -3.0]
    fig, ax = _fig(7, 4)
    running = 10.0
    ax.bar(0, 10.0, color=GREEN, edgecolor="white")
    ax.text(0, 10.2, "10.0", ha="center", fontsize=9)
    for i, v in enumerate(vals[1:], start=1):
        ax.bar(i, -(-v), bottom=running + v, color=RED, edgecolor="white")
        ax.text(i, running + v - 0.4, f"{v:.1f}", ha="center", fontsize=9, color=RED)
        running += v
    ax.bar(4, running, color=BLUE, edgecolor="white")
    ax.text(4, running + 0.2, f"{running:.1f}", ha="center", fontsize=9)
    ax.set_xticks(range(5), labels)
    ax.axhline(0, color=SLATE, lw=1)
    ax.set_title("Transaction costs eat the edge: gross → net")
    ax.set_ylabel("Return (bps per trade)")
    return fig


def bollinger_bands(seed=15):
    """Price with a moving average and ±2σ Bollinger bands."""
    price = _gbm_price(n=260, seed=seed)
    n = len(price)
    w = 20
    ma = np.convolve(price, np.ones(w) / w, mode="valid")
    sd = np.array([price[i - w:i].std() for i in range(w, n + 1)])
    x = np.arange(w - 1, n)
    fig, ax = _fig(7.2, 4.1)
    ax.plot(price, color="#94a3b8", lw=1.0, label="Price")
    ax.plot(x, ma, color=BLUE, lw=2.0, label=f"{w}-day MA")
    ax.plot(x, ma + 2 * sd, color=RED, lw=1.4, ls="--", label="+2σ")
    ax.plot(x, ma - 2 * sd, color=GREEN, lw=1.4, ls="--", label="−2σ")
    ax.fill_between(x, ma - 2 * sd, ma + 2 * sd, color=BLUE, alpha=0.07)
    ax.set_title("Bollinger Bands: volatility envelope around a moving average")
    ax.set_xlabel("Trading day")
    ax.set_ylabel("Price")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    return fig


# ----------------------------------------------------------------------------
# Registry exposed to the renderer
# ----------------------------------------------------------------------------
CHARTS = {
    name: obj
    for name, obj in list(globals().items())
    if callable(obj) and not name.startswith("_") and name not in {"CHARTS"}
}
