# House Price Prediction using Machine Learning

## Project Overview

This project focuses on predicting house prices using machine learning regression techniques.

The notebook follows an end-to-end machine learning workflow including data loading, exploratory data analysis, data preprocessing, feature analysis, model training, model comparison, and evaluation.

## Dataset

The project uses the **House Pricing India** dataset.

The dataset contains property-related features that can be used to understand and predict house prices.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook / Google Colab

## Machine Learning Workflow

### 1. Data Loading

The house price dataset is loaded into a Pandas DataFrame for analysis.

### 2. Exploratory Data Analysis

The dataset is explored to understand:

- Dataset structure
- Feature types
- Statistical information
- Relationships between variables
- Correlations between features
- Distribution of house prices

Visualizations are used to identify patterns and relationships in the data.

### 3. Data Preprocessing

The dataset is prepared for machine learning by:

- Inspecting the data
- Handling relevant data issues
- Separating input features and target variable
- Preparing the data for model training

### 4. Train-Test Split

The dataset is divided into training and testing sets to evaluate how well the trained models perform on unseen data.

### 5. Regression Models

Three regression algorithms are implemented and compared:

#### Linear Regression

Used as a baseline regression model to understand the linear relationship between property features and house prices.

#### Decision Tree Regression

Used to capture non-linear relationships between the input features and house prices.

#### Random Forest Regression

An ensemble learning method that combines multiple decision trees to improve prediction performance and generalization.

## Model Evaluation

The models are evaluated using:

- Mean Squared Error (MSE)
- R² Score

### Model Comparison

The evaluated models produced the following results:

| Model | MSE | R² Score |
|---|---:|---:|
| Linear Regression | 38,262,747,927.97 | 74.15% |
| Decision Tree Regression | 8,615,450,476.07 | 94.18% |
| Random Forest Regression | 4,768,750,950.78 | 96.78% |

## Result

Among the evaluated models, **Random Forest Regression** achieved the best performance, with the highest R² score and the lowest Mean Squared Error.

The Random Forest model achieved an R² score of approximately **96.78%**, demonstrating strong predictive performance on the test data.

## Key Concepts Demonstrated

- Exploratory Data Analysis
- Data preprocessing
- Feature analysis
- Regression
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- Model comparison
- Mean Squared Error
- R² Score
- Data visualization
- Machine learning evaluation

## Project Structure

```text
house-price-prediction/
│
├── House_Price_Prediction.ipynb
├── House_Price_India.csv
└── README.md
```

## Disclaimer

This project is developed for educational and machine learning practice purposes. The predictions are based on the available dataset and should not be considered professional real-estate valuation.
