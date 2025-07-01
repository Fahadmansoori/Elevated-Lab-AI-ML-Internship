# Iris Dataset Classification with K-Nearest Neighbors (KNN)

This project demonstrates classification using the **K-Nearest Neighbors (KNN)** algorithm on the classic **Iris dataset**. It includes normalization, model training, evaluation, and decision boundary visualization.

---

## Dataset

- **File**: `Iris.csv`
- **Target Variable**: `Species` (Setosa, Versicolor, Virginica)
- **Features**: Sepal and petal length/width

---

## Tasks Performed

### 1. Load & Preprocess Dataset
- Dropped `Id` column
- Encoded target labels using `LabelEncoder`
- Normalized features using `StandardScaler`

### 2. Train/Test Split
- Split data into **80% training** and **20% testing**

### 3. KNN Classification
- Used `KNeighborsClassifier` from Scikit-learn
- Trained and evaluated models with multiple **K values**: 1, 3, 5, 7
- Printed **accuracy** and **confusion matrices**

### 4. Visualization
- Used only first two features for 2D visualization
- Plotted **decision boundaries** using a custom function
- Colored regions indicate predicted class zones

---

## Outputs

- Accuracy and confusion matrix for each K value
- A visual representation of **decision regions** in 2D space
- Helps in understanding how different K values affect classification
