# Neural Networks in Trading (Foundations)

Neural networks are function approximators: they learn a mapping from inputs (features) to outputs (predictions). In trading, the hard part is not the model—it’s **data quality, leakage control, and evaluation**.

## Key Terms

- **Feature**: input signal (returns, volatility, fundamentals, microstructure stats).
- **Label/target**: what you want to predict (next-day return, direction, volatility, regime).
- **Overfitting**: learning noise that won’t repeat; looks great in-sample, fails live.
- **Leakage**: using future information (even accidentally) that won’t exist in real time.
- **Stationarity**: data distribution staying similar over time; markets often violate this.

## What Neural Nets Are Good At

- Combining many weak signals into one prediction.
- Learning nonlinear relationships.
- Handling sequence inputs (e.g., recent returns) when you use temporal models.

## What Neural Nets Are NOT Good At (Common Misconceptions)

- They do not “discover alpha” from thin air.
- They do not fix a noisy label or bad execution model.
- Bigger model ≠ better strategy; it can mean more overfitting.

## A Clean First Project (Maintainable)

1. **Pick one target** (e.g., predict next-day volatility, not return).
2. **Keep features boring** (returns, realized vol, moving averages, volume).
3. **Use walk-forward validation** (train on past, test on later).
4. **Compare to a baseline** (e.g., simple linear regression).
5. **Add costs** before celebrating.

## Typical Model Choices

- **MLP (feedforward)**: good default when your features are tabular.
- **1D CNN**: good for short pattern extraction in sequences.
- **LSTM/GRU**: sequence memory; can help but easy to overfit.
- **Transformer**: powerful, but typically needs more data and careful regularization.

## Evaluation That Makes Sense

- Use **time-based splits** (not random).
- Track **calibration** (when the model says 70% confidence, is it right ~70% of the time?).
- Report **turnover and costs** on the strategy built from predictions.

## Practical Tip

If you can’t beat a simple baseline out-of-sample, do not add complexity—fix data, labels, and evaluation first.
