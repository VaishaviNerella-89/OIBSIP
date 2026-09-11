# OASIS Infobyte Data Analytics - Task 3
## Data Cleaning

### Objective

The objective of this project is to clean and preprocess a raw dataset
using Python and pandas. The project focuses on identifying and treating
common data quality problems such as missing values, duplicate records,
inconsistent categorical values, incorrect data types, and potential
outliers.

### Dataset

The Titanic dataset was used for this project.

The dataset contains information about passengers, including:

- PassengerId
- Survived
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked

### Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

### Data Quality Checks

The following checks were performed:

1. Dataset shape and column names
2. Missing values
3. Duplicate rows
4. Data types
5. Unique values
6. Numerical value ranges
7. Potential outliers

### Missing Value Handling

#### Age

Missing Age values were replaced using the median because Age is a
numerical variable and the median is less affected by extreme values.

#### Embarked

Missing Embarked values were replaced using the mode because Embarked is
a categorical variable.

#### Cabin

Missing Cabin values were replaced with `Unknown` to preserve passenger
records while clearly indicating unavailable cabin information.

### Duplicate Removal

Duplicate rows were checked using pandas `duplicated()`.

Exact duplicate records were removed using `drop_duplicates()`.

The source dataset contained no exact duplicate rows, so no records were
removed during this step.

### Data Standardization

Categorical values were standardized to maintain consistent formatting.

- Sex values were stripped of extra spaces and converted to title case.
- Embarked values were stripped of extra spaces and converted to uppercase.

The source Titanic dataset already contained largely consistent
categorical values, so this step was used as a validation and
normalization process.

### Data Type Correction

Numerical columns were validated and converted using `pd.to_numeric()`.

Categorical columns such as Sex, Embarked and Cabin were converted to
string types.

### Outlier Detection

The IQR (Interquartile Range) method was used to detect potential
outliers in numerical columns such as Age and Fare.

Potential outliers were reviewed rather than automatically deleted.
Extreme Fare values may represent legitimate passenger or ticket
characteristics.

### Before vs After Comparison

The dataset was compared before and after cleaning using:

- Total null values
- Duplicate rows
- Total number of rows
- Data types

### Output

The cleaned dataset was saved as:

`data/cleaned_titanic.csv`

### Project Structure

```text
DataAnalytics-L1-CleaningData
│
├── data
│   ├── train.csv
│   └── cleaned_titanic.csv
│
├── screenshots
│   ├── outlier_detection.png
│   ├── before_after_summary.png
│   └── final_quality_check.png
│
├── Data_Cleaning.ipynb
└── README.md