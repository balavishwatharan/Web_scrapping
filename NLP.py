# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:40:51 2024

@author: balav
"""

# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd












#text separated values - tsv file
# Importing the dataset
dataset = pd.read_csv('C:/Users\Ranjith\Desktop\IMAGECON\MACHINE LEARNING\ML -CODING\webscrape_text mining\webscrape_text mining\Restaurant_Reviews.tsv', delimiter = '\t')





# Cleaning the texts
import re
#pip install nltk -> natural language toolkit
import nltk
nltk.download('stopwords') #1






from nltk.corpus import stopwords #2
from nltk.stem.porter import PorterStemmer #stemming
#combination of words is called documents 
#combination of document is called corpus.







corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    
    
    
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review 
              if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
    
    
    
    
    
    
    
    
# Creating the Bag of Words model
#text document is converted into vector file
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values






# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y,
                        test_size = 0.20, random_state = 0)













# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)












# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn import metrics

metrics.accuracy_score(y_test, y_pred)