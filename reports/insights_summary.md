# Customer Churn Prediction — Insights Summary

## 1. Key KPIs

- **Overall churn rate:** 26.54%  
  (1,869 churned out of 7,043 customers)
- **Tenure distribution:**
  - 0–12 months: 2,175 customers
  - 13–24 months: 1,024 customers
  - 25–48 months: 1,594 customers
  - 49+ months: 2,239 customers

---

## 2. Logistic Regression Performance

- Accuracy: 0.7918
- Precision: 0.6302
- Recall: 0.5241
- F1 Score: 0.5723
- ROC–AUC: 0.8346

**Summary:**  
Logistic Regression performs well overall, achieving strong ROC–AUC and balanced classification metrics. Recall is moderate, meaning it identifies a fair portion of churners but still misses some.

---

## 3. Random Forest Performance

- Accuracy: 0.7861
- Precision: 0.6272
- Recall: 0.4813
- F1 Score: 0.5446
- ROC–AUC: 0.8259

**Summary:**  
Random Forest underperforms Logistic Regression across all metrics, including recall and ROC–AUC. Logistic Regression is the better-performing model for this dataset.

---

## 4. Top Churn Drivers (Random Forest Feature Importance)

The most influential features predicting churn were:

1. TotalCharges
2. Tenure
3. MonthlyCharges
4. Contract: Month-to-month
5. Tenure group: 0–12 months
6. PaymentMethod: Electronic check
7. OnlineSecurity: No
8. TechSupport: No
9. InternetService: Fiber optic
10. OnlineBackup: No

**Summary:**  
Customers with high charges, short tenure, insecure service packages, month-to-month contracts, and electronic check payments are the most likely to churn.

---

## 5. Business Recommendations

Based on the model results and feature importance:

- Incentivize month-to-month customers to switch to longer-term contracts.
- Focus retention efforts on new customers (tenure < 12 months).
- Review pricing or service quality for fiber-optic subscribers.
- Improve security/support add-ons such as OnlineSecurity and TechSupport.
- Investigate the electronic check payment experience, which correlates with higher churn.
