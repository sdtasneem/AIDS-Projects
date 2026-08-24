
import streamlit as st
import pandas as pd
import pickle

# Load saved files
with open("paysentinel_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("paysentinel_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

with open("paysentinel_feature_info.pkl", "rb") as f:
    feature_info = pickle.load(f)

features = feature_info["features"]
categorical_cols = feature_info["categorical_cols"]

st.set_page_config(
    page_title="PaySentinel",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PaySentinel")
st.subheader("AI-Powered Payment Risk Intelligence")

st.divider()

st.header("Transaction Details")

col1, col2 = st.columns(2)

with col1:
    step = st.number_input(
        "Step",
        min_value=0,
        value=1
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
    )

    branch = st.selectbox(
        "Branch",
        ["India", "Japan", "Australia", "Mexico", "Cuba", "Panama"]
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    oldbalanceOrg = st.number_input(
        "Old Origin Balance",
        min_value=0.0,
        value=5000.0
    )

    newbalanceOrig = st.number_input(
        "New Origin Balance",
        min_value=0.0,
        value=4000.0
    )

with col2:
    oldbalanceDest = st.number_input(
        "Old Destination Balance",
        min_value=0.0,
        value=1000.0
    )

    newbalanceDest = st.number_input(
        "New Destination Balance",
        min_value=0.0,
        value=2000.0
    )

    unusual_login = st.selectbox(
        "Unusual Login",
        [0, 1]
    )

    flagged_fraud = st.selectbox(
        "Flagged Fraud",
        [0, 1]
    )

    acct_type = st.selectbox(
        "Account Type",
        ["Savings"]
    )

    time_of_day = st.selectbox(
        "Time of Day",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

st.divider()

if st.button("🔍 Analyze Transaction", use_container_width=True):

    input_data = pd.DataFrame([{
        "step": step,
        "type": transaction_type,
        "branch": branch,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "unusuallogin": unusual_login,
        "isFlaggedFraud": flagged_fraud,
        "Acct type": acct_type,
        "Time of day": time_of_day
    }])

    input_data = input_data[features]

    input_data[categorical_cols] = encoder.transform(
        input_data[categorical_cols]
    )

    prediction = model.predict_proba(input_data)[0]

    probability = prediction[1]

    risk_score = round(probability * 100, 2)

    if risk_score < 30:
        risk_level = "LOW"
        decision = "APPROVE"

    elif risk_score < 70:
        risk_level = "MEDIUM"
        decision = "REVIEW"

    else:
        risk_level = "HIGH"
        decision = "BLOCK"

    st.divider()

    st.header("Risk Analysis")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with c2:
        st.metric(
            "Risk Level",
            risk_level
        )

    with c3:
        st.metric(
            "Decision",
            decision
        )

    if decision == "APPROVE":
        st.success(" Transaction Approved")

    elif decision == "REVIEW":
        st.warning("Transaction Requires Manual Review")

    else:
        st.error(" Transaction Blocked")

    st.info(
        f"Fraud probability predicted by the model: {probability:.2%}"
    )
