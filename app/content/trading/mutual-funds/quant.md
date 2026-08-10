# Mutual Funds: NAV Mechanics, Fee Drag, and the Arithmetic of Active Management

A mutual fund is an open-end pooled vehicle whose share count is elastic: shares are issued and redeemed on demand at net asset value rather than traded between investors on a secondary market. Four quantitative consequences follow from that single structural fact. NAV is an accounting identity, not a market price. End-of-day pricing creates a dilution channel when the underlying marks are stale. Fees impose a deterministic geometric drag. And the redemption mechanism — cash rather than in-kind — imposes a tax externality that the ETF wrapper avoids. We derive each.

## 1. The NAV identity and elastic share supply

Let $A_t$ be the market value of fund assets, $L_t$ liabilities (accrued fees, payables), and $N_t$ shares outstanding. Then

$$\text{NAV}_t = \frac{A_t - L_t}{N_t}.$$

Because a subscription of cash $c$ increases both the numerator and, at the transaction price, the denominator by $c/\text{NAV}_t$, the identity is invariant to flow:

$$\text{NAV}_t' = \frac{(A_t + c) - L_t}{N_t + c/\text{NAV}_t} = \frac{A_t - L_t + c}{\frac{(A_t - L_t) + c}{\text{NAV}_t}} = \text{NAV}_t.$$

Transacting at NAV is therefore *exactly* the non-dilutive price: an incoming investor neither gains from nor imposes a cost on existing holders. This is the structural claim of the open-end form, and §2 is the story of when it fails.

Note the contrast with the closed-end and ETF cases. There $N_t$ is fixed over short horizons, secondary-market price $P_t$ is set by supply and demand, and the premium/discount $\pi_t = P_t/\text{NAV}_t - 1$ is a free variable. In an open-end fund $\pi_t \equiv 0$ by construction — the fund *is* the counterparty.

## 2. Forward pricing and the stale-price dilution channel

Suppose the fund holds securities whose last recorded prices are stale — foreign equities that closed hours earlier, illiquid small caps, thinly traded bonds. Write the stale NAV as $\text{NAV}_t^{\text{stale}}$ and the unobserved fair value as $\text{NAV}_t^{\ast}$, with

$$\text{NAV}_t^{\ast} = \text{NAV}_t^{\text{stale}}(1 + \delta_t), \qquad \mathbb{E}[\delta_t \mid \mathcal{I}_t] \neq 0,$$

where $\mathcal{I}_t$ is public information available before the cutoff (say, the U.S. session's move, which predicts tomorrow's Tokyo open). A timer who subscribes when $\delta_t > 0$ buys a claim worth $\text{NAV}^{\ast}$ for $\text{NAV}^{\text{stale}}$.

Quantify the transfer. Let the fund have $N$ shares and receive $m$ timing shares at the stale price. Post-subscription, the correctly valued pool is $N\,\text{NAV}^{\ast} + m\,\text{NAV}^{\text{stale}}$ spread over $N + m$ shares, so the fair post-trade value per share is

$$\widetilde{\text{NAV}} = \frac{N\,\text{NAV}^{\ast} + m\,\text{NAV}^{\text{stale}}}{N+m}.$$

The loss borne by each incumbent share is

$$\text{NAV}^{\ast} - \widetilde{\text{NAV}} = \frac{m\left(\text{NAV}^{\ast} - \text{NAV}^{\text{stale}}\right)}{N+m} = \frac{m}{N+m}\,\delta_t\,\text{NAV}^{\text{stale}},$$

so aggregate dilution is $\frac{Nm}{N+m}\delta_t \text{NAV}^{\text{stale}}$ — increasing in both the staleness $\delta_t$ and the timer's size $m$. This is not a hypothetical: it is the arithmetic behind the 2003 market-timing scandals, and the reason funds now apply **fair-value pricing** to stale marks, short-term redemption fees, and hard cutoffs. Forward pricing (you get the *next* struck NAV, never the last one) is the first line of defence — it removes the option to transact at an already-known price.

## 3. Fee drag as deterministic geometric decay

Let gross annual return be $g$ and the total expense ratio $f$, accrued daily but expressible as an annual net factor $(1 + g - f)$. Relative terminal wealth after $T$ years is

$$\frac{W_T^{\text{net}}}{W_T^{\text{gross}}} = \left(\frac{1+g-f}{1+g}\right)^{T} = \left(1 - \frac{f}{1+g}\right)^{T}.$$

Take logs, and with $x = f/(1+g) \ll 1$ use $\log(1-x) = -x - x^2/2 - O(x^3)$:

$$\log\frac{W_T^{\text{net}}}{W_T^{\text{gross}}} = T\log(1-x) \approx -Tx \;\Longrightarrow\; \frac{W_T^{\text{net}}}{W_T^{\text{gross}}} \approx \exp\!\left(-\frac{fT}{1+g}\right).$$

The shortfall is $1 - e^{-fT/(1+g)} \approx fT/(1+g)$ to first order — **linear in the fee and linear in the horizon**. At $g = 0.07$ and $T = 30$, an active fund at $f = 0.0075$ versus an index fund at $f = 0.0004$ gives $\Delta f = 0.0071$ and a shortfall of about $0.0071 \times 30 / 1.07 \approx 0.20$: the active investor ends roughly 20% poorer for identical gross performance. On a \$250,000 terminal stake that is about \$50,000 surrendered to costs.

```chart
expense_ratio_drag()
```

The qualitative point is that fee drag is a *rate* applied to an exponentially growing base. It is linear in log-wealth but super-linear in dollars, so the absolute damage is concentrated in the final years — exactly the years a retirement saver cares about most.

## 4. Sharpe's arithmetic: why the average active dollar must lose

Partition all dollars invested in a market into passive ($P$) and active ($A$) sets. Passive dollars hold the market portfolio by construction. Since the union of all dollars *is* the market,

$$w_P R_P + w_A R_A = R_M, \qquad w_P + w_A = 1,$$

where returns are gross of costs and $w$ denotes the value-weight of each set. Passive investors hold the market, so $R_P = R_M$. Substituting:

$$w_P R_M + w_A R_A = R_M \;\Longrightarrow\; w_A R_A = R_M(1 - w_P) = w_A R_M \;\Longrightarrow\; R_A = R_M.$$

**Before costs, the average actively managed dollar earns exactly the market return.** This is an accounting identity, not an empirical claim — it holds in every period, in every market, regardless of manager skill. Now subtract costs $c_A$ and $c_P$:

$$\mathbb{E}\!\left[R_A^{\text{net}}\right] - \mathbb{E}\!\left[R_P^{\text{net}}\right] = -(c_A - c_P) < 0 \quad \text{whenever } c_A > c_P.$$

The average active dollar must underperform the average passive dollar by precisely the cost differential. Note carefully what this does *not* say: it is a statement about the value-weighted average, not about any individual fund. Skill can exist and be large; it is simply zero-sum across active participants gross of fees, so the aggregate shortfall is fully determined by costs.

The distribution around that mean is what the empirical literature studies. Fama and French (2010) find that after costs, the cross-section of fund alphas is close to what pure chance would generate, with a left tail too fat to be luck alone. Berk and Green (2004) supply the equilibrium explanation: skilled managers attract flows until decreasing returns to scale drive net alpha to zero, so skill accrues to the manager as fee revenue rather than to the investor as return.

```chart
diversification_smoothing()
```

Diversification, by contrast, is not zero-sum — it is the one free lunch, and it is exactly what the pooled structure delivers.

## 5. The tax externality of cash redemptions

This is where the mutual fund structurally loses to the ETF. When an investor redeems, an open-end fund typically sells securities for cash. Realised gains must be distributed to *all* remaining shareholders, who owe tax on them regardless of their own trading.

Let the fund hold unrealised appreciation fraction $u$ (embedded gain as a share of NAV), face redemptions of fraction $\rho$ of assets, and let $\tau$ be the shareholder's capital gains rate. Forced sales realise approximately $\rho u$ of NAV as gain, so the per-share after-tax drag on a non-redeeming holder is

$$d = \tau \rho u.$$

With $\tau = 0.20$, $\rho = 0.15$, and an overhang $u = 0.30$, that is $d = 0.009$ — 90 basis points a year, comparable to the entire expense ratio, and invisible on any fee disclosure. It also produces the counterintuitive outcome noted in the standard tier: a fund can post a **negative** annual return and still hand you a taxable gain, because $\rho$ and $u$ are driven by other investors' redemptions and the manager's cost basis, not by your holding period.

The ETF wrapper avoids this because redemptions are settled **in kind** — the authorised participant receives securities, not cash, and §852(b)(6) of the Internal Revenue Code exempts that distribution from gain recognition. The fund can even hand out its lowest-basis lots, cleansing the overhang. This is a wrapper effect, not a strategy effect: two funds with identical holdings and identical gross returns differ in after-tax return purely by structure. It applies only in taxable accounts — inside a 401(k) or IRA the distinction vanishes, which is precisely why mutual funds remain dominant in retirement plans.

## 6. Where the clean story breaks

- **The fee is not the whole cost.** The expense ratio excludes trading commissions, bid-ask spreads, and market impact from portfolio turnover. For a high-turnover active fund these can rival the disclosed fee, so the $f$ in §3 understates the true drag.
- **Cash drag.** Open-end funds hold a liquidity buffer against redemptions. A 3% cash position in a market returning 8% costs roughly 24 basis points a year — a structural cost of the redemption promise itself.
- **Flow-performance asymmetry.** Retail flows chase past returns, so the dollar-weighted return earned by investors is systematically below the fund's time-weighted return. The published performance figure is not what the average investor received.
- **Survivorship bias.** Poor funds are merged or liquidated. Trailing performance tables computed on surviving funds overstate the category's historical return, biasing any naive test of §4's prediction toward active management.
- **The identity in §4 is value-weighted, not equal-weighted.** A simple average across funds does not obey it, and neither does any self-selected subset — a frequent misreading.
- **Money market funds are not riskless.** The stable \$1.00 NAV is a convention, not a guarantee; the Reserve Primary Fund broke the buck in September 2008, which is why institutional prime funds now float their NAV.

## References & further reading

- Sharpe, W. F. (1991). *The Arithmetic of Active Management.* Financial Analysts Journal 47(1) — the identity derived in §4.
- Bogle, J. C. (2017). *The Little Book of Common Sense Investing*, 2nd ed. Wiley — the cost-minimisation thesis and the "cost matters hypothesis."
- Carhart, M. M. (1997). *On Persistence in Mutual Fund Performance.* Journal of Finance 52(1) — four-factor evaluation; persistence is largely momentum and expenses.
- Fama, E. F., & French, K. R. (2010). *Luck versus Skill in the Cross-Section of Mutual Fund Returns.* Journal of Finance 65(5).
- Berk, J. B., & Green, R. C. (2004). *Mutual Fund Flows and Performance in Rational Markets.* Journal of Political Economy 112(6) — the decreasing-returns-to-scale equilibrium.
- Zitzewitz, E. (2003). *Who Cares About Shareholders? Arbitrage-Proofing Mutual Funds.* Journal of Law, Economics & Organization 19(2) — the dilution arithmetic of §2.
- Dickson, J. M., & Shoven, J. B. (1995). *Taxation and Mutual Funds: An Investor Perspective.* Tax Policy and the Economy 9 — after-tax return measurement.
- Jensen, M. C. (1968). *The Performance of Mutual Funds in the Period 1945–1964.* Journal of Finance 23(2) — the original alpha study.

*Educational content, not investment advice.*
