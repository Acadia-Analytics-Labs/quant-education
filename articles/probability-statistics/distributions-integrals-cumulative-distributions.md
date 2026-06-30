# Mean vs. variance, probability density functions, and common distributions

## Introduction

Many quantitative trading models are built on statistical concepts that describe how market data behaves. Rather than attempting to predict exactly what the market will do next, traders use statistics to estimate the likelihood of different outcomes and make decisions based on those probabilities. Four of the most fundamental concepts are the mean, variance, probability density functions (PDFs), and probability distributions. Together, these concepts provide a framework for understanding expected returns, measuring risk, and modeling price behavior.

---

## Mean

The mean is the average value of a dataset and is often interpreted as the expected value of a variable. In trading, the mean is commonly used to estimate the average return of an asset or trading strategy over a given period.

\[
\mu=\frac{1}{n}\sum_{i=1}^{n}x_i
\]

where \(x_i\) represents each observation, \(n\) is the total number of observations, and \(\mu\) is the mean.

### Example

Suppose a strategy produces daily returns of 0.01, -0.02, 0.03, 0.00, and 0.02. The mean return is

\[
\mu=\frac{0.01-0.02+0.03+0.00+0.02}{5}=0.008,
\]

or 0.8%.

Although the mean summarizes the average performance of a strategy, it does not indicate how consistent those returns are. Two strategies can have the same average return while behaving very differently over time.

---

## Variance

Variance measures how much observations differ from the mean. While the mean describes the center of a dataset, variance describes how spread out the data is around that center. In finance, variance is commonly used as a measure of volatility, with larger values indicating greater uncertainty in returns.

\[
\sigma^2=\frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2
\]

where \(\sigma^2\) represents the variance.

A strategy with low variance produces returns that stay relatively close to the average, while a strategy with high variance experiences larger swings above and below the mean. Because of this, variance is often viewed as a measure of risk. Investors generally prefer strategies that provide higher expected returns while maintaining relatively low variance.

---

## Mean vs. variance

The mean and variance provide different but complementary information about a dataset. The mean estimates the expected return, while the variance measures the uncertainty associated with that return. Looking at only one of these measures can lead to misleading conclusions. For example, two strategies may both average a 10% annual return, but the strategy with lower variance is generally considered more reliable because its returns are more consistent over time.

---

## Probability density functions

Many quantities in finance, such as asset returns, are continuous rather than discrete. Instead of assigning probabilities to individual values, continuous variables are described using probability density functions (PDFs). A PDF specifies how probability is distributed across all possible values of a random variable.

The probability that a random variable lies between two values, \(a\) and \(b\), is given by

\[
P(a \le X \le b)=\int_a^b f(x)\,dx.
\]

A valid probability density function must always be nonnegative, and the total area under the curve must equal one. Rather than representing the probability of a single value, the curve shows where observations are more or less likely to occur. Regions with greater density correspond to outcomes that occur more frequently.

In quantitative trading, PDFs are used to model the distribution of returns and estimate the likelihood of different market outcomes. This allows traders to evaluate the probability of gains, losses, and extreme price movements instead of relying on a single prediction.

---

## Common probability distributions

Different probability distributions are designed to model different types of data. Several distributions appear frequently in finance because they capture different characteristics of market behavior.

### Normal distribution

The normal distribution is the familiar bell-shaped curve and is one of the most widely used probability distributions in statistics. It is symmetric about its mean, with most observations concentrated near the center and fewer observations occurring farther away.

Many financial models assume that returns follow a normal distribution because it is mathematically convenient. Although this assumption is often a reasonable approximation, real markets tend to experience more extreme price movements than a normal distribution predicts.

### Binomial distribution

The binomial distribution models situations with a fixed number of independent trials, where each trial has only two possible outcomes. In trading, these outcomes might represent a winning or losing trade.

This distribution is useful for estimating the probability of achieving a certain number of winning trades over a given sample and for evaluating the consistency of a trading strategy.

### Poisson distribution

The Poisson distribution models the number of events that occur during a fixed interval of time. Unlike the binomial distribution, it focuses on counting events rather than measuring values.

In finance, it can be used to model relatively rare events, such as sudden volatility spikes, large price jumps, or bursts of trading activity over a specified period.

### Pareto distribution

The Pareto distribution describes heavy-tailed data, where extreme outcomes occur more frequently than they would under a normal distribution. This characteristic makes it particularly useful in finance, where large market moves are uncommon but can have a significant impact.

Models based on the Pareto distribution are often used when studying tail risk because they better account for the possibility of unusually large gains or losses.

---

## Application in trading

These concepts work together to help traders better understand financial markets. The mean provides an estimate of expected return, variance measures the uncertainty of those returns, PDFs describe how probability is distributed across possible outcomes, and probability distributions provide mathematical models for different types of market behavior.

Rather than asking whether a stock will increase or decrease in price, quantitative traders ask how likely different outcomes are and how much risk is associated with each one. This probabilistic approach forms the basis of many modern trading strategies and risk management techniques.
