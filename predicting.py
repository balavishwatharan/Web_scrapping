# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:41:34 2024

@author: balav
"""

#Naive Bayes
#pca for linear
#kernel pca for non-linear analysis
#principal of pca following an unsupervised method , 
#why because of taken only x data.
#but we are applying in a supervised learning algorithm 
#(regression,classification)



#Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dataset
dataset=pd.read_csv("C:/Users\Ranjith\Desktop\IMAGECON\DATASETS/Iris_new.csv")
dataset.info()
dataset.head()
dataset.tail()
dataset.isnull().sum()




#Encoding
from sklearn.preprocessing import LabelEncoder
la=LabelEncoder()
dataset.spectype=la.fit_transform(dataset.spectype)  
x=dataset.iloc[:,0:4].values
y=dataset.iloc[:,-1].values





#split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)







#Dimensionality reduction
from sklearn.decomposition import PCA
pca=PCA(n_components=1)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)
explained_variance=pca.explained_variance_ratio_
#threshold












#model fit
from sklearn.naive_bayes import GaussianNB
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.naive_bayes import BernoulliNB

# classifier=BernoulliNB()
# classifier=MultinomialNB()
classifier=GaussianNB()
classifier.fit(x_train,y_train)
classifier.score(x_train,y_train)
#pred
y_pred=classifier.predict(x_test)




#cm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

cm=confusion_matrix(y_test,y_pred)
cm
acc=sum(np.diag(cm)/len(y_test))
acc

accuracy=accuracy_score(y_test,y_pred)
accuracy







#visualization
from matplotlib.colors import ListedColormap

x_set,y_set=x_train,y_train
x1,x2=np.meshgrid(np.arange(x_set[:,0].min()-1,x_set[:,0].max()+1,step=0.1),
                  np.arange(x_set[:,1].min()-1,x_set[:,1].max()+1,step=0.1))

#meshgrid formation
plt.figure(dpi=300)
plt.contourf(x1,x2,classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),
             cmap=ListedColormap(("red","blue",'orange')),alpha=0.85)

plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set==j,0],x_set[y_set==j,1],
                c=ListedColormap(('black','white','cyan'))(i),label=j)

plt.title('Naive Bayes algorithms')
plt.xlabel('X of plot')
plt.ylabel('Y of plot')
plt.legend()
plt.show()