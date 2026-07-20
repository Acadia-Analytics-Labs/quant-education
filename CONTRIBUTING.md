# Contributing to Acadia Analytics Education Content

This repository contains educational content for the Acadia Analytics learning platform. All content is written in Markdown and automatically discovered by the application.

## Quick Start: Adding a New Article

### 1. Create the Markdown File

Add your article to the appropriate category folder:

```
articles/
  ├── trading/
  ├── probability-statistics/
  ├── machine-learning/
  ├── quantitative-finance/
  └── economics/
      └── your-new-article.md  ← Add here
```

### 2. Write Your Content

Use standard Markdown with optional YAML frontmatter:

```markdown
---
title: Understanding Treasury Rates and Bond Market Signals
description: Comprehensive guide to interpreting Treasury yields
difficulty: Intermediate
tags: [Economics, Bonds, Interest Rates]
---

# Understanding Treasury Rates

Your content here...
```

**Frontmatter fields (all optional):**
- `title`: Article title (defaults to first `# heading` or filename)
- `description`: Short summary (defaults to first paragraph, truncated)
- `difficulty`: `Beginner`, `Intermediate`, or `Advanced` (defaults to `Beginner`)
- `tags`: Array of relevant keywords (defaults to `[]`)

### 3. Update the Article Registry

Edit `articlesData.ts` to register your article:

```typescript
economics: {
  items: [
    {
      title: "Understanding Treasury Rates and Bond Market Signals",
      description: "Comprehensive guide to interpreting Treasury yields",
      difficulty: "Intermediate",
      tags: ["Economics", "Bonds", "Interest Rates"],
      filename: "understanding-treasury-rates",  // Without .md extension
      order: 1,  // Optional: controls display order
    },
    // ... other articles
  ],
},
```

### 4. Test Locally

If using Vite auto-discovery (UI repo):
- Content appears automatically after dev server restart
- No manual registry needed in that environment

If using manual registry (this repo):
- Ensure `articlesData.ts` is updated
- Filename must match exactly (without `.md`)

## Content Guidelines

### Writing Style

**Educational articles should:**
- Explain concepts clearly without assuming prior knowledge
- Use real-world examples to illustrate abstract ideas
- Include mathematical formulas where relevant (supports LaTeX via KaTeX)
- Be analytical and factual, avoiding opinions or recommendations
- Link to related articles for deeper exploration

**Blog posts should:**
- Be timely and news-focused
- Provide context and analysis of current events
- Be concise (suitable for blog format)
- Include source links

### Formatting

**Headings:**
```markdown
# Main Title (H1)
## Major Section (H2)
### Subsection (H3)
```

**Math (KaTeX):**
```markdown
Inline: $E = mc^2$

Block:
$$
\text{Stock Value} = \sum_{n=1}^{\infty} \frac{\text{Cash Flow}_n}{(1 + r)^n}
$$
```

**Code:**
```markdown
Inline: `const value = 42`

Block:
\`\`\`python
def calculate_yield(price, coupon):
    return coupon / price
\`\`\`
```

**Links:**
```markdown
External: [CNN Article](https://www.cnn.com/...)
Internal: [Related Article](../trading/position-sizing)
```

**Lists:**
```markdown
- Unordered item
- Another item

1. Ordered item
2. Second item
```

## File Organization

### Categories

Current categories:
- `trading/` - Execution, costs, risk management, position sizing
- `probability-statistics/` - Probability, distributions, Bayesian methods
- `machine-learning/` - ML models, neural networks, reinforcement learning
- `quantitative-finance/` - Quant strategies, HMM, trend following
- `economics/` - Market analysis, economic theory, fixed income

### Naming Conventions

**Files:**
- Use kebab-case: `understanding-treasury-rates.md`
- Be descriptive but concise
- Avoid dates in filenames (they become outdated)

**Frontmatter tags:**
- Title Case: `["Risk Management", "Portfolio Theory"]`
- Be specific: `["MACD", "RSI"]` not just `["Indicators"]`
- Keep to 3-5 tags per article

## Content Structure

### Educational Articles

Recommended structure:
1. **Introduction** - What the article covers and why it matters
2. **Core Concepts** - Fundamental definitions and principles
3. **Mechanisms/Examples** - How things work in practice
4. **Case Studies** - Real-world applications
5. **Mathematical Details** - Formulas and calculations
6. **Practical Applications** - How to use this knowledge
7. **Further Reading** - Links to related articles

### Blog Posts

Recommended structure:
1. **Overview** - What happened and key numbers
2. **Context** - Background and drivers
3. **Analysis** - What it means and implications
4. **Source Links** - Attribution and deeper reading

## Version Control

### Commits

Use clear, descriptive commit messages:
```bash
git commit -m "Add Treasury rates educational article"
git commit -m "Update position sizing article with new examples"
git commit -m "Fix typo in Bayesian thinking article"
```

### Branches

For new content:
```bash
git checkout -b article/treasury-rates
# Make changes
git commit -m "Add Treasury rates article"
git push origin article/treasury-rates
# Create pull request
```

### Pull Requests

- One article per PR when possible
- Include a brief description of the content
- Tag relevant reviewers if applicable

## Technical Details

### Auto-Discovery (UI Repository)

The UI repository uses Vite's glob import:

```typescript
import.meta.glob('/public/content/articles/**/*.md', {
  query: '?raw',
  import: 'default',
  eager: true
})
```

This automatically:
- Discovers all `.md` files in article folders
- Loads them at build time
- Makes them available to the article viewer

### Manual Registry (This Repository)

This repository maintains `articlesData.ts` as the source of truth.

**Structure:**
```typescript
export interface Article {
  title: string;
  description: string;
  difficulty: "Beginner" | "Intermediate" | "Advanced";
  tags: string[];
  filename: string;  // Without .md extension
  order?: number;    // Optional display order
}

export interface Articles {
  [category: string]: {
    items: Article[];
  };
}
```

### Article Loading

The `ArticleViewer` component loads articles by:
1. Looking up the article in `articlesData.ts` by category and index
2. Constructing the path: `/public/content/articles/{category}/{filename}.md`
3. Fetching and rendering the markdown
4. Processing math (KaTeX) and syntax highlighting

### Progress Tracking

User progress is stored in localStorage:
```typescript
localStorage.getItem('acadia.educationProgress')
// Format: { "trading-0": true, "economics-1": true, ... }
```

Future enhancement: Backend persistence tied to user profiles.

## Maintenance

### Updating Existing Articles

1. Edit the `.md` file directly
2. Update `articlesData.ts` if title/description/tags changed
3. Commit with descriptive message
4. No restart needed in dev mode (hot reload)

### Removing Articles

1. Delete the `.md` file
2. Remove entry from `articlesData.ts`
3. Update any articles that link to the removed content
4. Commit changes

### Reordering Articles

Update the `order` field in `articlesData.ts`:

```typescript
items: [
  { ..., filename: "first-article", order: 1 },
  { ..., filename: "second-article", order: 2 },
  { ..., filename: "third-article", order: 3 },
]
```

Articles without `order` appear after ordered articles.

## Quality Checklist

Before submitting new content:

- [ ] Markdown renders correctly (headings, lists, code blocks)
- [ ] Math formulas display properly (if applicable)
- [ ] Links work (both internal and external)
- [ ] Frontmatter is valid YAML
- [ ] `articlesData.ts` entry matches filename exactly
- [ ] Difficulty level is appropriate
- [ ] Tags are specific and relevant
- [ ] Writing is clear and educational
- [ ] Examples are accurate and helpful
- [ ] Content is original or properly attributed

## Getting Help

Questions about:
- **Content**: Review existing articles for style and structure examples
- **Technical**: Check `ArticleViewer.tsx` in the UI repo for rendering logic
- **Registry**: See `articlesData.ts` for schema and examples

## License

All content in this repository is © 2025 Acadia Analytics. See [LICENSE](LICENSE) for details.
