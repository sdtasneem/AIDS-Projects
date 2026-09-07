import streamlit as st
import tensorflow as tf
import pandas as pd
import pickle
import os


# Get the folder where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Load trained model
model = tf.keras.models.load_model(
    os.path.join(BASE_DIR, "best_churn_prediction.h5"),
    compile=False
)


# Load scaler
with open(os.path.join(BASE_DIR, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)


# Load selected features
with open(os.path.join(BASE_DIR, "selected_features.pkl"), "rb") as f:
    selected_features = pickle.load(f)


# App title
st.title("📞 Telco Customer Churn Prediction")

st.write(
    "Enter customer details to predict whether the customer is likely to churn."
)


# Customer inputs
tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=100,
    value=34
)

online_security = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=56.96
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1900.0
)


# Convert categorical values to the same factor codes
online_security_code = {
    "No": 0,
    "Yes": 1,
    "No internet service": 2
}[online_security]

contract_code = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}[contract]


# Prediction button
if st.button("🔮 Predict Churn"):

    input_data = pd.DataFrame(
        [[
            tenure,
            online_security_code,
            contract_code,
            monthly_charges,
            total_charges
        ]],
        columns=selected_features
    )

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled, verbose=0)[0][0]

    probability = float(prediction)

    # Same threshold used in your notebook
    churn_status = "Yes" if probability > 0.50 else "No"

    st.write("### Prediction Result")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    if churn_status == "Yes":
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is unlikely to churn")
