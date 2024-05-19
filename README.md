
# [SMS Spam Classfier](https://sms-email-spam-clf.onrender.com)

Its a Spam Detector it can detect if a message is a spam or not.


## Table of Content
- Introduction
- Dataset
- Installation
- Model Traning
- Evaluation

### Introduction
This project aims to classify SMS messages as spam or ham (non-spam) using machine learning algorithms. We use a dataset containing labeled SMS messages and implement various machine learning models to identify spam messages effectively.

### Dataset

The dataset used in this project is the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset). It consists of 5000+ SMS messages in English, which are labeled as either 'spam' or 'ham'.

### Installation
 1. Clone the repository:

 ```bash
 git clone https://github.com/BEASTBOYJAY/SMS-Email_spam-clf.git

 cd SMS-Email_spam-clf

```
2. Install the required Pakages:
```bash
pip install -r requirements.txt
```

3.Run the app.py Streamlit file:
```bash
streamlit run app.py
```
it will open your defalut web browser then you can predict your messages

### Model Traning
The project includes multiple machine learning models for spam detection, such as:

- Naive Bayes
- Support Vector machine(SVM)
- Random Forest
- Logistic Regression etc.


The models are trained after preprocessing the dataset, and various techniques like TF-IDF vectorization are used to convert text into numerical features.

### Evaluation
The models are evaluated based on metrics such as accuracy, precision, recall, and F1-score.You can go through them in the .pynb file

