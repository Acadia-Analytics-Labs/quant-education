# Introduction to Machine Learning

Machine Learning (ML) enables systems to learn patterns from data without being explicitly programmed. In trading, this means building models that adapt to market conditions rather than hard-coding rules.

**The core idea:** Instead of writing "if RSI < 30, buy", you show the model thousands of examples and let it learn what patterns predict profitable trades.

## Why ML for Trading?

### What ML Can Do
- Find complex, nonlinear patterns humans miss
- Process more information than manual analysis
- Adapt to changing market conditions (if retrained)
- Combine weak signals into strong predictions

### What ML Cannot Do
- Predict the future with certainty
- Work without good data and features
- Overcome fundamental market efficiency (if alpha doesn't exist, ML won't find it)
- Replace risk management and execution

**Reality check:** ML is a tool, not magic. Most successful quant funds use simple models with great execution, not the fanciest algorithms.

## The Three Learning Paradigms

### 1. Supervised Learning

You have historical examples with known outcomes (labels). The model learns to map inputs → outputs.

**Regression example:** Predict tomorrow's return
- Input: Today's returns, volatility, volume
- Output: Tomorrow's return (continuous number)
- Goal: Minimize prediction error

**Classification example:** Predict market direction
- Input: Technical indicators, market features
- Output: Up or Down (discrete class)
- Goal: Maximize classification accuracy

**When to use:** You have clear targets (price movements, regime labels) and historical examples.

### 2. Unsupervised Learning

Discover hidden structure in data without labels.

**Clustering:** Group similar market conditions
- Example: Find "bull", "bear", "choppy" regimes automatically
- Use: Adapt strategy to detected regime

**Dimensionality reduction:** Compress 50 correlated indicators into 10 independent factors
- Example: PCA on technical indicators
- Use: Reduce overfitting, visualize data

**When to use:** You don't have clear labels but want to find patterns, reduce dimensions, or detect anomalies.

### 3. Reinforcement Learning

Agent learns through trial and error by taking actions and receiving rewards.

**Trading as RL:**
- Agent: Your trading algorithm
- State: Current market conditions, position
- Action: Buy, sell, hold, position size
- Reward: PnL minus costs and risk penalties

**When to use:** Optimizing sequential decisions (entry, sizing, exit). Advanced topic with many pitfalls.

**Note:** Most successful trading ML uses supervised learning. Start there.

## The ML Trading Workflow

### Step 1: Define the Problem

**Bad:** "Predict the stock market"
**Good:** "Predict next-day return for SPY using previous 20 days of OHLCV data"

Be specific:
- What are you predicting? (direction, return, volatility, regime)
- What inputs do you have?
- What's the time horizon?
- How will predictions be used? (sizing, entry/exit, filtering)

### Step 2: Collect and Clean Data

**Minimum requirements:**
- Historical price and volume
- Aligned timestamps (handle missing data, holidays)
- No look-ahead bias (use only information available at prediction time)
- Survivorship bias handling (include delisted stocks)

**Data quality > data quantity.** 1,000 clean samples beat 10,000 messy ones.

### Step 3: Feature Engineering

Transform raw data into meaningful inputs. This is often more important than model choice.

**Basic features:**
- Returns (not raw prices)
- Volatility (rolling standard deviation)
- Volume ratios
- Technical indicators (RSI, MACD, Bollinger Bands)

**Advanced features:**
- Market microstructure (bid-ask spread, order book imbalance)
- Alternative data (sentiment, fundamentals, macro indicators)
- Interaction features (volatility × volume)

**Key principle:** Use features that make economic sense. If you can't explain why a feature should predict returns, it's probably spurious.

### Step 4: Choose a Model

See the "Machine Learning Model Types" article for details.

**Quick guide:**
- Start with linear regression (interpretable, fast, regularized)
- Move to tree-based if nonlinearity helps (Random Forest, Gradient Boosting)
- Only use neural networks if you have lots of data (10,000+ samples)

### Step 5: Train and Validate

**Critical: Use time-based splits**, not random shuffling.

```python
# Walk-forward validation
for train_end in range(train_size, len(data), step_size):
    train_data = data[train_end - train_size : train_end]
    test_data = data[train_end : train_end + test_size]
    
    model.fit(train_data.X, train_data.y)
    predictions = model.predict(test_data.X)
    
    # Evaluate on test_data
```

**Why time-based?** Markets change. Your model must work on future data, not interpolate between past data points.

### Step 6: Backtest with Costs

Predictions don't matter—PnL after costs matters.

**Include:**
- Bid-ask spread (often 0.01-0.05% per trade)
- Commissions
- Slippage (worse fills when trading is aggressive)
- Market impact (your trades move the market)

**Reality check:** If backtest Sharpe is 3.0, live will likely be <1.5 after costs and slippage.

### Step 7: Monitor and Retrain

Markets change. Monitor:
- Out-of-sample performance degradation
- Feature distribution drift
- Prediction calibration

**Retrain** when performance degrades, but avoid overreacting to noise.

## Trading-Specific Challenges

### 1. Non-Stationarity

Markets change. A pattern that worked in 2020 may not work in 2024.

**Strategies:**
- Shorter training windows (recent data weighs more)
- Regime detection (adapt to current conditions)
- Regularization (simpler models generalize better)
- Frequent retraining

### 2. Limited Data

You might have 10 years of daily data = 2,500 samples. That's tiny for ML.

**Strategies:**
- Use simple models (linear, shallow trees)
- Heavy regularization
- Feature selection
- Consider higher frequency if execution allows

### 3. Low Signal-to-Noise

Markets are noisy. Even great signals have weak correlations (0.05-0.10).

**Strategies:**
- Combine multiple weak signals
- Use ensemble methods
- Focus on risk-adjusted metrics, not raw accuracy
- Accept that you'll be wrong often (50-55% accuracy can still profit)

### 4. Survivorship Bias

Backtesting only on stocks that still exist overstates performance.

**Solution:** Include delisted stocks in historical tests.

### 5. Look-Ahead Bias

Accidentally using future information that wouldn't be available in real-time.

**Common sources:**
- Using end-of-day data to predict intraday
- Forward-filling missing data
- Using non-lagged features

**Solution:** Paranoid data pipeline audits.

## Performance Metrics That Matter

### Sharpe Ratio
Risk-adjusted returns:

$$\text{Sharpe} = \frac{\text{Mean Return} - \text{Risk-Free Rate}}{\text{Std Dev of Returns}}$$

Target: >1.0 for daily signals, >0.5 for monthly

### Maximum Drawdown
Largest peak-to-trough decline. Can you stomach a 20% drawdown?

### Information Ratio
Excess return per unit of tracking error (for benchmarked strategies)

### Win Rate vs. Payoff
50% win rate with 2:1 payoff ratio beats 60% win rate with 1:1 payoff.

**Don't optimize accuracy—optimize risk-adjusted PnL.**

## Getting Started: Your First ML Trading Model

### Minimal Viable Model

```python
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# 1. Load data
df = pd.read_csv('spy_daily.csv')
df['return'] = df['close'].pct_change()
df['volatility'] = df['return'].rolling(20).std()
df['volume_ratio'] = df['volume'] / df['volume'].rolling(20).mean()

# 2. Create features and target
features = ['return', 'volatility', 'volume_ratio']
df['target'] = df['return'].shift(-1)  # Next day return
df = df.dropna()

# 3. Train/test split (80/20 time-based)
split = int(len(df) * 0.8)
train, test = df[:split], df[split:]

# 4. Train model
model = Ridge(alpha=1.0)
model.fit(train[features], train['target'])

# 5. Predict and evaluate
test['prediction'] = model.predict(test[features])
test['position'] = test['prediction'].apply(lambda x: 1 if x > 0 else -1)
test['strategy_return'] = test['position'].shift(1) * test['target']

sharpe = test['strategy_return'].mean() / test['strategy_return'].std() * (252**0.5)
print(f"Sharpe ratio: {sharpe:.2f}")
```

**This 20-line script:**
- Predicts next-day returns
- Uses simple features
- Validates on out-of-sample data
- Calculates Sharpe ratio

If this gives Sharpe > 0.5, you have something. If not, your features don't have signal (or need better features/model).

## Common Beginner Mistakes

### 1. Starting Too Complex
Using LSTM neural networks on 500 samples. Start with linear regression.

### 2. Optimizing the Wrong Thing
Maximizing R² or accuracy instead of Sharpe or PnL.

### 3. Not Accounting for Costs
A 55% win rate strategy with 20 trades/day may lose money after costs.

### 4. Using Random Train/Test Splits
Markets are time-ordered. Random splits leak future information.

### 5. Trusting Single Backtest
Test across multiple periods and market regimes.

## Next Steps

1. **Read "Machine Learning Model Types"** - Understand when to use linear models vs. trees vs. neural networks

2. **Study "The Curse of Dimensionality"** - Learn why more features often hurt performance

3. **Explore "The Manifold Hypothesis"** - Understand dimensionality reduction for better features

4. **Build the minimal model above** - Get hands-on experience

5. **Iterate:** Add features → validate → compare to baseline → repeat

## Key Takeaways

- ML is a tool, not magic. It finds patterns in data.
- Start simple: linear regression beats complex models on small datasets.
- Feature engineering matters more than model choice.
- Always use time-based validation.
- Optimize for Sharpe/PnL, not accuracy.
- Markets are noisy—expect weak signals and frequent failures.
- Transaction costs kill many strategies that look good in backtest.

**Remember:** A simple model you understand and can maintain beats a complex model you don't. In live trading, execution and risk management matter more than the perfect ML model.
