---
title: Expected Value (E[X])
description: Learn how expected value transforms trading decisions from guessing to mathematics. Discover why win rate alone doesn't determine profitability and how to calculate the true edge of your trading setups.
difficulty: Intermediate
tags: [probability, statistics, risk management, trading psychology, position sizing]
order: 3
---

# Expected Value (E[X])

## Overview

If an individual repeated the same uncertain decision under the same rules, they can determine the average gain or loss through calculating the expected value. While single outcomes may differ from the expected value, the average result converges towards it over repetitions. The idea of expected value is foundational in probability, economics, and finance.

## Expected Value in the Context of Trading

In trading, expected value reframes how to think about a setup, or a repeatable trade defined by specific entry, exit, and risk rules. The relevant question is not whether the next trade will win, but whether the setup makes money across many trades. A setup has positive expected value if, over time, winning trades more than offset losing ones. If they do not, the strategy is unprofitable, even if individual trades feel successful.

To formalize this, outcomes are represented numerically using a **random variable**. A random variable assigns a number to each possible outcome of an uncertain process. For example, a coin flip might assign 1 to heads and 0 to tails, a die assigns values from 1 through 6, and a trade might assign +2R to a win and −1R to a loss. Once outcomes are expressed as numbers, averages can be meaningfully discussed.

### Mathematical Definition

In the discrete case, expected value is a weighted average of all possible outcomes. A random variable can take several possible values, denoted $R_i$ (where the subscript $i$ simply labels each outcome), and each value occurs with probability $p_i$. The expected value is thus:

$$E[X] = \sum_{i} p_i \cdot R_i$$

Outcomes with higher probabilities receive more weight in the average. The formula is simple, but it captures the whole idea behind expected value.

### Trading Application

Most trading decisions can be simplified to wins and losses. In that case, expected value can be written as:

$$EV = [p(\text{win}) \cdot R(\text{win})] - [p(\text{loss}) \cdot R(\text{loss})]$$

Where:
- $p(\text{win})$ is the probability of a winning trade
- $R(\text{win})$ is the profit when the trade wins
- $R(\text{loss})$ is the loss when it fails

**If EV is positive, the trade is favorable in the long run. If EV is negative, it is not, regardless of how often it wins.**

## The Common Deception of Winning Often

Suppose a setup wins 40 percent of the time. When it wins, it makes 2R, and when it loses, it loses 1R. The expected value is:

$$EV = [0.40 \cdot 2R] - [0.60 \cdot 1R]$$

$$= 0.8R - 0.6R$$

$$= 0.2R$$

This means that, on average, the trader earns 0.2 units of risk per trade. Individual outcomes are still either +2R or −1R. The average only reveals itself over repetition.

### Key Insights

This highlights several important points:

1. **You can lose more often than you win and still have a profitable system**
2. **The edge comes from the combination of win rate and payoff, not from either one in isolation**
3. **A high win rate by itself guarantees nothing**

This is why win rate is a common trap, and leads new traders to focus on accuracy. Professionals, however, focus on expectation.

### Example: High Win Rate ≠ Profitability

Consider a strategy that wins 70 percent of the time, but loses 3R on losers and makes 1R on winners. Its expected value is:

$$EV = 0.7 \cdot 1R - 0.3 \cdot 3R = 0.7R - 0.9R = -0.2R$$

This is a **losing system** despite the 70% win rate.

Now consider another strategy that wins only 35 percent of the time, but makes 3R on winners and loses 1R on losers:

$$EV = 0.35 \cdot 3R - 0.65 \cdot 1R = 1.05R - 0.65R = 0.4R$$

This is a **winning system** with only a 35% win rate. The second strategy feels worse emotionally because it loses more often, but it is mathematically superior.

## Expected Value ≠ Probable Value

Another common mistake is assuming expected value describes what is most likely to happen. **It does not.**

### Example

A trade with:
- 99% chance of losing $1
- 1% chance of winning $200

Has expected value:

$$E[X] = 0.99(-1) + 0.01(200) = -0.99 + 2.00 = +1.01$$

You will almost always lose money, yet the average outcome is positive. This distinction explains why casinos make money, why insurance companies exist, and why some profitable strategies feel uncomfortable to trade.

**Expected value is not a prediction tool, but a decision tool.** It helps answer whether a trade or strategy is favorable over time, not whether the next instance will work. That distinction is critical for rational decision making under uncertainty.

## Practical Application

In practice, traders do not need perfect probabilities or advanced mathematics to use expected value. They need honest estimates and consistency.

### Steps to Calculate EV

1. **Log trades by setup** with consistent rules
2. **After a meaningful sample**, calculate:
   - Win rate
   - Average win
   - Average loss
3. **Use the approximation:**

$$EV \approx \text{WinRate} \cdot \text{AvgWin} - (1 - \text{WinRate}) \cdot \text{AvgLoss}$$

This is often enough to identify which setups actually pay.

### Acting on EV

Once expected value is estimated, behavior should follow:

- **High expected value setups** deserve attention and frequency
- **Low expected value setups** should be reduced, redesigned, or eliminated

Although a positive expected value strategy will still experience losing streaks, it is important to remember that **expected value lives in the long run, not in individual outcomes**.

## Scalability of Expected Value

One reason expected value scales so cleanly is its **linearity**. Expected value has two key linear properties:

### 1. Additivity
The expected value of the sum of strategies is simply the sum of their expected values:

$$E[X + Y] = E[X] + E[Y]$$

### 2. Scalar Multiplication
When you multiply a random variable by a constant (e.g., changing position size), the expected value scales proportionally:

$$E[c \cdot X] = c \cdot E[X]$$

Where $c$ is any real number (your position size multiplier).

### Practical Implications

These properties allow:
- **Complex systems to be broken into basic parts** and analyzed independently
- **Position sizing to scale predictably** - if a 1-lot trade has EV of +0.2R, then a 10-lot trade has EV of +2R
- **Portfolio construction** by combining multiple strategies with known expected values
- **Risk-adjusted position sizing** without recalculating probabilities

This is why expected value is central to portfolio thinking and quantitative finance.

## Importance of Risk Management

Expected value tells you the center of outcomes, but **it says nothing about how spread out those outcomes are**. Two strategies can have the same expected value and feel completely different because of variance.

**Risk management exists to survive the variability around the average, not to replace expected value.**

## Common Pitfalls

Many traders misuse expected value by:

1. **Chasing lucky outcomes** instead of process
2. **Overfitting probabilities** to narrow conditions
3. **Ignoring rare but catastrophic losses**
4. **Treating expected value as a guarantee**

Expected value is a statement about distributions, not certainty. Its role is to identify edge, not to eliminate randomness.

## Conclusion

At a deeper level, expected value is the backbone of rational trading. It separates:

- Outcomes from processes
- Emotion from structure
- Short term noise from long term edge

Once expected value is understood, concepts like risk, sizing, optimization, and system design become much easier to reason about.

**The goal is not to win every trade, but to trade setups with positive expected value consistently enough that the law of large numbers works in your favor.**
