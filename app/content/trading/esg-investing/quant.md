# ESG as a Risk Factor: Signal, Noise, and Aggregate Confusion

ESG investing raises a precise empirical question that its marketing usually blurs: **is "ESG" a priced factor that earns risk-adjusted return, or is it a noisy relabeling of exposures we already know how to price?** Answering it forces us through factor attribution, the statistics of disagreeing raters, the materiality distinction, and the selection biases that contaminate the whole literature. This note treats ESG as a measurement and estimation problem, not a moral one.

## 1. Factor-model framing: does ESG earn alpha or load on known factors?

Take a long–short ESG portfolio (long high-rated, short low-rated). Its excess return $r_{ESG,t}$ can be projected onto standard factors:

$$r_{ESG,t} = \alpha + \beta_{M} \, \text{MKT}_t + \beta_{S}\, \text{SMB}_t + \beta_{H}\, \text{HML}_t + \beta_{R}\, \text{RMW}_t + \beta_{C}\, \text{CMA}_t + \beta_{W}\, \text{WML}_t + \varepsilon_t$$

The empirical regularities are robust across studies:

- High-ESG firms tilt toward **large-cap** (negative SMB loading), **profitable/quality** (positive RMW), and **low-volatility / low-beta** names. This is nearly mechanical: governance and disclosure quality correlate with size, and large mature firms have both the resources to report ESG data and the profitability that quality screens reward.
- Once you control for these loadings, the **intercept $\alpha$ is typically small and statistically fragile**. Much of the raw ESG "outperformance" in backtests is a **quality/size premium in disguise**, plus a repricing effect.
- **Repricing vs. expected return.** Pedersen, Fitzgibbons & Pomorski (2021) formalize an "ESG-efficient frontier": ESG can help (it carries information about fundamentals), hurt (it constrains the opportunity set), or be neutral, depending on whether ESG predicts returns beyond risk. Separately, a flow-driven repricing (Pástor, Stambaugh & Taylor 2021) means that as demand for green assets rises, green stocks earn **lower** expected returns in equilibrium even if they **realize** higher returns during the transition. Realized ≠ expected: a green-minus-brown series can be positive in-sample precisely because the discount rate on green assets fell.

**Takeaway:** the honest null is that ESG's marginal alpha is close to zero after controlling for quality, size, and low-risk. Where ESG adds value, it is more defensible as **risk management** — reducing exposure to tail events (regulatory, litigation, reputational) — than as a standalone alpha source.

## 2. The rating-divergence problem, quantified

The deepest empirical obstacle is that the independent variable itself is poorly identified. Berg, Kölbl & Rigobon (2022), *"Aggregate Confusion: The Divergence of ESG Ratings"* (Review of Finance), measure agreement across six major raters:

- **Pairwise correlations average ≈ 0.54, ranging roughly 0.38 to 0.71.** Contrast credit ratings, where Moody's and S&P correlate near **0.99**. The same firm can sit in the top decile for one provider and the bottom half for another.

```chart
esg_rating_divergence()
```

Berg et al. decompose the divergence into three sources via a common taxonomy of indicators:

$$\text{Divergence} = \underbrace{\text{Scope}}_{\text{which categories}} + \underbrace{\text{Measurement}}_{\text{same category, different indicator}} + \underbrace{\text{Weight}}_{\text{how categories aggregate}}$$

Their attribution assigns the largest share to **measurement** (~53%), then **scope** (~44%), with **weight** smallest (~3%). The dominant driver is subtle and important: **measurement divergence** means raters disagree on the *same* attribute (e.g. two providers score "labor practices" differently using different proxies), not merely that they weight categories differently. A "rater effect" is also present — a firm scored well in one category by an agency tends to be scored well by that same agency elsewhere, consistent with analyst-level halo effects.

### Why this matters statistically

If the true latent ESG quality is $\theta_i$ and each rater observes $x_i^{(k)} = \theta_i + u_i^{(k)}$ with idiosyncratic noise $u^{(k)}$, then a correlation of ~0.5 between two raters implies a **noise-to-signal ratio near 1**: under the classical measurement-error model, $\text{corr}(x^{(1)}, x^{(2)}) = \sigma_\theta^2 / (\sigma_\theta^2 + \sigma_u^2)$, so $0.5 \approx \sigma_\theta^2/(\sigma_\theta^2+\sigma_u^2) \Rightarrow \sigma_u^2 \approx \sigma_\theta^2$. Roughly half the cross-sectional variation in any single ESG score is noise. Two consequences follow:

1. **Attenuation bias.** Regressing returns (or cost of capital) on a noisy ESG score biases the coefficient toward zero by the factor $\sigma_\theta^2/(\sigma_\theta^2+\sigma_u^2) \approx 0.5$. True effects are *understated* in single-rater studies, and the *sign of estimated effects can flip with the choice of rater* — which is exactly what the literature exhibits.
2. **Non-replicability.** Because the "treatment" (ESG quality) is provider-dependent, empirical results are contingent on the data vendor, undermining the usual cumulative-evidence logic.

## 3. Materiality: signal lives in a subset of the indicators

If half the ESG score is noise, the natural response is to isolate the part that should matter financially. Khan, Serafeim & Yoon (2016), *"Corporate Sustainability: First Evidence on Materiality"* (The Accounting Review), do exactly this using **SASB's** industry-specific materiality map to split each firm's ESG performance into **material** and **immaterial** issues:

- Firms rated highly on **material** sustainability issues significantly **outperform** firms rated poorly on them (a positive, statistically robust return spread and lower cost of capital).
- Firms rated highly on **immaterial** issues show **no** outperformance — and high immaterial-only scores can even signal wasted resources or greenwashing.

The design is powerful because it separates the two hypotheses: an *undifferentiated* ESG score mixes a possibly-priced material component with an unpriced immaterial one, diluting any real signal. This is the analytical justification for **materiality-weighted** rather than headline ESG scores, and it reframes "does ESG pay?" as "does *material* ESG pay?" — a much better-posed question.

## 4. Greenwashing, selection, and measurement error

Three biases systematically inflate naïve ESG-performance estimates:

- **Selection / self-reporting bias.** ESG data is largely voluntary and self-reported. Firms disclose selectively; larger, more profitable firms disclose more (see §1), so ESG scores are entangled with the very characteristics that predict returns. Missing-not-at-random disclosure is the norm, not the exception.
- **Greenwashing as deliberate measurement error.** Model reported ESG as $\tilde\theta_i = \theta_i + b_i + u_i$ where $b_i \ge 0$ is a strategic disclosure bias. Greenwashing makes $b_i$ correlate with incentives (funds marketing ESG products, firms facing scrutiny), so the error is **not** classical — it biases estimates in direction-dependent ways rather than merely attenuating them.
- **Survivorship and backfill.** ESG index reconstitutions and vendor methodology changes are frequently applied retroactively, importing look-ahead bias into backtests. A "green" backtest can bake in post-hoc winners.

Net effect: a meaningful part of reported ESG–performance correlation is an artifact of *who gets measured and how*, not a causal ESG effect.

## 5. The aggregate evidence, read carefully

Friede, Busch & Bassen (2015) aggregate **more than 2,000 empirical studies** and report that roughly **90% find a non-negative** ESG–financial-performance relation, with a **majority positive**. This is the headline supporters cite. Read it with the caveats above:

- "Non-negative" is a weak bar; publication bias and the attenuation/selection issues cut both ways.
- The positive results concentrate where the design is cleanest — **material** factors (§3) and **cost-of-capital / risk** channels rather than pure alpha (§1).
- Vote-counting across studies with **provider-dependent treatments** (§2) is not the same as a clean meta-effect; heterogeneity across raters is a confound, not just sampling noise.

A defensible synthesis: ESG most credibly operates as a **risk-mitigation and disclosure-quality signal** with a small, materiality-concentrated return effect, rather than a large standalone premium.

## 6. Fiduciary duty and double materiality

The framing dispute is not merely semantic; it changes the objective function.

- **Single (financial) materiality** — the fiduciary-consistent view — counts an ESG issue only insofar as it affects the firm's cash flows and risk: ESG $\subseteq$ risk management. Under this view, ignoring **material** ESG risk is itself a breach of fiduciary duty, while pursuing non-pecuniary goals with beneficiaries' money is suspect.
- **Double materiality** — the EU's regulatory stance (CSRD) — adds the firm's **impact on society and the environment** as an independent reporting object, regardless of financial feedback. The objective becomes two-dimensional: $\{$financial return, external impact$\}$, which cannot be collapsed to a single number without a stated trade-off (an implicit shadow price on impact).

Formally, single materiality maximizes risk-adjusted return $\mathbb{E}[U(W)]$ subject to ESG entering only through the return distribution; double materiality optimizes a bi-objective $\lambda \cdot \text{return} + (1-\lambda)\cdot \text{impact}$, and the entire dispute is about whether a fiduciary is permitted to set $\lambda < 1$ on others' capital. The **UN PRI** signatory framework and the growth of impact mandates presuppose some $\lambda<1$; strict fiduciary readings insist on $\lambda = 1$. Empirical work cannot resolve this — it is a question of mandate and law, not estimation — but clarity about which objective is in force is a prerequisite for coherent portfolio construction.

## 7. Practical implications for the quant

- **Treat the ESG score as a noisy, provider-specific measurement**, not ground truth. Prefer **materiality-mapped** signals (SASB-style) over headline aggregates.
- **Blend or orthogonalize across raters** to attenuate rater-specific noise; report sensitivity of any result to the choice of vendor.
- **Attribute before you attribute causation**: run the factor regression (§1) and check whether ESG alpha survives quality/size/low-vol controls before claiming a premium.
- **Distinguish realized from expected returns**: a green tilt that worked in-sample may reflect repricing (falling discount rates), which implies *lower* forward expected returns, not a durable edge.
- **Guard the backtest** against retroactive methodology changes, survivorship, and self-selection in disclosure.

## References & further reading

- Berg, F., Kölbl, J. F., & Rigobon, R. (2022). *Aggregate Confusion: The Divergence of ESG Ratings.* Review of Finance.
- Khan, M., Serafeim, G., & Yoon, A. (2016). *Corporate Sustainability: First Evidence on Materiality.* The Accounting Review.
- Friede, G., Busch, T., & Bassen, A. (2015). *ESG and financial performance: aggregated evidence from more than 2000 empirical studies.* Journal of Sustainable Finance & Investment.
- Pástor, Ľ., Stambaugh, R. F., & Taylor, L. A. (2021). *Sustainable investing in equilibrium.* Journal of Financial Economics.
- Pedersen, L. H., Fitzgibbons, S., & Pomorski, L. (2021). *Responsible investing: The ESG-efficient frontier.* Journal of Financial Economics.
- SASB — Sustainability Accounting Standards Board: industry-specific financial-materiality standards.
- UN PRI — Principles for Responsible Investment: institutional framework and signatory reporting.
