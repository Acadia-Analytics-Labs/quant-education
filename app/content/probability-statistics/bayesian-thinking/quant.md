# Probability: Measure-Theoretic Foundations and the Bayesian–Frequentist Split

## 1. The Kolmogorov axioms

Modern probability is a special case of measure theory. Fix a **sample space** $\Omega$ (the set of all elementary outcomes). We do not, in general, assign probability to *every* subset of $\Omega$ — that is impossible for uncountable $\Omega$ (Vitali) — so we restrict to a well-behaved collection of "measurable" events.

A **$\sigma$-algebra** $\mathcal{F} \subseteq 2^\Omega$ is a family of subsets satisfying:

1. $\Omega \in \mathcal{F}$;
2. **closure under complement**: $A \in \mathcal{F} \Rightarrow A^c \in \mathcal{F}$;
3. **closure under countable unions**: $A_1, A_2, \dots \in \mathcal{F} \Rightarrow \bigcup_{i=1}^{\infty} A_i \in \mathcal{F}$.

A **probability measure** is a set function $P : \mathcal{F} \to [0,1]$ obeying Kolmogorov's three axioms:

$$\textbf{(K1)}\quad P(A) \ge 0 \ \ \forall A \in \mathcal{F}, \qquad \textbf{(K2)}\quad P(\Omega) = 1,$$

$$\textbf{(K3, countable additivity)}\quad P\!\left(\bigsqcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i) \quad \text{for pairwise disjoint } A_i.$$

The triple $(\Omega, \mathcal{F}, P)$ is a **probability space**. Everything else is a theorem. From (K1)–(K3): $P(\varnothing)=0$; monotonicity $A \subseteq B \Rightarrow P(A) \le P(B)$; the complement rule $P(A^c) = 1 - P(A)$; inclusion–exclusion $P(A \cup B) = P(A) + P(B) - P(A\cap B)$; and **continuity from below**, $A_n \uparrow A \Rightarrow P(A_n) \uparrow P(A)$, which is equivalent to (K3) given finite additivity.

A **random variable** is a measurable map $X : \Omega \to \mathbb{R}$ (i.e. $X^{-1}(B) \in \mathcal{F}$ for every Borel $B$), and its law is the pushforward measure $P_X = P \circ X^{-1}$ on $(\mathbb{R}, \mathcal{B})$. Expectation is the Lebesgue integral $\mathbb{E}[X] = \int_\Omega X \, dP$.

Two events are **independent** if $P(A \cap B) = P(A)P(B)$; **conditional probability** is defined (for $P(B)>0$) by $P(A \mid B) = P(A \cap B)/P(B)$, from which Bayes' rule is immediate. Crucially, *the axioms are silent on what $P$ means.* That interpretive gap is where the two schools part ways.

## 2. The frequentist program

**Ontology.** $P(A)$ is an objective, fixed (if unknown) property of a repeatable data-generating process — operationally, the limiting relative frequency $P(A) = \lim_{n\to\infty} \tfrac{1}{n}\sum_{i=1}^n \mathbf{1}_{A}(\omega_i)$ over i.i.d. replications. Parameters $\theta$ are fixed constants; **data are random**. Probability statements attach to *procedures*, not to $\theta$.

**Why the frequency converges — the LLN.** Let $X_1, X_2, \dots$ be i.i.d. with $\mathbb{E}[X] = \mu$ and $\operatorname{Var}(X) = \sigma^2 < \infty$, and $\bar X_n = \tfrac1n\sum_{i=1}^n X_i$. Then $\mathbb{E}[\bar X_n] = \mu$ and $\operatorname{Var}(\bar X_n) = \sigma^2/n$. By Chebyshev, for any $\varepsilon > 0$,

$$P\big(|\bar X_n - \mu| \ge \varepsilon\big) \le \frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \xrightarrow[n\to\infty]{} 0,$$

which is the **weak law** ($\bar X_n \xrightarrow{P} \mu$). Kolmogorov's **strong law** strengthens this to almost-sure convergence, $\bar X_n \xrightarrow{\text{a.s.}} \mu$, under only $\mathbb{E}|X| < \infty$. Taking $X_i = \mathbf{1}_A(\omega_i)$ gives $\mu = P(A)$: the empirical frequency of an event converges to its probability. This *is* the frequentist interpretation, promoted from definition to theorem. The jitter-then-settle behavior is visible in repeated coin-tossing:

```chart
frequentist_convergence()
```

**Estimators and confidence intervals.** For Bernoulli$(\theta)$ data with $k$ successes in $n$ trials, the MLE is $\hat\theta = k/n$. By the CLT, $\sqrt{n}(\hat\theta - \theta) \xrightarrow{d} \mathcal{N}(0, \theta(1-\theta))$, giving the Wald $(1-\alpha)$ interval

$$\hat\theta \pm z_{1-\alpha/2}\sqrt{\tfrac{\hat\theta(1-\hat\theta)}{n}}.$$

The coverage statement is subtle: a 95% CI means the **random interval** covers the fixed $\theta$ in 95% of repeated experiments. It does **not** say $P(\theta \in [\,\ell, u\,]) = 0.95$ for the realized numeric bounds — under this ontology $\theta$ is not random, so that probability is either 0 or 1. Frequentist inference (Neyman–Pearson tests, $p$-values, unbiasedness) controls error rates *over the sampling distribution*.

## 3. The Bayesian program

**Ontology.** $P$ encodes a rational agent's **degree of belief**, coherent in the sense that a bookmaker quoting these numbers cannot be Dutch-booked (de Finetti). Here $\theta$ is treated as **random** — not because it fluctuates, but because it is unknown — and data, once observed, are fixed. Inference is conditioning:

$$\underbrace{\pi(\theta \mid D)}_{\text{posterior}} = \frac{\overbrace{p(D \mid \theta)}^{\text{likelihood}}\ \overbrace{\pi(\theta)}^{\text{prior}}}{\underbrace{\textstyle\int p(D\mid\theta)\pi(\theta)\,d\theta}_{\text{evidence } p(D)}} \ \propto\ p(D \mid \theta)\,\pi(\theta).$$

De Finetti's **representation theorem** supplies the philosophical bridge: if a sequence is *exchangeable* (its law is invariant to finite permutations), then it is a mixture of i.i.d. sequences, $P(x_1,\dots,x_n) = \int \big(\prod_i \theta^{x_i}(1-\theta)^{1-x_i}\big)\,d\mu(\theta)$. The "unknown fixed frequency" $\theta$ and its prior $\mu$ emerge as *mathematical consequences* of subjective exchangeability — the frequentist parameter is recovered inside the Bayesian frame.

### Conjugate example: the Beta–Binomial model

Put a **Beta$(\alpha, \beta)$** prior on the success probability $\theta$:

$$\pi(\theta) = \frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha,\beta)}, \qquad B(\alpha,\beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}.$$

Observe $k$ heads and $n-k$ tails, so the Binomial likelihood is $p(D\mid\theta) \propto \theta^{k}(1-\theta)^{n-k}$. Then

$$\pi(\theta \mid D) \ \propto\ \theta^{k}(1-\theta)^{n-k}\cdot \theta^{\alpha-1}(1-\theta)^{\beta-1} = \theta^{(\alpha+k)-1}(1-\theta)^{(\beta+n-k)-1},$$

which is the kernel of a **Beta$(\alpha + k,\ \beta + n - k)$** density. The Beta family is **conjugate** to the Binomial likelihood — the posterior stays in the family, so updating is just arithmetic on the hyperparameters:

$$\boxed{\ \text{Beta}(\alpha, \beta) \ \xrightarrow{\ k\ \text{heads},\ t = n-k\ \text{tails}\ }\ \text{Beta}(\alpha + k,\ \beta + t)\ }$$

The prior hyperparameters act as **pseudo-counts** ($\alpha - 1$ prior successes, $\beta - 1$ prior failures). The posterior mean is a precision-weighted blend of prior mean and sample proportion,

$$\mathbb{E}[\theta \mid D] = \frac{\alpha + k}{\alpha + \beta + n} = \underbrace{\frac{\alpha+\beta}{\alpha+\beta+n}}_{\to\, 0}\cdot\frac{\alpha}{\alpha+\beta} \;+\; \underbrace{\frac{n}{\alpha+\beta+n}}_{\to\, 1}\cdot\frac{k}{n},$$

so as $n \to \infty$ the posterior mean $\to \hat\theta_{\text{MLE}} = k/n$ and the posterior concentrates ($\operatorname{Var} = O(1/n)$) — the **Bernstein–von Mises** phenomenon, whereby the prior washes out and Bayesian and frequentist answers coincide asymptotically. Starting from a weak Beta$(2,2)$ prior and observing 8 heads, 2 tails:

```chart
beta_update(prior_a=2, prior_b=2, heads=8, tails=2)
```

Unlike a confidence interval, the Bayesian **95% credible interval** $[\ell, u]$ with $\int_\ell^u \pi(\theta\mid D)\,d\theta = 0.95$ *does* license the statement $P(\theta \in [\ell, u] \mid D) = 0.95$ — because here $\theta$ carries a distribution.

## 4. Where each framework strains

- **Frequentist:** no coherent probability for one-off, non-repeatable events (a specific firm's default this year); reliance on the counterfactual "reference class" of repetitions is ambiguous; $p$-values are routinely misinterpreted as $P(H_0\mid D)$.
- **Bayesian:** answers depend on the prior, which can smuggle in bias; the evidence integral $p(D) = \int p(D\mid\theta)\pi(\theta)\,d\theta$ is generally intractable, forcing MCMC/variational approximation; improper priors can yield improper posteriors.
- **Shared failure modes:** i.i.d./exchangeability and stationarity assumptions break under regime shift and heavy tails; model misspecification voids both the CLT-based CI and the Bernstein–von Mises guarantee. In finance, treat the "known likelihood" itself as uncertain (model risk).

## 5. Synthesis

The Kolmogorov axioms are interpretation-neutral plumbing; the split is epistemic, over what the symbol $P$ *refers to*. Frequentism randomizes the data and fixes the parameter (procedures with guaranteed long-run error rates); Bayesianism randomizes belief about the parameter and conditions on the data (coherent updating). They agree in the large-sample limit (Bernstein–von Mises) and, via de Finetti, are two readings of the same exchangeable structure. Competent quantitative practice is bilingual: Bayesian updating where priors are principled and events are unique, frequentist error control where procedures must be calibrated across many trades.

## References & further reading

- Kolmogorov, A. N. (1933). *Grundbegriffe der Wahrscheinlichkeitsrechnung* (Foundations of the Theory of Probability).
- de Finetti, B. (1937). *La prévision: ses lois logiques, ses sources subjectives* — exchangeability and the representation theorem.
- Jaynes, E. T. (2003). *Probability Theory: The Logic of Science.*
- Gelman, A., Carlin, Stern, Dunson, Vehtari & Rubin (2013). *Bayesian Data Analysis*, 3rd ed. (BDA3).
- Billingsley, P. (1995). *Probability and Measure.*
- Casella, G. & Berger, R. L. (2002). *Statistical Inference* (frequentist estimation, CIs).
- van der Vaart, A. W. (1998). *Asymptotic Statistics* (LLN, CLT, Bernstein–von Mises).
