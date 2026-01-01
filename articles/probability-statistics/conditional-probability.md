# Conditional probability & Bayes’ theorem 

## Introduction
Conditional probability is the probability of an event occurring given that another event has already occurred. Conditional probability is especially important when new information becomes available and prior assumptions must be updated.

Conditional probability is written as:
$$P(A|B) \text{ or } P_B(A)$$

Where $A$ is the event of interest and $B$ is the event that has already occurred. $P(A|B)$ expresses the probability of $A$ occurring given that $B$ has occurred.

In comparison, $P(E)$ represents an unconditional or absolute probability, meaning it is unaffected by the outcome of a separate event.

## Conditional Probability Formula
The formula for conditional probability is:

$$P(A | B) = \frac{P(A \text{ and } B)}{P(B)}$$

Where:
- $P(A \text{ and } B)$ is the probability of both $A$ and $B$ occurring
- $P(B)$ is the probability of $B$ occurring

### Example:
A simple example to illustrate conditional probability is marbles in a bag. Say you have 10 marbles: 5 red, 3 blue, and 2 green. Let the event of pulling a red marble be $R$, and let the event of pulling a marble that is not green be $B$.

We know:
$$P(R) = \frac{5}{10} = 0.5 \text{ and } P(B) = \frac{8}{10} = 0.8$$

If we know that the next marble we pull is not green, then the conditional probability that the marble is red can be expressed as:
$$P(R|B) = \frac{P(R \text{ and } B)}{P(B)} = \frac{5/10}{8/10} = \frac{5}{8} = 0.625$$

### Application in Trading
Conditional probability is useful in trading because it allows traders to update the likelihood of future price movements based on new market information.

## Bayes' Theorem
Bayes' Theorem is the foundation of Bayesian thinking and provides a systematic way to update probabilities based on prior beliefs and new evidence.

Bayes' Theorem states:
$$P(A | B) = \frac{P(B | A)\cdot P(A)}{P(B)}$$

Where:
- $P(A | B)$ is the posterior (updated) conditional probability that $A$ occurs given $B$
- $P(B | A)$ is the conditional probability that $B$ occurs given $A$
- $P(A)$ is the prior probability of $A$
- $P(B)$ is the prior probability of $B$

### Proof:
We can derive this formula by using the conditional probability. 
Given: (1) $P(A | B) = \frac{P(A \text{ and } B)}{P(B)}$ and (2) $P(B | A) = \frac{P(B \text{ and } A)}{P(A)}$ from applying the definition of conditional probability, the key observation is that $P(A \text{ and } B) = P(B \text{ and } A)$, since both expressions describe the same situation, which is that $A$ and $B$ happen together. 

As a result, we can multiply both sides of equation (2) by $$\frac{P(A)}{P(B)}$$:

$$\frac{P(A)}{P(B)} \cdot P(B | A) = \frac{P(B \text{ and } A)}{P(A)} \cdot \frac{P(A)}{P(B)}$$
$$\frac{P(B | A)\cdot P(A)}{P(B)} = \frac{P(B \text{ and } A)}{P(B)} = P(A | B)$$

Where the last equality follows by equation (1). $\square$


### Example:
We can again use the example of marbles in a bag to illustrate how Bayes' Theorem can be applied.

Say we have two bags of marbles $B_1$ and $B_2$. Bag $B_1$ has 5 green marbles and 5 red marbles. Bag $B_2$ has 7 green marbles and 3 red marbles. Say you have one of these two bags but you do not know which. As such, our prior beliefs are:

$$P(B_1) = \frac{1}{2}$$ $$P(B_2) = \frac{1}{2}$$

Say you pull a green marble from your bag. We can then update the probabilities of $B_1$ and $B_2$ using Bayes' Theorem. Letting $G$ be the event of pulling a green marble at random from _either_ bag, $P(G)=\frac{5+7}{20} = \frac{12}{20}$, and thus

$$P(B_1 | G) = \frac{P(G | B_1)\cdot P(B_1)}{P(G)} = \frac{\frac{5}{10}\cdot \frac{1}{2}}{\frac{12}{20}} = \frac{5}{12} \approx 0.417$$

$$P(B_2 | G) = \frac{P(G | B_2)\cdot P(B_2)}{P(G)} = \frac{\frac{7}{10}\cdot \frac{1}{2}}{\frac{12}{20}} = \frac{7}{12} \approx 0.583$$

Given that you pulled a green marble from the bag, there is a higher 58.3% probability that you have bag $B_2$ compared to a 41.7% probability that you have bag $B_1$.

### Application in Trading:
In trading, Bayes’ Theorem allows traders to systematically incorporate new evidence, such as price action, volume, or macroeconomic data, into existing beliefs about market behavior. By continuously updating probabilities as conditions change, traders can make more informed, adaptive, and risk-aware decisions. We will learn how this helps us develop more comprehensive and robust models of price data.
