# Monte Carlo Risk Forecasting: Estimation, Convergence, and Model Risk

## 1. Monte Carlo as integration

Every risk number we want is an expectation under a return model. Let $X \in \mathbb{R}^d$ carry the randomness (a path of correlated shocks) with density $f$, and let $g$ map that path to the quantity of interest (terminal PnL, a drawdown functional, a limit-breach indicator). Then the target is

$$\theta = \mathbb{E}_f[g(X)] = \int_{\mathbb{R}^d} g(x)\,f(x)\,dx.$$

The Monte Carlo estimator draws $X_1,\dots,X_N \overset{\text{iid}}{\sim} f$ and averages:

$$\hat{\theta}_N = \frac{1}{N}\sum_{i=1}^{N} g(X_i).$$

This reframes *risk forecasting as numerical integration* over the space of futures — the reason it scales to portfolios where closed-form densities of PnL do not exist.

## 2. Unbiasedness and the $O(N^{-1/2})$ convergence rate

**Bias.** By linearity, $\mathbb{E}[\hat{\theta}_N] = \frac{1}{N}\sum_i \mathbb{E}[g(X_i)] = \theta$, so the estimator is exactly unbiased for every $N$.

**Variance.** With $\sigma^2 := \operatorname{Var}_f\!\big(g(X)\big) < \infty$ and independence,

$$\operatorname{Var}(\hat{\theta}_N) = \frac{1}{N^2}\sum_{i=1}^{N}\operatorname{Var}\!\big(g(X_i)\big) = \frac{\sigma^2}{N}, \qquad \text{RMSE}(\hat{\theta}_N) = \frac{\sigma}{\sqrt{N}} = O\!\big(N^{-1/2}\big).$$

The rate is the single most important fact about Monte Carlo: the error shrinks like $N^{-1/2}$ **independently of the dimension $d$**. Deterministic grid quadrature converges at $O(N^{-r/d})$ for an order-$r$ rule, which is annihilated by dimension; MC's rate is dimension-free (the constant $\sigma$ hides the difficulty, but the *rate* does not degrade). The price is that halving the error costs $4\times$ the paths.

**Central limit theorem and error bars.** If $\sigma^2 < \infty$,

$$\sqrt{N}\,(\hat{\theta}_N - \theta) \xrightarrow{d} \mathcal{N}(0,\sigma^2),$$

so an asymptotic $(1-\alpha)$ confidence interval is $\hat{\theta}_N \pm z_{1-\alpha/2}\,\hat{\sigma}/\sqrt{N}$ with $\hat{\sigma}^2$ the sample variance. Never report a simulated risk number without this standard error — it is what tells you whether the tail estimate is real or sampling noise. The running average visibly settling is the CLT at work:


```chart
frequentist_convergence()
```


## 3. Sampling the paths: GBM and Euler discretization

The canonical continuous-time model is geometric Brownian motion,

$$dS_t = \mu S_t\,dt + \sigma S_t\,dW_t.$$

Applying Itô's lemma to $Y_t = \log S_t$ removes the state dependence in the diffusion:

$$dY_t = \Big(\mu - \tfrac{1}{2}\sigma^2\Big)dt + \sigma\,dW_t \;\Longrightarrow\; S_{t+\Delta} = S_t \exp\!\Big[\big(\mu - \tfrac{1}{2}\sigma^2\big)\Delta + \sigma\sqrt{\Delta}\,Z\Big],\quad Z\sim\mathcal{N}(0,1).$$

Because the log-increment is exact, GBM should be simulated on the **log scale** — there is no discretization bias. The naive **Euler–Maruyama** scheme applied directly to $S$,

$$\hat{S}_{t+\Delta} = \hat{S}_t\big(1 + \mu\Delta + \sigma\sqrt{\Delta}\,Z\big),$$

is only *weakly* order 1 and *strongly* order $\tfrac{1}{2}$, and can go negative — acceptable for coarse risk work, inferior to the exact log update. For a portfolio, draw a standard normal vector $Z$ and correlate it with a **Cholesky factor** $\Sigma = LL^\top$, using $LZ$ so the sampled shocks carry the target covariance:

$$\mathbf{r} = \boldsymbol{\mu}\,\Delta + \sqrt{\Delta}\,L\,Z, \qquad Z \sim \mathcal{N}(0, I_d).$$


```chart
monte_carlo_paths()
```


## 4. Estimating VaR and Expected Shortfall

Let the loss be $L = -\Delta V$ over the horizon, with CDF $F_L$. Value-at-Risk at confidence $\alpha$ is the quantile

$$\operatorname{VaR}_\alpha = F_L^{-1}(\alpha) = \inf\{\ell \in \mathbb{R} : F_L(\ell) \ge \alpha\}.$$

Given simulated losses $L_1,\dots,L_N$ with order statistics $L_{(1)} \le \dots \le L_{(N)}$, the empirical estimator is

$$\widehat{\operatorname{VaR}}_\alpha = L_{(\lceil \alpha N \rceil)}.$$

VaR ignores the shape beyond the threshold and **fails subadditivity** — it is not a coherent risk measure (Artzner et al., 1999). Expected Shortfall repairs both defects:

$$\operatorname{ES}_\alpha = \mathbb{E}\big[L \,\big|\, L \ge \operatorname{VaR}_\alpha\big] = \frac{1}{1-\alpha}\int_{\alpha}^{1} \operatorname{VaR}_u \, du, \qquad \widehat{\operatorname{ES}}_\alpha = \frac{1}{N - \lceil \alpha N\rceil}\!\!\sum_{i > \lceil \alpha N\rceil}\!\! L_{(i)}.$$

ES is coherent (subadditive, so diversification never increases it) and averages the *entire* tail, which is why post-2016 regulation (FRTB) moved from VaR to ES. Note both estimators consume only the tail sample: the worst $(1-\alpha)N$ paths, so their variance is governed by that small count — the motivation for the variance-reduction machinery below.

## 5. Variance reduction

Since RMSE $= \sigma/\sqrt{N}$, we can either raise $N$ (linear cost) or lower the effective $\sigma$ (free, if we are clever). Two workhorses:

### Antithetic variates (derivation)

Suppose $g$ is driven by a standard normal draw $Z$, and note $-Z$ has the same law. Form pairs and average within each pair:

$$Y_i = \tfrac{1}{2}\big(g(Z_i) + g(-Z_i)\big), \qquad \hat{\theta}_{\text{AV}} = \frac{1}{N}\sum_{i=1}^{N} Y_i .$$

The estimator is unbiased. With $\sigma^2 = \operatorname{Var}(g(Z))$ and $\rho = \operatorname{Corr}\!\big(g(Z), g(-Z)\big)$,

$$\operatorname{Var}(Y_i) = \tfrac{1}{4}\Big[\operatorname{Var}\big(g(Z)\big) + \operatorname{Var}\big(g(-Z)\big) + 2\operatorname{Cov}\big(g(Z),g(-Z)\big)\Big] = \frac{\sigma^2}{2}\,(1+\rho),$$

so over $N$ pairs (i.e. $2N$ function evaluations)

$$\operatorname{Var}(\hat{\theta}_{\text{AV}}) = \frac{\sigma^2}{2N}\,(1+\rho).$$

The benchmark using the **same** $2N$ independent draws has variance $\sigma^2/(2N)$. Therefore

$$\frac{\operatorname{Var}(\hat{\theta}_{\text{AV}})}{\operatorname{Var}(\hat{\theta}_{\text{iid}})} = 1 + \rho,$$

and antithetic sampling **strictly reduces variance iff $\rho < 0$** — guaranteed when $g$ is monotone in $Z$ (a long-only PnL is), and counterproductive for symmetric payoffs where $g(Z)=g(-Z)$ makes $\rho>0$.

### Control variates

If $h(X)$ is correlated with $g(X)$ and has a *known* mean $\mathbb{E}[h] = m$ (e.g. a Black–Scholes price when pricing a nearby exotic), then for any $c$,

$$\hat{\theta}_{\text{CV}} = \frac{1}{N}\sum_{i=1}^{N}\Big[g(X_i) - c\big(h(X_i) - m\big)\Big]$$

is unbiased. Minimizing over $c$ gives $c^\star = \operatorname{Cov}(g,h)/\operatorname{Var}(h)$ and a variance multiplied by $\big(1 - \rho_{g,h}^2\big)$: a control variate correlated at $\rho = 0.9$ cuts variance by $\approx 80\%$. Related techniques — stratified sampling, importance sampling (essential for deep-tail VaR, where you tilt $f$ toward the loss region), and quasi-Monte Carlo (low-discrepancy sequences achieving nearly $O(N^{-1})$) — trade generality for larger gains.

## 6. Where the model breaks: fat tails and the fragility of the rate

Every result above from Section 2 rests on $\sigma^2 = \operatorname{Var}(g) < \infty$. Heavy tails threaten this directly. If PnL inherits a Student-$t$ shape with $\nu \le 2$ degrees of freedom, the **variance is infinite**, the CLT with a $\sqrt{N}$ rate fails, and the sample standard error $\hat{\sigma}/\sqrt{N}$ is itself meaningless — the estimator converges slower (a stable-law rate $N^{-1+1/\alpha}$) and tail metrics are wildly unstable across seeds.


```chart
normal_vs_fat_tail(nu=2)
```


Beyond the rate, the modeling hazards compound:

- **Gaussian input, power-law reality.** A normal engine assigns a $5\sigma$ day a probability near $3\times10^{-7}$ (once in ~14,000 years); markets deliver them every few years. Simulated VaR/ES then look reassuring until they are catastrophically wrong. Use Student-$t$, a normal-variance mixture, extreme-value tail fits, or filtered historical bootstrap.
- **Correlation breakdown.** $\Sigma$ is not constant; correlations tend to $1$ in a sell-off. A Cholesky drawn from a calm-market covariance understates joint tail losses. Stress $\Sigma$, or use a copula with tail dependence.
- **Non-stationarity and estimation error.** $\boldsymbol\mu, \Sigma$ drift with regime, and parameters estimated in-sample bias the risk downward; selecting the best-looking model inflates the effect (deflated-Sharpe / backtest-overfit logic, López de Prado).
- **Leverage and path-dependence.** Risk is the return distribution *times exposure*; margin calls and stops make PnL path-dependent, so terminal-distribution VaR can miss intra-horizon ruin.

The discipline is to treat Monte Carlo as an **amplifier of assumptions**: with honest, heavy-tailed, regime-aware inputs it is the most flexible risk tool available; with a Gaussian i.i.d. model it manufactures false precision.

## References & further reading

- Metropolis, N. & Ulam, S. (1949). *The Monte Carlo Method.* Journal of the American Statistical Association, 44(247), 335–341.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering.* Springer. (Path generation, discretization bias, variance reduction, quasi-MC.)
- Jorion, P. (2006). *Value at Risk: The New Benchmark for Managing Financial Risk*, 3rd ed. McGraw-Hill.
- Boyle, P. (1977). *Options: A Monte Carlo Approach.* Journal of Financial Economics, 4(3), 323–338.
- Artzner, Delbaen, Eber & Heath (1999). *Coherent Measures of Risk.* Mathematical Finance, 9(3), 203–228. (Why ES is coherent and VaR is not.)
- Rockafellar, R. T. & Uryasev, S. (2000). *Optimization of Conditional Value-at-Risk.* Journal of Risk, 2(3), 21–41.
- L'Ecuyer, P. (2009). *Quasi-Monte Carlo Methods with Applications in Finance.* Finance and Stochastics, 13, 307–349.
- McNeil, Frey & Embrechts (2015). *Quantitative Risk Management*, 2nd ed. Princeton. (EVT, copulas, tail dependence.)
