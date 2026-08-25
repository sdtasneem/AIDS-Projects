# PaySentinel

## Payment Fraud Detection

PaySentinel is a machine-learning project developed to identify potentially fraudulent payment transactions. It analyzes transaction details, predicts the probability of fraud, and converts the prediction into a simple risk score and transaction decision.

## Objective

The main objective is to detect suspicious transactions and provide an easy way to understand the level of risk associated with each transaction.

## How It Works

The transaction data is first cleaned and prepared for modelling. Since fraudulent transactions are much fewer than normal transactions, SMOTENC is used to handle the class imbalance. A Random Forest classifier is then trained to predict the probability of fraud.

The predicted probability is converted into a risk score from 0 to 100. The system then assigns a risk level and recommends an action.

## Risk Levels

**LOW (0–29):** Approve the transaction

**MEDIUM (30–69):** Send the transaction for review

**HIGH (70–100):** Block the transaction

## Technologies Used

Python, Pandas, NumPy, Scikit-learn, SMOTENC, Random Forest, Streamlit and Pickle.

## Application

The Streamlit application provides a simple interface where transaction details can be entered and the user can view the fraud probability, risk score, risk level and recommended decision.

## Live Streamlit Application

[Click here to open PaySentinel](https://twilight-frigidity-nervous.ngrok-free.dev)

> **Note:** This is a temporary ngrok link and will work only while the corresponding Colab and Streamlit session is running.
## Sample Prediction Screenshots

The following PDF files contain screenshots of PaySentinel prediction examples:

- [PaySentinel _example1_Screenshots.pdf](PaySentinel%20_example1_Screenshots.pdf)
- [PaySentinel _example2_Screenshots.pdf](PaySentinel%20_example2_Screenshots.pdf)
- [PaySentinel _example3_Screenshots.pdf](PaySentinel%20_example3_Screenshots.pdf)


## Project Files

```text
paysentinel.ipynb
app.py
paysentinel_model.pkl
paysentinel_encoder.pkl
paysentinel_feature_info.pkl
requirements.txt
README.md
```

## Conclusion

PaySentinel combines machine learning with a simple risk-based decision system to make payment fraud detection easier to understand and demonstrate.
