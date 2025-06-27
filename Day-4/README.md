# Binary Classification with Logistic Regression

This project demonstrates a complete binary classification pipeline using **Logistic Regression**. It includes preprocessing, model training, evaluation with key metrics, and threshold tuning with a sigmoid explanation.

---

## Dataset

- **File**: `data.csv`
- **Target**: Binary classification (assumed to be the last column)
- **Features**: Mixture of numerical and categorical variables

---

## Tasks Performed

### 1. Data Preprocessing
- Loaded dataset using `pandas`
- Handled categorical variables using `LabelEncoder`
- Checked and handled missing values
- Split data into **features (X)** and **target (y)**

### 2. Train-Test Split
- Split the dataset into training (80%) and testing (20%) sets

### 3. Feature Standardization
- Scaled features using `StandardScaler` for improved model performance

### 4. Logistic Regression Model
- Trained a `LogisticRegression` model from `sklearn`
- Predicted class probabilities and binary outcomes

### 5. Evaluation
- **Confusion Matrix**
- **Precision & Recall**
- **ROC-AUC Score**
- **Classification Report**
- **ROC Curve Visualization**

### 6. Threshold Tuning & Sigmoid Explanation
- Plotted **precision and recall** against various thresholds
- Explained how the **sigmoid function** is used to convert raw scores into probabilities and how threshold affects predictions

---

## Output Insights

- Evaluate trade-offs between **precision** and **recall**
- Visualize **ROC Curve** to understand classification performance
- Customize decision threshold to suit domain-specific needs

---

## Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

