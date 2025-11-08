# Probability Distributions in Trading

## Introduction

Understanding probability distributions is fundamental to successful trading. Financial markets exhibit complex behaviors that can be modeled using various statistical distributions, each with unique characteristics that affect risk assessment and strategy development.

## Key Distributions in Finance

### 1. Normal Distribution

The foundation of classical finance theory:

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

Where:
- $\mu$ = mean
- $\sigma$ = standard deviation

**Properties:**
- Bell-shaped and symmetric
- 68% of data within 1 standard deviation
- 95% within 2 standard deviations

**Limitations in Trading:**
- Markets show fat tails (extreme events more common)
- Skewness often present
- Volatility clustering not captured

### 2. Log-Normal Distribution

Used for modeling asset prices:

$$f(x) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}$$

**Applications:**
- Stock price modeling
- Options pricing (Black-Scholes)
- Assumes prices cannot go negative

### 3. Student's t-Distribution

Better captures market reality:

$$f(t) = \frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\Gamma\left(\frac{\nu}{2}\right)} \left(1+\frac{t^2}{\nu}\right)^{-\frac{\nu+1}{2}}$$

**Advantages:**
- Heavier tails than normal distribution
- Accommodates extreme market events
- Approaches normal as degrees of freedom increase

## Fat Tails and Market Crashes

### Empirical Evidence

Real market returns show:
- **Excess kurtosis**: More extreme events than normal distribution predicts
- **Asymmetric tails**: Crashes more severe than equivalent upward moves
- **Volatility clustering**: High volatility periods followed by high volatility

### Practical Implications

1. **Risk Management**
   - VaR models using normal distributions underestimate risk
   - Stress testing becomes crucial
   - Tail risk hedging strategies needed

2. **Position Sizing**
   - Kelly Criterion needs adjustment for fat tails
   - Conservative position sizing in volatile markets

## Skewness in Returns

### Measuring Skewness

$$\text{Skewness} = \frac{E[(X - \mu)^3]}{\sigma^3}$$

- **Negative skew**: More frequent small gains, occasional large losses
- **Positive skew**: More frequent small losses, occasional large gains

### Trading Implications

- **Equity markets**: Typically negatively skewed (crash risk)
- **Trend following**: Often positively skewed strategies
- **Mean reversion**: Usually negatively skewed

## Practical Applications

### 1. Risk Assessment

**Value at Risk (VaR) Calculation:**

Using normal distribution (tends to underestimate risk):
```
VaR_normal = μ + σ × Φ⁻¹(α)
```

Using t-distribution (more realistic for fat-tailed returns):
```
VaR_t = μ + σ × t⁻¹(α, df)
```

Where:
- μ = expected return
- σ = volatility
- α = confidence level (e.g., 0.05 for 95% VaR)
- df = degrees of freedom

### 2. Monte Carlo Simulation

Use appropriate distributions for:
- Portfolio stress testing
- Strategy backtesting
- Risk scenario analysis

### 3. Options Pricing

Account for:
- Volatility smile/skew
- Fat tails in underlying returns
- Time-varying volatility

## Distribution Selection Guidelines

### For Different Assets

1. **Stocks**: Log-normal for prices, t-distribution for returns
2. **Currencies**: Often closer to normal, but with fat tails
3. **Commodities**: Highly skewed due to supply constraints
4. **Cryptocurrencies**: Extreme fat tails and high kurtosis

### Model Validation

- **Kolmogorov-Smirnov test**: Overall distribution fit
- **Anderson-Darling test**: Better for tail behavior
- **Q-Q plots**: Visual assessment of distribution fit

## Advanced Concepts

### Mixture Models

Combine multiple distributions:
- Normal times + crisis periods
- Different market regimes
- Time-varying parameters

### Copulas

Model dependence between assets:
- Preserve marginal distributions
- Capture tail dependence
- Portfolio risk assessment

## Conclusion

Understanding probability distributions is crucial for:
- Accurate risk assessment
- Realistic backtesting
- Proper position sizing
- Options pricing and hedging

Key takeaways:
1. Normal distribution is often inadequate for financial data
2. Fat tails and skewness are pervasive in markets
3. Use appropriate distributions for different assets and time periods
4. Validate your distributional assumptions regularly

Always remember: **All models are wrong, but some are useful.** Choose distributions that capture the essential features of your data while remaining tractable for analysis.