# Exploratory Data Analysis on Retail Sales Data

## OASIS Infobyte – Data Analytics Level 1 – Task 1

### Project Objective

The objective of this project is to perform Exploratory Data Analysis (EDA) on retail sales data to identify sales patterns, customer behaviour, product category performance, and useful business insights.

### Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

### Dataset

The project uses the Customer Shopping Dataset – Retail Sales Data.

The dataset contains information such as:

- Invoice number
- Customer ID
- Gender
- Age
- Product category
- Quantity
- Price
- Payment method
- Invoice date
- Shopping mall

### Analysis Performed

The following analysis was performed:

1. Dataset loading and initial inspection
2. Dataset shape and column information
3. Data type inspection
4. Missing-value analysis
5. Mean, median, mode and standard deviation
6. Monthly sales trend
7. Quarterly sales trend
8. Customer age-group distribution
9. Gender breakdown
10. Product category sales analysis
11. Revenue by product category
12. Correlation analysis using a heatmap
13. Revenue by payment method
14. Revenue by shopping mall
15. Key business findings and recommendations

### Business Recommendations

Based on the analysis:

- Maintain sufficient inventory for high-performing categories.
- Use customer demographic information for targeted marketing.
- Plan inventory based on monthly and quarterly sales trends.
- Study high-performing shopping malls to improve lower-performing locations.
- Support commonly used payment methods.
- Use data-driven promotional strategies.

### Project Structure

```text
DataAnalytics-L1-EDARetailSales/
│
├── data/
│   └── customer_shopping_data.csv
│
├── screenshots/
│   ├── best_selling_products.png
│   ├── customer_agegroup_diastribution.png
│   ├── dataset_statistics.png
│   ├── monthly_sales.png
│   └── revenue _by_shoppingmall.png
│
├── EDA_Retail_Sales.ipynb
└── README.md