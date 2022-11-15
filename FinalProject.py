import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("mammographic_masses.data.txt",na_values=["?"], names=["BI_RADS", "age", "shape", "margin", "density", "severity"] )




df.describe()

df.loc[(df['age'].isnull()) |
              (df['shape'].isnull()) |
              (df['margin'].isnull()) |
              (df['density'].isnull())]


df.dropna(inplace=True)

feature_data = df.loc[:,['age','shape','margin', 'density']]
class_data = df.loc[:,['severity']]

feature_names = ['age', 'shape', 'margin', 'density']
feature_data.head() 
class_data.head()

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
feature_data_scaled=scaler.fit_transform(feature_data)


from sklearn.model_selection import cross_val_score, train_test_split

X_train, X_test, y_train, y_test = train_test_split(feature_data_scaled, class_data, test_size=0.25, random_state=0)

from sklearn import tree

clf = tree.DecisionTreeClassifier(random_state=1)
clf = clf.fit(X_train,y_train)

fig=plt.figure(figsize= (5,5))
tree.plot_tree(clf, class_names= ['No', 'Yes'], feature_names=feature_names, filled=True)
#plt.show()


from sklearn.metrics import accuracy_score
print("Tree Accuracy train test Split")
print(accuracy_score(y_test, clf.predict(X_test)))

clf = tree.DecisionTreeClassifier(random_state=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)

print("Kfold Tree Accuracy and mean ")
#print(scores)
print(scores.mean())


from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10,random_state=1)

scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print("Forest Accuracy and mean ")
#print(scores)
print(scores.mean())

#SVM
from sklearn import svm

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("SVM Score")
#print(scores)
print(scores.mean())



from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier (n_neighbors=10)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("KNN Score for K=10")
#print(scores)
print(scores.mean())

print ("Checking from 1 to 50 neighbours")
for x in range(50):
    clf = KNeighborsClassifier (n_neighbors=x+1)
    scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
    print ("KNN Score for K= ",(x+1),scores.mean())
    #print(scores)
    #print(scores.mean())



from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler

clf = MultinomialNB()

min_max=MinMaxScaler()
feature_data_scaled_minmax=min_max.fit_transform(feature_data)
scores = cross_val_score(clf, feature_data_scaled_minmax, class_data , cv=10)

print("Multinomial Naive Bayes")
#print(scores)
print(scores.mean())

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("SVM Score Linear")
#print(scores)
print(scores.mean())


clf = svm.SVC(kernel='rbf', C=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("SVM Score RBF")
#print(scores)
print(scores.mean())

clf = svm.SVC(kernel='sigmoid', C=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("SVM Score sigmoid")
#print(scores)
print(scores.mean())

clf = svm.SVC(kernel='poly', C=1)
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("SVM Score poly")
#print(scores)
print(scores.mean())

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
scores = cross_val_score(clf, feature_data_scaled, class_data , cv=10)
print ("Logistic Regression")
#print(scores)
print(scores.mean())



