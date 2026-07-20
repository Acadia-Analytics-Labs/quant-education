# Backtesting Basics (What New Quants Miss)

Backtests are easy to run and easy to fool yourself with. This article is a checklist of the most common failure modes so your results stay believable.

## Key Terms

- **Look-ahead bias**: using information in the backtest that wasn’t available at the time.
- **Survivorship bias**: testing only assets that survived (e.g., today’s index members).
- **Overfitting**: tuning rules to noise; performance collapses out-of-sample.
- **Out-of-sample**: data your model never “saw” during design.

## The Checklist

### 1) Data Integrity

- Are prices adjusted correctly for splits/dividends?
- Do you have missing bars and how do you handle them?
- Are you mixing different trading calendars (crypto vs equities)?

### 2) Time Alignment

- Use the correct bar: signal computed on bar *t* should execute on bar *t+1* (unless you can prove same-bar execution).
- For features like “close-to-close returns”, be explicit about when they become available.

### 3) Costs and Slippage

At minimum include:

- Bid/ask spread (or a spread proxy)
- Fees/commissions
- Market impact (even a simple model is better than zero)

### 4) Position Sizing and Risk

Great signals fail with bad sizing.

- Use volatility scaling (e.g., ATR or realized vol) so risk stays stable.
- Cap exposure and drawdown. A strategy that can blow up is not a strategy.

### 5) Validation

- Split into train/validation/test (or use walk-forward).
- Report performance by regime (bull/bear/high vol) not just overall.
- Track turnover; high turnover often means high costs and fragility.

## A Simple “Good Enough” First Backtest

- Daily bars
- Next-day open execution
- Fixed spread + fee model
- One signal + one risk rule (e.g., volatility sizing)

Once this pipeline is correct, you can add complexity safely.
