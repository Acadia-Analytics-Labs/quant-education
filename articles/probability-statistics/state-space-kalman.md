# State-Space Modeling with Kalman Filters

Kalman filters are a practical way to separate **signal** (what you care about) from **noise** (random wiggles). They estimate a hidden state (like “fair value” or a smooth spread) from noisy price observations.

## Key Terms

- **State** – the hidden variable you want (e.g., a smooth spread).
- **Observation** – what you actually measure (e.g., last price).
- **Process noise (Q)** – how much the state is allowed to drift each step.
- **Observation noise (R)** – how noisy the measurements are (quote flicker, microstructure noise).
- **Kalman gain** – the adaptive weight that blends prediction vs. new observation.

## Building a Simple Filter

1. **Define the Hidden Signal** – e.g., a random-walk spread `x_t`.
2. **Specify Noise Levels** – `Q` for state noise (how much the trend can drift) and `R` for observation noise (quote noise).
3. **Predict Step** – project `x_t` and its covariance one step ahead.
4. **Update Step** – blend the prediction with the observed price using the Kalman gain.
5. **Repeat** – store the filtered state; this becomes your clean series for trading logic or risk.

## Popular Trading Uses

- **Cointegration / pairs**: filter the spread so z-scores react faster than a rolling mean.
- **Microstructure smoothing**: remove quote flicker before feeding returns into machine-learning models.
- **Adaptive volatility**: treat realized vol as the state to size positions in real time.
- **Inventory targeting**: market makers model “fair value” as a state and quote around the filtered signal.

## Beginner Tips

- Start with a **single variable** (one asset, one state) so you can compare the raw vs. smoothed series.
- Normalize inputs; extremely large values make the covariance matrices unstable.
- Log every model parameter; risk and audit teams will ask how the “magic smoothing” works.
