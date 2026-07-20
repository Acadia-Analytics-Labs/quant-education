# Trend Following: A Long-Volatility, Positive-Skew Strategy

## 1. What is actually being harvested

Trend following is not a directional forecast; it is a **convexity trade on the persistence of returns**. The system enters after a move is underway, cuts losers at a fixed stop, and lets winners run under a trailing stop. That rule set mechanically manufactures a **truncated-left, heavy-right P&L distribution**: bounded small losses and an open-ended right tail.

```chart
win_loss_hist()
```

Fung & Hsieh (2001) formalized the shape: the returns of trend followers are well replicated by a portfolio of **lookback straddles** on the underlying markets — options whose payoff is the *maximum* move over the holding window. The strategy is therefore structurally **long volatility** and **long gamma**: its payoff is convex in the magnitude of realized moves and largest precisely during extreme, sustained dislocations. This is the analytic root of "crisis alpha" — trend following tends to be long-skewed and to pay off when static long-only portfolios suffer.

Formally, if $M_T = \max_{t\le T} S_t - \min_{t\le T} S_t$ is the peak-to-trough range, the lookback-straddle payoff scales with $M_T$, and a stop-and-trail rule is a discrete, path-dependent approximation to holding that straddle. The cost of the "option" is the accumulated small losses (theta); the payoff is the occasional large trend (gamma).

## 2. The arithmetic of asymmetry: expectancy, not hit rate

Let a trade produce average win $W$ with probability $p$ and average loss $L$ (magnitude) with probability $1-p$. Per-trade **expectancy** is

$$E = p\,W - (1-p)\,L.$$

Define the **win/loss ratio** (payoff ratio) $k = W/L$. Then $E > 0 \iff pW > (1-p)L \iff p\,k > 1-p$, giving the **break-even hit rate**

$$p^\star = \frac{1}{1+k} = \frac{L}{W+L}.$$

With $k = 3$ (the 2:1–3:1 win/loss ratios typical of trend systems), $p^\star = 0.25$: a system winning only **25%** of the time is already profitable. This is why a 30–40% hit rate is not a defect — it is the expected operating point of a positive-skew strategy. The worked source example ($p=0.3$, a \$400 average win $W$, a \$100 average loss $L$) gives $E = 0.3(400) - 0.7(100) = +50$ per trade, i.e. $+0.5L$ per trade in $R$-multiples.

The **profit factor** (gross profit ÷ gross loss over $N$ trades) is

$$\text{PF} = \frac{pW}{(1-p)L} = \frac{p}{1-p}\,k, \qquad \text{PF} > 1 \iff E > 0.$$

So PF, $k$, and expectancy are three views of the same inequality; **hit rate alone is uninformative** without $k$. Chaining these trades produces the characteristic jagged-but-rising equity curve — shallow, frequent drawdowns funding a few regime-defining runs:

```chart
trend_equity_curve()
```

A subtle consequence: because the win tail is heavy, the **sample mean expectancy converges slowly** and is dominated by rare large winners. Finite backtests understate variance and overstate the significance of the edge; the effective sample size is the number of *large* trends captured, not the number of trades.

## 3. The signal: positive serial correlation

The economic content of trend following is that returns exhibit **positive autocorrelation at the trading horizon** — momentum. Consider the stylized time-series-momentum position $\theta_{t-1} = \operatorname{sign}(r_{t-1})$ (or the sign of a trailing return). Expected per-period P&L is

$$\mathbb{E}[\theta_{t-1} r_t] = \mathbb{E}\!\left[\operatorname{sign}(r_{t-1})\, r_t\right],$$

which is positive precisely when returns are positively serially dependent. More generally, any **linear** trend filter that takes a position $\theta_{t-1} = \sum_{k\ge 1} w_k\, r_{t-k}$ has expected profit

$$\mathbb{E}[\theta_{t-1} r_t] = \sum_{k\ge 1} w_k\, \gamma(k), \qquad \gamma(k) = \operatorname{Cov}(r_t, r_{t-k}),$$

a weighted sum of return **autocovariances**. Trend following is, at bottom, a bet that $\gamma(k) > 0$ over the relevant lags $k$; a mean-reverting market ($\gamma(k)<0$) turns the same rules into a losing strategy. This is the Lo–MacKinlay decomposition applied to a single instrument: the strategy monetizes the autocovariance structure of prices.

**Empirical support.** Moskowitz, Ooi & Pedersen (2012) document significant **time-series momentum** across 58 futures and forwards spanning equities, bonds, currencies and commodities: the past ~12 months' excess return positively predicts the next month's, and a diversified TSMOM portfolio earns large risk-adjusted returns with **positive skew**, strongest in extreme up- and down-markets. Hurst, Ooi & Pedersen (AQR, "A Century of Evidence on Trend-Following Investing") extend the result back to 1880, finding consistent positive performance across a century and many asset classes — evidence the autocorrelation signal is structural, not a recent artifact.

## 4. The moving-average crossover as a linear filter

The dual-MA filter is a **band-pass linear filter** of the price. An exponential moving average with smoothing $\alpha$ (span $N$, $\alpha = 2/(N{+}1)$) is

$$\text{EMA}_t = \alpha P_t + (1-\alpha)\,\text{EMA}_{t-1} = \alpha \sum_{k\ge 0} (1-\alpha)^k P_{t-k},$$

geometric weights with **center of mass** (mean lag) $\tfrac{1-\alpha}{\alpha} = \tfrac{N-1}{2}$. The crossover signal

$$s_t = \text{EMA}^{\text{fast}}_t - \text{EMA}^{\text{slow}}_t$$

subtracts two low-pass filters, yielding a band-pass response: it suppresses both high-frequency noise (the fast EMA smooths ticks) and the slow drift (the slow EMA removes the level), leaving the intermediate-frequency **trend** component. Taking $\operatorname{sign}(s_t)$ as the position, this is exactly a linear trend filter of the form in §3, so its expected P&L is again a weighted autocovariance sum.

```chart
ema_crossover(fast=50, slow=200)
```

The design tension is **lag vs. noise**: longer windows (larger $N$) reduce whipsaw from spurious crossings but increase mean lag $\tfrac{N-1}{2}$, entering later and giving back more at the top. Faster windows react sooner but pay more theta in choppy regimes. There is no universally optimal pair; the choice trades transaction costs and whipsaw frequency against captured trend length.

## 5. Diversification and the $\sqrt{N}$ smoothing of the Sharpe ratio

Diversification across markets is the highest-leverage improvement because it raises the **Sharpe ratio** without altering any single market's edge. Take $N$ trend programs, each with per-period Sharpe $s$, equally weighted, with pairwise return correlation $\rho$. The portfolio mean scales with $N$ while its variance is

$$\operatorname{Var}\!\Big(\tfrac{1}{N}\textstyle\sum_i X_i\Big) = \frac{\sigma^2}{N}\big[1 + (N-1)\rho\big],$$

so the portfolio Sharpe is

$$\text{SR}_{\text{port}} = s\,\sqrt{N}\,\Big/\sqrt{1 + (N-1)\rho}.$$

At $\rho = 0$ this is the clean **$\text{SR}_{\text{port}} = s\sqrt{N}$**: uncorrelated streams multiply the Sharpe by $\sqrt{N}$. As $N\to\infty$ with $\rho>0$ the ratio saturates at $s/\sqrt{\rho}$ — correlation, not count, sets the ceiling, so the payoff is in finding *uncorrelated* markets, not merely more of them. Because different assets trend at different times, a diversified book converts idiosyncratic, jagged single-market curves into a far smoother aggregate at unchanged per-market risk:

```chart
diversification_smoothing()
```

This is the rigorous statement of the Turtles' insistence on many markets: with each market's Sharpe modest, the ensemble's $\sqrt{N}$ smoothing is what makes the drawdowns survivable and the compounding steady.

## 6. Where the model breaks

- **Regime dependence.** The edge is $\sum_k w_k\gamma(k)$; in mean-reverting or range-bound regimes $\gamma(k)<0$ and the same rules bleed. This motivates **regime detection** (e.g. a Hidden Markov Model labeling trending vs. choppy latent states, gating signals to suppress trades in whipsaw regimes) — an augmentation of the filter, not a price forecast.
- **Non-stationary correlations.** The $\rho$ in §5 rises toward 1 in crises across risk assets, collapsing the $\sqrt{N}$ benefit exactly when it is most wanted; genuine diversification requires structurally uncorrelated markets, not merely historically uncorrelated ones.
- **Fat tails and gap risk.** Trailing stops assume roughly continuous fills; overnight gaps and illiquidity mean realized left-tail losses exceed the "bounded" stop, eroding the clean straddle payoff.
- **Backtest fragility.** With returns dominated by a few large winners, in-sample optimization of window lengths overfits to which historical trends happened to occur; walk-forward validation and out-of-sample deflation are essential.
- **Capacity and cost.** Faster systems generate more signals and more turnover; transaction costs scale with signal frequency and can dominate the thin per-trade edge.

## References & further reading

- Covel, M. (2009). *Trend Following: Learn to Make Millions in Up or Down Markets.*
- Fung, W. & Hsieh, D. A. (2001). *The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers.* Review of Financial Studies, 14(2). (Lookback-straddle replication.)
- Moskowitz, T., Ooi, Y. H. & Pedersen, L. H. (2012). *Time Series Momentum.* Journal of Financial Economics, 104(2).
- Hurst, B., Ooi, Y. H. & Pedersen, L. H. (2017). *A Century of Evidence on Trend-Following Investing.* AQR Capital Management.
- Lo, A. W. & MacKinlay, A. C. (1990). *When Are Contrarian Profits Due to Stock Market Overreaction?* (Autocovariance decomposition of momentum/contrarian P&L.)
- Faith, C. (2007). *Way of the Turtle.* (The Turtle system, first-hand.)
