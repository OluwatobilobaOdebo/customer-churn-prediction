# Customer Churn Prediction

This project analyzes telecom customer behavior to identify drivers of churn and predict which customers are at risk of leaving using machine learning models. It includes a full analytics workflow: exploratory data analysis (EDA), feature engineering, model development, and an interactive Streamlit dashboard for visualization and real-time churn prediction.

---

## Project Overview

Customer churn is a critical metric for subscription-based businesses. Reducing churn directly increases profitability by improving retention and lowering customer acquisition costs.

This project uses the **Telco Customer Churn dataset** to:

- Understand key patterns that influence customer churn  
- Analyze customer behavioral and demographic segments  
- Build machine learning models to predict churn  
- Deploy an interactive Streamlit application for dashboards and customer-level risk scoring  

The final solution supports data-driven retention strategies and enables proactive churn management.

---

## Features

### **1. Exploratory Data Analysis (EDA)**
- Churn distribution  
- Customer segmentation (tenure, contract type, internet service, payment method)  
- Revenue and billing behavior analysis  
- Visualizations of key churn drivers  

### **2. Data Processing & Feature Engineering**
- Handling missing or inconsistent values  
- Creating `tenure_group` categories  
- Encoding categorical variables  
- Scaling numeric variables  
- Preparing final modeling dataset  

### **3. Machine Learning Models**
Two predictive models are built and evaluated:

| Model | Accuracy | Recall | F1 Score | ROC-AUC |
|-------|----------|--------|----------|---------|
| Logistic Regression | ~0.79 | ~0.52 | ~0.57 | ~0.83 |
| Random Forest | ~0.78 | ~0.48 | ~0.54 | ~0.82 |

Logistic Regression outperforms in recall and overall generalization.

### **4. Interactive Streamlit App**
Includes:

#### **Overview Dashboard**
- Overall churn rate  
- Month-to-month churn rate  
- Average charges (churned vs. retained)  
- Churn distribution chart  

#### **Segment Analysis**
- Churn by tenure group  
- Churn by internet service type  
- Churn by payment method  

#### **Model Insights**
- Side-by-side model performance comparison  
- Discussion of feature importance  

#### **Churn Risk Prediction**
A simple interface allowing users to input customer characteristics and generate a predicted churn probability.

---

## Dataset Description

The project uses the **Telco Customer Churn dataset**, which contains:

### **Customer Demographics**
- `customerID`  
- `gender`  
- `SeniorCitizen`  
- `Partner`, `Dependents`

### **Account Information**
- `tenure`  
- `Contract` (Month-to-month, One year, Two year)  
- `PaymentMethod`  
- `PaperlessBilling`

### **Services Opted Into**
- `PhoneService`, `MultipleLines`  
- `InternetService`  
- `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`  
- `StreamingTV`, `StreamingMovies`  

### **Billing Information**
- `MonthlyCharges`  
- `TotalCharges`

### **Target Variable**
- `Churn` — indicates whether the customer left ("Yes") or stayed ("No").

Data was cleaned and engineered, including:
- Creating `tenure_group`
- Encoding categorical features
- Handling missing values
- Preparing the dataset for model training

---
