# Distribution Functions, Moments, and the Quantile Map

The mean and the variance are not primitive objects. Both are functionals of a single primitive — the distribution function $F$ — and so is every risk number a desk quotes. Working directly with $F$ unifies the discrete and continuous cases, makes the estimation questions precise, and exposes exactly where the machinery fails on financial data.

## 1. The distribution function as the primitive

For a real random variable $X$ on $(\Omega,\mathcal{F},\mathbb{P})$, define

$$F(x) = \mathbb{P}(X \le x).$$

$F$ is non-decreasing, right-continuous, with $\lim_{x\to-\infty}F(x)=0$ and $\lim_{x\to+\infty}F(x)=1$. Conversely (Lebesgue–Stieltjes) any such $F$ induces a unique probability measure on $\mathcal{B}(\mathbb{R})$, so $F$ *is* the distribution. Right-continuity is not cosmetic: it is what makes $\mathbb{P}(X \le x)$ rather than $\mathbb{P}(X < x)$ the canonical object, and it is what forces the particular generalised inverse in §4.

Expectation is then a single integral against $dF$, with no case split:

$$\mathbb{E}[g(X)] = \int_{\mathbb{R}} g(x)\,dF(x),$$

reducing to $\int g(x)f(x)\,dx$ when $F$ is absolutely continuous with density $f = F'$, and to $\sum_i g(x_i)p_i$ when $F$ is a step function. The mean and variance of the standard tier are the cases $g(x) = x$ and $g(x) = (x-\mu)^2$.

A useful reformulation follows from Fubini. For $X \ge 0$, write $X = \int_0^\infty \mathbf{1}\{X > t\}\,dt$ and exchange:

$$\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t)\,dt = \int_0^\infty \left(1 - F(t)\right)dt.$$

The mean is the area *above* the CDF. This is the form that makes tail behaviour visibly decisive: if $1-F(t)$ decays too slowly, the integral diverges and the mean does not exist. §5 makes that quantitative.

## 2. Why the sample variance divides by $n-1$

Let $X_1,\dots,X_n$ be i.i.d. with mean $\mu$ and variance $\sigma^2$, and let $\bar X = \frac1n\sum_i X_i$. Start from the algebraic identity obtained by adding and subtracting $\mu$:

$$\sum_{i=1}^n (X_i - \bar X)^2 = \sum_{i=1}^n \left[(X_i - \mu) - (\bar X - \mu)\right]^2 .$$

Expanding the square,

$$= \sum_{i=1}^n (X_i-\mu)^2 - 2(\bar X - \mu)\sum_{i=1}^n (X_i - \mu) + n(\bar X - \mu)^2 .$$

Since $\sum_i (X_i - \mu) = n(\bar X - \mu)$, the middle term equals $-2n(\bar X-\mu)^2$, giving

$$\sum_{i=1}^n (X_i - \bar X)^2 = \sum_{i=1}^n (X_i-\mu)^2 - n(\bar X - \mu)^2 .$$

Now take expectations. The first term contributes $n\sigma^2$. For the second, independence gives $\operatorname{Var}(\bar X) = \sigma^2/n$, so $\mathbb{E}[(\bar X - \mu)^2] = \sigma^2/n$ and the term contributes $\sigma^2$. Therefore

$$\mathbb{E}\left[\sum_{i=1}^n (X_i - \bar X)^2\right] = n\sigma^2 - \sigma^2 = (n-1)\sigma^2,$$

and dividing by $n-1$ yields an unbiased estimator:

$$S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar X)^2, \qquad \mathbb{E}[S^2] = \sigma^2 .$$

The geometry behind the arithmetic: the residual vector $(X_i - \bar X)_i$ is the projection of $(X_i - \mu)_i$ onto the hyperplane orthogonal to $\mathbf{1}$, and that subspace has dimension $n-1$. One degree of freedom was spent estimating the centre.

Two cautions. First, unbiasedness does not transfer through the square root — by Jensen, $\mathbb{E}[S] < \sigma$, so the sample **standard deviation** is biased low even though $S^2$ is unbiased. Second, unbiasedness is not optimality: $S^2$ does not minimise mean squared error, and it presumes finite fourth moments for its own variance to exist.

## 3. Densities and the meaning of $f$

When $F$ is absolutely continuous, the Radon–Nikodym derivative $f = dF/d\lambda$ exists and

$$P(a \le X \le b) = F(b) - F(a) = \int_a^b f(x)\,dx .$$

The density is a *rate*, not a probability: $f(x)$ may exceed 1, and $\mathbb{P}(X = x) = 0$ for every $x$. Only its integral over a set carries probability. This is why every practical computation routes through $F$ rather than $f$.

## 4. The quantile function and the probability integral transform

Because $F$ need be neither strictly increasing nor continuous, the inverse is defined as the **generalised inverse**

$$F^{-1}(p) = \inf\{x \in \mathbb{R} : F(x) \ge p\}, \qquad p \in (0,1),$$

which is left-continuous and coincides with the ordinary inverse when $F$ is continuous and strictly increasing. The defining Galois relation is

$$F^{-1}(p) \le x \iff p \le F(x).$$

From it, two results follow immediately.

**Probability integral transform.** If $F$ is continuous, $U := F(X) \sim \text{Uniform}(0,1)$. Proof: $\mathbb{P}(F(X) \le p) = \mathbb{P}(X \le F^{-1}(p)) = F(F^{-1}(p)) = p$. Every continuous distribution is a deterministic reshaping of a uniform — the basis of copula modelling, of goodness-of-fit tests, and of backtesting a risk model by checking that realised PIT values are uniform.

**Inverse transform sampling.** Conversely, if $U \sim \text{Uniform}(0,1)$ then $F^{-1}(U) \sim F$, since $\mathbb{P}(F^{-1}(U) \le x) = \mathbb{P}(U \le F(x)) = F(x)$. This is how Monte Carlo engines draw from arbitrary distributions given only uniforms.

**Value at Risk is just a quantile.** For a loss variable $L$, $\text{VaR}_\alpha(L) = F_L^{-1}(\alpha)$. All of VaR's mathematical content is contained in the map above — which is also why its defects are structural rather than fixable by better estimation.

Specifically, VaR is **not subadditive**. Take two independent bonds, each losing 100 with probability 0.04 and gaining 5 otherwise. For a single bond, $\mathbb{P}(L \le -5) = 0.96 \ge 0.95$, so $\text{VaR}_{0.95} = -5$: at the 95% level the position looks profitable. Now hold half of each. The portfolio loses $(100-5)/2 = 47.5$ if exactly one defaults, which happens with probability $2(0.04)(0.96) = 0.0768$. Since $\mathbb{P}(L_p \le -5) = 0.9216 < 0.95$, the quantile jumps to $\text{VaR}_{0.95}(L_p) = 47.5$, while the sum of the halved standalone VaRs is $-2.5 + -2.5 = -5$. Diversifying made the reported risk *worse*, violating

$$\rho(X+Y) \le \rho(X) + \rho(Y).$$

VaR therefore fails the Artzner–Delbaen–Eber–Heath coherence axioms. **Expected shortfall**, $\text{ES}_\alpha = \frac{1}{1-\alpha}\int_\alpha^1 F^{-1}(p)\,dp$, averages the tail beyond the quantile instead of reading a single point off it, and is coherent — which is why Basel moved to it.

## 5. Moment existence under heavy tails

Let $X$ be Pareto with $f(x) = \alpha x_m^{\alpha} x^{-(\alpha+1)}$ for $x \ge x_m > 0$. Then

$$\mathbb{E}[X^k] = \alpha x_m^{\alpha}\int_{x_m}^{\infty} x^{k-\alpha-1}\,dx,$$

and the integral converges precisely when $k - \alpha - 1 < -1$, i.e. $k < \alpha$. So:

- $\alpha \le 1$: **the mean does not exist.** Sample averages fail to converge and wander with $n$.
- $1 < \alpha \le 2$: the mean exists but **the variance is infinite.** The sample variance still returns a finite number for any finite sample, but it grows without bound as data accumulates — it is estimating something that is not there.

```chart
pareto_pdf(alpha=1.5)
```

At $\alpha = 1.5$ the mean exists and the variance does not. This is the central practical warning of the whole topic: a volatility figure computed on such data is an artefact of the sample size, and the central limit theorem's $\sqrt{n}$ rate does not apply — sums converge instead to an $\alpha$-stable law with a slower rate.

```chart
normal_vs_fat_tail()
```

Equity index returns are not Pareto, but estimated tail indices typically land near $\alpha \in [3,5]$: enough for finite variance, often not enough for a finite fourth moment. Since the variance of $S^2$ depends on the fourth moment, this means the *error bars on your volatility estimate* may be the thing that fails to exist, even when volatility itself is well defined.

## 6. Where the framework breaks on market data

- **Non-stationarity.** $F$ is assumed fixed while estimating it. Return distributions shift with regime, so a long sample buys precision in the wrong parameter. This is a bias–variance trade with no clean solution.
- **Dependence.** The i.i.d. assumption of §2 fails: returns are near-uncorrelated but their squares are strongly dependent (volatility clustering). Standard errors computed under independence are far too narrow.
- **The tail is where the data is not.** By construction, few observations inform the region that dominates risk. Extreme value theory — fitting a generalised Pareto above a high threshold via Pickands–Balkema–de Haan, or Hill's estimator for $\alpha$ — extrapolates rather than interpolates, and is sensitive to threshold choice.
- **Unconditional versus conditional.** $F$ estimated over a decade is a mixture across regimes; it is not the distribution the next trade faces. Conditional models exist for exactly this reason.
- **Multivariate structure.** Marginals plus correlation do not determine a joint distribution. Tail dependence — the tendency to break together — is invisible to correlation and is what turns a diversified book into a concentrated one in a crisis.

## References & further reading

- Billingsley, P. (1995). *Probability and Measure*, 3rd ed. Wiley — distribution functions, Lebesgue–Stieltjes integration.
- Feller, W. (1971). *An Introduction to Probability Theory and Its Applications*, Vol. II, 2nd ed. Wiley — stable laws and domains of attraction.
- Rosenblatt, M. (1952). *Remarks on a Multivariate Transformation.* Annals of Mathematical Statistics 23(3) — the probability integral transform.
- Devroye, L. (1986). *Non-Uniform Random Variate Generation.* Springer — inverse transform and beyond.
- Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999). *Coherent Measures of Risk.* Mathematical Finance 9(3) — the axioms VaR fails.
- Acerbi, C., & Tasche, D. (2002). *On the Coherence of Expected Shortfall.* Journal of Banking & Finance 26(7).
- Embrechts, P., Klüppelberg, C., & Mikosch, T. (1997). *Modelling Extremal Events for Insurance and Finance.* Springer.
- McNeil, A. J., Frey, R., & Embrechts, P. (2015). *Quantitative Risk Management*, rev. ed. Princeton — tail estimation, copulas, tail dependence.
- Hill, B. M. (1975). *A Simple General Approach to Inference About the Tail of a Distribution.* Annals of Statistics 3(5).
- Mandelbrot, B. (1963). *The Variation of Certain Speculative Prices.* Journal of Business 36(4).

*Educational content, not investment advice.*
