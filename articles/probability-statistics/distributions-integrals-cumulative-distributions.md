# Mean vs Variance, Probability Density Functions, and Common Distributions

## Introduction

In quantitative trading, price and return behavior is described using a few core statistical tools. The most important are mean, variance, probability density functions (PDFs), and probability distributions.

These ideas help shift decision-making from intuition to a more structured, probability-based framework.

---

# Mean vs Variance

## Mean

The mean is the average value of a dataset and is often used as a simple estimate of expected return.

μ = (1/n) Σ xᵢ

Where:
- xᵢ = individual observations  
- n = number of observations  
- μ = mean  

### Example

Returns: 0.01, -0.02, 0.03, 0.00, 0.02  
Mean = 0.008

### In trading

The mean gives a baseline expectation for returns. If a strategy has a consistently positive mean, it suggests a potential edge, assuming results are stable over time.

---

## Variance

Variance measures how far values spread from the mean. In trading terms, it is a direct measure of volatility.

σ² = (1/n) Σ (xᵢ − μ)²

Where:
- σ² = variance  
- μ = mean  

### In trading

Variance captures risk. Two strategies can have the same mean return, but the one with higher variance will produce more unpredictable outcomes.

---

## Mean vs Variance (core idea)

- Mean describes the center of the distribution (expected return)  
- Variance describes the spread around that center (risk)  

Both are needed to evaluate performance. Looking at return without risk gives an incomplete picture.

---

# Probability Density Functions (PDFs)

A probability density function describes how probability is distributed across continuous values.

P(a ≤ X ≤ b) = ∫ f(x) dx

### Key properties

- f(x) is always ≥ 0  
- Total area under the curve equals 1  

### Intuition

A PDF shows where outcomes are concentrated. Higher regions indicate more likely values, while lower regions represent less likely outcomes.

### In trading

PDFs are used to model return distributions. This helps estimate:
- probability of gains or losses  
- likelihood of hitting stop-loss or take-profit levels  
- tail risk and extreme moves  

---

# Common Probability Distributions

## Normal distribution

A symmetric, bell-shaped distribution defined by its mean and variance.

**Used for:**
- modeling asset returns (as an approximation)  
- volatility and risk estimates (e.g., VaR)  
- general market assumptions in many models  

Most values cluster around the mean, with extreme moves assumed to be rare.

---

## Binomial distribution

Models repeated independent trials with two outcomes: success or failure.

**Used for:**
- win/loss probability modeling  
- evaluating consistency of a strategy  
- estimating probability of streaks  

It is useful when thinking in terms of trade outcomes over a fixed number of attempts.

---

## Poisson distribution

Models the number of events occurring over a fixed time period.

**Used for:**
- rare market events (gaps, spikes)  
- volatility clustering  
- order flow arrivals or trade frequency  

It focuses on event counts rather than price magnitude.

---

## Pareto distribution

A heavy-tailed distribution where extreme outcomes carry most of the impact.

P(X > x) ∝ x⁻ᵅ

**Used for:**
- modeling fat tails in returns  
- large price movements  
- crash risk and extreme market behavior  

Unlike the normal distribution, it assumes extreme events are more important than they appear.

---

# Summary

- Mean = expected return  
- Variance = risk or volatility  
- PDF = structure of probabilities across outcomes  
- Distributions = models of how real market data behaves  

Together, they form the basis of probabilistic thinking in trading and help turn uncertainty into something that can be measured and managed.
