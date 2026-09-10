# Customer Segmentation Analysis

## OASIS Infobyte - Data Analytics Level 1 - Task 2

## Project Overview

Customer segmentation is the process of dividing customers into groups
based on their purchasing behaviour.

This project analyzes customer transaction data and uses RFM analysis
and K-Means clustering to identify different customer segments.

The three RFM metrics used are:

- Recency: How recently a customer made a purchase.
- Frequency: How often a customer makes purchases.
- Monetary: How much a customer spends.

The identified customer segments can help businesses develop targeted
marketing and customer retention strategies.

---

## Objective

The main objectives of this project are:

1. Analyze customer purchasing behaviour.
2. Calculate Recency, Frequency, and Monetary metrics.
3. Calculate descriptive statistics.
4. Standardize the RFM features.
5. Determine a suitable number of clusters using the Elbow Method.
6. Apply K-Means clustering.
7. Visualize customer segments.
8. Profile the identified customer groups.
9. Develop marketing recommendations for each segment.

---

## Dataset

The project uses the UCI Online Retail dataset.

The dataset contains transactional records from a UK-based online
retailer.

Important columns include:

- InvoiceNo
- StockCode
- Description
- Quantity
- InvoiceDate
- UnitPrice
- CustomerID
- Country

Dataset source:

UCI Machine Learning Repository - Online Retail Dataset

https://archive.ics.uci.edu/dataset/352/online%2Bretail

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

## Methodology

### 1. Data Cleaning

The dataset was cleaned by:

- Removing duplicate records.
- Removing transactions with missing CustomerID.
- Removing cancelled invoices.
- Removing invalid quantities.
- Removing invalid unit prices.
- Converting InvoiceDate into datetime format.

A new TotalAmount column was calculated using:

Quantity × UnitPrice

---

### 2. RFM Analysis

Customer-level RFM metrics were calculated.

#### Recency

Measures the number of days since the customer's most recent
purchase.

#### Frequency

Measures the number of unique invoices associated with the customer.

#### Monetary

Measures the total amount spent by the customer.

---

### 3. Customer Lifetime Value

A simple historical spending value was used as a Customer Lifetime Value
proxy.

This represents the customer's historical monetary contribution and is
not a forecast of future customer value.

---

### 4. Feature Standardization

The RFM features were standardized using StandardScaler.

This ensures that features with different numerical scales can be used
fairly by the clustering algorithm.

---

### 5. Elbow Method

The Elbow Method was used to determine a suitable number of clusters.

The analysis identified **4 clusters** as a suitable choice.

---

### 6. K-Means Clustering

K-Means clustering was applied with:

- Number of clusters: 4
- Random state: 42
- n_init: 10

The algorithm grouped customers according to similarities in their RFM
characteristics.

---

## Customer Segments

The four identified customer groups were interpreted using their average
RFM values.

### Cluster 0 - Regular / Moderate-Value Customers

These customers show moderate purchasing activity and spending.

Recommended strategies:

- Loyalty programs.
- Personalized offers.
- Bundle promotions.
- Cross-selling.
- Product recommendations.

### Cluster 1 - At-Risk / Low-Value Customers

These customers have not purchased for a long time and have relatively
low frequency and spending.

Recommended strategies:

- Re-engagement emails.
- Personalized discounts.
- Limited-time offers.
- Product reminders.

### Cluster 2 - High-Value Customers

These customers purchase very recently, purchase frequently, and have
very high spending.

Recommended strategies:

- VIP rewards.
- Exclusive offers.
- Early access to products.
- Personalized recommendations.
- Customer retention campaigns.

### Cluster 3 - Loyal / Valuable Customers

These customers purchase recently and relatively frequently and have
strong monetary value.

Recommended strategies:

- Loyalty points.
- Special promotions.
- Personalized recommendations.
- Bundle offers.
- Repeat-purchase campaigns.

---

## Visualizations

The project includes:

- Recency distribution.
- Purchase frequency distribution.
- Monetary value distribution.
- Elbow Method graph.
- Number of customers per cluster.
- Recency vs Monetary scatter plot.
- Frequency vs Monetary scatter plot.
- Recency vs Frequency scatter plot.
- Customer cluster profile.

---

## Key Insights

1. Customer purchasing behaviour differs across the identified clusters.

2. Recency helps identify customers who have recently interacted with
   the business.

3. Frequency identifies customers who purchase repeatedly.

4. Monetary value identifies customers who contribute more revenue.

5. Cluster 2 represents the highest-value customer group.

6. Cluster 1 represents an at-risk group because customers have not
   purchased recently and have relatively low spending.

7. K-Means clustering successfully groups customers with similar
   purchasing behaviour.

8. Customer segmentation can support targeted marketing, retention,
   loyalty, and re-engagement strategies.

---

## Project Structure

```text
DataAnalytics-L1-CustomerSegmentation/
│
├── data/
│   └── Online Retail.csv
│
├── screenshots/
│   ├── monetary_distribution.png
│   ├── elbow_method.png
│   ├── final_cluster_profile.png
│   ├── customers_per_cluster.png
│   ├── cluster_scatter_recency_monetary.png
│   ├── cluster_scatter_frequency_monetary.png
│   └── cluster_scatter_recency_frequency.png
│
├── Customer_Segmentation.ipynb
├── RFM_Customer_Data.csv
├── RFM_Customer_Segments.csv
└── README.md