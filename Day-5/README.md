# Heart Disease Prediction using Decision Tree and Random Forest

This project builds and evaluates two classification models—**Decision Tree** and **Random Forest**—on a heart disease dataset. It includes visualizing the decision tree using **Graphviz**, analyzing overfitting, comparing model accuracy, interpreting feature importances, and performing cross-validation.

---

## Dataset

- **File**: `heart.csv`
- **Target Variable**: `target` (1 = heart disease, 0 = no disease)
- **Features**: Various patient health indicators (age, cholesterol, etc.)

---

## Tasks Performed

### 1. Load and Preprocess Dataset
- Read CSV using `pandas`
- Separated features and target
- Standardized features using `StandardScaler`

### 2. Train and Visualize Decision Tree
- Trained a `DecisionTreeClassifier`
- Exported and rendered tree using **Graphviz**
- Saved tree visualization as `decision_tree_heart.png`

### 3. Analyze Overfitting
- Trained decision trees with varying depths
- Plotted **train/test accuracy** vs. **tree depth**

### 4. Train Random Forest & Compare Accuracy
- Trained a `RandomForestClassifier`
- Compared evaluation metrics with Decision Tree

### 5. Feature Importances
- Plotted top features influencing heart disease prediction

### 6. Cross-Validation
- Performed **5-fold cross-validation** for both models
- Reported average accuracy scores

---

## Libraries Used

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `graphviz` (for tree visualization)

---

## Insights

- Random Forest outperforms a single Decision Tree in both test accuracy and stability (CV score).
- Features like **thalach**, **cp**, and **exang** are strong predictors.
- Tree depth tuning helps reduce overfitting and improve generalization.

---
