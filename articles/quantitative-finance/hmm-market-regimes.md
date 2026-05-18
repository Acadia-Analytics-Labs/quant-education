# Hidden Markov Models (HMM) for Market Regimes

An HMM is a probabilistic model that assumes markets switch between a small number of **hidden regimes** (like “low volatility” vs “high volatility”). You don’t observe regimes directly—you observe prices/returns—and the HMM estimates regime probabilities for you.

## Key Terms

- **Hidden state (regime)**: the unobserved mode the market is in.
- **Observation**: what you measure (returns, volatility, spreads).
- **Transition probability**: chance of moving from one regime to another.
- **Emission distribution**: how observations behave in each regime (e.g., returns ~ Normal with different vol per regime).
- **Posterior probability**: the probability you are in each regime *given the data*.

## Why Quants Use HMMs

- They turn a vague idea (“volatility feels different”) into a measurable probability.
- They help you build **rule-based regime filters** (e.g., trade trend strategies only in low-vol regimes).
- They are interpretable compared to many deep learning models.

## A Simple HMM Setup

### 1) Choose Observations

Common first choices:

- daily returns
- realized volatility (e.g., rolling std of returns)
- return + volatility together (2D observations)

### 2) Choose Number of Regimes

Start with **2 or 3**:

- 2-state: low vol vs high vol
- 3-state: calm / normal / stress

Too many states often creates unstable “micro-regimes”.

### 3) Fit the Model

The model learns:

- transition matrix between regimes
- distribution parameters for observations in each regime

### 4) Use the Output

Use the posterior probabilities as features:

- “if P(high-vol) > 0.7, reduce leverage”
- “if P(stress) rising, tighten risk limits”

## Common Pitfalls

- Regimes are **model-dependent**: different features lead to different regimes.
- Real markets can shift in ways your emission distribution can’t capture (fat tails).
- HMMs are not “predictors” of returns; they are best used as **risk and context** tools.

## Next Step

Once the 2-state model works end-to-end, try a 3-state model and add a simple rule: change position sizing based on regime probability instead of switching strategies completely.
