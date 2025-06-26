# Housing Price Prediction with Linear Regression

This project demonstrates how to perform linear regression using the `Housing.csv` dataset to predict housing prices. It includes data preprocessing, model training, evaluation, and result visualization.

---

## Dataset

- **File**: `Housing.csv`
- **Target variable**: `price`
- **Features**: Various numerical and categorical housing-related features

---

## Steps Performed

### 1. Import and Preprocess Dataset
- Loaded data using `pandas`
- Encoded categorical variables using `LabelEncoder`
- Scaled numerical features using `StandardScaler`
- Checked and handled missing values (if any)

### 2. Train-Test Split
- Split the dataset into **80% training** and **20% testing** using `train_test_split`

### 3. Linear Regression Model
- Trained a **Linear Regression** model using `sklearn.linear_model.LinearRegression`

### 4. Model Evaluation
Evaluated performance using the following metrics:
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **R² Score** (Coefficient of Determination)

### 5. Visualization & Interpretation
- Plotted a **regression line** for the feature most correlated with `price`
- Displayed and interpreted **model coefficients**

---

## Sample Output

- **MAE**: ~Low = Better accuracy
- **R² Score**: Closer to 1 indicates a better fit
- **Plot**: Shows the linear relationship between the top feature and price

---

##  Libraries Used

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`

---
