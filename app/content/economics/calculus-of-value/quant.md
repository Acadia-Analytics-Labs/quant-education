# The Calculus of Value: A Quantitative Treatment

Howard Marks' memo *The Calculus of Value* (2025) is, at its core, an informal statement of discounted-cash-flow theory plus a behavioral claim about the discount rate. Here we make the "calculus" literal: we derive the valuation identity, decompose the discount rate, connect sentiment to the equity risk premium, and examine the empirical mean-reversion of valuations that underwrites the claim *high valuation → low forward return*.

## 1. The valuation identity (DCF)

The value of a claim is the present value of the cash flows it delivers. For an equity paying cash flows $CF_t$ and discounted at a required rate $r$,

$$P_0 = \sum_{t=1}^{\infty} \frac{CF_t}{(1+r)^t}.$$

This is the formal content of Marks' "business-school" rule: an asset is worth its future earnings, adjusted for time and risk. Intrinsic value $V_0$ is the same expression evaluated at *fundamentals-justified* cash flows and a *fundamentals-justified* discount rate; price $P_0$ is the market's realized version, and their ratio is **valuation**.

## 2. The Gordon growth model, derived

Assume dividends grow at a constant rate $g < r$, so $D_t = D_0 (1+g)^t$. Then

$$P_0 = \sum_{t=1}^{\infty} \frac{D_0(1+g)^t}{(1+r)^t} = D_0 \sum_{t=1}^{\infty} x^t, \qquad x \equiv \frac{1+g}{1+r} < 1.$$

The tail is an infinite geometric series. For $|x|<1$, $\sum_{t=1}^{\infty} x^t = \dfrac{x}{1-x}$. Substituting,

$$P_0 = D_0 \cdot \frac{x}{1-x} = D_0 \cdot \frac{\frac{1+g}{1+r}}{1 - \frac{1+g}{1+r}} = D_0 \cdot \frac{1+g}{(1+r)-(1+g)} = \frac{D_0(1+g)}{r-g}.$$

Writing $D_1 = D_0(1+g)$ for next period's dividend gives the **Gordon growth formula**:

$$\boxed{\,P_0 = \frac{D_1}{r - g}\,}$$

Rearranging exposes the expected return as **dividend yield plus growth**:

$$r = \frac{D_1}{P_0} + g.$$

Two structural facts matter for Marks' argument. First, $P_0$ is *hyperbolically* sensitive to the spread $r-g$: as $r \to g^+$, $P_0 \to \infty$. Small shifts in the discount rate produce large swings in price when $r-g$ is small — exactly the fragile regime that breeds bubbles. Second, the earnings/dividend yield is a first-order proxy for the discount rate net of growth, which is why the P/E ratio functions as a valuation gauge (§4).

## 3. The discount rate, and how sentiment moves it

Decompose the required return into a risk-free rate and an equity risk premium (ERP):

$$r = r_f + \pi, \qquad \pi = \text{ERP}.$$

Fundamentals pin down $r_f$ (via the term structure) and a "rational" $\pi$ (via consumption risk, leverage, cash-flow covariance). But the *realized* $\pi$ is a behavioral quantity. Marks' claim is that sentiment sets the effective discount rate:

- **Optimism / greed** compresses $\pi \downarrow \Rightarrow r \downarrow \Rightarrow P_0 \uparrow$ (multiple expansion, bubble).
- **Fear / capitulation** widens $\pi \uparrow \Rightarrow r \uparrow \Rightarrow P_0 \downarrow$ (multiple contraction, crash).

Because $P_0 = D_1/(r-g)$, a swing in $\pi$ of even 100–200 bps re-rates price sharply when $r-g$ is small. Sentiment thus drives short-run price *without any change in fundamentals* — value is unmoved while price detaches. This is the mechanism behind the "value is a magnet, price wanders" picture:

```chart
price_value_convergence()
```

## 4. From the model to the multiple: P/E and CAPE

Under Gordon growth with payout ratio $b = D_1/E_1$, the forward P/E is

$$\frac{P_0}{E_1} = \frac{b}{r - g},$$

so a high multiple encodes some combination of a low discount rate (rich sentiment), high expected growth, or a high payout. The trouble is that single-year earnings $E_1$ are cyclical. Graham & Dodd recommended averaging earnings over a full cycle; Shiller operationalized this as the **cyclically adjusted P/E (CAPE)**:

$$\text{CAPE}_t = \frac{P_t}{\frac{1}{10}\sum_{i=1}^{10} E_{t-i}^{\text{real}}},$$

price divided by the trailing 10-year average of inflation-adjusted earnings. CAPE strips out the cyclical noise in $E$ and isolates the valuation state.

## 5. Valuation predicts forward returns

The empirical backbone of Marks' thesis is the regression of subsequent long-horizon real returns on starting valuation. Using CAPE,

$$R_{t \to t+10}^{\text{real}} = \alpha + \beta \cdot \frac{1}{\text{CAPE}_t} + \varepsilon_t \qquad (\beta > 0),$$

or equivalently regressing the return on the *level* of CAPE yields a **negative slope**. Historically this relationship carries an $R^2$ of roughly **0.3–0.4** at the 10-year horizon — modest but among the most robust predictive relationships in equities. Starting valuation explains a meaningful share of the variance in decade-ahead returns; it explains almost none of next month's.

```chart
pe_vs_forward_return()
```

The mechanism is not magic — it is the arithmetic of §2 combined with mean reversion (§6): buying at a low earnings yield ($1/(P/E)$) mechanically locks in a low forward return unless growth surprises to the upside, and a rich multiple has more room to contract than to expand.

## 6. Mean reversion of valuations

Fundamentals ($E$, $D$) trend; valuations do not. The P/E and CAPE are **bounded, stationary-like** ratios — they cannot drift to infinity or zero — so deviations from their long-run mean tend to revert:

$$\text{CAPE}_{t+1} - \mu = \phi\,(\text{CAPE}_t - \mu) + u_{t+1}, \qquad 0 < \phi < 1.$$

An AR(1) with $\phi<1$ pulls the ratio back toward $\mu$; the half-life is $\ln(0.5)/\ln\phi$. This stationarity is the formal version of Marks' "magnet." A CAPE far above $\mu$ is expected to fall, and since $P = \text{CAPE} \times \bar E^{\text{real}}$, the reversion of the multiple is a headwind on price precisely when starting valuation is high.

## 7. Decomposing returns: growth vs. re-rating

Marks distinguishes returns from *fundamental change* and from *valuation change*. Make it exact. Since $P = (P/E)\cdot E$, take logs and difference:

$$\underbrace{\Delta \ln P}_{\text{price return}} = \underbrace{\Delta \ln E}_{\text{fundamental growth}} + \underbrace{\Delta \ln (P/E)}_{\text{multiple re-rating}}.$$

Adding the dividend yield $D/P$ gives the standard total-return decomposition,

$$R_{\text{total}} \approx \underbrace{\frac{D}{P}}_{\text{income}} + \underbrace{g_E}_{\text{earnings growth}} + \underbrace{\Delta\ln(P/E)}_{\text{re-rating}}.$$

The first two terms are durable and fundamentals-driven; the third is a **sentiment transfer** that is zero-sum over a full cycle (multiples that expand must eventually contract). High starting valuations bias the re-rating term negative over the subsequent decade — the quantitative content of "high valuations presage low returns."

### The dynamic-Gordon (Campbell–Shiller) view

The clean-form Gordon model assumes constant $r,g$. Campbell & Shiller (1988) log-linearized the return identity to relax that. Defining the log dividend-price ratio, the approximate present-value identity is

$$d_t - p_t \approx \text{const} + \mathbb{E}_t\!\left[\sum_{j=0}^{\infty} \rho^{j}\big(r_{t+1+j} - \Delta d_{t+1+j}\big)\right], \qquad \rho \approx \frac{1}{1+\exp(\overline{d-p})}.$$

A high price relative to dividends (low $d_t-p_t$) must be justified by *either* high future dividend growth *or* low future returns. Empirically, most of the variation loads onto the **returns** term, not the growth term — valuation ratios forecast returns, not dividend growth. This is the econometric foundation under Marks' informal calculus.

## 8. Where the framework strains

- **$r$ and $g$ are latent and unstable.** Point estimates of the ERP and long-run growth are noisy; the hyperbolic sensitivity near $r=g$ means the model is ill-conditioned exactly in the high-valuation regime it is used to judge.
- **Predictive $R^2$ is horizon-dependent.** The CAPE relationship is strong at 10 years and near-useless at 1 year. Convergence timing is unforecastable — Marks' explicit caution against betting on *when*.
- **Regime change in the denominator.** Structural shifts (buybacks replacing dividends, intangible-heavy earnings, secularly lower $r_f$) can raise the equilibrium multiple $\mu$, so a naive "revert to the historical mean" over-predicts return drag.
- **Overlapping observations.** 10-year-ahead returns sampled monthly are massively autocorrelated; the true standard errors are far wider than OLS reports (Hodrick / Newey–West corrections are essential), which tempers confidence in the slope even where the sign is reliable.

## References & further reading

- Marks, H. (2025). *The Calculus of Value.* Oaktree Capital Management memo, August 13, 2025.
- Graham, B. & Dodd, D. (1934). *Security Analysis.* (Origin of cycle-averaged earnings and the price-vs-value discipline.)
- Williams, J. B. (1938). *The Theory of Investment Value.* (Dividend discount model.)
- Gordon, M. J. (1959). *Dividends, Earnings, and Stock Prices.* Rev. Econ. Stat.
- Shiller, R. J. (2000, rev. 2015). *Irrational Exuberance.* (CAPE and valuation-based return prediction.)
- Campbell, J. Y. & Shiller, R. J. (1988). *The Dividend-Price Ratio and Expectations of Future Dividends and Discount Factors.* Rev. Financial Studies.
- Campbell, J. Y. & Shiller, R. J. (1998). *Valuation Ratios and the Long-Run Stock Market Outlook.* J. Portfolio Management.
