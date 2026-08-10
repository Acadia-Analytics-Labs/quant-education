# Orders, Slippage & Transaction Costs: Implementation Shortfall and Optimal Execution

Transaction costs are not a nuisance to be bolted onto a backtest — they are a **first-order determinant of realizable Sharpe** and the binding constraint on strategy capacity. This note decomposes the cost of turning a target trade into fills (Perold's *implementation shortfall*), derives the square-root market-impact law, sketches the Almgren–Chriss execution trade-off, and shows why net Sharpe collapses relative to gross Sharpe as assets grow.

## 1. Implementation shortfall, defined

Perold (1988) defines the cost of execution as the return gap between a frictionless **paper portfolio** that transacts the full target instantly at the decision price and the **real portfolio** you actually achieve. Fix a buy program (sells are symmetric under sign reversal) with

- $P_d$ — decision price (quote when the signal fired),
- $P_0$ — arrival price (quote when trading begins),
- $\bar P$ — volume-weighted average price of executed shares,
- $P_T$ — terminal reference price (e.g. the close) used to value unfilled shares,
- $X$ — target quantity, $x \le X$ — quantity actually executed.

The paper portfolio buys $X$ at $P_d$; the real portfolio buys $x$ at $\bar P$ and leaves $X-x$ untraded. In dollars, the total shortfall is

$$\text{IS} \;=\; \underbrace{x\,(\bar P - P_d)}_{\text{realized cost}} \;+\; \underbrace{(X - x)\,(P_T - P_d)}_{\text{opportunity cost}} \;+\; \text{fees}.$$

### Decomposition into economically distinct buckets

Insert the arrival price $P_0$ into the realized-cost term:

$$x(\bar P - P_d) \;=\; \underbrace{x(P_0 - P_d)}_{\text{delay / timing}} \;+\; \underbrace{x(\bar P - P_0)}_{\text{execution cost}},$$

and split execution cost into the price you concede crossing the book plus the price you move:

$$\bar P - P_0 \;=\; \tfrac{1}{2}\,s \;+\; \mathcal{I},$$

where $s$ is the effective spread and $\mathcal{I}$ is market impact. The five orthogonal components are therefore:

| Bucket | Term | Driver |
|---|---|---|
| Spread | $\tfrac12 s \cdot x$ | crossing bid–ask |
| Market impact | $\mathcal{I}\cdot x$ | own-order pressure |
| Delay / timing | $x(P_0 - P_d)$ | drift before trading starts |
| Opportunity cost | $(X-x)(P_T - P_d)$ | unfilled shares in a moving market |
| Fees | commissions, taxes | explicit |

The waterfall from gross alpha to net realized edge:


```chart
slippage_costs()
```


The subtle bucket is **opportunity cost**: it is the cost of *passivity*. A limit order that never fills has zero spread and zero impact, yet in a rising market it forfeits $(X-x)(P_T - P_d)$ — the "free" limit order is not free. This is the fundamental tension of execution: aggressiveness pays spread and impact; passivity pays timing and opportunity cost.

## 2. The square-root law of market impact

Empirically, across asset classes and decades, the impact of executing $Q$ shares in a name with average daily volume $V$ and (daily) return volatility $\sigma$ obeys the concave **square-root law**

$$\mathcal{I} \;\approx\; Y\,\sigma\,\sqrt{\frac{Q}{V}}, \qquad Y = O(1).$$

**Heuristic derivation.** To absorb your order imbalance, liquidity providers warehouse inventory and must be compensated for the price risk borne until they can unwind it. If you participate at a bounded rate, the time to work $Q$ shares scales as $\tau \propto Q/V$. Over that horizon the inventory's price risk is $\sigma\sqrt{\tau}$ (a random walk accumulates standard deviation like $\sqrt{\text{time}}$). Charging in proportion to the risk absorbed gives

$$\mathcal{I} \;\propto\; \sigma\sqrt{\tau} \;\propto\; \sigma\sqrt{Q/V}.$$

The key structural fact is **concavity**: doubling size raises impact by only $\sqrt{2}\approx 1.41\times$, not $2\times$. Linear-impact models (Kyle's $\lambda$, where $\mathcal{I}=\lambda Q$) are the right local approximation for a *single* small slice but overstate the cost of large parent orders, which is why they are worked as many small children.

## 3. Optimal execution: the Almgren–Chriss trade-off

Splitting a parent order over time reduces impact but exposes you to price drift — **timing risk**. Almgren & Chriss (2000) formalize the trade-off. Liquidate $X$ over $[0,T]$ with holdings $x(t)$, $x(0)=X$, $x(T)=0$, and trade rate $v(t) = -\dot x(t)$. With linear temporary impact $h(v)=\eta v$, the execution-cost and cost-variance are

$$\mathbb{E}[C] = \int_0^T \eta\,v(t)^2\,dt, \qquad \operatorname{Var}(C) = \sigma^2 \int_0^T x(t)^2\,dt.$$

Minimizing the mean–variance objective $\mathbb{E}[C] + \lambda\operatorname{Var}(C)$ via the Euler–Lagrange equation $\eta\,\ddot x = \lambda\sigma^2 x$ yields the exponential trajectory

$$x(t) = X\,\frac{\sinh\!\big(\kappa(T-t)\big)}{\sinh(\kappa T)}, \qquad \kappa = \sqrt{\frac{\lambda\sigma^2}{\eta}}.$$

Higher risk aversion $\lambda$ (larger $\kappa$) front-loads trading to cut exposure; risk-neutrality flattens it.

### TWAP as the risk-neutral optimum

Set $\lambda = 0$ (pure cost minimization). We minimize $\int_0^T v(t)^2\,dt$ subject to $\int_0^T v(t)\,dt = X$. By Cauchy–Schwarz,

$$\left(\int_0^T v\,dt\right)^{2} \le T \int_0^T v^2\,dt \;\;\Longrightarrow\;\; \int_0^T v^2\,dt \;\ge\; \frac{X^2}{T},$$

with equality **iff $v(t)$ is constant**. The optimal schedule is therefore $v(t)=X/T$ — a flat, uniform-in-time trajectory. This is exactly **TWAP** (time-weighted average price). **VWAP** generalizes it by matching the participation schedule to the intraday volume curve $u(t)$, i.e. $v(t)\propto u(t)$, which minimizes participation-rate variance and hence realized impact when volume is non-uniform. TWAP is the special case of a flat volume profile.

## 4. Why net Sharpe $\ll$ gross Sharpe at scale

Let a strategy generate, per trade, gross alpha $\alpha$ (in return units), idiosyncratic volatility $s$, and round-trip cost $c$. Over $N$ approximately independent trades per year the annualized Sharpe ratios are

$$\text{SR}_{\text{gross}} = \frac{\alpha}{s}\sqrt{N}, \qquad \text{SR}_{\text{net}} = \frac{\alpha - c}{s}\sqrt{N}, \qquad \frac{\text{SR}_{\text{net}}}{\text{SR}_{\text{gross}}} = 1 - \frac{c}{\alpha}.$$

Two forces drive the ratio toward zero as capital grows:

1. **Cost rises with size.** Deploying more AUM forces larger $Q$, and by the square-root law $c(Q) = \tfrac12 s_0 + \kappa\,\sigma\sqrt{Q/V}$ grows without bound. When $c(Q) \to \alpha$, net Sharpe $\to 0$; beyond it, net edge is *negative*.
2. **Turnover multiplies the toll.** To put more money to work you often trade more (larger $N$), and every trade pays $c$. High-turnover, small-$\alpha$ strategies have almost no room: a 1 bp cost against a 1.5 bp gross edge is a coin flip after frictions.

**Capacity** is the AUM at which the marginal trade's net edge vanishes, $c(Q^\star) = \alpha$:

$$\kappa\,\sigma\sqrt{\frac{Q^\star}{V}} = \alpha - \tfrac12 s_0 \quad\Longrightarrow\quad Q^\star = V\left(\frac{\alpha - \tfrac12 s_0}{\kappa\,\sigma}\right)^{2}.$$

Capacity scales **linearly with liquidity** $V$ and **quadratically with net-of-spread edge** — a reason large funds chase liquid, high-alpha signals and abandon crowded, low-margin ones.

The consolation: a positive *net* edge, however small, still compounds toward near-certainty over many independent trades — provided it clears costs. The entire game is keeping $\alpha - c > 0$.


```chart
many_small_bets(edge=0.02)
```


## 5. Practical estimators and pitfalls

- **Effective spread** $\;s_{\text{eff}} = 2\,|P_{\text{trade}} - m|$, where $m$ is the prevailing mid — the realized cost, which can exceed the quoted spread for size.
- **Backtest realism.** Fills at the mid, or worse at the *next bar's open*, embed look-ahead and understate cost. Model a half-spread crossing plus a $\sigma\sqrt{Q/V}$ impact term, and cap fills at a fraction of bar volume.
- **Cost is convex and correlated with alpha.** Impact is largest exactly when signals are strongest (everyone trades the same way), so realized cost is worse than an unconditional average suggests.
- **Report net.** Deflate Sharpe for cost *and* for selection (López de Prado): the strategy chosen as best-of-many overstates both edge and its cost-resilience.

## References & further reading

- Perold, A. F. (1988). *The Implementation Shortfall: Paper versus Reality.* Journal of Portfolio Management.
- Almgren, R. & Chriss, N. (2000). *Optimal Execution of Portfolio Transactions.* Journal of Risk.
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* Econometrica (the linear-impact $\lambda$).
- Kissell, R. (2013). *The Science of Algorithmic Trading and Portfolio Management.*
- Tóth, B. et al. (2011). *Anomalous Price Impact and the Critical Nature of Liquidity.* Phys. Rev. X (the square-root law).
- Grinold, R. & Kahn, R. (1999). *Active Portfolio Management* (turnover, transfer coefficient, net alpha).
- López de Prado, M. (2018). *Advances in Financial Machine Learning* (deflated Sharpe, execution).
