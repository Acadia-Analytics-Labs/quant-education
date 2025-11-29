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
        title: "Bayesian Thinking for Traders",
        description:
          "How to update your beliefs with new information using Bayesian methods",
        difficulty: "Advanced",
        tags: ["Bayesian Statistics", "Decision Making", "Uncertainty"],
        markdownPath: "/src/content/articles/probability-statistics/bayesian-thinking.md",
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
    items: [],
  },
};

export default articles;
