# Telco Customer Churn Prediction using ANN

## About the Project

This project is about predicting customer churn in a telecom company.

Customer churn means a customer stops using the company's services. The main aim of this project is to use the customer's information and predict whether the customer is likely to leave the service or not.

For this project, I used an Artificial Neural Network (ANN) for the prediction.

## Dataset

I used the IBM Telco Customer Churn dataset.

The dataset contains information about telecom customers, including:

- Customer gender
- Senior citizen status
- Partner and dependents
- Tenure
- Phone service
- Internet service
- Online security
- Online backup
- Device protection
- Technical support
- Streaming services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Churn

The target column is `Churn`.

- `Yes` means the customer has churned.
- `No` means the customer has not churned.

## What I Did in This Project

The project was completed in the following steps:

1. Loaded the dataset using Pandas.
2. Checked the dataset and its columns.
3. Cleaned the data and handled missing values.
4. Converted categorical values into numerical values.
5. Removed duplicate records.
6. Selected important features using Recursive Feature Elimination (RFE).
7. Used Random Forest feature importance to understand the important features.
8. Split the data into training and testing sets.
9. Scaled the selected features using StandardScaler.
10. Built an Artificial Neural Network using TensorFlow and Keras.
11. Trained the ANN model.
12. Checked the training and validation performance.
13. Used Keras Tuner to find better ANN hyperparameters.
14. Used Early Stopping during training.
15. Evaluated the final model using the test data.
16. Saved the trained model and preprocessing objects.
17. Created a function to predict churn for a new customer.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TensorFlow
- Keras
- Keras Tuner
- Google Colab

## Model

The main model used in this project is an Artificial Neural Network.

The ANN contains dense layers and uses:

- ReLU activation in the hidden layers
- Sigmoid activation in the output layer
- Adam optimizer
- Binary cross-entropy loss
- Accuracy as the evaluation metric

Since churn prediction is a binary classification problem, the final output represents the probability that a customer will churn.

## Feature Selection

I used Recursive Feature Elimination (RFE) with a Random Forest classifier to select the most useful features for the ANN.

This helps reduce the number of input features and focuses the model on the features that are more useful for predicting churn.

## Hyperparameter Tuning

Keras Tuner was used to try different ANN configurations.

The tuning process was used to find suitable values for the number of neurons and the network structure.

Early Stopping was also used to stop training when the validation loss stopped improving.

## Prediction

After training the model, a prediction function was created.

The function takes the selected customer information as input, applies the same scaling used during training, and returns the churn probability and predicted churn status.

## Project Files

```text
Telco-Customer-Churn-ANN/
│
├── Telco_Customer_Churn_ANN_Project.ipynb
├── README.md
├── best_churn_prediction.h5
├── scaler.pkl
└── selected_features.pkl
```

The `.h5` file contains the trained ANN model.

The `scaler.pkl` file contains the scaler used during preprocessing.

The `selected_features.pkl` file contains the features selected for the model.

## How to Run

1. Open the notebook in Google Colab or Jupyter Notebook.
2. Install the required Python libraries.
3. Run the notebook cells from beginning to end.
4. Train the ANN model.
5. Run the hyperparameter tuning section.
6. Evaluate the final model.
7. Use the prediction function to test new customer data.

## Conclusion

This project helped me understand how an Artificial Neural Network can be used for a real-world classification problem.

The model can be used to identify customers who may be likely to churn. This information can help a telecom company understand customer behaviour and take steps to improve customer retention.

## Author

**SYED TASNEEM**
