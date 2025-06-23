# Titanic Dataset Preprocessing

This project performs essential data preprocessing steps on the Titanic dataset to prepare it for machine learning analysis.

## Dataset
- Source: `Titanic-Dataset.csv` (Kaggle Titanic dataset)

## Steps Performed

1. **Data Import & Exploration**
   - Loaded the dataset using `pandas`
   - Displayed basic info, data types, and missing values

2. **Missing Value Handling**
   - `Age`: Filled with median
   - `Embarked`: Filled with mode
   - `Cabin`: Dropped due to excessive missing data

3. **Categorical Encoding**
   - Converted `Sex` and `Embarked` into numerical format using `LabelEncoder`

4. **Feature Scaling**
   - Standardized numerical features (`Age`, `Fare`, `SibSp`, `Parch`) using `StandardScaler`

5. **Outlier Detection & Removal**
   - Visualized outliers using seaborn boxplots
   - Removed outliers using the IQR method

## Libraries Used
- pandas
- sklearn
- seaborn
- matplotlib

## Output
- Cleaned and standardized dataset, ready for training machine learning models.
