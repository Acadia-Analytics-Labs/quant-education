// Copyright © 2025 Acadia Analytics. All rights reserved.
// Article registry for public content articles.
// Articles are loaded from /public/content/articles/{topic}/{filename}.md at runtime.

export interface Article {
  title: string;
  description: string;
  difficulty: "Beginner" | "Intermediate" | "Advanced";
  tags: string[];
  filename: string;
  order?: number;
}

export interface ArticleCategory {
  items: Article[];
}

export interface Articles {
  [key: string]: ArticleCategory;
}

const articles: Articles = {
  trading: {
    items: [
      {
        title: "The Thorp Edge Principle: More Bets, Not Bigger Bets",
        description: "How Ed Thorp learned to beat casinos and Wall Street by maximizing bet frequency, not bet size",
        difficulty: "Beginner",
        tags: ["Money Management", "Edge", "Risk Management", "Ed Thorp"],
        filename: "thorp-edge-principle",
      },
      {
        title: "Position Sizing and Risk Management",
        description: "Learn how to calculate optimal position sizes and manage risk across your portfolio",
        difficulty: "Beginner",
        tags: ["Position Sizing", "Portfolio Theory"],
        filename: "position-sizing",
      },
      {
        title: "Orders, Slippage, and Trading Costs",
        description: "Understanding order types, execution costs, and how they impact trading performance",
        difficulty: "Beginner",
        tags: ["Order Types", "Execution", "Costs"],
        filename: "orders-slippage-costs",
      },
      {
        title: "Backtesting Basics",
        description: "Fundamentals of backtesting trading strategies and avoiding common pitfalls",
        difficulty: "Intermediate",
        tags: ["Backtesting", "Strategy Testing"],
        filename: "backtesting-basics",
      },
      {
        title: "Technical Indicator Cheatsheet",
        description: "Quick reference guide to common technical indicators and their applications",
        difficulty: "Beginner",
        tags: ["Technical Analysis", "Indicators"],
        filename: "indicator-cheatsheet",
      },
      {
        title: "ESG Investing",
        description: "Environmental, Social, and Governance factors in investment decisions",
        difficulty: "Intermediate",
        tags: ["ESG", "Sustainable Investing"],
        filename: "esg-investing",
      },
    ],
  },
  "probability-statistics": {
    items: [
      {
        title: "Probability Distributions in Trading",
        description: "Understanding normal, log-normal, and fat-tailed distributions in financial markets",
        difficulty: "Intermediate",
        tags: ["Probability", "Statistics", "Market Behavior"],
        filename: "distributions",
      },
      {
        title: "Bayesian Thinking for Traders",
        description: "How to update your beliefs with new information using Bayesian methods",
        difficulty: "Advanced",
        tags: ["Bayesian Statistics", "Decision Making", "Uncertainty"],
        filename: "bayesian-thinking",
      },
      {
        title: "Expected Value",
        description: "Understanding expected value and its applications in trading decisions",
        difficulty: "Beginner",
        tags: ["Probability", "Expected Value"],
        filename: "expected-value",
      },
      {
        title: "Conditional Probability",
        description: "Understanding conditional probability and its role in trading analysis",
        difficulty: "Intermediate",
        tags: ["Probability", "Conditional Probability"],
        filename: "conditional-probability",
      },
      {
        title: "Monte Carlo Risk Forecasting",
        description: "Using Monte Carlo simulation for risk assessment and portfolio analysis",
        difficulty: "Advanced",
        tags: ["Monte Carlo", "Risk Management", "Simulation"],
        filename: "monte-carlo-risk-forecasting",
      },
      {
        title: "State Space Models and Kalman Filters",
        description: "Introduction to state space models and Kalman filtering for time series analysis",
        difficulty: "Advanced",
        tags: ["State Space", "Kalman Filter", "Time Series"],
        filename: "state-space-kalman",
      },
    ],
  },
  "machine-learning": {
    items: [
      {
        title: "Introduction to Machine Learning in Trading",
        description: "Overview of ML applications in algorithmic trading and getting started",
        difficulty: "Beginner",
        tags: ["Machine Learning", "Algorithmic Trading", "Getting Started"],
        filename: "intro-ml-trading",
      },
      {
        title: "Model Types",
        description: "Overview of different machine learning model types and their applications",
        difficulty: "Intermediate",
        tags: ["Machine Learning", "Model Types"],
        filename: "model-types",
      },
      {
        title: "Neural Networks Foundations",
        description: "Fundamental concepts of neural networks and deep learning",
        difficulty: "Intermediate",
        tags: ["Neural Networks", "Deep Learning"],
        filename: "neural-networks-foundations",
      },
      {
        title: "Curse of Dimensionality",
        description: "Understanding the curse of dimensionality and techniques to address it",
        difficulty: "Intermediate",
        tags: ["Dimensionality", "Feature Engineering"],
        filename: "curse-of-dimensionality",
      },
      {
        title: "Manifold Hypothesis",
        description: "The manifold hypothesis and its implications for machine learning",
        difficulty: "Advanced",
        tags: ["Manifold", "Theory"],
        filename: "manifold-hypothesis",
      },
      {
        title: "Reinforcement Learning Trading Agents",
        description: "Foundations of using reinforcement learning for trading agent development",
        difficulty: "Advanced",
        tags: ["Reinforcement Learning", "Trading Agents"],
        filename: "rl-trading-agents-foundations",
      },
    ],
  },
  "quantitative-finance": {
    items: [
      {
        title: "Introduction to Quantitative Trading",
        description: "Core concepts and methods for quantitative trading strategies",
        difficulty: "Beginner",
        tags: ["Quantitative Finance", "Trading Strategies"],
        filename: "intro-quant-trading",
      },
      {
        title: "Trend Following",
        description: "Understanding trend following strategies and their implementation",
        difficulty: "Intermediate",
        tags: ["Trend Following", "Strategies"],
        filename: "trend-following",
      },
      {
        title: "HMM Market Regimes",
        description: "Using Hidden Markov Models to identify and trade market regimes",
        difficulty: "Advanced",
        tags: ["HMM", "Market Regimes", "State Models"],
        filename: "hmm-market-regimes",
      },
    ],
  },
  economics: {
    items: [
      {
        title: "Understanding Treasury Rates and Bond Market Signals",
        description: "Comprehensive guide to interpreting Treasury yields, transmission mechanisms, and market signals with real-world examples",
        difficulty: "Intermediate",
        tags: ["Economics", "Bonds", "Interest Rates", "Monetary Policy", "Fixed Income"],
        filename: "understanding-treasury-rates",
        order: 1,
      },
      {
        title: "Day Trading Affordability Crisis",
        description: "Analysis of accessibility and affordability in day trading",
        difficulty: "Intermediate",
        tags: ["Economics", "Day Trading", "Accessibility"],
        filename: "day-trading-affordability-crisis",
        order: 2,
      },
      {
        title: "Calculus of Value",
        description: "Mathematical foundations of value and pricing in economics",
        difficulty: "Advanced",
        tags: ["Economics", "Calculus", "Pricing"],
        filename: "Calculus_Of_Value",
        order: 3,
      },
    ],
  },
};

export default articles;

