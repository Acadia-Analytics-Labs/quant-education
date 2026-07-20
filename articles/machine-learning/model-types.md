# Machine Learning Model Types

Understanding different ML model families helps you choose the right tool for your trading problem. Each model type has distinct characteristics, strengths, and failure modes.

## Linear Models

The simplest and most interpretable family. Assumes the output is a linear combination of inputs.

### Linear Regression

Predicts a continuous value:

$$y = w_0 + w_1 x_1 + w_2 x_2 + ... + w_n x_n$$

**When to use:**
- Baseline model (always start here)
- You need interpretability (which features matter?)
- Your relationship is roughly linear
- High-dimensional data with limited samples

**Example: Predicting next-day returns**
```python
from sklearn.linear_model import Ridge

# Features: recent returns, volatility, volume
X = df[['return_1d', 'return_5d', 'volatility_20d', 'volume_ratio']]
y = df['future_return']

model = Ridge(alpha=1.0)  # L2 regularization
model.fit(X, y)

# See which features matter
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
```

**Strengths:**
- Fast to train and predict
- Interpretable coefficients
- Works well with regularization in high dimensions
- Stable and predictable

**Weaknesses:**
- Can't learn nonlinear patterns
- Assumes features are already good
- Sensitive to outliers (unless robust regression)

### Logistic Regression

For classification (e.g., predict up/down):

$$P(\text{up}) = \frac{1}{1 + e^{-(w_0 + w_1 x_1 + ... + w_n x_n)}}$$

**Use for:** Binary predictions with interpretable probabilities.

## Tree-Based Models

Learn decision rules by recursively splitting data. Think "if volatility > 0.02 and volume > 1M, then..."

### Decision Trees

A single tree that makes splits based on features.

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=5,        # Limit tree depth
    min_samples_leaf=50 # Require 50 samples per leaf
)
model.fit(X, y)
```

**Strengths:**
- Handles nonlinear relationships
- Automatically finds interactions (e.g., "high vol AND low price")
- No need to scale features
- Easy to visualize (for shallow trees)

**Weaknesses:**
- Overfit easily (need depth limits)
- Unstable (small data changes → big tree changes)
- Poor extrapolation outside training range

### Random Forest

Many trees, each trained on a random subset of data and features. Final prediction is the average.

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,   # 100 trees
    max_depth=10,       # Limit depth
    min_samples_leaf=20,
    max_features='sqrt' # Random feature subset
)
model.fit(X, y)

# Feature importance
importances = model.feature_importances_
```

**Strengths:**
- More stable than single trees
- Built-in feature importance
- Hard to overfit (with enough trees and depth limits)
- Handles missing data and outliers well

**Weaknesses:**
- Less interpretable than single trees
- Slower than linear models
- Can still overfit if trees are too deep
- Memory intensive

### Gradient Boosting

Builds trees sequentially, each correcting errors of previous trees. Very powerful but easy to overfit.

```python
from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.05,  # Slow learning = better generalization
    max_depth=3,         # Shallow trees
    subsample=0.8        # Use 80% of data per tree
)
model.fit(X, y)
```

**Popular implementations:**
- XGBoost (fast, widely used)
- LightGBM (faster, good for large datasets)
- CatBoost (handles categorical features well)

**Strengths:**
- Often wins on tabular data
- Excellent performance with proper tuning
- Can capture complex patterns

**Weaknesses:**
- Overfits easily (needs careful regularization)
- Sensitive to hyperparameters
- Slower to train than Random Forest
- Less interpretable

## Support Vector Machines (SVM)

Finds the best boundary between classes by maximizing the margin. Can use kernels for nonlinear boundaries.

```python
from sklearn.svm import SVR

model = SVR(
    kernel='rbf',  # Radial basis function (nonlinear)
    C=1.0,         # Regularization
    epsilon=0.1    # Margin of tolerance
)
model.fit(X, y)
```

**When to use:**
- Small to medium datasets
- High-dimensional spaces
- Need robust boundaries

**Strengths:**
- Effective in high dimensions
- Memory efficient (uses support vectors only)
- Versatile (different kernels)

**Weaknesses:**
- Slow on large datasets (n > 10,000)
- Requires feature scaling
- Hard to interpret
- Hyperparameter tuning is critical

## Neural Networks

Layers of interconnected neurons that learn hierarchical representations.

### Feedforward Networks (MLP)

Stack of fully connected layers:

```python
from sklearn.neural_network import MLPRegressor

model = MLPRegressor(
    hidden_layer_sizes=(100, 50),  # Two hidden layers
    activation='relu',
    alpha=0.01,     # L2 regularization
    learning_rate_init=0.001,
    max_iter=500
)
model.fit(X, y)
```

**Strengths:**
- Learn complex nonlinear patterns
- Can approximate any function (universal approximation)
- Scale to large datasets

**Weaknesses:**
- Need lots of data (or will overfit)
- Hard to interpret
- Sensitive to initialization and hyperparameters
- Require feature scaling

### When Neural Networks Make Sense

**Good use cases:**
- Large datasets (10,000+ samples)
- Image/text/sequence data (use CNNs, RNNs, Transformers)
- You've exhausted simpler models

**Bad use cases:**
- Small datasets (<1,000 samples) → use linear models or trees
- Need interpretability → use linear models or single trees
- Limited compute → use linear models

## k-Nearest Neighbors (k-NN)

Non-parametric: stores all training data, predicts based on k closest neighbors.

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(
    n_neighbors=10,
    weights='distance'  # Closer neighbors weigh more
)
model.fit(X, y)
```

**Strengths:**
- No training time (lazy learning)
- Naturally handles nonlinear relationships
- Simple concept

**Weaknesses:**
- Slow predictions (must search all training data)
- Suffers from curse of dimensionality
- Requires feature scaling
- Memory intensive

## Naive Bayes

Probabilistic classifier based on Bayes' theorem. Assumes features are independent (hence "naive").

**When to use:**
- Text classification
- Fast baseline for classification
- When independence assumption roughly holds

**Avoid for:** Financial data (features are usually correlated).

## Model Selection Guidelines

### Start Simple
1. **Linear regression** (regression) or **logistic regression** (classification)
2. Check if it's "good enough" (often it is!)
3. Use as baseline to beat

### Go to Trees If
- Nonlinear relationships exist
- Feature interactions matter
- Don't need perfect interpretability

**Progression:** Decision Tree → Random Forest → Gradient Boosting

### Consider Neural Networks If
- Very large dataset (>10,000 samples)
- Tried trees and need more capacity
- Working with images/text/sequences

### Quick Decision Tree

**Small data (<1,000 samples)?**
- Linear models with regularization

**Tabular data (1,000-100,000 samples)?**
- Random Forest or Gradient Boosting

**Need interpretability?**
- Linear model or single decision tree (shallow)

**Large data + complex patterns?**
- Gradient Boosting or Neural Networks

**High-frequency or online learning?**
- Linear models (fast updates)

## Ensemble Methods

Combine multiple models for better performance.

### Voting/Averaging
Train several models, average their predictions:

```python
from sklearn.ensemble import VotingRegressor
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

ensemble = VotingRegressor([
    ('linear', Ridge(alpha=1.0)),
    ('rf', RandomForestRegressor(n_estimators=50)),
    ('svm', SVR(kernel='rbf'))
])
ensemble.fit(X, y)
```

### Stacking
Train a meta-model on predictions from base models:

```python
from sklearn.ensemble import StackingRegressor

stacking = StackingRegressor(
    estimators=[
        ('rf', RandomForestRegressor(n_estimators=50)),
        ('gbm', GradientBoostingRegressor(n_estimators=50))
    ],
    final_estimator=Ridge()
)
stacking.fit(X, y)
```

**When to ensemble:**
- Models make different types of errors
- You have compute budget
- Every bit of performance matters

**When not to:**
- Early development (too complex)
- Need fast predictions
- Models are too similar (won't help)

## Trading-Specific Considerations

### Transaction Costs
More complex models often trade more frequently. Calculate:

$$\text{Net Sharpe} = \frac{\text{Gross Return} - \text{Costs}}{\text{Volatility}}$$

A simpler model with lower turnover may win.

### Regime Changes
Markets change. Simpler models often generalize better across regimes.

**Strategy:**
- Use simple models for long-term signals
- Use complex models for short-term patterns (retrain frequently)

### Interpretability vs Performance
In trading, understanding why your model works is valuable:
- Helps debug failures
- Builds confidence
- Satisfies regulators/clients

**Rule of thumb:** Use the simplest model that meets your performance target.

## Practical Workflow

1. **Start with linear regression** (or logistic for classification)
   - If Sharpe > 1.0, you might be done
   - Use coefficients to understand what matters

2. **Try Random Forest**
   - Check feature importances
   - If big improvement, continue
   - If not, stick with linear

3. **Try Gradient Boosting** (if Random Forest helped)
   - Tune carefully (easy to overfit)
   - Compare out-of-sample

4. **Consider Neural Networks** (if you have lots of data)
   - Start small (few layers)
   - Compare to boosting

5. **Ensemble top 2-3 models** (if worth the complexity)

**Always:**
- Use walk-forward validation
- Account for transaction costs
- Compare to buy-and-hold baseline

## Common Mistakes

### 1. Starting Too Complex
Neural networks on 500 samples will overfit. Start simple.

### 2. Not Using Regularization
Always use L1/L2 for linear models, depth limits for trees, dropout for neural networks.

### 3. Optimizing Wrong Metric
Accuracy doesn't matter if the model doesn't make money after costs. Optimize Sharpe or PnL.

### 4. Ignoring Model Assumptions
Linear models assume linear relationships. If your data is nonlinear, use trees.

### 5. Trusting Single Train/Test Split
Markets change. Use walk-forward validation across multiple periods.

## Summary

**For most trading problems:**
- **Start:** Linear regression with L1/L2 regularization
- **Next:** Random Forest (if nonlinearity helps)
- **Advanced:** Gradient Boosting (if you have the data)
- **Rare:** Neural networks (unless you have 10,000+ samples or special data types)

**Remember:** A simple model you understand beats a complex model you don't. In trading, the model is just one piece—execution, risk management, and costs matter more.
