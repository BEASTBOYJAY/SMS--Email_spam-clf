import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import pickle

ps=PorterStemmer()

def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)

  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text=y[:]
  y.clear()

  for i in text:
    y.append(ps.stem(i))


  return " ".join(y)


vectorize=pickle.load(open("Vectorize.pkl",'rb'))
model=pickle.load(open("Model.pkl",'rb'))

st.title("SMS/Email Spam Classifier")

input_sms=st.text_area("Enter the message")

if st.button('predict',type='primary'):
  #1.Preprocess
  transformed_text=transform_text(input_sms)
  #2.Vectorize
  vectorized_text=vectorize.transform([transformed_text])
  #3.result
  result=model.predict(vectorized_text)[0]
  #4.Display
  if result==1:
    st.header("Spam")
  else:
    st.header("Not Spam")