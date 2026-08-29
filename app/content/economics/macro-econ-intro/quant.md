# Macroeconomics: Identities, Equilibrium, and the Policy Response

## 1. The national income identity

Start from the accounting fact that, in a closed measurement of a single economy, **total output = total expenditure = total income**. Writing the expenditure decomposition with net exports split into exports $X$ and imports $M$:

$$Y = C + I + G + (X - M).$$

This is an **identity**, not a behavioral equation — it holds by construction because unsold output is booked as inventory investment inside $I$. From it we recover the fundamental saving–investment relation. Define private saving $S_p = (Y - T) - C$ and public saving $S_g = T - G$, where $T$ is net taxes. National saving is $S = S_p + S_g = Y - C - G$. Substituting the identity:

$$S = Y - C - G = I + (X - M) \;\;\Longrightarrow\;\; \boxed{S - I = X - M = NX.}$$

A country that invests more than it saves ($S < I$) must run a current-account deficit ($NX < 0$) and import the difference in foreign capital. This links the trade balance to the saving–investment gap without any theory of behavior — pure accounting.

## 2. The Keynesian cross and the fiscal multiplier (derivation)

Now add behavior. Let consumption respond to disposable income with a **marginal propensity to consume** $b \equiv \text{MPC} \in (0,1)$:

$$C = a + b\,(Y - T), \qquad 0 < b < 1,$$

and treat $I$, $G$, $T$, and net exports as exogenous for the short run. Impose goods-market equilibrium $Y = C + I + G + NX$ and solve:

$$
\begin{aligned}
Y &= a + b(Y - T) + I + G + NX \\
Y - bY &= a - bT + I + G + NX \\
Y &= \frac{a - bT + I + G + NX}{1 - b}.
\end{aligned}
$$

Differentiating with respect to government purchases gives the **government-spending multiplier**, and with respect to taxes the **tax multiplier**:

$$\frac{\partial Y}{\partial G} = \frac{1}{1 - b}, \qquad \frac{\partial Y}{\partial T} = \frac{-b}{1 - b}.$$

With $b = 0.6$ the spending multiplier is $1/(1-0.6) = 2.5$: a marginal dollar of $G$ raises equilibrium output by \$2.50 in this stylized model, because each round of spending re-spends a fraction $b$ of the last. The geometric series $\sum_{k=0}^{\infty} b^k = 1/(1-b)$ is exactly the multiplier. Real-world multipliers are smaller once one adds taxes proportional to income, import leakage, interest-rate crowding-out, and forward-looking (Ricardian) households — all of which raise the effective leakage per round.

## 3. Aggregate demand and aggregate supply

The Keynesian cross fixes the price level; the **AD–AS** framework lets it move. Aggregate demand $Y^d(P)$ slopes downward in the price level $P$ (real-balance, interest-rate, and net-export channels). Short-run aggregate supply slopes upward (sticky wages/prices); long-run aggregate supply is **vertical** at potential output $Y^*$, the level consistent with full employment of factors:

```mermaid
flowchart LR
  A["AD shift: ΔG, ΔT, Δ money, sentiment"] --> B["Short run: P and Y both move along SRAS"]
  B --> C["Wages/prices adjust"]
  C --> D["Long run: Y returns to potential Y*, only P is permanently changed"]
```

Two comparative statics matter:

- **Demand shock** (e.g. fiscal or monetary expansion): AD shifts right. Short run — output *and* prices rise. Long run — as expectations and wages catch up, SRAS shifts back and the economy returns to $Y^*$ at a **higher price level** (monetary neutrality in the long run).
- **Supply shock** (e.g. an oil spike): SRAS shifts left, producing **stagflation** — higher $P$ with lower $Y$ — the uncomfortable case policy cannot fix by moving AD alone.

The business cycle is the path of the output gap $(Y_t - Y^*)/Y^*$ as these shocks and adjustments play out around trend:

```chart
business_cycle()
```

## 4. Okun's law — output gaps and unemployment

Okun (1962) documented a stable empirical link between the **output gap** and the **unemployment gap**. In gap form,

$$u_t - u^\ast \;=\; -\,c\,\frac{Y_t - Y^\ast}{Y^\ast},$$

where $u^\ast$ is the natural rate and $c$ is Okun's coefficient. Okun's original US estimate implied roughly **1 percentage point** of extra unemployment per **~3%** of output lost relative to potential; modern estimates put $c \approx 2$ (so $1/c \approx 2\text{–}3\%$ of output per point of unemployment). The gap exceeds one-for-one because employers adjust hours, participation, and labor hoarding before headcount — so measured productivity is procyclical.

## 5. The Phillips curve and its expectations-augmented correction

Phillips (1958) found an inverse empirical relation between wage inflation and unemployment. The naive reading — a **permanent** menu trading lower unemployment for higher inflation — collapsed in the 1970s. Friedman (1968) and Phelps independently showed why: what firms and workers care about is the *real* wage, so **expected inflation** must enter. The **expectations-augmented Phillips curve** is

$$\pi_t \;=\; \pi_t^e \;-\; \beta\,(u_t - u^\ast) \;+\; \varepsilon_t, \qquad \beta > 0,$$

with $\pi_t^e$ expected inflation and $\varepsilon_t$ a supply shock. The crucial implication is a **vertical long-run Phillips curve**: in a stationary state $\pi_t = \pi_t^e$, which forces $u_t = u^\ast$ (the **NAIRU**) regardless of the inflation rate. There is *no* exploitable long-run trade-off; any attempt to hold $u < u^\ast$ merely ratchets $\pi^e$ upward, giving accelerating inflation at unchanged unemployment. Under adaptive expectations $\pi_t^e = \pi_{t-1}$ this becomes the "accelerationist" form $\Delta \pi_t = -\beta(u_t - u^\ast) + \varepsilon_t$; under **rational** expectations, only the *unanticipated* component of policy moves output at all (the Lucas critique).

## 6. Money, inflation, and the monetary transmission

The long-run anchor for the price level is the **quantity theory of money**. From the identity of exchange $MV = PY$ (money stock $M$, velocity $V$, price level $P$, real output $Y$), take logs and differentiate:

$$g_M + g_V = g_P + g_Y \;\;\Longrightarrow\;\; \pi = g_P = g_M + g_V - g_Y.$$

If velocity is roughly stable ($g_V \approx 0$) and real growth is set by the supply side, then **inflation tracks money growth** in excess of output growth — Friedman's "always and everywhere a monetary phenomenon" in the long run. Cross-country and long-horizon data bear out the positive slope, even as the short-run relationship is noisy:

```chart
money_supply_inflation()
```

Monetary policy operates in the short run through the interest-rate/credit channel rather than direct control of $M$: a central bank following a **Taylor-type rule** sets the policy rate as

$$i_t = r^\ast + \pi_t + \phi_\pi(\pi_t - \pi^\ast) + \phi_y\,\frac{Y_t - Y^\ast}{Y^\ast}, \qquad \phi_\pi > 0,\ \phi_y > 0,$$

leaning against inflation and output gaps. The **Taylor principle** $\phi_\pi > 0$ (raising *real* rates when inflation rises) is what pins down a determinate, stable inflation equilibrium.

## 7. Putting policy in the AD–AS diagram

- **Fiscal expansion** ($\uparrow G$ or $\downarrow T$) shifts AD right via the multiplier of §2 — output and prices up in the short run, crowding out some $I$ through higher rates.
- **Monetary expansion** ($\downarrow i$) shifts AD right through investment and durable-consumption channels and a weaker currency (↑ $NX$).
- **Long-run neutrality**: because LRAS is vertical, sustained demand stimulus ends up in $P$, not $Y$ — the policy debate is about the *speed of adjustment*, not the destination.
- **Traders' lens**: releases (GDP, CPI, payrolls, FOMC) are shocks to the market's estimate of $(\pi, Y - Y^*)$ and hence of the Taylor-rule path; bonds, FX, and equities reprice the implied rate trajectory in real time.

## References & further reading

- Mankiw, N. G. *Macroeconomics* (Worth) — the standard intermediate text; national accounts, AD–AS, Phillips curve.
- Blanchard, O. *Macroeconomics* (Pearson) — IS–LM, medium-run and open-economy treatment.
- Okun, A. M. (1962). *Potential GNP: Its Measurement and Significance.* Proc. Business and Economic Statistics Section, ASA.
- Phillips, A. W. (1958). *The Relation between Unemployment and the Rate of Change of Money Wage Rates in the United Kingdom, 1861–1957.* Economica.
- Friedman, M. (1968). *The Role of Monetary Policy.* American Economic Review — the expectations-augmented critique and natural-rate hypothesis.
- Phelps, E. S. (1967). *Phillips Curves, Expectations of Inflation and Optimal Unemployment over Time.* Economica.
- Taylor, J. B. (1993). *Discretion versus Policy Rules in Practice.* Carnegie-Rochester Conference Series.

*Educational content, not investment advice.*
