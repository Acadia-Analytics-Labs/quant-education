# Volatility, Implied Variance, and Beta: Estimation and Its Failure Modes

Volatility, the VIX, and beta are three projections of one object: the covariance structure of returns. Volatility is the square root of a diagonal element, beta is a normalised off-diagonal element, and the VIX is a risk-neutral expectation of future quadratic variation. Treating them as separate "risk measures" obscures how tightly they are linked — and where each estimator breaks.

## 1. Setup and the realized variance estimator

Let $P_t$ be the price process and $r_t = \log(P_t/P_{t-1})$ the log return over interval $t$. Log returns are used because they aggregate additively: the $h$-period return is $r_{t,t+h} = \sum_{k=1}^{h} r_{t+k}$, which is what makes §2 work.

For a continuous semimartingale $dP_t/P_t = \mu_t\,dt + \sigma_t\,dW_t$, the object volatility estimators target is the **integrated variance** over $[0,T]$:

$$IV_{[0,T]} = \int_0^T \sigma_t^2\,dt.$$

Its natural estimator is **realized variance**, the sum of squared intraday returns:

$$RV_{[0,T]}^{(n)} = \sum_{i=1}^{n} r_{t_i}^2 \;\xrightarrow{\;p\;}\; IV_{[0,T]} \quad \text{as } \sup_i |t_i - t_{i-1}| \to 0,$$

by the theory of quadratic variation. Realized variance is consistent, and it is *model-free*: no distributional assumption is required, only that $P$ is a semimartingale. The sample standard deviation of the standard tier is the low-frequency special case, with a mean subtracted:

$$\hat\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(r_i - \bar r)^2.$$

The $n-1$ divisor is Bessel's correction. Its necessity is easy to see: $\bar r$ is chosen to minimise $\sum (r_i - \bar r)^2$, so the residual sum is mechanically smaller than $\sum (r_i - \mu)^2$ around the true mean. Dividing by $n$ would inherit that downward bias; dividing by $n-1$ removes it exactly, since the residual vector lives in an $(n-1)$-dimensional subspace once $\bar r$ is fixed. At daily frequency over a year the mean term is negligible anyway ($\bar r \approx 0.0003$ against $\sigma \approx 0.01$), which is why practitioners often set $\bar r = 0$ and gain a little efficiency.

## 2. Square-root-of-time scaling and what it assumes

Aggregate $h$ single-period returns. Variance of the sum is

$$\operatorname{Var}\!\left(\sum_{k=1}^{h} r_{t+k}\right) = \sum_{k=1}^{h}\operatorname{Var}(r_{t+k}) + 2\sum_{j<k}\operatorname{Cov}(r_{t+j}, r_{t+k}).$$

Impose two conditions: **covariance stationarity** ($\operatorname{Var}(r_t) = \sigma^2$ for all $t$) and **serial uncorrelatedness** ($\operatorname{Cov}(r_{t+j}, r_{t+k}) = 0$ for $j \neq k$). The cross terms vanish and

$$\operatorname{Var}\!\left(r_{t,t+h}\right) = h\sigma^2 \;\Longrightarrow\; \sigma_h = \sigma\sqrt{h}.$$

Hence the familiar $\sigma_{\text{annual}} = \sigma_{\text{daily}}\sqrt{252}$. Note precisely what was used: **not** normality, and **not** independence — only zero autocorrelation and constant variance. That matters, because the rule survives fat tails (§6 shows it does not survive autocorrelation or heteroskedasticity in the way people assume).

The failure is quantitative and signed. With AR(1) returns, $\operatorname{Cov}(r_t, r_{t+k}) = \rho^{|k|}\sigma^2$, and summing the geometric cross terms gives

$$\operatorname{Var}(r_{t,t+h}) = h\sigma^2\left[1 + \frac{2\rho}{1-\rho}\left(1 - \frac{1-\rho^h}{h(1-\rho)}\right)\right].$$

Momentum ($\rho > 0$) makes true multi-period risk **exceed** the square-root rule; mean reversion ($\rho < 0$) makes it fall short. Applying $\sqrt{h}$ scaling to a trending or mean-reverting series therefore misstates horizon risk in a predictable direction — a live problem for VaR computed at one horizon and scaled to another.

## 3. Beta is the OLS slope — a derivation

Posit the market model $R_i = \alpha + \beta R_m + \varepsilon$ with $\mathbb{E}[\varepsilon] = 0$ and $\operatorname{Cov}(R_m, \varepsilon) = 0$. Choose $(\alpha, \beta)$ to minimise expected squared error:

$$L(\alpha,\beta) = \mathbb{E}\!\left[(R_i - \alpha - \beta R_m)^2\right].$$

First-order condition in $\alpha$:

$$\frac{\partial L}{\partial \alpha} = -2\,\mathbb{E}\!\left[R_i - \alpha - \beta R_m\right] = 0 \;\Longrightarrow\; \alpha = \mathbb{E}[R_i] - \beta\,\mathbb{E}[R_m].$$

First-order condition in $\beta$:

$$\frac{\partial L}{\partial \beta} = -2\,\mathbb{E}\!\left[R_m\left(R_i - \alpha - \beta R_m\right)\right] = 0.$$

Substitute $\alpha$ and group:

$$\mathbb{E}\!\left[R_m R_i\right] - \mathbb{E}[R_m]\mathbb{E}[R_i] + \beta\,\mathbb{E}[R_m]^2 - \beta\,\mathbb{E}\!\left[R_m^2\right] = 0,$$

which is exactly

$$\operatorname{Cov}(R_i, R_m) - \beta\operatorname{Var}(R_m) = 0 \;\Longrightarrow\; \boxed{\;\beta = \frac{\operatorname{Cov}(R_i,R_m)}{\operatorname{Var}(R_m)}\;}$$

So the covariance ratio quoted everywhere is not a definition handed down — it is the unique minimiser of mean squared error in a linear projection of the asset onto the market. Everything CAPM-adjacent inherits this least-squares interpretation.

```chart
linear_regression_fit()
```

## 4. Variance decomposition: systematic versus idiosyncratic

Take variances through the market model, using $\operatorname{Cov}(R_m, \varepsilon) = 0$:

$$\sigma_i^2 = \beta^2\sigma_m^2 + \sigma_\varepsilon^2.$$

The first term is **systematic** risk — undiversifiable, because it is exposure to the common factor. The second is **idiosyncratic** and vanishes in a large portfolio: for $N$ equally weighted names with independent residuals, the residual variance of the portfolio is $\sigma_\varepsilon^2/N \to 0$.

The share explained by the market is

$$R^2 = \frac{\beta^2\sigma_m^2}{\sigma_i^2} = \rho_{im}^2,$$

the squared correlation. This exposes the most common misreading of beta. Two stocks can share $\beta = 1.2$ while one has $R^2 = 0.8$ (the market genuinely drives it) and the other $R^2 = 0.1$ (the point estimate is mostly noise). **Beta without $R^2$ is close to uninformative**, and the standard error of $\hat\beta$ scales as $\sigma_\varepsilon/(\sigma_m\sqrt{n})$ — large precisely for the high-idiosyncratic-risk names where people most want a clean number.

## 5. The VIX as a model-free implied volatility

The VIX is often mislabelled a Black–Scholes implied volatility. It is not; since the 2003 methodology change it is a **model-free** expectation of realized variance, derived from variance-swap replication.

The key result (Neuberger; Demeterfi, Derman, Kamal & Zou) is that the payoff $\log(F_T/F_0)$ can be replicated with a static portfolio of options across all strikes plus a dynamic futures position. Under the risk-neutral measure $\mathbb{Q}$, for a continuous price process,

$$\mathbb{E}^{\mathbb{Q}}\!\left[\int_0^T \sigma_t^2\,dt\right] = 2\int_0^\infty \frac{Q(K)}{K^2}\,dK,$$

where $Q(K)$ is the price of the out-of-the-money option struck at $K$ (put below the forward, call above), discounted to today. The $1/K^2$ weighting is the whole content of the result: a strip of options weighted inversely to the square of the strike has a payoff whose expectation is exactly the expected integrated variance. The VIX is the discretised version of that integral over the listed strike grid, annualised and square-rooted:

$$\text{VIX} = 100 \times \sqrt{\frac{2}{T}\sum_i \frac{\Delta K_i}{K_i^2}e^{rT}Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0}-1\right)^2}.$$

Two consequences follow immediately.

**The VIX is a $\mathbb{Q}$-expectation, not a $\mathbb{P}$-forecast.** It embeds a risk premium. Empirically $\mathbb{E}^{\mathbb{Q}}[RV] > \mathbb{E}^{\mathbb{P}}[RV]$ by a persistent margin — the **variance risk premium**, typically 2–4 volatility points. Investors pay above fair value for protection because variance pays off exactly when marginal utility is highest. This is why systematically selling variance earns a premium, and why doing so is a short-tail-convexity trade rather than free money.

**The jump correction matters.** The replication above assumes a continuous path. With jumps, the log-contract expectation picks up higher-order cumulants, so the VIX conflates diffusive variance with jump risk — part of why it spikes so violently on discrete news.

```chart
normal_vs_fat_tail()
```

## 6. Where these measures break

- **Volatility clustering.** Returns are close to serially uncorrelated but their *squares* are strongly autocorrelated. Constant-$\sigma$ models are therefore misspecified; ARCH/GARCH and stochastic-volatility models exist precisely to capture $\sigma_t^2$ dynamics. A single trailing standard deviation is a lagging estimate of a fast-moving quantity.
- **Fat tails and moment existence.** Return distributions are leptokurtic. If tails are Paretian with index $\alpha \le 2$, the population variance is infinite and $\hat\sigma$ does not converge — it merely grows with the sample. Volatility is then not a well-defined risk measure at all.
- **Volatility is a symmetric measure of an asymmetric concern.** It penalises upside and downside identically, while investors care about the left tail. Semi-deviation, VaR, and expected shortfall address this; the leverage effect (negative return–volatility correlation) means the asymmetry is real, not merely a preference.
- **Beta instability.** $\hat\beta$ drifts with leverage, business mix, and regime. Blume-style shrinkage toward 1 is standard because raw estimates mean-revert.
- **Non-synchronous trading** biases $\hat\beta$ downward for illiquid names, since their prices incorporate market news with a lag. The Dimson correction — summing slopes on lagged and leading market returns — repairs it.
- **Correlations converge in crises.** The decomposition in §4 treats $\beta$ and $\sigma_m$ as stable. In a crash, cross-sectional correlations rise toward 1 and idiosyncratic diversification evaporates exactly when it is needed.
- **Roll's critique.** Beta is defined against an unobservable market portfolio. Using the S&P 500 as a proxy means every beta is measured against something that is not the theoretical benchmark, and tests of the CAPM are jointly tests of that proxy.

## References & further reading

- Markowitz, H. (1952). *Portfolio Selection.* Journal of Finance 7(1) — variance as the risk measure.
- Sharpe, W. F. (1964). *Capital Asset Prices.* Journal of Finance 19(3) — beta and systematic risk.
- Mandelbrot, B. (1963). *The Variation of Certain Speculative Prices.* Journal of Business 36(4) — fat tails and infinite variance.
- Engle, R. F. (1982). *Autoregressive Conditional Heteroscedasticity.* Econometrica 50(4); Bollerslev, T. (1986). *Generalized ARCH.* Journal of Econometrics 31(3).
- Andersen, T. G., Bollerslev, T., Diebold, F. X., & Labys, P. (2003). *Modeling and Forecasting Realized Volatility.* Econometrica 71(2).
- Demeterfi, K., Derman, E., Kamal, M., & Zou, J. (1999). *More Than You Ever Wanted to Know About Volatility Swaps.* Goldman Sachs Quantitative Strategies — the replication of §5.
- Carr, P., & Wu, L. (2009). *Variance Risk Premiums.* Review of Financial Studies 22(3).
- CBOE (2019). *The VIX Index Methodology* white paper — the exact discretisation used.
- Dimson, E. (1979). *Risk Measurement When Shares Are Subject to Infrequent Trading.* Journal of Financial Economics 7(2).
- Roll, R. (1977). *A Critique of the Asset Pricing Theory's Tests.* Journal of Financial Economics 4(2).

*Educational content, not investment advice.*
