# The Affordability Crisis and the Arithmetic of Retail Speculation

## 1. The push factor, stated as an expectation problem

The macro backdrop is a widening gap between the price of housing and labor income. A stylized index makes the divergence concrete:

```chart
affordability_gap()
```

The behavioral consequence is best read through expected utility. Let $S$ be the wealth needed for a down payment and $r_{\text{save}}$ the risk-free saving rate. If $S$ grows at rate $g_H$ (home-price appreciation) while wages grow at $g_W < g_H$, the *time-to-target* under patient saving diverges as $g_H \to r_{\text{save}}$. A rational agent facing a receding target rationally raises variance: when the low-variance path has near-zero probability of reaching the goal, a high-variance path with a small probability of a large payoff can carry *higher* goal-probability even at *lower or negative* expected value. This is aspiration-based risk-seeking, and it is the quantitative core of why the affordability squeeze channels capital into day trading, crypto, and prediction markets. The rest of this note shows why those venues are, for the typical participant, negative-expectation.

## 2. Per-trade expectancy after frictions

Model a single round-trip trade as a wager with win probability $p$, average gain $W$, average loss $L$, and round-trip cost $c$ (commission $+$ half-spread each way $+$ slippage). Net expectancy is

$$\mathbb{E}[\pi] = p\,W - (1-p)\,L - c.$$

Two structural facts follow immediately:

- **A fair game is a losing game.** For a symmetric bet ($p=\tfrac12,\ W=L$), $\mathbb{E}[\pi] = -c < 0$. Frictions alone guarantee negative expectancy; you need a genuine edge merely to break even.
- **Taxes are asymmetric.** Short-term gains are taxed as ordinary income while losses offset only at capital-loss rates/caps, so the *after-tax* expectancy is strictly below the pre-tax figure whenever the strategy is profitable — the tax code shaves the right tail and not the left.

Turnover multiplies the leak. Over $N$ round trips per year the cost drag is $N\,c$; high-frequency retail day trading can run $N$ into the thousands, so even a modest $c$ (a few basis points of spread plus fees) compounds into a decisive headwind. Expectancy, not hit rate, is what compounds — a 60%-win strategy with $W < \tfrac{1-p}{p}(L) + \tfrac{c}{p}$ still bleeds.

## 3. The arithmetic of active management (Sharpe 1991)

Sharpe's argument is an accounting identity, not an empirical claim. Partition all dollars invested in a market into *passive* (hold the market portfolio) and *active* (everything else). Because the two groups together hold the market, and passive holders earn the market return gross of costs, the average actively managed dollar must also earn the market return **before costs**. Therefore:

$$\underbrace{\mathbb{E}[R_{\text{active}}^{\text{net}}]}_{\text{after costs}} = R_{\text{market}} - \bar c_{\text{active}} \; < \; R_{\text{market}} - \bar c_{\text{passive}} = \mathbb{E}[R_{\text{passive}}^{\text{net}}],$$

since $\bar c_{\text{active}} > \bar c_{\text{passive}}$. Active management is zero-sum before costs and negative-sum after. Retail day trading is the high-cost, high-turnover extreme of the active bucket, and it typically trades *against* better-informed institutional flow — so the representative retail trader sits well below the average active dollar. The activity does not merely fail to add value on average; it is structurally value-subtracting for the group.

## 4. Empirical evidence: trading is hazardous to your wealth

The theory is confirmed by the microstructure literature:

- **Barber & Odean (2000), "Trading Is Hazardous to Your Wealth."** Across ~66,000 U.S. household brokerage accounts, gross returns were roughly indistinguishable from the market, but *net* returns fell with turnover: the most active quintile underperformed the least active by a wide margin, almost entirely explained by trading costs. Activity itself was the destroyer of returns.
- **Barber, Lee, Liu & Odean (2011, 2014), Taiwan.** Using the full population of day traders on the Taiwan Stock Exchange, they found the vast majority lose money net of fees; only a very small minority (on the order of **~1%**, and by generous measures up to a few percent) earn positive risk-adjusted returns reliably, and this top sliver persists — consistent with a thin layer of genuine skill atop a large negative-expectation majority. Common shorthand in this literature is that roughly **1–3%** of day traders are net profitable after costs over meaningful horizons.
- Overconfidence amplifies the leak: Barber & Odean (2001) show that groups who trade more (in their data, men vs. women) earn *lower* net returns precisely because they trade more, not because they pick worse.

The gap between the visible track record and the true one is **survivorship bias** made quantitative: conditioning on the population that still posts P&L over-samples the surviving right tail and hides the left tail that has already blown out.

## 5. Gambler's ruin under a negative edge

Frame speculation as a random walk on capital. With unit bets, win probability $p$, loss probability $q=1-p$, starting bankroll $i$ units and an implicit "cash-out" target $N$, the classical gambler's-ruin probability of reaching $N$ before $0$ is

$$P_{\text{win}} = \frac{1-(q/p)^{\,i}}{1-(q/p)^{\,N}}, \qquad p \neq q.$$

When the edge is negative ($p < q$, i.e. $q/p > 1$), taking the horizon to infinity gives

$$\lim_{N\to\infty} P_{\text{win}} = 0 \quad\Longrightarrow\quad P_{\text{ruin}} \to 1.$$

With a negative per-trade expectancy, **ruin is certain in the limit** regardless of starting bankroll — the only free variables are how long it takes and how large the terminal drawdown is. This is the formal counterpart to "the house edge always wins if you keep playing": frictions (Section 2) put retail on the wrong side of $p<q$, and continued play converges to ruin. Increasing bet size to "make it back" only accelerates the walk toward the absorbing barrier.

## 6. Variance, skew, and the lottery preference

If the expectation is negative, why do people keep playing? Because humans do not maximize expected value over the full distribution — they respond to its *shape*, especially **skewness**. Prospect theory (Kahneman & Tversky 1979; Tversky & Kahneman 1992) supplies a probability-weighting function $w(\cdot)$ that **overweights small probabilities**: $w(p) > p$ for small $p$. A positive-skew bet — many small losses, a rare enormous gain — is exactly the payoff profile that this distortion inflates.

Formally, decompose the perceived value of a gamble beyond its mean:

$$V \approx \mathbb{E}[\pi] \;+\; \phi\cdot \text{Skew}[\pi] \;-\; \psi\cdot \text{Var}[\pi],$$

with $\phi > 0$ for skew-loving agents. Lottery-like assets (out-of-the-money options, small-cap "moonshots", many crypto tokens, longshot prediction-market contracts) carry large positive $\text{Skew}[\pi]$, so a negative $\mathbb{E}[\pi]$ can still yield a positive *perceived* $V$. Barberis & Huang (2008), "Stocks as Lotteries," formalize this: under cumulative prospect theory, positively skewed securities are **overpriced** and earn low or negative average returns in equilibrium — precisely the assets the affordability-driven cohort gravitates toward. The preference is not irrational noise; it is a systematic bias that the market prices, to the buyer's disadvantage.

## 7. Prediction markets as a (near) zero- to negative-sum game

A binary prediction market is a wager whose gross payoffs sum to zero across counterparties: for every dollar a YES holder gains, a NO holder loses it. It is **zero-sum before frictions**. Frictions make it negative-sum for the average participant:

- **Overround / vig.** If the executable YES price is $\pi_Y$ and NO is $\pi_N$ with $\pi_Y + \pi_N = 1 + v$, the platform's spread/fee $v>0$ is the overround. The expected return to a price-taker is negative by construction: a set of contracts that must pay out \$1 collectively costs $1+v$.
- **Fees on winnings / withdrawal.** Explicit take-rates on settled winnings push realized expectancy further below zero.
- **Adverse selection.** As in any market, uninformed flow transacts against informed counterparties; the marginal informed trader extracts the overround *and more* from the marginal noise trader.

So the ranking is: passive index (positive-sum, you own real cash-flow growth) $>$ prediction markets (zero-sum gross, negative-sum net) $\approx$ high-turnover day trading (negative-sum net) for the representative retail participant. "Gamified finance" is, mathematically, a game with a rake.

## 8. Implication for sizing: the Kelly verdict is "don't"

The growth-optimal bet fraction (see the *Position Sizing* article) is

$$f^\star = p - \frac{q}{b},$$

and for the discrete case reduces to $f^\star = \dfrac{bp-q}{b}$. A **negative edge** ($bp < q$) yields $f^\star < 0$: the growth-maximizing position size is *zero* (you cannot short the game itself). Any $f>0$ places you left of the origin on the log-growth curve, where $g(f)<0$ and wealth decays almost surely. The quantitative advice that follows is therefore not "size it optimally" but "if the edge is not demonstrably positive net of all frictions, the optimal exposure is none." The barbell in the standard tier is the practical compromise for those who will speculate regardless: cap the speculative sleeve so that its worst case — total loss, the honest base rate for a negative-expectation game played to the limit — leaves the stable core and the essentials untouched.

## References and further reading

- Barber, B. M., & Odean, T. (2000). *Trading Is Hazardous to Your Wealth: The Common Stock Investment Performance of Individual Investors.* Journal of Finance, 55(2).
- Barber, B. M., & Odean, T. (2001). *Boys Will Be Boys: Gender, Overconfidence, and Common Stock Investment.* Quarterly Journal of Economics, 116(1).
- Barber, B. M., Lee, Y.-T., Liu, Y.-J., & Odean, T. (2011, 2014). *The Cross-Section of Speculator Skill: Evidence from Day Trading* (Taiwan). Journal of Financial Markets.
- Sharpe, W. F. (1991). *The Arithmetic of Active Management.* Financial Analysts Journal, 47(1).
- Kahneman, D., & Tversky, A. (1979). *Prospect Theory: An Analysis of Decision under Risk.* Econometrica, 47(2). Tversky & Kahneman (1992), cumulative prospect theory.
- Barberis, N., & Huang, M. (2008). *Stocks as Lotteries: The Implications of Probability Weighting for Security Prices.* American Economic Review, 98(5).
- Bhattacharya, U., et al. Work on retail investor performance, product complexity, and structured-product / warrant losses (e.g., German discount-broker and warrant studies) documenting systematic underperformance of active retail flow.
- Kelly, J. L. (1956). *A New Interpretation of Information Rate.* Bell System Technical Journal — growth-optimal sizing; see the *Position Sizing* article.
- *Educational material only; not investment advice.*
