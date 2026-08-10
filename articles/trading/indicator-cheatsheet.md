# Trading Indicators Cheat Sheet

This is a quick, practical reference for common indicators. Indicators do not “predict” markets by themselves; they are **features** that summarize price/volume behavior.

## Key Terms (Beginner-Friendly)

- **Lookback window**: how many bars/days the indicator uses (e.g., 14).
- **Smoothing**: filtering noisy data to see the underlying trend (often via moving averages).
- **Lag**: indicators often react after price moves; less lag usually means more noise.

## Moving Average (MA)

**What it is:** a smoothed price.  
**What it’s good for:** trend direction and basic filters (e.g., “only long above MA”).  
**Common mistake:** using MA crossovers alone without risk control and costs.

- SMA: simple average over N bars (smooth but slower).
- EMA: exponentially weighted (reacts faster than SMA).

## RSI (Relative Strength Index)

**What it is:** a bounded oscillator (0–100) measuring recent gains vs. losses.  
**What it’s good for:** mean-reversion filters and “overbought/oversold” context.  
**Common mistake:** treating RSI>70 as “sell” in strong trends without trend context.

## MACD

**What it is:** difference between two EMAs + a signal line.  
**What it’s good for:** momentum changes (acceleration/deceleration).  
**Common mistake:** over-trading crossovers on noisy timeframes.

## ATR (Average True Range)

**What it is:** a volatility measure in price units (e.g., dollars).  
**What it’s good for:** setting stops/position sizes based on volatility.  
**Common mistake:** using a fixed stop distance across assets with very different ATRs.

## Bollinger Bands

**What it is:** moving average ± k × standard deviation.  
**What it’s good for:** framing “relative expensiveness” given recent volatility.  
**Common mistake:** assuming touching the band means immediate reversal.

## VWAP (Volume-Weighted Average Price)

**What it is:** average price weighted by volume over a session.  
**What it’s good for:** intraday benchmarking and execution context.  
**Common mistake:** using VWAP as a predictive indicator in daily strategies.

## When Indicators Help (and When They Don’t)

- Help: **risk rules**, **position sizing**, and **context** (“only trade mean reversion in range regimes”).
- Hurt: using many correlated indicators together (it looks sophisticated but is often redundant).

## A Minimal “Clean” Stack

If you want something maintainable:

- Trend filter: `EMA(200)` or `SMA(200)`
- Volatility: `ATR(14)`
- A single oscillator: `RSI(14)` (only as a filter, not the whole strategy)
