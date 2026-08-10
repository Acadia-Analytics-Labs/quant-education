# Consumer Choice as Constrained Optimization

## 1. The primitive: preferences to utility

Let the consumption set be $X = \mathbb{R}^n_+$. A rational preference relation $\succeq$ on $X$ is **complete** and **transitive**. If $\succeq$ is additionally continuous, it admits a continuous utility representation $U: X \to \mathbb{R}$ with $x \succeq y \iff U(x) \ge U(y)$ (Debreu's theorem). Utility is therefore **ordinal**: for any strictly increasing $\phi:\mathbb{R}\to\mathbb{R}$, $\phi \circ U$ represents the same preferences, so cardinal statements about "utils" are not identified — only the ranking and the shapes of level sets are.

The level sets $\{x : U(x) = \bar u\}$ are **indifference curves**. Two regularity assumptions do the analytical work:

- **Local nonsatiation** ⟹ the budget constraint binds (no wasted income).
- **Strict quasiconcavity** of $U$ ⟹ indifference sets are strictly convex, i.e. a *diminishing* marginal rate of substitution, which guarantees a unique interior optimum where it exists.

## 2. The consumer problem and the Lagrangian derivation

For two goods with prices $p_x, p_y > 0$ and income $m > 0$, the utility-maximization problem (UMP) is

$$\max_{x,\,y\,\ge 0}\; U(x,y) \quad\text{s.t.}\quad p_x x + p_y y = m.$$


```mermaid
flowchart LR
  A["max U(x,y)"] --> B["s.t. p_x x + p_y y = m"]
  B --> C["L = U(x,y) + λ(m − p_x x − p_y y)"]
  C --> D["FOC: U_x = λ p_x,  U_y = λ p_y"]
  D --> E["MRS = U_x / U_y = p_x / p_y"]
```


Form the Lagrangian with multiplier $\lambda$:

$$\mathcal{L}(x,y,\lambda) = U(x,y) + \lambda\big(m - p_x x - p_y y\big).$$

At an interior optimum the first-order conditions are

$$\frac{\partial \mathcal{L}}{\partial x} = U_x - \lambda p_x = 0, \qquad \frac{\partial \mathcal{L}}{\partial y} = U_y - \lambda p_y = 0, \qquad \frac{\partial \mathcal{L}}{\partial \lambda} = m - p_x x - p_y y = 0,$$

where $U_x \equiv \partial U/\partial x$ is the marginal utility of $x$. Dividing the first condition by the second eliminates $\lambda$:

$$\boxed{\;\frac{U_x}{U_y} = \frac{p_x}{p_y} \;=\; \text{MRS}_{xy}.\;}$$

This is the **tangency condition**: the slope of the indifference curve equals the slope of the budget line. Rearranged, the first two conditions also give

$$\lambda = \frac{U_x}{p_x} = \frac{U_y}{p_y},$$

so the marginal utility *per dollar* is equalized across goods — the equimarginal principle. The multiplier $\lambda = \partial V/\partial m$ is the **marginal utility of income** (by the envelope theorem, where $V(p,m) = \max U$ is the indirect utility function): the shadow price of relaxing the budget by one dollar.

**Sufficiency.** Because $U$ is strictly quasiconcave and the constraint set is convex and compact, the stationary point is the unique global maximizer. Formally, the bordered Hessian condition

$$\begin{vmatrix} 0 & -p_x & -p_y \\ -p_x & U_{xx} & U_{xy} \\ -p_y & U_{yx} & U_{yy} \end{vmatrix} > 0$$

is exactly the statement that the indifference curve is convex at the tangency (MRS diminishing), ruling out a tangency from below.

## 3. Worked closed form: Cobb–Douglas demand

Let $U(x,y) = x^{a} y^{b}$ with $a,b>0$. Then $U_x = a x^{a-1} y^{b}$ and $U_y = b x^{a} y^{b-1}$, so

$$\text{MRS} = \frac{U_x}{U_y} = \frac{a}{b}\,\frac{y}{x} \stackrel{!}{=} \frac{p_x}{p_y} \;\Longrightarrow\; p_x x = \frac{a}{b}\,p_y y.$$

Substituting into the budget $p_x x + p_y y = m$ yields the **Marshallian demands**

$$x^\star(p,m) = \frac{a}{a+b}\,\frac{m}{p_x}, \qquad y^\star(p,m) = \frac{b}{a+b}\,\frac{m}{p_y}.$$

Two testable structural facts fall out immediately: expenditure shares $p_x x^\star / m = a/(a+b)$ are **constant** (independent of prices and income), and each good's own-price elasticity is exactly $-1$ (unit elastic) while its income elasticity is $+1$ — Cobb–Douglas goods are homothetic normal goods with a linear, ray-shaped income-consumption curve.

## 4. Price elasticity of demand and the revenue theorem

Define the **price elasticity of demand** as the log-derivative of quantity with respect to price:

$$\varepsilon \equiv \frac{dQ/Q}{dP/P} = \frac{dQ}{dP}\cdot\frac{P}{Q} = \frac{d\log Q}{d\log P}.$$

For a downward-sloping demand $\varepsilon < 0$; demand is **elastic** if $|\varepsilon|>1$ and **inelastic** if $|\varepsilon|<1$. Its central consequence is the effect of a price change on **revenue** $R(P) = P\cdot Q(P)$. Differentiate:

$$\frac{dR}{dP} = Q + P\frac{dQ}{dP} = Q\left(1 + \frac{P}{Q}\frac{dQ}{dP}\right) = Q\big(1 + \varepsilon\big).$$

Since $Q>0$, the sign of $dR/dP$ is the sign of $1+\varepsilon$:

- **Inelastic** ($-1 < \varepsilon < 0$): $1+\varepsilon > 0$, so raising price **raises** revenue.
- **Elastic** ($\varepsilon < -1$): $1+\varepsilon < 0$, so raising price **lowers** revenue.
- **Unit elastic** ($\varepsilon = -1$): revenue is stationary — the revenue-maximizing price.

The same algebra in quantity space gives the firm's **marginal revenue**,

$$MR = \frac{dR}{dQ} = P + Q\frac{dP}{dQ} = P\left(1 + \frac{1}{\varepsilon}\right),$$

the Amoroso–Robinson relation. Equating $MR = MC$ for a monopolist yields the optimal markup (Lerner index)

$$\frac{P - MC}{P} = -\frac{1}{\varepsilon} = \frac{1}{|\varepsilon|},$$

so pricing power is inversely proportional to demand elasticity — a perfectly competitive firm faces $|\varepsilon|\to\infty$ and prices at marginal cost.

## 5. Equilibrium and comparative statics

Market demand $Q^d(P)$ and supply $Q^s(P)$ pin down the clearing price $P^\star$ by $Q^d(P^\star) = Q^s(P^\star)$. Local stability is Walrasian: with excess demand $Z(P) = Q^d - Q^s$, the tâtonnement $\dot P = \kappa Z(P)$ converges iff $Z'(P^\star) < 0$, i.e. demand cuts supply from above.


```chart
supply_demand()
```


Comparative statics follow by implicit differentiation of the equilibrium condition. A demand shift parameter $\theta$ (income, tastes) moves the clearing price by

$$\frac{dP^\star}{d\theta} = \frac{\partial Q^d/\partial\theta}{\partial Q^s/\partial P - \partial Q^d/\partial P} > 0,$$

positive when the denominator (supply slope minus demand slope) is positive — the stable case shown by the rightward shift in the chart.

## 6. Opportunity cost and comparative advantage, formally

Opportunity cost is the multiplier from a *different* constrained program. On the production possibility frontier $T(q_1,q_2)=0$, the marginal opportunity cost of good 1 in terms of good 2 is the marginal rate of transformation $\text{MRT} = -dq_2/dq_1 = (\partial T/\partial q_1)/(\partial T/\partial q_2)$. Pareto efficiency requires the consumption tangency to meet the production tangency: $\text{MRS} = \text{MRT} = p_1/p_2$.

**Comparative advantage (Ricardo).** With unit labor requirements $a_{ij}$ (hours for good $j$ in country $i$), country 1 has a comparative advantage in good $A$ iff its *relative* opportunity cost is lower:

$$\frac{a_{1A}}{a_{1B}} < \frac{a_{2A}}{a_{2B}}.$$

This can hold even if country 1 is absolutely more productive in both goods ($a_{1A}<a_{2A}$ and $a_{1B}<a_{2B}$): absolute advantage cancels out of a *ratio*, so gains from specialization and trade exist whenever autarky price ratios differ. The equilibrium terms of trade settle strictly between the two countries' autarky ratios $a_{1A}/a_{1B}$ and $a_{2A}/a_{2B}$.

## 7. Where the tidy model strains

- **Non-convexities.** If $U$ is not quasiconcave (e.g. addictive or complementary goods with increasing MRS), the tangency FOC identifies a *minimum* or a saddle; the optimum jumps to a corner and demand becomes discontinuous in prices.
- **Corner solutions.** Interior FOCs assume $x^\star, y^\star > 0$. With satiation or sufficiently skewed prices the Karush–Kuhn–Tucker conditions bind: $U_x - \lambda p_x \le 0$ with complementary slackness $x(U_x - \lambda p_x)=0$.
- **Integrability and revealed preference.** Observed demand rationalizes *some* utility only if the Slutsky substitution matrix $S = \partial x/\partial p + (\partial x/\partial m)\,x^\top$ is symmetric and negative semidefinite — the empirical content of GARP (Afriat / Varian). Real panels frequently violate symmetry.
- **Ordinality vs. welfare.** Since utility is ordinal, interpersonal comparisons and cardinal "utility summation" are not well defined; surplus and deadweight-loss measures implicitly assume quasilinearity or a constant $\lambda$ (marginal utility of income), which fails with large income effects.
- **Behavioral departures.** Reference dependence, hyperbolic discounting, and menu effects break transitivity/independence; the neoclassical program is a first-order approximation, not a law.

## References & further reading

- Varian, H. R. (2014). *Intermediate Microeconomics: A Modern Approach*, 9th ed. (budget sets, MRS tangency, elasticity).
- Varian, H. R. (1992). *Microeconomic Analysis*, 3rd ed. (indirect utility, envelope theorem, Slutsky, integrability).
- Mas-Colell, A., Whinston, M. D., & Green, J. R. (1995). *Microeconomic Theory*. Oxford University Press. (UMP/EMP duality, revealed preference, GARP).
- Debreu, G. (1954). *Representation of a Preference Ordering by a Numerical Function.*
- Afriat, S. N. (1967). *The Construction of Utility Functions from Expenditure Data.* Int. Econ. Rev.
- Robinson, J. (1933). *The Economics of Imperfect Competition* (marginal revenue and the Amoroso–Robinson relation).

*Educational material only — not investment or financial advice.*
