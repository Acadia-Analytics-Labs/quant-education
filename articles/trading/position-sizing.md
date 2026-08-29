# Position Sizing and Risk Management

## Introduction

Position sizing is one of the most critical aspects of risk management in trading. It determines how much capital you allocate to each trade, directly impacting your portfolio's risk and return profile.

## Key Concepts

### 1. Kelly Criterion

The Kelly Criterion helps determine optimal position sizes based on the probability of success and the potential risk-reward ratio:

$$f = \frac{bp - q}{b}$$

Where:
- $f$ = fraction of capital to wager
- $b$ = odds received on the wager
- $p$ = probability of winning
- $q$ = probability of losing (1 - p)

### 2. Fixed Fractional Method

This method allocates a fixed percentage of total capital to each trade:

$$\text{Position Size} = \frac{\text{Account Balance} \times \text{Risk Percentage}}{\text{Stop Loss Distance}}$$

### 3. Volatility-Based Sizing

Adjust position sizes based on asset volatility using Average True Range (ATR):

$$\text{Position Size} = \frac{\text{Risk Amount}}{\text{ATR} \times \text{ATR Multiplier}}$$

## Risk Management Rules

1. **Never risk more than 2% of your account on a single trade**
2. **Diversify across uncorrelated assets**
3. **Use stop-losses on every position**
4. **Monitor portfolio-wide exposure**

## Practical Example

Let's calculate position size for a stock trade:

- Account Balance: \$100,000
- Risk per trade: 1% (\$1,000)
- Entry price: \$50
- Stop loss: \$47
- Stop loss distance: \$3

$$\text{Position Size} = \frac{\$1,000}{\$3} = 333 \text{ shares}$$

## Advanced Concepts

### Portfolio Heat

Monitor the total risk exposure across all open positions:

$$\text{Portfolio Heat} = \sum_{i=1}^{n} \text{Risk per Position}_i$$

Keep portfolio heat below 6-8% of total capital.

### Correlation Adjustments

When trading correlated assets, reduce individual position sizes to account for increased portfolio risk:

$$\text{Adjusted Position Size} = \frac{\text{Base Position Size}}{1 + \text{Correlation Factor}}$$

## Conclusion

Proper position sizing is essential for long-term trading success. It protects your capital during losing streaks while allowing you to capitalize on winning trades. Always prioritize risk management over potential profits.