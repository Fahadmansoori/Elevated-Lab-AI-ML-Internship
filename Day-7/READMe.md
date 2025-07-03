# Breast Cancer Classification using SVM

This project demonstrates how to build and evaluate a **Support Vector Machine (SVM)** model for binary classification on a breast cancer dataset. The pipeline includes data preprocessing, model training (linear & RBF kernels), decision boundary visualization, hyperparameter tuning, and cross-validation.

---

## Dataset

- **File**: `breast-cancer.csv`
- **Target Variable**: `target` (binary classification: 0 = benign, 1 = malignant)
- **Features**: Various numerical medical indicators

---

## Tasks Performed

### 1. Data Preparation
- Loaded dataset using `pandas`
- Encoded categorical target (if applicable)
- Normalized features using `StandardScaler`

### 2. SVM Training
- Trained SVM with **linear kernel**
- Trained SVM with **RBF kernel**
- Used first two features to visualize **decision boundaries**

### 3. Decision Boundary Visualization
- Visualized model decision regions in 2D
- Used `matplotlib` to display how each kernel separates classes

### 4. Hyperparameter Tuning
- Used `GridSearchCV` to tune:
  - `C`: Regularization parameter
  - `gamma`: RBF kernel coefficient
- Evaluated model using **cross-validation accuracy**

### 5. Final Evaluation
- Selected best SVM model
- Evaluated using:
  - Accuracy
  - Confusion matrix
  - Classification report
