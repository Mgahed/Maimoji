import nltk
# nltk.download('stopwords')
from sklearn.model_selection import cross_validate
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from textblob import TextBlob
import os
import sys
basdir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(1, basdir+'../')
from app import *

def ftblob(text):

    df = pd.read_csv("training.txt",sep='\t', names=['liked','txt'])

    stopset = set(stopwords.words('english'))

    vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)
    y=df.liked
    x=vectorizer.fit_transform(df.txt)

    X_train, X_test, y_train, y_test = train_test_split(x,y, random_state=42)

    clf = naive_bayes.MultinomialNB()
    clf.fit(X_train, y_train)

    # input_text = input("Enter text: ")

    blob = TextBlob(text)


    if blob.subjectivity <= 0.5:
        # print("0.5")
        return '0.5'
    else :
        reviews_array = np.array([text])
        reviews_vector = vectorizer.transform(reviews_array)

        prediction = clf.predict(reviews_vector)
        return prediction
print(ftblob("fine"))
