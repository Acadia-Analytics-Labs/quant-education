# The Curse of Dimensionality

The **curse of dimensionality** refers to various phenomena that make machine learning harder as the number of features grows. In trading, this manifests as: more indicators ≠ better predictions. Often, it's the opposite.

**The core problem**: In high dimensions, data becomes sparse, distances become meaningless, and models need exponentially more samples to learn anything useful.

## The Problem in Plain Terms

You have 1,000 historical days of data. That sounds like a lot until you try to:
- Use 50 features → only 20 samples per dimension
- Find similar historical patterns → most days look equally "different"
- Estimate probability densities → almost all regions have zero observations

**Result**: Your model overfits to noise because it has no choice. The data is too sparse.

## Mathematical Intuition

### Volume of High-Dimensional Space

Consider a unit hypercube [0, 1]^D in D dimensions. To cover 10% of each dimension, you need to sample:

$$\text{Fraction of volume} = 0.1^D$$

**Examples:**
- 2D: 1% of volume, need 100 points for 1% density
- 5D: 0.001% of volume, need 100,000 points
- 10D: 0.0000000001 of volume, need 100 billion points
- 50D: Essentially 0, need 10^52 points

**Implication**: With 1,000 samples in 50 dimensions, your data is unimaginably sparse.

### Distance Concentration

In high dimensions, all points become approximately equidistant. The ratio of maximum to minimum distances approaches 1:

$$\frac{\text{max distance} - \text{min distance}}{\text{min distance}} \to 0 \text{ as } D \to \infty$$

**Implication**: "Nearest neighbor" searches become meaningless. Everything is equally far away.

### The Empty Space Phenomenon

Most of the volume of a high-dimensional sphere is near its surface. For a sphere with radius reduction $\epsilon$:

$$\frac{\text{inner volume}}{\text{outer volume}} = (1 - \epsilon)^D$$

For $\epsilon = 0.1$ (10% radius reduction):
- 2D: Inner circle has 81% of the area
- 10D: Inner sphere has 35% of the volume  
- 50D: Inner sphere has 0.5% of the volume

**Implication**: Randomly sampled high-dimensional data points are almost all near the boundary of the space, far from the center.

## How This Manifests in Trading

### 1. Feature Explosion

You start with OHLCV data (5 dimensions). Then you add:
- 10 moving averages
- 5 oscillators (RSI, MACD, Stochastic, etc.)
- 3 volatility measures
- 5 volume indicators
- 10 fundamental ratios
- 5 sentiment scores

Now you're in 43 dimensions with maybe 1,000 training samples. **You're doomed.**

### 2. Overfitting Becomes Inevitable

A flexible model (neural net, random forest) will find spurious patterns:
- "When RSI is between 47.3 and 48.1 AND 20-day MA is rising AND volume is..."
- This pattern occurred 3 times in your training set, all before up-moves
- It never occurs again in live trading

**Why it happens**: In high dimensions, any finite sample looks like it has structure, even if it's pure noise.

### 3. Cross-Validation Fails

Your train/test split might both be in weird, unrepresentative regions of the high-dimensional space:
- Train set: clustered in one corner
- Test set: clustered in a different corner
- Live data: in yet another region

**Result**: Good test performance, terrible live performance.

## Sample Size Requirements

The number of samples needed typically grows exponentially with dimensions. A rough heuristic for smooth function approximation:

$$N \approx k^D$$

where $k$ is samples per dimension (5-10 is typical).

**Examples with k=10:**
- 2 dimensions → 100 samples needed
- 5 dimensions → 100,000 samples needed
- 10 dimensions → 10 billion samples needed
- 20 dimensions → 10^20 samples needed (more than atoms in Earth)

**Reality check**: You'll never have this much data. The universe contains approximately 10^80 atoms.

## Practical Strategies to Combat the Curse

### 1. Feature Selection (Reduce $D$)

Only keep features that actually help:

```python
from sklearn.feature_selection import SelectKBest, f_regression

# Keep only top 10 features by F-statistic
selector = SelectKBest(f_regression, k=10)
X_selected = selector.fit_transform(X, y)

# Or use model-based selection
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import SelectFromModel

rf = RandomForestRegressor(n_estimators=100)
selector = SelectFromModel(rf, threshold='median')
X_selected = selector.fit_transform(X, y)
```

**Rule of thumb**: Aim for $N > 10 \times D$ at minimum, preferably $N > 100 \times D$.

### 2. Regularization (Constrain the Model)

Force the model to ignore irrelevant features:

**L1 regularization (Lasso)**: Drives coefficients to exactly zero

$$\text{minimize: } ||y - Xw||^2 + \lambda \sum |w_i|$$

```python
from sklearn.linear_model import Lasso

# L1 regularization for sparse feature selection
model = Lasso(alpha=0.1)  # alpha controls sparsity
model.fit(X, y)

# Check which features were kept
important_features = np.where(model.coef_ != 0)[0]
print(f"Used {len(important_features)} of {X.shape[1]} features")
```

**L2 regularization (Ridge)**: Shrinks coefficients toward zero

$$\text{minimize: } ||y - Xw||^2 + \lambda \sum w_i^2$$

**Elastic Net**: Combines both L1 and L2

### 3. Dimensionality Reduction

Project to a lower-dimensional space (see manifold hypothesis article):
- **PCA**: Linear projection to principal components
- **Autoencoders**: Nonlinear compression
- **Factor models**: Use domain knowledge (Fama-French factors, etc.)

```python
from sklearn.decomposition import PCA

# Reduce from 50 to 10 dimensions
pca = PCA(n_components=10)
X_reduced = pca.fit_transform(X)

# Check how much information you kept
print(f"Variance retained: {pca.explained_variance_ratio_.sum():.2%}")
```

### 4. Domain Knowledge

Use economic intuition to reduce features:
- Don't include both price and log-price
- Don't include RSI-14 and RSI-15 (highly correlated)
- Don't include raw price and returns (use returns only)
- Combine related indicators into factors

### 5. Simpler Models

In high dimensions with limited data:
- Linear models often outperform complex ones
- Decision trees with limited depth beat deep trees
- Ensemble methods with strong regularization (gradient boosting with high learning rate decay)

```python
from sklearn.linear_model import Ridge
from sklearn.ensemble import GradientBoostingRegressor

# Simple linear model often wins in high-D, low-N regime
simple_model = Ridge(alpha=1.0)

# Or gradient boosting with strong regularization
gb_model = GradientBoostingRegressor(
    n_estimators=50,      # Few trees
    max_depth=3,          # Shallow trees
    learning_rate=0.1,    # Slow learning
    subsample=0.5         # Use only half the data per tree
)
```

## The Blessing of Non-Uniformity

Not all hope is lost. Real-world data has structure:

1. **Data lies on manifolds** (see manifold hypothesis article)
2. **Features are correlated** (reduces effective dimensionality)
3. **Sparsity**: Most features are irrelevant for any given prediction
4. **Smoothness**: The true function is smooth, not arbitrary

Modern ML exploits this:
- Deep learning assumes compositional structure
- Kernel methods assume smoothness
- Tree-based methods assume axis-aligned structure

## Distance Metrics in High Dimensions

Euclidean distance becomes less meaningful. Consider alternatives:

### Mahalanobis Distance
Accounts for correlations:

$$d(x, y) = \sqrt{(x - y)^T \Sigma^{-1} (x - y)}$$

where $\Sigma$ is the covariance matrix.

### Cosine Similarity
Focus on direction, not magnitude:

$$\text{similarity}(x, y) = \frac{x \cdot y}{||x|| \cdot ||y||}$$

**Use case**: Finding similar market conditions by feature direction.

## Practical Example: Building a Robust Signal

**Bad approach** (cursed):
```python
# 100 features, 1000 samples → disaster
features = [
    'price', 'log_price', 'returns', 'log_returns',  # redundant
    'sma_5', 'sma_6', ..., 'sma_50',  # 46 correlated features
    'rsi_10', 'rsi_11', ..., 'rsi_20',  # 11 nearly identical
    # ... 40 more indicators
]
X = df[features].values  # shape: (1000, 100)
y = df['future_return'].values

# Complex model on sparse data
model = RandomForestRegressor(n_estimators=1000, max_depth=20)
model.fit(X, y)  # Will overfit spectacularly
```

**Good approach** (curse-aware):
```python
# Start with economically meaningful features
base_features = [
    'returns',           # not price (non-stationary)
    'volume_change',     # relative, not absolute volume
    'volatility_20d',    # single volatility measure
    'rsi_14',           # single momentum measure
    'macd',             # single trend measure
]

# Add fundamental factors if available
if has_fundamentals:
    base_features += ['pe_ratio', 'book_to_market']

# Add regime indicators
base_features += ['vix', 'market_return']

X = df[base_features].values  # shape: (1000, 8-10)
y = df['future_return'].values

# Simple, regularized model
from sklearn.linear_model import ElasticNet
model = ElasticNet(alpha=0.01, l1_ratio=0.5)
model.fit(X, y)

# Check feature importance
for feature, coef in zip(base_features, model.coef_):
    if abs(coef) > 0.001:
        print(f"{feature}: {coef:.4f}")
```

## When More Dimensions Actually Help

The curse isn't absolute. More features help when:

1. **New information**: Each feature adds genuinely independent signal
2. **Large $N$**: You have 100,000+ samples (HFT, crypto)
3. **Strong structure**: Features lie on a low-dimensional manifold
4. **Sparse signals**: You're using L1 regularization to select from a candidate pool

**Example**: Text sentiment from 10,000 words can work if you have millions of data points and use sparse methods.

## Detecting If You're Cursed

Signs you're suffering from dimensionality curse:

1. **Train accuracy >> Test accuracy**: Especially with flexible models
2. **Performance degrades with more features**: Adding data should help, not hurt
3. **Unstable feature importance**: Retraining gives completely different top features
4. **Poor performance on simple baselines**: Can't beat a 3-feature linear model

**Diagnostic**:
```python
# Compare performance vs. number of features
results = []
for n_features in [5, 10, 20, 50, 100]:
    selector = SelectKBest(f_regression, k=n_features)
    X_subset = selector.fit_transform(X, y)
    
    # Walk-forward validation
    score = walk_forward_cv(X_subset, y, model)
    results.append((n_features, score))

# Plot: if score peaks at low n_features, you're cursed
plt.plot([r[0] for r in results], [r[1] for r in results])
plt.xlabel('Number of Features')
plt.ylabel('Out-of-Sample R²')
```

## The Dimensionality-Sample Size Trade-off

A practical guide based on sample count:

**100 samples:**
- Safe: 3-5 dimensions
- Risky: >10 dimensions

**1,000 samples:**
- Safe: 10-15 dimensions
- Risky: >30 dimensions

**10,000 samples:**
- Safe: 20-50 dimensions
- Risky: >100 dimensions

**100,000 samples:**
- Safe: 50-100 dimensions
- Risky: >500 dimensions

**1,000,000 samples:**
- Safe: 100-500 dimensions
- Risky: >1000 dimensions

These assume:
- Moderate feature correlation
- Regularized models
- Proper validation

## Conclusion

The curse of dimensionality is real and especially painful in trading where:
- Sample sizes are limited (markets change, history is short)
- Features are easy to generate (hundreds of technical indicators)
- Overfitting is invisible until you trade live

**Key principles**:
1. **Start simple**: 5-10 thoughtfully chosen features beat 100 random ones
2. **Regularize**: Always use L1/L2 regularization or tree depth limits
3. **Validate properly**: Time-based splits, walk-forward analysis
4. **Use domain knowledge**: Economic intuition > brute force feature search
5. **Monitor dimension vs. sample ratio**: Keep $D/N < 0.1$ as a guideline

When in doubt, remember: **fewer, better features > more, mediocre features**.
