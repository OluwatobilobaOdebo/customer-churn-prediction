import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# -----------------------------
# Paths (project root aware)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent  # from app/ → project root
MODEL_PATH = BASE_DIR / "models" / "churn_logreg.pkl"
DATA_PATH = BASE_DIR / "data" / "processed" / "telco_churn_processed.csv"

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Dashboard",
    layout="wide",
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load(MODEL_PATH)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# -----------------------------
# TAB LAYOUT
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Segment Analysis", "Model Insights", "Predict Churn"])

# ============================================================
# TAB 1 — OVERVIEW (KPIs)
# ============================================================
with tab1:
    st.title("Customer Churn Dashboard")
    st.subheader("Key Metrics")

    # ---------------------------------------------
    # KPI Values (MUST COME FIRST)
    # ---------------------------------------------
    overall_churn = df["Churn"].value_counts(normalize=True)["Yes"] * 100

    month_to_month_churn = (
        df[df["Contract"] == "Month-to-month"]["Churn"]
        .value_counts(normalize=True)
        .get("Yes", 0) * 100
    )

    avg_monthly_churned = df[df["Churn"] == "Yes"]["MonthlyCharges"].mean()
    avg_monthly_retained = df[df["Churn"] == "No"]["MonthlyCharges"].mean()

    # ---------------------------------------------
    # KPI Cards
    # ---------------------------------------------
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="small")
    col1.metric("Overall Churn Rate", f"{overall_churn:.1f}%")
    col2.metric("MTM Churn Rate", f"{month_to_month_churn:.1f}%")
    col3.metric("Avg Charges (Churned)", f"${avg_monthly_churned:.2f}")
    col4.metric("Avg Charges (Retained)", f"${avg_monthly_retained:.2f}")

    # ---------------------------------------------
    # Churn Distribution Chart
    # ---------------------------------------------
    st.markdown("---")
    st.subheader("Churn Distribution")
    churn_counts = df["Churn"].value_counts()
    st.bar_chart(churn_counts)

# ============================================================
# TAB 2 — SEGMENT ANALYSIS
# ============================================================
with tab2:
    st.header("Churn Analysis by Customer Segments")

    # Tenure Group Chart
    tenure_churn = (
        df.groupby("tenure_group")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="ChurnRate")
    )

    st.subheader("Churn Rate by Tenure Group")
    st.bar_chart(tenure_churn.set_index("tenure_group"))

    # Internet Service Chart
    internet_churn = (
        df.groupby("InternetService")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="ChurnRate")
    )

    st.subheader("Churn Rate by Internet Service")
    st.bar_chart(internet_churn.set_index("InternetService"))

    # Payment Method Chart
    payment_churn = (
        df.groupby("PaymentMethod")["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="ChurnRate")
    )

    st.subheader("Churn Rate by Payment Method")
    st.bar_chart(payment_churn.set_index("PaymentMethod"))

# ============================================================
# TAB 3 — MODEL INSIGHTS
# ============================================================
with tab3:
    st.header("Model Comparison")

    comparison_df = pd.DataFrame({
        "Model": ["Logistic Regression", "Random Forest"],
        "Accuracy": [0.7918, 0.7861],
        "Recall": [0.5241, 0.4813],
        "F1 Score": [0.5723, 0.5446],
        "ROC-AUC": [0.8346, 0.8259]
    })

    st.table(comparison_df)

    st.markdown("---")
    st.subheader("Feature Importance (Random Forest)")

    # Load RF importances if you later want (optional)
    st.info("Feature importance chart available in your modeling notebook. Add here if you export the values.")

# ============================================================
# TAB 4 — CHURN PREDICTOR
# ============================================================
with tab4:
    st.header("Customer Churn Risk Calculator")
    st.write("Adjust the inputs to estimate a customer's churn probability.")

    # Inputs
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 150.0, 70.0)
    total_charges = tenure * monthly_charges

    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    payment = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

    online_security = st.selectbox("Online Security", ["Yes", "No"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

    # Predict Button
    if st.button("Predict Churn Risk"):
        input_df = pd.DataFrame([{
            "SeniorCitizen": 0,
            "tenure": tenure,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges,
            "Contract": contract,
            "InternetService": internet,
            "PaymentMethod": payment,
            "OnlineSecurity": online_security,
            "TechSupport": tech_support,
            "gender": "Male",
            "Partner": "No",
            "Dependents": "No",
            "PhoneService": "Yes",
            "MultipleLines": "No",
            "OnlineBackup": "No",
            "DeviceProtection": "No",
            "StreamingTV": "No",
            "StreamingMovies": "No",
            "PaperlessBilling": "Yes",
            "customerID": "0000"
        }])

        # Add tenure_group (required for model)
        if tenure <= 12:
            tg = "0-12"
        elif tenure <= 24:
            tg = "13-24"
        elif tenure <= 48:
            tg = "25-48"
        else:
            tg = "49+"

        input_df["tenure_group"] = tg

        # Predict
        prob = model.predict_proba(input_df)[0][1]
        st.success(f"Estimated Churn Probability: {prob*100:.2f}%")
