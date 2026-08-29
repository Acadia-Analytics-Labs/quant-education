---
title: Sharpe Ratio and Strategy Backtesting
description: Measuring return per unit of risk, and using it to compare and evaluate trading strategies in a backtest.
difficulty: Intermediate
tags:
  - Sharpe Ratio
  - Risk-Adjusted Return
  - Backtesting
  - Performance Metrics
---

# Sharpe ratio and strategy backtesting

## Introduction

Developing a profitable trading strategy requires more than simply measuring returns. A strategy that generates high returns may also expose investors to excessive risk, making it difficult to determine whether its performance is truly desirable. The Sharpe ratio addresses this problem by measuring return relative to risk, allowing traders to compare strategies on a more consistent basis.

Because it combines both return and volatility into a single metric, the Sharpe ratio has become one of the most widely used performance measures in quantitative finance. It is commonly used when evaluating portfolios, comparing investment strategies, and analyzing backtest results.

---

## Sharpe ratio

The Sharpe ratio measures the excess return earned per unit of risk taken. It compares a strategy's average return above the risk-free rate to the variability of those returns.

The Sharpe ratio is defined as

$$S=\frac{R_p-R_f}{\sigma_p}$$

where:

- **$R_p$** is the expected return of the portfolio or strategy.
- **$R_f$** is the risk-free rate of return.
- **$\sigma_p$** is the standard deviation of the portfolio's returns.

The numerator, **$R_p-R_f$**, is known as the **excess return**, representing the return earned above what could have been achieved with a risk-free investment. The denominator measures the volatility of the strategy. As a result, the Sharpe ratio indicates how much excess return is earned for each unit of risk.

### Example

Suppose a trading strategy has an annual return of **15%**, the risk-free rate is **3%**, and the annual standard deviation of returns is **10%**.

The Sharpe ratio is

$$S=\frac{0.15-0.03}{0.10}=1.2$$

This means the strategy generates **1.2 units of excess return for every unit of risk taken**.

---

## Strategy backtesting

One of the most common applications of the Sharpe ratio is evaluating trading strategies during backtesting. While total return measures how profitable a strategy would have been historically, it does not indicate how much risk was required to achieve those returns.

For example, consider two strategies that both produce a **20% annual return**. If one experiences relatively stable returns while the other experiences large swings in performance, the first strategy would have a higher Sharpe ratio because it generates similar returns with less volatility. From a risk-adjusted perspective, it would generally be considered the stronger strategy.

Because of this, quantitative traders often compare Sharpe ratios when selecting between multiple trading models. A strategy with a slightly lower return may still be preferable if it achieves those returns with substantially lower risk.

While there is no universal threshold, the following guidelines are commonly used when interpreting Sharpe ratios:

| Sharpe Ratio | Interpretation |
|--------------|----------------|
| < 1.0 | Weak risk-adjusted performance |
| 1.0 – 2.0 | Good |
| 2.0 – 3.0 | Very good |
| > 3.0 | Excellent |

These values should always be interpreted within the context of the strategy being evaluated. Different markets and asset classes naturally exhibit different levels of return and volatility.

---

## Limitations

Although the Sharpe ratio is one of the most widely used performance metrics, it should not be viewed as a complete measure of strategy quality.

One limitation is that it assumes volatility is an appropriate measure of risk. In practice, volatility captures both positive and negative price movements, even though investors are generally more concerned with downside risk. Additionally, financial returns are not always normally distributed. Markets often experience extreme price movements, or **fat tails**, more frequently than a normal distribution predicts, which can make the Sharpe ratio overly optimistic.

The Sharpe ratio is also only as reliable as the data used to calculate it. A strategy with an impressive Sharpe ratio over a short backtesting period may be the result of favorable market conditions rather than a genuine trading edge. For this reason, it should be interpreted alongside other performance metrics and tested across multiple market environments.

---

## Application in trading

The Sharpe ratio provides a simple way to compare strategies by considering both return and risk. Rather than focusing solely on profitability, traders can evaluate how efficiently a strategy generates returns relative to the volatility it experiences.

When used alongside other evaluation metrics, the Sharpe ratio becomes a valuable tool for selecting trading strategies, comparing backtest results, and building portfolios with stronger risk-adjusted performance. While no single metric can fully capture strategy quality, the Sharpe ratio remains one of the most important benchmarks in quantitative finance.
