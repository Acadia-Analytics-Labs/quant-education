# Machine Learning in Trading: A Rigorous Introduction

## 1. Supervised learning as empirical risk minimization

Let $(X, Y) \sim P$ on $\mathcal{X}\times\mathcal{Y}$ be drawn from an unknown joint law. A **loss** $L:\mathcal{Y}\times\mathcal{Y}\to\mathbb{R}_{\ge 0}$ measures the cost of predicting $\hat y$ when the truth is $y$ (squared loss $L(y,\hat y)=(y-\hat y)^2$ for regression, $0\text{-}1$ or cross-entropy for classification). The object we actually want to minimize is the **population risk**

$$R(f) = \mathbb{E}_{(X,Y)\sim P}\big[L(Y, f(X))\big].$$

For squared loss the risk-minimizer over all measurable $f$ is the **regression function** $f^\*(x)=\mathbb{E}[Y\mid X=x]$; for $0\text{-}1$ loss it is the **Bayes classifier**. We cannot compute $R$ because $P$ is unknown, so given a sample $D=\{(x_i,y_i)\}_{i=1}^n$ we minimize the **empirical risk** over a hypothesis class $\mathcal{F}$:

$$\hat f = \arg\min_{f\in\mathcal{F}} \; \widehat R_n(f), \qquad \widehat R_n(f) = \frac{1}{n}\sum_{i=1}^n L\big(y_i, f(x_i)\big).$$

The generalization question is the gap $R(\hat f) - \widehat R_n(\hat f)$. It decomposes into **approximation error** (how well the best $f\in\mathcal{F}$ can do) and **estimation error** (how much finite noisy data misleads us). Enlarging $\mathcal{F}$ shrinks the first and inflates the second — the formal statement of the bias–variance trade-off derived next.

## 2. The bias–variance decomposition (derivation)

Fix a query point $x$ and adopt the signal-plus-noise model

$$Y = f^\*(x) + \varepsilon, \qquad \mathbb{E}[\varepsilon]=0, \quad \operatorname{Var}(\varepsilon)=\sigma^2, \quad \varepsilon \perp \hat f.$$

The estimator $\hat f(x)$ is random because it depends on the training sample $D$. Write $\bar f(x)=\mathbb{E}_D[\hat f(x)]$. We evaluate the expected test error over both the noise $\varepsilon$ and the draw of $D$:

$$
\mathbb{E}\big[(Y-\hat f(x))^2\big]
= \mathbb{E}\big[(f^\* + \varepsilon - \hat f)^2\big]
= \underbrace{\mathbb{E}[(f^\* - \hat f)^2]}_{\text{estimation}} + \underbrace{\mathbb{E}[\varepsilon^2]}_{\sigma^2} + 2\,\mathbb{E}[\varepsilon(f^\*-\hat f)].
$$

Because $\varepsilon$ is the *test-point* noise, independent of the training draw $\hat f$, and mean-zero, the cross term vanishes: $\mathbb{E}[\varepsilon(f^\*-\hat f)] = \mathbb{E}[\varepsilon]\,\mathbb{E}[f^\*-\hat f] = 0$. Now split the first term by adding and subtracting $\bar f$:

$$
\mathbb{E}[(f^\* - \hat f)^2]
= \mathbb{E}\big[(f^\* - \bar f + \bar f - \hat f)^2\big]
= (f^\* - \bar f)^2 + \mathbb{E}[(\bar f - \hat f)^2] + 2(f^\*-\bar f)\,\mathbb{E}[\bar f - \hat f].
$$

Here $f^\*-\bar f$ is deterministic and $\mathbb{E}[\bar f - \hat f] = \bar f - \mathbb{E}[\hat f] = 0$, so the last term drops. Collecting everything:

$$
\boxed{\;\mathbb{E}\big[(Y-\hat f(x))^2\big] = \underbrace{(f^\*(x)-\bar f(x))^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}\big[(\hat f(x)-\bar f(x))^2\big]}_{\text{Variance}} + \underbrace{\sigma^2}_{\text{irreducible}}\;}
$$

The irreducible term $\sigma^2$ is a hard floor set by $P$ itself — no estimator beats it. Model complexity trades the other two: a rigid model has high bias and low variance; a flexible one has low bias and high variance. Minimizing test error means minimizing $\text{Bias}^2+\text{Variance}$, which is generally **not** at zero training error.

```chart
overfitting_curve()
```

## 3. Why financial ML is uniquely hard

The i.i.d. assumptions underneath the theory above fail in markets, in three compounding ways.

**Low signal-to-noise.** For daily equity returns the predictable component of variance is a few percent at best; $R^2$ values of $0.001$–$0.01$ can still be economically meaningful. With such a low true signal, the *variance* term dominates the decomposition, so the effective sweet spot sits at very low complexity and heavy regularization. Almost any flexible model will fit noise.

**Non-stationarity.** $P$ drifts: $P_t \neq P_{t+h}$. Volatility regimes, microstructure, and the reflexive effect of crowded strategies mean the map learned on 2015–2019 need not hold in 2020. The population risk is a moving target, so out-of-sample decay is the norm, not a bug.

**Non-i.i.d., serially dependent samples.** Overlapping labels (e.g. a 5-day forward return sampled daily) and volatility clustering make adjacent observations strongly dependent. Two consequences:

1. Effective sample size $n_{\text{eff}} \ll n$, so variance estimates and $t$-statistics are badly inflated.
2. **Random k-fold cross-validation leaks.** If a test fold sits between two training folds, an observation whose label horizon overlaps a training observation shares information across the split — the model is graded on data it has effectively seen. Shuffling destroys the time ordering that is the entire point.

## 4. Honest validation: purged and embargoed CV

Because information flows forward in time, validation must respect that arrow. The minimal correct scheme is **walk-forward**: train on $[t_0, t)$, test on $[t, t+h)$, roll forward.

```chart
walk_forward_cv()
```

López de Prado's **purged k-fold with embargo** generalizes this while still using multiple folds. Let each observation $i$ carry a label spanning the interval $[t_{i,0}, t_{i,1}]$ (e.g. entry to exit). For a given test fold $T$:

- **Purge:** drop from the training set every observation $j$ whose label interval $[t_{j,0}, t_{j,1}]$ overlaps any test label interval — these would leak future information into training.
- **Embargo:** additionally remove training observations within a small window of length $\eta$ *after* the test set, since serial correlation makes the samples just after the test period informative about it. A typical $\eta \approx 0.01\,T$ of the series length.

Only after purging and embargoing is the estimated $R(\hat f)$ an approximately unbiased estimate of live performance. Skipping this is the single most common reason a backtest Sharpe evaporates in production.

## 5. Classification metrics and asymmetric cost

For a direction classifier, raw accuracy is nearly useless: a 55%-accurate model can be highly profitable and a 60%-accurate one can lose money, depending on *which* errors occur and their P&L size. Decompose predictions into the confusion matrix and attach an economic cost to each cell.

```chart
confusion_matrix_demo()
```

With costs $c_{\text{FP}}, c_{\text{FN}}$ the decision threshold should minimize expected cost, not error count: predict "up" when the posterior $\mathbb{P}(\text{up}\mid x)$ exceeds $c_{\text{FP}}/(c_{\text{FP}}+c_{\text{FN}})$ rather than $0.5$. The relevant objective is expected utility of realized P&L, so metrics should be P&L-weighted (a false long into a crash is not a false short into a rally).

## 6. Multiple testing and backtest overfitting

The deepest pitfall is statistical, not algorithmic. If you evaluate $N$ strategy configurations and keep the best Sharpe, you are sampling the **maximum** of $N$ noisy statistics; under the null of zero skill its expectation grows like $\sqrt{2\log N}$. Reporting the winner's in-sample Sharpe without adjusting for $N$ is guaranteed selection bias.

The **Probabilistic Sharpe Ratio** (Bailey–López de Prado) tests an observed $\widehat{SR}$ (per-observation) against a benchmark $SR^\*$, correcting for the higher moments of returns:

$$\widehat{\text{PSR}}(SR^\*) = \Phi\!\left(\frac{(\widehat{SR}-SR^\*)\,\sqrt{T-1}}{\sqrt{\,1 - \gamma_3\,\widehat{SR} + \tfrac{\gamma_4-1}{4}\,\widehat{SR}^2\,}}\right),$$

where $T$ is the number of returns, $\gamma_3$ their skewness, $\gamma_4$ their kurtosis, and $\Phi$ the standard normal CDF. Fat left tails ($\gamma_3<0$) and excess kurtosis ($\gamma_4>3$) *lower* confidence in a given Sharpe.

The **Deflated Sharpe Ratio** sets the benchmark $SR^\*$ to the expected maximum Sharpe under $N$ independent trials of no-skill strategies:

$$
SR^\*_0 = \sqrt{\operatorname{Var}[\widehat{SR}_n]}\;\Big[(1-\gamma)\,\Phi^{-1}\!\big(1-\tfrac{1}{N}\big) + \gamma\,\Phi^{-1}\!\big(1-\tfrac{1}{N e}\big)\Big], \qquad \text{DSR}=\widehat{\text{PSR}}(SR^\*_0),
$$

with $\gamma\approx 0.5772$ the Euler–Mascheroni constant and $\operatorname{Var}[\widehat{SR}_n]$ the variance of Sharpe across the $N$ trials. As $N$ grows, $SR^\*_0$ rises, so a strategy must clear a higher bar to be judged skillful. Track $N$ honestly — every parameter you swept counts.

## 7. Regularization

Regularization operationalizes the bias–variance trade-off by penalizing complexity, deliberately adding bias to cut variance:

$$\hat\beta = \arg\min_{\beta}\; \frac{1}{n}\sum_{i=1}^n L\big(y_i, f_\beta(x_i)\big) + \lambda\,\Omega(\beta).$$

- **Ridge ($L_2$):** $\Omega(\beta)=\lVert\beta\rVert_2^2$ shrinks coefficients smoothly; with Gaussian noise it is the MAP estimate under a Gaussian prior and always lowers variance. For $X^\top X$ ill-conditioned by collinear features (ubiquitous with technical indicators), ridge stabilizes the solution.
- **Lasso ($L_1$):** $\Omega(\beta)=\lVert\beta\rVert_1$ induces sparsity, performing feature selection — valuable when you have hundreds of candidate signals and expect most to be noise.
- **Elastic net:** a convex combination of the two.

The penalty strength $\lambda$ is itself a hyperparameter and must be tuned **inside** the purged/embargoed CV loop — tuning it on the test set silently reintroduces look-ahead bias. Early stopping, dropout, and tree-depth limits are the analogous complexity controls for neural nets and gradient-boosted trees.

## References & further reading

- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer. — bias–variance, ERM, regularization.
- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley. — purged/embargoed CV, labeling, backtest overfitting.
- Bailey, D. H., & López de Prado, M. (2014). *The Deflated Sharpe Ratio.* Journal of Portfolio Management. — PSR and DSR.
- Bailey, D. H., Borwein, J., López de Prado, M., & Zhu, Q. J. (2014). *Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting.* Notices of the AMS.
- Arnott, R., Harvey, C. R., & Markowitz, H. (2019). *A Backtesting Protocol in the Era of Machine Learning.* Journal of Financial Data Science.
- Harvey, C. R., Liu, Y., & Zhu, H. (2016). *…and the Cross-Section of Expected Returns.* Review of Financial Studies. — multiple-testing haircuts.
