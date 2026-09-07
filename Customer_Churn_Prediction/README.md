# 📞 Telco Customer Churn Prediction Using ANN

🚀 **Live Demo:** [Telco Customer Churn Prediction](https://aids-projects-2khphca8l3fkzwjyfuvappn.streamlit.app/)

## 📌 Project Overview

Customer churn is a major challenge for telecom companies. Predicting which customers are likely to leave helps businesses take proactive actions such as offering personalized plans, discounts, and better customer support.

This project uses an **Artificial Neural Network (ANN)** to predict whether a telecom customer is likely to churn based on selected customer attributes.

The trained ANN model is deployed as an interactive **Streamlit web application**, allowing users to enter customer information and receive a churn prediction with probability.

---

## 🎯 Objectives

- Predict whether a customer is likely to churn.
- Build an Artificial Neural Network (ANN) for binary classification.
- Apply preprocessing and feature scaling.
- Save and reuse the trained model.
- Deploy the prediction model using Streamlit.
- Provide an easy-to-use interface for making predictions.

---

## 📊 Dataset

The project uses the **IBM Telco Customer Churn Dataset**.

### 🔗 Dataset Link

The dataset used in the notebook is available here:

👉 **[IBM Telco Customer Churn Dataset](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv)**

### Selected Features

The ANN model uses the following five selected features:

| Feature | Definition |
|---------|------------|
| `tenure` | Number of months the customer has stayed with the telecom company. |
| `OnlineSecurity` | Indicates whether the customer has an online security service, does not have it, or has no internet service. |
| `Contract` | Type of contract chosen by the customer: month-to-month, one year, or two year. |
| `MonthlyCharges` | The amount charged to the customer each month. |
| `TotalCharges` | The total amount charged to the customer over the duration of the service. |

These selected features are used as the input variables for the trained ANN model.

---

## 🧠 Model

An **Artificial Neural Network (ANN)** was developed for binary classification.

The model predicts:

```text
0 → Customer is unlikely to churn
1 → Customer is likely to churn
```

The final prediction is based on a probability threshold of **0.50**.

```text
Probability > 0.50 → Churn: Yes
Probability ≤ 0.50 → Churn: No
```

---

## ⚙️ Preprocessing

The following preprocessing steps were used:

1. Selected relevant features.
2. Converted categorical values into numerical values using factorization.
3. Applied `StandardScaler` to scale the input features.
4. Used the same preprocessing objects during prediction.

The following preprocessing artifacts are saved with the project:

```text
scaler.pkl
selected_features.pkl
```

---

## 📁 Project Structure

```text
Customer_Churn_Prediction/
│
├── app.py
├── best_churn_prediction.h5
├── scaler.pkl
├── selected_features.pkl
├── requirements.txt
├── README.md
└── Telco_Customer_Churn_ANN_Project.ipynb
```

### File Description

| File | Description |
|------|-------------|
| `app.py` | Streamlit application for customer churn prediction |
| `best_churn_prediction.h5` | Trained ANN model |
| `scaler.pkl` | Saved StandardScaler used during preprocessing |
| `selected_features.pkl` | Saved list of model input features |
| `requirements.txt` | Required Python libraries |
| `Telco_Customer_Churn_ANN_Project.ipynb` | Complete model development notebook |
| `README.md` | Project documentation |

---

## 🖥️ Streamlit Application

The Streamlit application allows users to enter:

- **Tenure**
- **Online Security**
- **Contract**
- **Monthly Charges**
- **Total Charges**

After clicking the **Predict Churn** button, the application displays:

- Churn probability
- Whether the customer is likely to churn

### Example

```text
Churn Probability: 6.55%

✅ Customer is unlikely to churn
```

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Jupyter Notebook
- GitHub

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/sdtasneem/AIDS-Projects.git
```

Navigate to the project directory:

```bash
cd AIDS-Projects/Customer_Churn_Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deployment

The Streamlit application is deployed using **Streamlit Community Cloud**.

The application uses:

```text
Repository: sdtasneem/AIDS-Projects
Branch: main
Main file: Customer_Churn_Prediction/app.py
```

### 🌐 Live Application

👉 [Open the Telco Customer Churn Prediction App](https://aids-projects-2khphca8l3fkzwjyfuvappn.streamlit.app/)

---

## 📈 Model Performance

The final tuned ANN model achieved approximately:

```text
Accuracy: 78.68%
Loss: 0.4434
```

---

## 🔄 Project Workflow

```text
IBM Telco Customer Churn Dataset
              ↓
       Data Preprocessing
              ↓
      Feature Selection
              ↓
       Feature Scaling
              ↓
       ANN Model Training
              ↓
       Model Evaluation
              ↓
     Save Model & Artifacts
              ↓
       Streamlit Application
              ↓
      Customer Input
              ↓
      Churn Prediction
```

---

## 💼 Business Use Case

Telecom companies can use customer churn prediction to identify customers who may be at risk of leaving.

The prediction can help businesses:

- Identify high-risk customers.
- Provide personalized offers.
- Improve customer retention.
- Reduce customer acquisition costs.
- Improve customer satisfaction.
- Develop targeted retention strategies.

---

## ⚠️ Note

This project is developed for **educational and demonstration purposes**.

The model's predictions should not be considered as guaranteed outcomes. Model performance depends on the quality and distribution of the data used for training.

---

## 👩‍💻 Author

**Tasneem Syed**

Artificial Intelligence & Data Science

---

⭐ If you find this project useful, consider giving the repository a star!
