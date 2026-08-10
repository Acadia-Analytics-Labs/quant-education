# Monte Carlo Risk Forecasting

Monte Carlo simulation is a simple idea: generate many “what could happen” return paths, then measure how your portfolio behaves across them. It is useful when you care about **tail risk** (rare but painful losses) and want more than a single forecast.

## Key Terms (Plain Language)

- **Scenario / path** – one simulated return history over your chosen horizon (e.g., 20 trading days).
- **Portfolio PnL** – profit and loss from your positions given a path of returns.
- **Drawdown** – how far your equity curve falls from a previous peak.
- **Value-at-Risk (VaR)** – a loss threshold you exceed only X% of the time (e.g., 1% for 99% VaR).
- **Expected shortfall (ES)** – the average loss in the worst X% of outcomes (the tail beyond VaR).

## Step-by-Step Workflow

1. **Prepare Inputs**
   - Clean historical returns, vol estimates, and weights.
   - Choose a correlation structure (sample covariance or a factor model).
2. **Generate Paths**
   - Sample correlated returns (common approach: Cholesky on the covariance matrix).
   - Decide your horizon (1-day, 10-day, 1-month) and number of simulations (often 10k+).
3. **Aggregate Portfolio PnL**
   - Convert each path into cumulative PnL, drawdown, margin utilization, etc.
4. **Extract Risk Metrics**
   - Compute VaR/ES, probability of breaching risk limits, and the distribution of holding-period returns.
5. **Explain the Results**
   - Identify what drives tail losses (which assets and correlations matter most).

## Common Pitfalls (Beginner-Friendly)

- **Assuming normal returns**: real markets have fat tails; Monte Carlo can still help, but be honest about limitations.
- **Using unstable correlations**: correlations change during stress. Consider stress-testing with higher correlations.
- **Ignoring leverage**: risk is not just return distribution; it’s return distribution *times exposure*.
- **Too few simulations**: tail estimates are noisy when you only run a few hundred paths.
- **No sanity checks**: compare simulated vol and correlations to real history to ensure you aren’t simulating nonsense.
