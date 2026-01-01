# Probability Basics: Bayesian & Frequentist Perspectives

## Introduction

Probability is the branch of mathematics that studies events and provides numerical descriptions of how likely they are to occur. In trading, probability helps us understand and reason about uncertainty present in the market. A solid understanding of probability can lead to better-informed trading decisions.

We express probabilities in the following way: for a 50% probability,

$$P(E) = 0.5$$

Where:
- $E$ is the event  
- $P(\cdot)$ denotes the probability function  
- $0.5$ is the probability of the event occurring  

A probability is always a number between 0 and 1, where 0 means an event is impossible and 1 means it is certain.

## Events and Probability

An **event** is defined as a subset of outcomes of an experiment. An experiment is any process that produces an outcome.

For example, in the case of flipping a coin:
- The flip itself is the experiment
- The possible outcomes are heads or tails
- An event could be the coin landing on heads

For experiments with equally likely outcomes, probability can be calculated using the following equation:

$$P(E) = \frac{\text{number of favorable outcomes to } E}{\text{total number of possible outcomes}}$$

### Combining Events
Set notation can also be applied to events in probability theory.  
The union, denoted by $A \cup B$, represents the event that at least one of the events $A$ or $B$ occurs.  
The intersection, denoted by $A \cap B$, represents the event that both events $A$ and $B$ occur.
The complement, denoted by $A'$, or $\overline A$, represents the event in which A does not happen.

## Interpreting Probability

The way we interpret probability depends on the philosophy used in statistics. The two most common interpretations are the **Bayesian** and **Frequentist** perspectives.


### Bayesian Perspective

The Bayesian perspective treats probability as a **degree of belief** and incorporates prior knowledge into analysis.

Using the coin example, a Bayesian thinker would say that, before the coin is flipped, they are 50\% certain that the coin will land on heads. This probability represents their belief based on the information currently available.


### Frequentist Perspective

The Frequentist perspective focuses on long-run frequencies of events across repeated trials. This approach is more rigid and often struggles in situations where events are unique or non-repeatable.

Continuing with the coin example, a frequentist would say that if the coin were flipped an infinite number of times, approximately half of the outcomes would be heads and half would be tails. A single flip landing on tails does not change the underlying probability; it is simply one outcome within the long-run distribution.

## Probability in Trading

In trading, it is important to have a solid understanding of both of these statistical models. Bayesian methods are often more intuitive, as they allow traders to incorporate prior knowledge and update beliefs as new information becomes available. However, they can be sensitive to assumptions and may introduce bias through the choice of prior. On the other hand, Frequentist methods rely on long-run frequencies and fixed procedures, but they are often less intuitive and can struggle when applied to short-term or non-repeatable market events. In practice, it is important to draw upon both of these statistical methods, utilizing both depending on the available data.
