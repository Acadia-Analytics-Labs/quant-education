# Discounted Cash Flow: Derivation, Cost of Capital, and Fragility

## 1. The valuation identity

Under the standard no-arbitrage / time-value argument, the value of a claim to a stream of cash flows is the sum of those flows discounted at the appropriate risk-adjusted rate. For a firm generating unlevered free cash flow $FCF_t$, discounted at the weighted average cost of capital $r$, with an explicit horizon of $n$ years and a terminal value $TV_n$ capturing all cash after year $n$:

$$
V_0 = \sum_{t=1}^{n} \frac{FCF_t}{(1+r)^t} + \frac{TV_n}{(1+r)^n}.
$$

$V_0$ is the **enterprise value**. Equity value follows from the capital-structure bridge

$$
E_0 = V_0 - D_{\text{net}}, \qquad P_0 = \frac{E_0}{N_{\text{shares}}} = \frac{V_0 - D_{\text{net}}}{N_{\text{shares}}},
$$

where $D_{\text{net}}$ is net debt (gross debt minus cash) and $N_{\text{shares}}$ is diluted shares outstanding.


```mermaid
flowchart LR
  A["Enterprise Value V0<br/>(PV of unlevered FCF + PV of TV)"] --> B["minus net debt D_net"]
  B --> C["Equity Value E0"]
  C --> D["divide by shares N"]
  D --> E["Intrinsic price per share P0"]
```


The choice of **unlevered** FCF discounted at WACC is deliberate and internally consistent: the numerator is the cash available to *all* capital providers, and the denominator is their blended required return. Using levered FCF (cash to equity only) would instead require discounting at the cost of equity $r_e$ — the flows-to-equity method. Mixing them is the most common valuation error.

## 2. Terminal value as an infinite geometric series (derivation)

The Gordon growth terminal value is not an ad-hoc formula; it is the closed form of a convergent geometric series. Assume that from year $n$ onward, unlevered FCF grows at a constant rate $g$ in perpetuity, so $FCF_{n+k} = FCF_n (1+g)^k$. The value **at time $n$** of all subsequent flows is

$$
TV_n = \sum_{k=1}^{\infty} \frac{FCF_{n+k}}{(1+r)^k} = FCF_n \sum_{k=1}^{\infty} \left(\frac{1+g}{1+r}\right)^{k}.
$$

Let $x = \dfrac{1+g}{1+r}$. The series $\sum_{k=1}^{\infty} x^k$ converges **iff** $|x| < 1$, i.e. iff $r > g$. When it converges,

$$
\sum_{k=1}^{\infty} x^k = \frac{x}{1-x}.
$$

Substituting $x = (1+g)/(1+r)$ and simplifying,

$$
\frac{x}{1-x} = \frac{\frac{1+g}{1+r}}{1 - \frac{1+g}{1+r}} = \frac{1+g}{(1+r) - (1+g)} = \frac{1+g}{r - g}.
$$

Therefore

$$
\boxed{\,TV_n = \frac{FCF_n (1+g)}{r-g}\,}
$$

and its present value is $TV_n/(1+r)^n$. Two structural consequences fall directly out of the derivation:

- **Convergence requires $r > g$.** If $g \ge r$ the series diverges: the model returns infinite (or negative, nonsensical) value. Economically, no firm can grow its cash flows faster than its cost of capital forever, which is also why $g$ is bounded above by long-run nominal GDP growth.
- The formula prices a growing perpetuity *starting one period after $n$*; the $(1+g)$ in the numerator advances $FCF_n$ to the first post-horizon flow $FCF_{n+1}$.

## 3. The discount rate: WACC and CAPM

The discount rate is the value-weighted required return of the firm's capital providers. With market values of equity $E$ and debt $D$, total capital $V = E + D$, and marginal tax rate $\tau$:

$$
WACC = \frac{E}{V}\, r_e + \frac{D}{V}\, r_d (1 - \tau).
$$

The factor $(1-\tau)$ is the **interest tax shield**: interest is tax-deductible, so the effective after-tax cost of debt is $r_d(1-\tau)$. (Adding preferred stock generalizes this to a three-term weighted average with weight $w_p$ and cost $r_p$, untaxed.)

The cost of equity is not observable and is estimated via the **CAPM**, the equilibrium relation of the security market line:

$$
r_e = r_f + \beta \,(\mathbb{E}[r_m] - r_f), \qquad \beta = \frac{\operatorname{Cov}(r_e, r_m)}{\operatorname{Var}(r_m)}.
$$

Here $\beta$ measures systematic (non-diversifiable) exposure to the market factor; idiosyncratic risk earns no premium because it is diversifiable. Practically, $\beta$ is estimated by regressing the stock's excess returns on the market's excess returns, then often **unlevered and re-levered** (Hamada) to reflect the firm's target capital structure. Every input — $r_f$, $\beta$, the equity risk premium — is itself an estimate, which propagates directly into $V_0$.

## 4. Why DCF is fragile: sensitivity to $r$ and $g$

Because terminal value routinely constitutes 60–80% of enterprise value, the whole valuation inherits the terminal value's sensitivity to $r$ and $g$. Differentiate $TV_n = FCF_n(1+g)/(r-g)$:

$$
\frac{\partial TV_n}{\partial r} = -\frac{FCF_n(1+g)}{(r-g)^2} = -\frac{TV_n}{r-g},
$$

$$
\frac{\partial TV_n}{\partial g} = \frac{FCF_n\big[(r-g) + (1+g)\big]}{(r-g)^2} = \frac{FCF_n(1+r)}{(r-g)^2} = \frac{TV_n(1+r)}{(1+g)(r-g)}.
$$

Both partials scale as $(r-g)^{-2}$. As the spread $r-g$ narrows, sensitivity **blows up quadratically** — a near-singularity as $g \to r^{-}$. The elasticity of terminal value with respect to the spread makes this concrete: writing $s = r - g$,

$$
TV_n = \frac{FCF_n(1+g)}{s} \;\Longrightarrow\; \frac{\partial \log TV_n}{\partial \log s} = -1,
$$

so a 1% *relative* tightening of the spread produces a 1% *increase* in terminal value — and when $s$ is small (say 5–7%), a mere 100 bp move in $r$ or $g$ is a large fraction of $s$. This is the analytic reason a DCF is only as trustworthy as its two least-knowable inputs. The SampleCo sensitivity grid makes it numeric:

| WACC \ g | 1.0% | 2.0% | 3.0% | 4.0% |
|---|---|---|---|---|
| 8.0% | 19.19 | 21.73 | 25.28 | 30.61 |
| 10.0% | 14.79 | 16.16 | 17.93 | 20.29 |
| 12.0% | 11.99 | 12.83 | 13.86 | 15.14 |

A 4-point box around the base case spans roughly \$12 to \$31 per share — a greater-than-2.5× range from assumptions no one can pin down precisely.

The discounting mechanics — future FCF collapsing toward present value, and the terminal value's outsized weight — are visible here:


```chart
dcf_discounting(r=0.10, g=0.05)
```


## 5. What the model assumes, and where it breaks

- **Constant discount rate.** A single $r$ across all horizons assumes a flat term structure of risk. A theoretically cleaner model discounts each $FCF_t$ at a maturity-matched rate $r_t$; practitioners collapse this to one WACC for tractability, silently mispricing the timing of cash flows.
- **Deterministic cash flows.** The formula treats $FCF_t$ as known. In reality they are random; a rigorous treatment discounts *certainty-equivalent* cash flows or, equivalently, prices with a stochastic discount factor $m_t$ so that $V_0 = \sum_t \mathbb{E}[m_t \, FCF_t]$. Point forecasts hide the distribution.
- **Perpetual constant growth.** The Gordon assumption of a single $g$ forever is an idealization; real firms mean-revert to industry and macro growth. Fade or multi-stage models mitigate this but add more free parameters.
- **Circularity in WACC.** WACC uses market weights $E/V$ and $D/V$, but the DCF is trying to *derive* $E$ — a fixed-point problem usually resolved by assuming a target structure, which imports another assumption.
- **Estimation and selection risk.** Because value is monotone and steep in $g$ and $r$, an analyst can back-solve almost any target price by nudging assumptions inside "reasonable" bands. Discipline (out-of-sample checks on growth, cross-checks against multiples, explicit sensitivity tables) is what separates valuation from motivated reasoning.

Empirically, starting valuation is informative about subsequent long-run returns — richer prices tend to precede lower forward returns — which is the market-level echo of intrinsic value acting as an attractor:


```chart
pe_vs_forward_return()
```


## 6. Summary

A DCF is the geometric-series identity $V_0 = \sum_t FCF_t/(1+r)^t + TV_n/(1+r)^n$ with $TV_n = FCF_n(1+g)/(r-g)$, discounted at a WACC whose equity leg comes from CAPM. Its elegance is that it forces an explicit statement of beliefs about cash generation, capital cost, and long-run growth; its fragility is that the terminal value dominates and depends quadratically on a spread $r-g$ that no one observes. Treat the output as a distribution conditioned on assumptions, never a point estimate of truth.

## References & further reading

- Williams, J. B. (1938). *The Theory of Investment Value.* — the original present-value-of-dividends argument.
- Gordon, M. J. (1959). *Dividends, Earnings, and Stock Prices.* Review of Economics and Statistics. — the constant-growth (Gordon growth) model.
- Sharpe, W. F. (1964); Lintner, J. (1965). — the Capital Asset Pricing Model.
- Modigliani, F. & Miller, M. (1958, 1963). *The Cost of Capital, Corporation Finance and the Theory of Investment.* — capital structure and the tax shield underlying WACC.
- Koller, T., Goedhart, M. & Wessels, D. (McKinsey & Company). *Valuation: Measuring and Managing the Value of Companies.* — the practitioner standard for enterprise DCF.
- Damodaran, A. *Investment Valuation* and *The Dark Side of Valuation.* — estimation of inputs, terminal value discipline, and where DCF fails.

*Educational content, not investment advice.*
