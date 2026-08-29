# Expected Value: The First Moment and Its Discontents

## 1. Definition and existence

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space and $X:\Omega\to\mathbb{R}$ a random variable. The **expected value** is the Lebesgue integral of $X$ with respect to $\mathbb{P}$:

$$E[X] = \int_\Omega X \, d\mathbb{P},$$

which specializes to the two familiar forms. For a **discrete** $X$ with support $\{x_i\}$ and mass function $p(x_i)=\mathbb{P}(X=x_i)$,

$$E[X] = \sum_i x_i \, p(x_i),$$

and for an **absolutely continuous** $X$ with density $f$,

$$E[X] = \int_{-\infty}^{\infty} x \, f(x)\, dx.$$

**Existence is not automatic.** The integral is defined only when $E[|X|] < \infty$ (absolute convergence); otherwise the expectation is undefined or infinite. The Cauchy distribution, $f(x) = \pi^{-1}(1+x^2)^{-1}$, has $\int |x| f(x)\,dx = \infty$ and *no* expected value — a warning that the very first moment can fail to exist, and with it every "average outcome" argument. This is the mathematical root of the fat-tail caveats in §6.

Expected value is the **first moment** of $X$; it locates the center of mass of the distribution but says nothing about dispersion, which is the job of the second central moment (§4).

## 2. Linearity of expectation

The single most useful property, and the one that makes EV a portfolio primitive:

$$E[aX + bY] = a\,E[X] + b\,E[Y] \qquad \text{for all } a,b\in\mathbb{R}.$$

**Proof (discrete case).** Let $(X,Y)$ have joint mass $p(x,y)$ with marginals $p_X, p_Y$. Then

$$E[X+Y] = \sum_x \sum_y (x+y)\,p(x,y) = \sum_x \sum_y x\,p(x,y) + \sum_x \sum_y y\,p(x,y).$$

Marginalizing each double sum, $\sum_y p(x,y)=p_X(x)$ and $\sum_x p(x,y)=p_Y(y)$, so this equals $\sum_x x\,p_X(x) + \sum_y y\,p_Y(y) = E[X] + E[Y]$. Homogeneity $E[aX]=aE[X]$ follows directly from factoring $a$ out of the sum. $\blacksquare$

The decisive feature is that **no independence is required** — linearity holds even for arbitrarily dependent, correlated positions. This is why the expected P&L of a book equals the sum of per-strategy expected P&Ls regardless of correlation, and why $EV$ of an $n$-lot trade is exactly $n$ times the $1$-lot $EV$. (Independence is needed only for the *variance* to add, not the mean.)

For a two-outcome trade returning $+b$ (prob. $p$) or $-a$ (prob. $q=1-p$), linearity gives the edge directly:

$$EV = p\,b - q\,a.$$


```chart
expected_value_bars(outcomes=(-100, 150), probs=(0.55, 0.45))
```


A 45%-win-rate setup that loses \$100 or wins \$150 has $EV = 0.55(-100) + 0.45(150) = +12.5$ — positive despite a sub-coinflip hit rate. Edge is a property of the *pair* (win rate, payoff), never either coordinate alone.

## 3. Why the sample mean finds E[X]: the Law of Large Numbers

EV is an *idealization*; what a trader observes is the sample mean $\bar{X}_n = \frac{1}{n}\sum_{i=1}^n X_i$. The bridge is the **Weak Law of Large Numbers**: for i.i.d. $X_i$ with $\mu = E[X]$ and finite variance $\sigma^2$,

$$\bar{X}_n \xrightarrow{\;\mathbb{P}\;} \mu \qquad (n\to\infty).$$

**Derivation via Chebyshev.** For any random variable $Z$ with mean $m$ and variance $v$, Chebyshev's inequality states $\mathbb{P}(|Z - m| \ge \varepsilon) \le v/\varepsilon^2$ (itself a one-line consequence of Markov's inequality applied to $(Z-m)^2$). Apply it to $\bar{X}_n$. By linearity, $E[\bar{X}_n] = \mu$; by independence, variance adds, so

$$\operatorname{Var}(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^n \operatorname{Var}(X_i) = \frac{\sigma^2}{n}.$$

Chebyshev then gives, for every $\varepsilon > 0$,

$$\mathbb{P}\!\left(|\bar{X}_n - \mu| \ge \varepsilon\right) \le \frac{\sigma^2}{n\,\varepsilon^2} \xrightarrow[n\to\infty]{} 0. \qquad \blacksquare$$

Convergence in probability follows. Under only $E[|X|]<\infty$ (no variance assumption) Kolmogorov's **Strong Law** upgrades this to almost-sure convergence, $\bar{X}_n \xrightarrow{\text{a.s.}} \mu$. Empirically, three sample paths of a fair-coin frequency settling onto its mean:


```chart
frequentist_convergence()
```


Two practical corollaries. (i) The rate is $O(\sigma/\sqrt{n})$ — halving sampling error costs *four times* the trades, so a real edge needs many independent repetitions to manifest, exactly the regime where a small per-bet edge becomes near-certain profit. (ii) The finite-variance hypothesis is load-bearing: when $\sigma^2=\infty$ the $\sigma^2/n$ bound is vacuous and the sample mean can wander indefinitely.

## 4. Variance: what EV omits

EV is silent about risk. The **variance** quantifies dispersion about the mean:

$$\operatorname{Var}(X) = E\big[(X-\mu)^2\big] = E[X^2] - (E[X])^2 \ge 0,$$

the identity following from expanding the square and applying linearity. Two setups can share an $EV$ yet differ wildly in $\operatorname{Var}$ — identical center, opposite path experience. Because variance is *not* invariant to dependence,

$$\operatorname{Var}\!\Big(\sum_i X_i\Big) = \sum_i \operatorname{Var}(X_i) + 2\sum_{i<j}\operatorname{Cov}(X_i, X_j),$$

correlated positions inflate portfolio variance even when their expected values simply add. This asymmetry — means always add, variances add only under independence — is precisely why position sizing and correlation control are a *separate* discipline from edge estimation.

## 5. The multiplicative caveat: St. Petersburg and log utility

Maximizing $E[X]$ is the right objective for **additive** payoffs. It fails spectacularly under **multiplicative** (compounding) wealth dynamics — the setting of actual investing. The historical exhibit is the **St. Petersburg paradox** (N. Bernoulli, posed 1713; resolved by D. Bernoulli 1738): a fair coin is tossed until the first head at toss $k$, paying $2^{k-1}$ dollars. The expected payoff is

$$E[\text{payoff}] = \sum_{k=1}^{\infty} \underbrace{2^{-k}}_{\mathbb{P}(\text{first head at }k)} \cdot\, 2^{\,k-1} = \sum_{k=1}^{\infty} \tfrac{1}{2} = \infty,$$

yet no rational agent pays more than a modest stake to play. Daniel Bernoulli's resolution: agents maximize expected **utility of wealth**, not wealth, and with logarithmic utility $u(w)=\log w$ the valuation is finite:

$$E[\log(\text{payoff})] = \sum_{k=1}^{\infty} 2^{-k}\,\log\!\big(2^{\,k-1}\big) = \log 2 \sum_{k=1}^{\infty} (k-1)2^{-k} = \log 2 < \infty.$$

The same $\log$ objective reappears rigorously in growth-optimal (Kelly) betting: over $n$ compounded rounds, $\frac{1}{n}\log(W_n/W_0) \to E[\log R]$ a.s. by the SLLN, so it is $E[\log R]$ — not $E[R]$ — that governs the almost-sure long-run growth rate. Maximizing $E[W_n]$ instead prescribes betting everything, which sends $W_n\to 0$ almost surely. Under multiplicative dynamics the mean and the typical (median) path diverge; **expected value alone is the wrong compass.**

## 6. Where the estimator and the assumptions break

- **Undefined / infinite expectation.** Heavy tails (Cauchy, Pareto with $\alpha \le 1$) have no finite mean; sample "averages" are meaningless. Even $\alpha \in (1,2]$ gives finite mean but infinite variance, voiding the Chebyshev/LLN rate and the CLT-based confidence intervals traders implicitly use.

```chart
normal_vs_fat_tail(nu=2)
```

  A Gaussian assigns negligible mass beyond $\pm 3\sigma$; a Student-$t$ with $\nu=2$ (infinite variance) puts orders of magnitude more probability in the tails — the region where a single realization can dominate the entire running average and invalidate an EV computed from a placid sample.

- **Non-stationarity / non-i.i.d.** The LLN assumes identical distribution and independence. Regime shifts, autocorrelation, and time-varying $\mu,\sigma$ mean $\bar{X}_n$ estimates a moving target; in-sample EV then over- or under-states the forward edge.
- **Selection / estimation bias.** Choosing the best of many backtested setups inflates the apparent $EV$ (multiple-testing / "deflated Sharpe" bias). The realized out-of-sample mean regresses toward — often below — zero. Estimate EV on held-out data and deflate for the number of trials.
- **Rare catastrophic losses.** A left tail truncated in the sample (a loss that simply hasn't happened yet) can flip a nominally positive EV negative. Absence of evidence of ruin is not evidence of its absence.

## 7. Synthesis

Expected value is the first moment: linear (dependence-free), estimable via the sample mean by the law of large numbers, and the exact statement of "edge per trade." Its limits are equally sharp — it can fail to exist under heavy tails, it ignores variance entirely, and it is the *wrong* objective under compounding, where $E[\log W]$ takes over. Used as a decision tool over many independent, finite-variance, stationary bets, it is the backbone of rational trading; used as a prediction or under any of those broken assumptions, it misleads.

## References & further reading

- Bernoulli, D. (1738). *Specimen Theoriae Novae de Mensura Sortis* (English: "Exposition of a New Theory on the Measurement of Risk," *Econometrica*, 1954). — origin of expected utility and the St. Petersburg resolution.
- Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung* (*Foundations of the Theory of Probability*). — measure-theoretic definition of expectation; the Strong Law of Large Numbers.
- Feller, W. (1968/1971). *An Introduction to Probability Theory and Its Applications*, Vols. I & II. — Chebyshev, LLN, St. Petersburg, heavy tails.
- Billingsley, P. (1995). *Probability and Measure.* — rigorous treatment of $E[X]$ as a Lebesgue integral and convergence theorems.
- Kelly, J. L. (1956). *A New Interpretation of Information Rate*, Bell System Technical Journal. — the $E[\log W]$ growth criterion.
- Markov / Chebyshev inequalities — see Feller Vol. I, Ch. IX, or Ross, S. *A First Course in Probability.*
