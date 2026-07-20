# Distributions, Tails, and the Limits of the Gaussian

## 1. Random variables as measurable functions

Fix a probability space $(\Omega, \mathcal{F}, \mathbb{P})$. A **random variable** is a measurable function

$$
X : (\Omega, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}),\qquad X^{-1}(B) \in \mathcal{F}\ \ \forall B \in \mathcal{B},
$$

where $\mathcal{B}$ is the Borel $\sigma$-algebra. Measurability is exactly what makes probabilities of level sets $\{X \le x\}$ well defined. The **law** of $X$ is the pushforward measure $\mu_X = \mathbb{P}\circ X^{-1}$ on $\mathbb{R}$, and the object we actually work with is the **cumulative distribution function** (CDF)

$$
F_X(x) = \mathbb{P}(X \le x) = \mu_X\big((-\infty, x]\big),
$$

which is non-decreasing, right-continuous, with $F_X(-\infty)=0$ and $F_X(+\infty)=1$. When $\mu_X \ll \lambda$ (absolutely continuous w.r.t. Lebesgue measure), the Radon–Nikodym derivative

$$
f_X = \frac{d\mu_X}{d\lambda}, \qquad F_X(x) = \int_{-\infty}^{x} f_X(t)\,dt
$$

is the **probability density function** (PDF). For discrete laws $\mu_X$ is a countable sum of atoms and $f$ is replaced by a probability mass function. The distinction "discrete vs. continuous" is precisely whether $\mu_X$ is atomic or dominated by $\lambda$; mixtures (e.g. a return that is continuous but with an atom at a limit-down halt) also occur.

## 2. Moments and the moment-generating function

Expectation is the Lebesgue integral against the law,

$$
\mathbb{E}[g(X)] = \int_\Omega g(X)\,d\mathbb{P} = \int_{\mathbb{R}} g(x)\,d\mu_X(x),
$$

whenever $\mathbb{E}|g(X)| < \infty$. The $k$-th raw moment is $m_k = \mathbb{E}[X^k]$; the central moments are $\mu_k = \mathbb{E}[(X-\mathbb{E}X)^k]$, with $\mathrm{Var}(X)=\mu_2$. The **moment-generating function**

$$
M_X(t) = \mathbb{E}[e^{tX}] = \sum_{k\ge 0} \frac{m_k}{k!}\,t^k
$$

encodes all moments through $m_k = M_X^{(k)}(0)$ — *when it exists in a neighborhood of $0$*. This caveat is the whole story of what follows: heavy-tailed laws have $M_X(t)=\infty$ for all $t>0$, and some lack even finite low-order moments. The characteristic function $\varphi_X(t)=\mathbb{E}[e^{itX}]$ always exists and is the correct tool in the heavy-tailed regime.

## 3. Two derivations

**Binomial mean and variance.** Let $X = \sum_{i=1}^n Y_i$ with $Y_i \overset{\text{iid}}{\sim} \mathrm{Bernoulli}(p)$, so $X \sim \mathrm{Bin}(n,p)$ counts successes. Since $\mathbb{E}[Y_i]=p$ and $\mathrm{Var}(Y_i)=\mathbb{E}[Y_i^2]-p^2 = p - p^2 = p(1-p)$, linearity gives $\mathbb{E}[X]=np$, and independence gives

$$
\mathrm{Var}(X) = \sum_{i=1}^n \mathrm{Var}(Y_i) = np(1-p).
$$

This is the win-count model: $n$ trades, hit rate $p$, expected wins $np$ — but profitability depends on the *magnitude* asymmetry of wins vs. losses, not on $p$ alone.

**Pareto tail exponent and moment existence.** For the Pareto law with PDF

$$
f(x) = \frac{\alpha\, x_m^{\alpha}}{x^{\alpha+1}},\quad x \ge x_m > 0,
$$

the survival function is $\bar F(x) = \mathbb{P}(X > x) = (x_m/x)^{\alpha}$ — a pure power law with **tail index** $\alpha$. The $k$-th moment is

$$
\mathbb{E}[X^k] = \int_{x_m}^{\infty} x^k\,\frac{\alpha x_m^{\alpha}}{x^{\alpha+1}}\,dx
= \alpha x_m^{\alpha}\int_{x_m}^{\infty} x^{\,k-\alpha-1}\,dx,
$$

which converges **iff $k < \alpha$**. Hence $\mathbb{E}[X]<\infty$ requires $\alpha>1$, and finite variance requires $\alpha>2$. For $1<\alpha\le 2$ the mean exists but the variance is *infinite* — the central object of financial tail modeling.

```chart
pareto_pdf(alpha=1.5)
```

With $\alpha=1.5$ the mean exists but the variance does not: sample variance will fail to converge as you add data, and any risk number built on $\sigma$ is meaningless in the limit.

## 4. The CLT — and why it seduces us toward normality

**Classical CLT.** If $X_1, X_2, \dots$ are iid with $\mathbb{E}[X_i]=\mu$ and $0<\sigma^2=\mathrm{Var}(X_i)<\infty$, then

$$
\frac{1}{\sqrt{n}}\sum_{i=1}^n (X_i - \mu) \xrightarrow{d} \mathcal{N}(0, \sigma^2).
$$

Because a $T$-period log-return is a *sum* of higher-frequency log-returns, the CLT is the standard justification for modeling returns as $\mathcal{N}(\mu, \sigma^2)$ and for the entire mean-variance / Black–Scholes edifice. The normal density

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\exp\!\Big(-\tfrac{(x-\mu)^2}{2\sigma^2}\Big)
$$

is the unique fixed point of this normalized-sum operation among finite-variance laws. Its normalization follows from the Gaussian integral: with $I=\int_{-\infty}^{\infty} e^{-x^2/2}\,dx$, squaring and passing to polar coordinates gives $I^2 = \int_0^{2\pi}\!\int_0^\infty e^{-r^2/2}\,r\,dr\,d\theta = 2\pi$, so $I=\sqrt{2\pi}$ and the density integrates to 1.

**The load-bearing hypothesis is $\sigma^2 < \infty$.** Everything above is exactly true and exactly conditional on finite variance.

## 5. Failure under infinite variance: stable laws and the generalized CLT

Drop the finite-variance assumption and the limit changes. The **generalized (Lévy–Gnedenko) CLT** states that the only possible non-degenerate limits of normalized iid sums are the **$\alpha$-stable** laws $S_\alpha$, indexed by $\alpha \in (0,2]$:

- $\alpha = 2$ recovers the Gaussian (the sole stable law with finite variance);
- $\alpha < 2$ gives power-law tails $\bar F(x) \sim C x^{-\alpha}$, hence infinite variance, and for $\alpha \le 1$ an undefined mean.

For $\alpha<2$ the proper scaling is $n^{1/\alpha}$, not $\sqrt n$, and the sum is dominated by its largest term — a single jump, not an accumulation of small shocks. Mandelbrot (1963) proposed exactly such stable laws for cotton prices; Fama (1965) carried the "stable Paretian" hypothesis into equities. Empirically the tail index of daily equity returns sits around $\alpha \approx 3\text{–}5$: heavier than Gaussian, but often with *finite* variance and infinite higher moments — which is why modern practice favors Student-$t$ or tempered-stable bodies over strictly stable laws, while retaining the power-law tail.

```chart
normal_vs_fat_tail(nu=2)
```

The Student-$t$ with $\nu=2$ shown here has tail index $\alpha=\nu=2$: the boundary case with finite mean and infinite variance. The shaded tail is the probability mass the Gaussian systematically discards.

## 6. Kurtosis and the fourth moment

For a finite-fourth-moment law, **excess kurtosis** is

$$
\kappa = \frac{\mu_4}{\sigma^4} - 3 = \frac{\mathbb{E}[(X-\mu)^4]}{\big(\mathbb{E}[(X-\mu)^2]\big)^2} - 3,
$$

normalized so the Gaussian has $\kappa=0$. Empirical daily return series exhibit strong **leptokurtosis**, $\kappa \gg 0$ — a sharp peak and heavy tails. Note the trap: if the true tail index $\alpha \le 4$, the population $\mu_4$ is *infinite* and the sample kurtosis does not converge; a large measured $\kappa$ is then not a stable statistic but a diagnostic that the fourth moment does not exist. This is Taleb's (2007) point that in fat-tailed regimes the sample moments are dominated by the largest observations and estimate nothing.

## 7. Why $\sigma$-based risk (VaR) understates tail risk

Gaussian Value-at-Risk sets $\mathrm{VaR}_p = \mu + \sigma\,\Phi^{-1}(p)$, a linear function of $\sigma$ — legitimate only if the return law is (near-)normal. When the true law is power-law with index $\alpha$, the ratio of true to Gaussian tail probability diverges: for large $x$,

$$
\frac{\mathbb{P}(X>x)}{\mathbb{P}(\mathcal{N}>x)} = \frac{C x^{-\alpha}}{\frac{1}{x}\phi(x)} \longrightarrow \infty,
$$

since a power law decays polynomially while the Gaussian decays like $e^{-x^2/2}$. Consequences:

- a "5$\sigma$" or "25$\sigma$" event (LTCM 1998, quant quake 2007) has Gaussian probability $\sim 10^{-138}$ yet occurs on decadal timescales;
- **VaR is not subadditive** for heavy tails, so it can penalize diversification — the coherent-risk-measure critique (Artzner et al.) motivates **Expected Shortfall** $\mathrm{ES}_p = \mathbb{E}[X \mid X \le \mathrm{VaR}_p]$, which itself is finite only when $\alpha>1$;
- the right toolkit is **Extreme Value Theory**: by Pickands–Balkema–de Haan, exceedances over a high threshold converge to the Generalized Pareto Distribution, whose shape parameter $\xi = 1/\alpha$ is the quantity to estimate (Embrechts, Klüppelberg, Mikosch).

## 8. What is actually modeled: log-returns and volatility clustering

Two modeling choices reconcile theory with data. First, one models **log-returns** $r_t = \log(S_t/S_{t-1})$ rather than prices: they are additive across time (so $T$-period return is $\sum r_t$, the CLT-friendly object), symmetric in a way simple returns are not (bounded below by $-100\%$), and keep prices positive under $S_t = S_0 e^{\sum r_t}$. Second, returns are **not iid**: while $r_t$ is nearly serially uncorrelated, $r_t^2$ and $|r_t|$ show strong positive autocorrelation — **volatility clustering** (Cont 2001, "stylized facts"). Conditional-heteroskedasticity models capture this, e.g. the GARCH(1,1) recursion

$$
\sigma_t^2 = \omega + \alpha\, \varepsilon_{t-1}^2 + \beta\, \sigma_{t-1}^2,\qquad r_t = \mu + \sigma_t z_t,\ \ z_t \overset{\text{iid}}{\sim}(0,1).
$$

Crucially, GARCH produces **unconditionally heavy-tailed** returns even with light-tailed (Gaussian) innovations $z_t$: mixing a fixed shape over a time-varying $\sigma_t$ manufactures fat tails and excess kurtosis. So the observed leptokurtosis is partly genuine jump risk and partly the footprint of time-varying volatility — and a competent tail model (Student-$t$ or GPD innovations inside a GARCH filter) accounts for both rather than assuming a single static Gaussian.

## References & further reading

- Mandelbrot, B. (1963). *The Variation of Certain Speculative Prices.* Journal of Business — stable-Paretian returns.
- Fama, E. (1965). *The Behavior of Stock-Market Prices.* Journal of Business.
- Gnedenko, B. & Kolmogorov, A. (1954). *Limit Distributions for Sums of Independent Random Variables* — the generalized CLT.
- Cont, R. (2001). *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues.* Quantitative Finance.
- Embrechts, Klüppelberg & Mikosch (1997). *Modelling Extremal Events* — EVT, GPD, tail-index estimation.
- Bollerslev, T. (1986). *Generalized Autoregressive Conditional Heteroskedasticity.* Journal of Econometrics.
- Taleb, N. N. (2007). *The Black Swan*; and *Statistical Consequences of Fat Tails* (2020) — non-convergence of sample moments.
- Artzner, Delbaen, Eber & Heath (1999). *Coherent Measures of Risk* — VaR vs. Expected Shortfall.
