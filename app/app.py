import streamlit as st
import pandas as pd
import joblib

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")
feature_names = joblib.load("models/feature_names.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:

    st.title("📊 Customer Churn")

    st.markdown("---")

    st.write("### Model")
    st.success("Logistic Regression")

    st.write("### Dataset")
    st.info("Telco Customer Churn")

    st.write("### Features")
    st.info("30 Features")

    st.write("### Accuracy")
    st.success("78.68%")

    st.write("### ROC-AUC")
    st.success("0.70")

    st.markdown("---")

    st.caption("Developed by Vivek Poonia & Keshav Sharma")

st.title("📊 Customer Churn Prediction")
st.write("Predict whether a telecom customer is likely to churn.")

st.header("Customer Information")

left, right = st.columns(2)

with left:

    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0
    )

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes", "No phone service"]
    )
    
with right:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )

    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


if st.button("Predict Churn"):

    input_data = {feature: 0 for feature in feature_names}
    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly_charges
    input_data["TotalCharges"] = total_charges
    input_data["SeniorCitizen"] = senior_citizen
    
    if gender == "Male":
        input_data["gender_Male"] = 1

    if partner == "Yes":
        input_data["Partner_Yes"] = 1

    if dependents == "Yes":
        input_data["Dependents_Yes"] = 1

    if phone_service == "Yes":
        input_data["PhoneService_Yes"] = 1
        
        # Gender
    if gender == "Male":
        input_data["gender_Male"] = 1

    # Partner
    if partner == "Yes":
        input_data["Partner_Yes"] = 1

    # Dependents
    if dependents == "Yes":
        input_data["Dependents_Yes"] = 1

    # Phone Service
    if phone_service == "Yes":
        input_data["PhoneService_Yes"] = 1

    # Multiple Lines
    if multiple_lines == "Yes":
        input_data["MultipleLines_Yes"] = 1
    elif multiple_lines == "No phone service":
        input_data["MultipleLines_No phone service"] = 1

    # Internet Service
    if internet_service == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1
    elif internet_service == "No":
        input_data["InternetService_No"] = 1

    # Online Security
    if online_security == "Yes":
        input_data["OnlineSecurity_Yes"] = 1
    elif online_security == "No internet service":
        input_data["OnlineSecurity_No internet service"] = 1

    # Online Backup
    if online_backup == "Yes":
        input_data["OnlineBackup_Yes"] = 1
    elif online_backup == "No internet service":
        input_data["OnlineBackup_No internet service"] = 1

    # Device Protection
    if device_protection == "Yes":
        input_data["DeviceProtection_Yes"] = 1
    elif device_protection == "No internet service":
        input_data["DeviceProtection_No internet service"] = 1

    # Tech Support
    if tech_support == "Yes":
        input_data["TechSupport_Yes"] = 1
    elif tech_support == "No internet service":
        input_data["TechSupport_No internet service"] = 1

    # Streaming TV
    if streaming_tv == "Yes":
        input_data["StreamingTV_Yes"] = 1
    elif streaming_tv == "No internet service":
        input_data["StreamingTV_No internet service"] = 1

    # Streaming Movies
    if streaming_movies == "Yes":
        input_data["StreamingMovies_Yes"] = 1
    elif streaming_movies == "No internet service":
        input_data["StreamingMovies_No internet service"] = 1

    # Contract
    if contract == "One year":
        input_data["Contract_One year"] = 1
    elif contract == "Two year":
        input_data["Contract_Two year"] = 1

    # Paperless Billing
    if paperless_billing == "Yes":
        input_data["PaperlessBilling_Yes"] = 1

    # Payment Method
    if payment_method == "Credit card (automatic)":
        input_data["PaymentMethod_Credit card (automatic)"] = 1
    elif payment_method == "Electronic check":
        input_data["PaymentMethod_Electronic check"] = 1
    elif payment_method == "Mailed check":
        input_data["PaymentMethod_Mailed check"] = 1
        
        # Create DataFrame
    input_df = pd.DataFrame([input_data])

    # Scale numerical columns
    numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges"]

    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Prediction
    prediction = model.predict(input_df)[0]

    # Prediction probability
    probability = model.predict_proba(input_df)[0][1]

    st.markdown("---")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error("## ⚠️ High Churn Risk")
        else:
            st.success("## ✅ Customer Will Stay")

    with col2:

        st.metric(
            label="Churn Probability",
            value=f"{probability:.2%}"
        )

    st.progress(float(probability))

    st.markdown("---")
    
    
    with st.expander("View Encoded Customer Features"):
        st.dataframe(input_df)

    st.markdown("---")
    
    st.subheader("Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "Logistic Regression")

    with col2:
        st.metric("Accuracy", "78.68%")

    with col3:
        st.metric("ROC-AUC", "0.70")
            
    st.markdown("---")

    st.caption(
        "Built using Streamlit • Scikit-learn • SHAP • Logistic Regression"
    )