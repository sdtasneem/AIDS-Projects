# Food Review Sentiment Analysis using RNN

## Project Overview

This project uses a Recurrent Neural Network (RNN) to classify restaurant reviews as **positive** or **negative**.

The project implements an end-to-end Natural Language Processing (NLP) workflow, including text cleaning, tokenization, sequence padding, model training, early stopping, performance visualization, model saving, and sentiment prediction on new reviews.

## Dataset

The project uses the **Restaurant Reviews** dataset downloaded from Kaggle using KaggleHub.

Dataset source:

https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews

The notebook loads the `Restaurant_Reviews.tsv` file and uses:

- `Review` as the input text
- `Liked` as the target label

## Technologies Used

- Python
- Pandas
- NumPy
- TensorFlow
- Keras
- Scikit-learn
- Matplotlib
- Pickle
- KaggleHub
- Jupyter Notebook / Google Colab

## NLP Workflow

### 1. Data Loading

The restaurant review dataset is downloaded from Kaggle using KaggleHub and loaded into a Pandas DataFrame.

### 2. Data Inspection

The dataset is inspected for:

- Sample records
- Missing values
- Dataset dimensions
- Duplicate records

Duplicate records are removed before model training.

### 3. Text Preprocessing

A custom text-cleaning function is applied to the reviews.

The preprocessing steps include:

- Converting text to lowercase
- Removing non-alphabetic characters
- Removing extra spaces

### 4. Tokenization

Keras `Tokenizer` is used to convert review text into numerical sequences.

The project uses:

- **Maximum vocabulary size:** 1,000 words
- **OOV token:** `<OOV>`

### 5. Sequence Padding

The numerical sequences are padded or truncated to a fixed length of **100 tokens**.

Padding is performed at the end of each sequence.

### 6. Train-Test Split

The processed data is divided into:

- **80% Training Data**
- **20% Testing Data**

Stratified splitting is used to maintain the target class distribution.

## RNN Model Architecture

The sentiment classification model is built using TensorFlow and Keras.

The architecture consists of:

- Embedding layer with 128-dimensional word representations
- SimpleRNN layer with 32 units
- Dropout layer with 0.2 dropout rate
- Dense layer with 64 neurons and ReLU activation
- Dense layer with 32 neurons and ReLU activation
- Output layer with 1 neuron and Sigmoid activation

The sigmoid output is used for binary sentiment classification.

## Model Training

The model is compiled using:

- **Optimizer:** Adam
- **Loss Function:** Binary Cross-Entropy
- **Metric:** Accuracy

The model is trained for a maximum of **300 epochs**, with 20% of the training data used for validation.

Early stopping is applied with:

- **Monitor:** Validation loss
- **Patience:** 3 epochs
- **Restore best weights:** Enabled

This helps stop training when validation performance stops improving and restores the best-performing model weights.

## Model Performance Visualization

Training and validation performance are visualized using Matplotlib.

The notebook plots:

- Training vs. validation accuracy
- Training vs. validation loss

These plots help observe the model's learning behavior and identify potential overfitting.

## Model Saving

The trained RNN model is saved as:

```text
restuart food reviews.h5
```

The trained tokenizer is saved using Pickle as:

```text
food review.pkl
```

Saving both the model and tokenizer allows the same preprocessing and prediction pipeline to be reused for new reviews.

## Sentiment Prediction

A reusable `predict_sentiment()` function is created for classifying new restaurant reviews.

The prediction pipeline:

1. Cleans the input review
2. Converts the review into a numerical sequence
3. Pads the sequence to 100 tokens
4. Passes the processed review to the trained RNN
5. Generates a prediction probability
6. Classifies the review as **positive** or **negative**

Example input:

```python
text = 'i love this good taste but to much cost'
predict_sentiment(text)
```

## Project Structure

```text
restaurant-review-sentiment-analysis-rnn/
│
├── food review.ipynb
├── restuart food reviews.h5
├── food review.pkl
├── README.md
└── requirements.txt
```

## Key Concepts Demonstrated

- Natural Language Processing
- Text preprocessing
- Tokenization
- Sequence padding
- Word embeddings
- Recurrent Neural Networks
- Binary sentiment classification
- TensorFlow and Keras
- Early stopping
- Model serialization
- Sentiment prediction

## Disclaimer

This project is developed for educational and machine learning practice purposes. The sentiment predictions are intended for demonstration and should not be treated as a definitive assessment of customer opinions.
