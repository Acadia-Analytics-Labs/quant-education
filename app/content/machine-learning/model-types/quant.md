# Machine Learning Model Types: A Decision-Theoretic Map

The taxonomy "supervised / unsupervised / reinforcement" is not a marketing partition — it is a statement about the *object being estimated*. Supervised learning estimates a conditional functional of an unknown joint law; unsupervised learning estimates the law's structure directly; reinforcement learning estimates an optimal control of a Markov decision process. Everything else — linear models, trees, kernels, nets — is a hypothesis class with a particular **inductive bias**. We formalize each and derive the results that govern model choice.

## 1. Supervised learning as risk minimization

Let $(X, Y) \sim P$ on $\mathcal{X} \times \mathcal{Y}$, with $P$ unknown. Fix a loss $L : \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\ge 0}$. For a predictor $f : \mathcal{X} \to \mathcal{Y}$ define the **risk** (expected loss)

$$R(f) = \mathbb{E}_{(X,Y)\sim P}\big[L(Y, f(X))\big].$$

The unconstrained minimizer $f^\star = \arg\min_f R(f)$ is the **Bayes predictor** and $R(f^\star)$ the **Bayes risk** — the irreducible floor. We never see $P$; we see a sample $\mathcal{D} = \{(x_i,y_i)\}_{i=1}^n \overset{\text{iid}}{\sim} P$ and minimize the **empirical risk** over a hypothesis class $\mathcal{F}$:

$$\hat f = \arg\min_{f \in \mathcal{F}} \; \underbrace{\frac{1}{n}\sum_{i=1}^n L(y_i, f(x_i))}_{\hat R_n(f)} \;+\; \lambda\,\Omega(f),$$

with a complexity penalty $\Omega$ (structural risk minimization). The excess risk decomposes as

$$R(\hat f) - R(f^\star) = \underbrace{\big[R(\hat f) - \inf_{f\in\mathcal F} R(f)\big]}_{\text{estimation error (variance)}} + \underbrace{\big[\inf_{f\in\mathcal F} R(f) - R(f^\star)\big]}_{\text{approximation error (bias)}}.$$

Enlarging $\mathcal{F}$ shrinks approximation error but inflates estimation error — the tension the rest of the article quantifies.

### Derivation: the Bayes predictor under squared loss is the conditional mean

For $L(y,a) = (y-a)^2$, condition on $X=x$ and minimize pointwise over the constant $a = f(x)$:

$$\mathbb{E}\big[(Y-a)^2 \mid X=x\big] = \underbrace{\mathrm{Var}(Y\mid X=x)}_{\text{independent of }a} + \big(\mathbb{E}[Y\mid X=x] - a\big)^2 .$$

The second term is minimized at $a = \mathbb{E}[Y\mid X=x]$, so

$$\boxed{\,f^\star(x) = \mathbb{E}[Y \mid X=x]\,}, \qquad R(f^\star) = \mathbb{E}\big[\mathrm{Var}(Y\mid X)\big] = \sigma^2_{\text{irr}}.$$

Regression *is* conditional-mean estimation. The analogous result for $0\text{-}1$ loss is the **Bayes classifier** $f^\star(x) = \arg\max_{k} P(Y=k \mid X=x)$, whose risk is $1 - \mathbb{E}[\max_k P(Y=k\mid X)]$.

## 2. The bias–variance decomposition

Let $Y = f(x) + \varepsilon$ with $\mathbb{E}[\varepsilon]=0$, $\mathrm{Var}(\varepsilon)=\sigma^2$, and let $\hat f$ be trained on a random $\mathcal{D}$. At a fixed test point $x$, taking expectation over $\mathcal{D}$ and $\varepsilon$:

$$
\mathbb{E}\big[(Y - \hat f(x))^2\big]
= \underbrace{\sigma^2}_{\text{irreducible}}
+ \underbrace{\big(\mathbb{E}[\hat f(x)] - f(x)\big)^2}_{\text{bias}^2}
+ \underbrace{\mathbb{E}\big[(\hat f(x) - \mathbb{E}[\hat f(x)])^2\big]}_{\text{variance}}.
$$

*Proof.* Write $Y - \hat f = (Y - f) + (f - \mathbb{E}\hat f) + (\mathbb{E}\hat f - \hat f)$. Square and take expectations; the three cross terms vanish because $\varepsilon \perp \hat f$, $\mathbb{E}[\varepsilon]=0$, and $\mathbb{E}[\hat f - \mathbb{E}\hat f]=0$. $\square$

Complexity trades bias for variance; the test-error minimum sits at their sum's low point — the U-curve that every regularizer, depth limit, and early-stop is chasing:


```chart
overfitting_curve()
```


This is *the* organizing principle of supervised model selection: linear models are high-bias/low-variance, deep trees and unregularized nets are low-bias/high-variance, and the "right" family is the one whose bias floor is low enough while its variance stays payable at your sample size.

## 3. Generative vs. discriminative

Two ways to obtain the classifier $f^\star(x) = \arg\max_k P(Y=k\mid x)$:

- **Discriminative** — model $P(Y\mid X)$ (or just the decision boundary) directly: logistic regression, SVM, trees, neural nets. Fewer assumptions, typically lower asymptotic error.
- **Generative** — model the class-conditionals and prior $P(X\mid Y)\,P(Y)$, then invert via Bayes: naive Bayes, Gaussian discriminant analysis, mixtures. Lets you sample $x$, handle missing features, and inject priors.

**Naive Bayes** assumes conditional independence $P(x\mid y) = \prod_j P(x_j\mid y)$, giving

$$P(y\mid x) \propto P(y)\prod_{j=1}^{d} P(x_j\mid y).$$

Ng & Jordan (2002) show the trade-off precisely: a generative model reaches its (higher) asymptotic error faster — $O(\log d)$ samples vs. $O(d)$ for its discriminative twin — so it wins in the small-$n$ regime and loses asymptotically. On financial features the independence assumption is badly violated (returns, volatility, and volume are strongly co-dependent), which is why naive Bayes is a weak default there.

## 4. Unsupervised learning as density / structure estimation

Now $Y$ is absent; the target is the law of $X$ or a low-dimensional summary of it.

**Density estimation.** Fit $p_\theta(x)$ by maximum likelihood, $\hat\theta = \arg\max_\theta \sum_i \log p_\theta(x_i)$ (mixtures via EM). **Clustering** is a quantization special case: $k$-means minimizes within-cluster distortion

$$J(\{\mu_k\}, \{z_i\}) = \sum_{i=1}^n \lVert x_i - \mu_{z_i}\rVert^2,$$

which is the small-variance / hard-assignment limit of EM for an isotropic Gaussian mixture.

### Derivation: PCA maximizes projected variance

Let $\Sigma = \mathrm{Cov}(X)$. The first principal direction solves $\max_{\lVert w\rVert = 1} \mathrm{Var}(w^\top X) = w^\top \Sigma w$. Form the Lagrangian $\mathcal{L}(w,\lambda) = w^\top\Sigma w - \lambda(w^\top w - 1)$ and set $\nabla_w \mathcal{L} = 0$:

$$2\Sigma w - 2\lambda w = 0 \;\Longrightarrow\; \Sigma w = \lambda w .$$

So $w$ is an eigenvector of $\Sigma$ and the projected variance equals its eigenvalue $\lambda$; the maximum is the top eigenvector. Equivalently, PCA minimizes reconstruction error $\mathbb{E}\lVert x - WW^\top x\rVert^2$ over orthonormal $W$ — variance maximization and best linear autoencoding are the same problem.

Why compression is *necessary*, not merely convenient: in high dimensions data concentrates on the boundary of its support, so almost all volume — and all near-neighbor distances — collapse toward the edge, gutting any method that relies on locality:


```chart
curse_of_dimensionality()
```


The **manifold hypothesis** is the escape hatch: real data of nominal dimension $D$ typically lies near a manifold of intrinsic dimension $d \ll D$, and PCA/autoencoders/UMAP recover coordinates on it.

## 5. Reinforcement learning as a Markov decision process

An RL problem is the tuple $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, r, \gamma)$: states $\mathcal{S}$, actions $\mathcal{A}$, transition kernel $P(s'\mid s,a)$, reward $r(s,a)$, discount $\gamma \in [0,1)$. A policy $\pi(a\mid s)$ induces the return $G_t = \sum_{k\ge 0}\gamma^k r_{t+k+1}$ and value functions

$$V^\pi(s) = \mathbb{E}_\pi[G_t \mid s_t = s], \qquad Q^\pi(s,a) = \mathbb{E}_\pi[G_t \mid s_t=s, a_t=a].$$

The **Bellman expectation equation** follows from the tower property:

$$V^\pi(s) = \sum_a \pi(a\mid s)\sum_{s'} P(s'\mid s,a)\big[r(s,a) + \gamma V^\pi(s')\big],$$

and the **Bellman optimality equation** characterizes $V^\star = \max_\pi V^\pi$:

$$V^\star(s) = \max_{a} \sum_{s'} P(s'\mid s,a)\big[r(s,a) + \gamma V^\star(s')\big], \qquad \pi^\star(s) = \arg\max_a Q^\star(s,a).$$

The Bellman operator is a $\gamma$-contraction in the sup-norm, so value/policy iteration converge geometrically to the unique fixed point. Model-free control (Q-learning, DQN, policy-gradient/PPO) estimates these without knowing $P$. Reward improves with training but at high variance across seeds:


```chart
rl_reward_curve()
```


On markets the MDP assumptions strain: state is **partially observed** (a POMDP), transitions are **non-stationary**, rewards are noisy and low signal-to-noise, and off-policy evaluation is treacherous — which is why RL trading agents so readily learn backtest artifacts.

## 6. No free lunch and inductive bias

Why can't one algorithm dominate? The **No-Free-Lunch theorem** (Wolpert 1996): averaged uniformly over *all* target functions, every learner has identical off-training-set expected error. Formally, for any two algorithms $A_1, A_2$,

$$\sum_{f} \mathbb{E}[E \mid f, A_1] = \sum_{f} \mathbb{E}[E \mid f, A_2].$$

Learning works only because real problems are *not* uniformly distributed — they carry structure (smoothness, sparsity, hierarchy, low intrinsic dimension). Every model encodes an **inductive bias** matched to some structure: linear models assume additivity, trees assume axis-aligned piecewise-constant regions, convolutional nets assume translation equivariance, kernels assume smoothness in a chosen RKHS. **Choosing a model type is choosing a bias.** Model selection, then, is the joint problem of (i) matching inductive bias to the data-generating process and (ii) controlling variance under a finite, non-stationary sample — which in finance means walk-forward validation, deflated performance metrics (López de Prado), and a strong prior toward the simplest hypothesis class that clears the bar.

## References & further reading

- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). — risk, bias–variance, trees, ensembles.
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning.* — generative/discriminative, EM, PCA, kernels.
- Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). — MDPs, Bellman equations, control.
- Vapnik, V. (1998). *Statistical Learning Theory.* — ERM, capacity, structural risk minimization.
- Wolpert, D. H. (1996). *The Lack of A Priori Distinctions Between Learning Algorithms.* *Neural Computation.* — no-free-lunch.
- Ng, A. Y., & Jordan, M. I. (2002). *On Discriminative vs. Generative Classifiers.* *NeurIPS.*
- López de Prado, M. (2018). *Advances in Financial Machine Learning.* — walk-forward, deflated Sharpe, backtest overfitting.
