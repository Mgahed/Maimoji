import nltk
nltk.download('stopwords')
from sklearn.model_selection import cross_validate
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import naive_bayes
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("training.txt",sep='\t', names=['liked','txt'])

stopset = set(stopwords.words('english'))

vectorizer = TfidfVectorizer(use_idf=True, lowercase=True, strip_accents='ascii', stop_words=stopset)
y=df.liked
x=vectorizer.fit_transform(df.txt)

X_train, X_test, y_train, y_test = train_test_split(x,y, random_state=42)

clf = naive_bayes.MultinomialNB()
clf.fit(X_train, y_train)

reviews_array = np.array(["the movie was good but the book was bad"])
reviews_vector = vectorizer.transform(reviews_array)

prediction = clf.predict(reviews_vector)
print (prediction) 
print (accuracy_score(y_test, clf.predict_proba(X_test)[:,1]))

