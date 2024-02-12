
import pickle
import streamlit as st
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import string


pickle_in = open("G:\DS\Projects\Email spam classifier\emailspam.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_spam(text):
	# download the stopwords package
	nltk.download("stopwords")
	texts=process(text)
	message = CountVectorizer(analyzer=process).fit_transform(texts)
	prediction=classifier.predict(message)
	print(prediction)
	return prediction


def process(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)

    clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    return clean
# to show the tokenization


def main():
    st.title("Email Spam Predictor")
    text = st.text_input("text","")
    
    result=""
    if st.button("Predict"):
        result=predict_spam(text)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()