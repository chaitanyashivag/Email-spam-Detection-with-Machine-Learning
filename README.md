# Email-spam-Detection-with-Machine-Learning
A collection of emails which are already classified as spam or not spam is taken as input to train the classifier model

# Objective

To developed a machine learning model using Multinomial Naive Bayes Classifier to classify whether the incoming email text as spam or not spam

#Prerequisites

Install following packages:

pip install numpy 
pip install pandas 
pip install nltk
from nltk.corpus import stopwords
import string

# Model Building

Used a Multinomial Naive Bayes classifier to classify the incoming text

## download the stopwords package

Stop words in natural language processing, are useless words (data).
nltk.download("stopwords")

## Remove punctuation marks
Any underlying punctuation marks are cleaned off using the library from the string function

## Convert the text into a matrix of token counts
Using a CountVectorizer function

Training the classifier with the training data and accordingly testing on the test data

# Deployment
The model is exported into pickle file and is imported into a streamlit web app to classify the incoming text as spam or not spam

# Conclusion
Arrived at an accuracy of 99.71% on the multinomial naive bayes classifier and succesfully deployed the project using streamlit
