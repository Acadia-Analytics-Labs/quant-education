// Copyright © 2025 Acadia Analytics. All rights reserved.
// Updated articles data structure pointing to markdown files

export interface Article {
  title: string;
  description: string;
  difficulty: "Beginner" | "Intermediate" | "Advanced";
  tags: string[];
  markdownPath: string;
}

export interface ArticleCategory {
  items: Article[];
}

export interface Articles {
  [key: string]: ArticleCategory;
}

const articles: Articles = {
  "trading": {
    items: [
      {
        title: "Understanding ESG Investing",
        description:
          "A comprehensive guide to Environmental, Social, and Governance investing, including strategies, measurement, and practical implementation",
        difficulty: "Intermediate",
        tags: ["ESG", "Sustainable Investing", "Risk Management", "Corporate Governance", "Impact Investing"],
        markdownPath: "/articles/trading/esg-investing.md",
      },
      {
        title: "Position Sizing and Risk Management",
        description:
          "Learn how to calculate optimal position sizes and manage risk across your portfolio",
        difficulty: "Beginner",
        tags: ["Position Sizing", "Portfolio Theory"],
        markdownPath: "/src/content/articles/trading/position-sizing.md",
      },
    ],
  },
  "probability-statistics": {
    items: [
      {
        title: "Probability Distributions in Trading",
        description:
          "Understanding normal, log-normal, and fat-tailed distributions in financial markets",
        difficulty: "Intermediate",
        tags: ["Probability", "Statistics", "Market Behavior"],
        markdownPath: "/src/content/articles/probability-statistics/distributions.md",
      },
      {
        title: "Probability and Bayesian Thinking",
        description:
          "Introduction to probability and Bayesian / Frequentist thinking",
        difficulty: "Beginner",
        tags: ["Bayesian Statistics", "Decision Making", "Uncertainty"],
        markdownPath: "/src/content/articles/probability-statistics/bayesian-thinking.md",
      },
      {
        title: "Conditional probability and Bayes’ theorem",
        description:
          "How to update your beliefs with new information using Bayesian methods",
        difficulty: "Intermediate",
        tags: ["Bayesian Statistics", "Decision Making", "Uncertainty"],
        markdownPath: "/src/content/articles/probability-statistics/conditional-probability.md",
      },
    ],
  },
  "machine-learning": {
    items: [
      {
        title: "Introduction to Machine Learning in Trading",
        description:
          "Overview of ML applications in algorithmic trading and getting started",
        difficulty: "Beginner",
        tags: ["Machine Learning", "Algorithmic Trading", "Getting Started"],
        markdownPath: "/src/content/articles/machine-learning/intro-ml-trading.md",
      },
    ],
  },
  "economics": {
    items: [
      {
        title: "Day Trading and the Affordability Crisis",
        description:
          "How the housing affordability crisis is driving young people toward high-risk trading strategies and creating demand for analytical tools",
        difficulty: "Beginner",
        tags: ["Day Trading", "Cryptocurrency", "Risk Management", "Prediction Markets", "Affordability Crisis"],
        markdownPath: "/articles/economics/day-trading-affordability-crisis.md",
      },
      {
        title: "On The Calculus of Value by Howard Marks",
        description:
          "Howard Marks discusses the relationship between price and value, investment psychology, and market valuation metrics",
        difficulty: "Intermediate",
        tags: ["Valuation", "Investment Psychology", "Market Analysis", "P/E Ratio"],
        markdownPath: "/src/content/articles/economics/Calculus_Of_Value.md",
      },
    ],
  },
  "quantitative-finance": {
    items: [
      {
        title: "Trend Following Systems",
        description:
          "Master systematic trading strategies that capture sustained price movements through disciplined trend identification and risk management",
        difficulty: "Intermediate",
        tags: ["Trend Following", "Systematic Trading", "Risk Management", "Position Sizing"],
        markdownPath: "/src/content/articles/quantitative-finance/trend-following.md",
      },
    ],
  },
};

export default articles;
