# Mall Customer Segmentation using K-Means Clustering

This project demonstrates how to perform **unsupervised customer segmentation** using the **K-Means clustering** algorithm on mall customer data. The pipeline includes data preprocessing, cluster modeling, dimensionality reduction for visualization, and evaluation using the **Silhouette Score**.

---

## Dataset

- **File**: `Mall_Customers.csv`
- **Features**: Includes numeric features like Age, Annual Income, Spending Score, etc.
- **Goal**: Identify meaningful customer groups (segments) based on behavior.

---

## Tasks Performed

### 1. Load and Preprocess Dataset
- Loaded data using `pandas`
- Removed non-numeric or identifier columns
- Scaled features using `StandardScaler` for uniform clustering behavior

### 2. Dimensionality Reduction
- Applied **PCA** to reduce data to 2 components for easier visualization

### 3. K-Means Clustering
- Fitted `KMeans` model with a default of 5 clusters
- Assigned cluster labels to each customer
- Added cluster column back to the original DataFrame

### 4. Elbow Method for Optimal K
- Plotted inertia vs. K to identify the "elbow" point
- Helps in selecting the best number of clusters visually

### 5. Cluster Visualization
- Visualized customer clusters in 2D PCA space
- Color-coded scatter plot for intuitive grouping

### 6. Clustering Evaluation
- Evaluated the clustering performance using the **Silhouette Score**

---

## Outputs

- Elbow Plot showing optimal K value
- Cluster visualization in PCA-reduced 2D space
- Silhouette Score to measure how well-separated clusters are
