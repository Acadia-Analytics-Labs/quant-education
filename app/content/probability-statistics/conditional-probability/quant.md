# Conditional Probability & Bayes' Theorem: A Rigorous Treatment

## 1. Formal definition

Work on a probability space $(\Omega, \mathcal{F}, P)$. For events $A, B \in \mathcal{F}$ with $P(B) > 0$, the **conditional probability of $A$ given $B$** is defined as

$$P(A \mid B) := \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.$$

This is a definition, not a theorem: it is the unique renormalization that makes $B$ the new sample space. Fixing $B$, the set function $A \mapsto P(A \mid B)$ is itself a probability measure on $(\Omega, \mathcal{F})$ — it is nonnegative, assigns $P(\Omega \mid B) = 1$, and is countably additive — concentrated on $B$ (i.e. $P(B^c \mid B) = 0$). All the usual axioms therefore transfer to the conditioned measure.

**On $P(B)=0$.** The elementary ratio is undefined when $P(B)=0$, yet we routinely condition on measure-zero events (e.g. a continuous observation $X = x$). The rigorous device is the **regular conditional probability**, built from the conditional expectation $P(A \mid \mathcal{G}) = \mathbb{E}[\mathbf{1}_A \mid \mathcal{G}]$, a $\mathcal{G}$-measurable random variable characterized (via the Radon–Nikodym theorem) by $\int_G P(A \mid \mathcal{G})\,dP = P(A \cap G)$ for all $G \in \mathcal{G}$. The elementary definition above is the special case $\mathcal{G} = \sigma(B)$ with $P(B)>0$.

## 2. Law of total probability

Let $\{A_i\}_{i=1}^{n}$ be a **partition** of $\Omega$: disjoint events with $\bigcup_i A_i = \Omega$ and each $P(A_i) > 0$. For any $B \in \mathcal{F}$,

$$P(B) = \sum_{i=1}^{n} P(B \cap A_i) = \sum_{i=1}^{n} P(B \mid A_i)\,P(A_i).$$

This decomposes an unconditional probability into a weighted average of conditional ones and supplies the denominator (the **normalizing constant** / marginal likelihood / "evidence") in Bayes' theorem.

## 3. Bayes' theorem

For $A, B \in \mathcal{F}$ with $P(A), P(B) > 0$:

$$\boxed{\,P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}\,}$$

**Proof.** By definition, $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ and $P(B \mid A) = \dfrac{P(B \cap A)}{P(A)}$. Since $A \cap B = B \cap A$, the second identity gives $P(A \cap B) = P(B \mid A)\,P(A)$. Substituting into the first,

$$P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}. \qquad \square$$

Expanding the denominator over a partition $\{A_i\}$ (Section 2) yields the operational form

$$P(A_j \mid B) = \frac{P(B \mid A_j)\,P(A_j)}{\sum_{i} P(B \mid A_i)\,P(A_i)}.$$

### 3.1 Odds (Bayes-factor) form

Dividing the posterior for $A$ by the posterior for its complement $A^c$, the shared evidence term $P(B)$ cancels:

$$\underbrace{\frac{P(A \mid B)}{P(A^c \mid B)}}_{\text{posterior odds}} = \underbrace{\frac{P(B \mid A)}{P(B \mid A^c)}}_{\text{likelihood ratio (Bayes factor)}} \times \underbrace{\frac{P(A)}{P(A^c)}}_{\text{prior odds}}.$$

In log form the update is *additive*: $\operatorname{logit} P(A\mid B) = \operatorname{logit} P(A) + \log \mathrm{BF}$. Evidence accumulates by summing log-likelihood ratios — the basis of sequential probability ratio tests and log-odds belief tracking.

### 3.2 Continuous form (densities)

Let $\theta$ be a parameter with prior density $\pi(\theta)$ and let data $x$ have sampling density (likelihood) $f(x \mid \theta)$. The posterior density is

$$\pi(\theta \mid x) = \frac{f(x \mid \theta)\,\pi(\theta)}{\displaystyle\int_{\Theta} f(x \mid \theta')\,\pi(\theta')\,d\theta'} \;\propto\; f(x \mid \theta)\,\pi(\theta).$$

The denominator $m(x) = \int f(x\mid\theta')\pi(\theta')\,d\theta'$ is the **marginal likelihood** (evidence); it is the continuous analogue of the total-probability sum and is often left implicit, writing $\text{posterior} \propto \text{likelihood} \times \text{prior}$.

## 4. Base rates and the false-positive problem

Bayes' theorem is most instructive where intuition fails: a highly accurate test for a rare condition. Let $D$ be "has the disease" and $+$ be "tests positive." Suppose

- **Prevalence (prior):** $P(D) = 0.001$ (1 in 1,000),
- **Sensitivity:** $P(+ \mid D) = 0.99$,
- **Specificity:** $P(- \mid D^c) = 0.99$, so the **false-positive rate** is $P(+ \mid D^c) = 0.01$.

By total probability the evidence is

$$P(+) = P(+\mid D)P(D) + P(+\mid D^c)P(D^c) = (0.99)(0.001) + (0.01)(0.999) = 0.00099 + 0.00999 = 0.01098.$$

Then

$$P(D \mid +) = \frac{P(+\mid D)\,P(D)}{P(+)} = \frac{0.00099}{0.01098} \approx 0.0902.$$

Despite a "99% accurate" test, a positive result implies only a **~9%** chance of disease. The reason is structural, and the odds form makes it transparent:

$$\underbrace{\frac{P(D)}{P(D^c)}}_{1:999} \times \underbrace{\frac{P(+\mid D)}{P(+\mid D^c)}}_{99:1} = \frac{99}{999} \approx 1:10 \;\Longrightarrow\; P(D\mid +) \approx \frac{1}{11} \approx 0.09.$$

The tiny prior swamps the strong likelihood ratio. Ignoring $P(D)$ — treating $P(D\mid+)$ as if it equaled the sensitivity $P(+\mid D)$ — is the **base-rate fallacy** (inverting the conditional). The same trap recurs in trading: a signal with a great hit rate on a rare event still produces mostly false alarms, and position sizing must respect the posterior, not the likelihood.

## 5. Sequential Bayesian updating

Bayes' theorem is recursive: after observing $x_1$, the posterior $\pi(\theta \mid x_1)$ becomes the **prior** for the next observation. For conditionally independent data $x_{1:n}$,

$$\pi(\theta \mid x_{1:n}) \;\propto\; \pi(\theta)\prod_{t=1}^{n} f(x_t \mid \theta),$$

and processing the data one point at a time gives the identical result — order-invariance is a hallmark of coherent updating. The discrete two-hypothesis version is the two-bags posterior: an even prior over $\{B_1, B_2\}$ updated by one green draw (likelihoods $0.5$ vs $0.7$) yields the posterior below.

```chart
bayes_update(prior=(0.5, 0.5), likelihood=(0.5, 0.7), labels=("Bag 1", "Bag 2"))
```

### 5.1 Conjugate updating: the Beta–Bernoulli model

For an unknown success probability $\theta \in [0,1]$ (a coin bias, a strategy's per-trade win rate) with a $\mathrm{Beta}(\alpha, \beta)$ prior, a Bernoulli/Binomial likelihood is **conjugate**: after $h$ successes and $t$ failures,

$$\pi(\theta) = \mathrm{Beta}(\alpha, \beta) \;\xrightarrow{\;h\text{ heads},\, t\text{ tails}\;}\; \pi(\theta \mid \text{data}) = \mathrm{Beta}(\alpha + h,\; \beta + t).$$

The proof is immediate from Section 3.2: $\pi(\theta\mid \text{data}) \propto \theta^{h}(1-\theta)^{t}\cdot \theta^{\alpha-1}(1-\theta)^{\beta-1} = \theta^{\alpha+h-1}(1-\theta)^{\beta+t-1}$, the kernel of a $\mathrm{Beta}(\alpha+h, \beta+t)$. The prior hyperparameters act as **pseudo-counts**, and the posterior mean $\frac{\alpha+h}{\alpha+\beta+h+t}$ shrinks the empirical frequency $\frac{h}{h+t}$ toward the prior mean — a Bayesian regularizer against small-sample overconfidence. Conjugacy is exactly what makes "posterior becomes next prior" computationally trivial: updating is just incrementing counters.

```chart
beta_update(prior_a=2, prior_b=2, heads=8, tails=2)
```

Starting from a symmetric $\mathrm{Beta}(2,2)$ prior, observing 8 wins and 2 losses concentrates the belief density toward higher $\theta$ while retaining honest uncertainty — the posterior is a distribution, not a point estimate, which is precisely what disciplined risk-taking requires.

### 5.2 Where the machinery strains

- **Likelihood misspecification.** Bayes is only as good as $f(x\mid\theta)$; a wrong model can update *confidently* toward a wrong answer, and the marginal likelihood offers no protection if the true data-generating process is outside the support of the prior (Cromwell's rule: never assign prior $0$ to a possible hypothesis).
- **Non-stationarity.** Financial $\theta$ drifts with regime; naive accumulation of all history over-weights stale data. Remedies include discounting (exponential forgetting), change-point priors, and state-space / particle filters.
- **Dependence.** The product-of-likelihoods form assumes conditional independence; serial correlation inflates effective sample size and produces spurious posterior certainty.

## References & further reading

- Bayes, T. (1763). *An Essay towards Solving a Problem in the Doctrine of Chances.* Phil. Trans. Royal Society.
- Laplace, P.-S. (1814). *Essai philosophique sur les probabilités.*
- Kolmogorov, A. N. (1933). *Foundations of the Theory of Probability* (measure-theoretic conditioning).
- Jaynes, E. T. (2003). *Probability Theory: The Logic of Science.* Cambridge University Press.
- Gelman, A., Carlin, J., Stern, H., Dunson, D., Vehtari, A., Rubin, D. (2013). *Bayesian Data Analysis*, 3rd ed. CRC Press.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning* (conjugate priors, sequential updating).
