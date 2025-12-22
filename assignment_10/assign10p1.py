# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 09:10:00 2025

assignment #10 program #1

@author: comma

Write a python program that defines this dataset and trains a 
Decision Tree Classifier. Then Predict the target class if the input 
feature vector = [1,1,0,0]

"""
from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report

x = [[0,0,0,0],[0,0,0,1],[0,0,1,0],[0,0,1,1],[0,1,0,0],[0,1,0,1],[0,1,1,0],
     [0,1,1,1],[1,0,0,0],[1,0,0,1],[1,0,1,0],[1,0,1,1],[1,1,0,0],[1,1,0,1],
     [1,1,1,0],[1,1,1,1]]

y = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]

Model = tree.DecisionTreeClassifier()

Model.fit(x,y)

y_pred = Model.predict(x)

print("Confusion Matrix:\n", confusion_matrix(y,y_pred))
print("\nClassification Report:\n",  (classification_report(y,y_pred)))