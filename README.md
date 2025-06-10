# 🕵️‍♂️ Fake Review Classifier 🕵️‍♀️
**Classify Product Reviews as Real or Fake Using Machine Learning (Naive Bayes, Random Forest, Decision Tree)**

![Streamlit App Screenshot](./assets/Screenshot-app.png)

---

## 🚀 Live Demo
🔗 [Try the App on Streamlit Cloud](https://fake-review-classifier.streamlit.app/)

---

## 💡 Overview
This project is a Streamlit web application designed to **detect fake product reviews**. It uses machine learning to classify a review as "Real" or "Fake" based on the review text, the reviewer's username, and the length of the review.

This app utilizes the following machine learning models:
- 🌳 **Random Forest**
- 🌲 **Decision Tree**
- 🧠 **Naive Bayes**

Simply enter a username and a review, choose a model, and let the app determine its authenticity.

---

## 📊 Model Performance
The models were trained and evaluated, yielding the following accuracies:
- **Random Forest**: 83% Accuracy
- **Decision Tree**: 78% Accuracy
- **Naive Bayes**: 63% Accuracy

---

## 🧠 Features
✅ **Model Selector**: Choose from Naive Bayes, Random Forest, or Decision Tree.
📝 **Text & User Input**: Provide both the review text and username for the prediction.
🤖 **Feature Engineering**: Predictions are based on a combination of:
  - TF-IDF vectorization of the review text.
  - Categorical encoding of the username.
  - The total word count of the review.
🔮 **Instant Predictions**: Get a direct "Real" or "Fake" classification.

---

## 📁 How to Run Locally

1.  Clone this repository:
    ```bash
    git clone https://github.com/fbrianzy/fake-review-classifier/
    cd your-repo-name
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
