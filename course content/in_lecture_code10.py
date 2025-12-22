#simple manual dataset
#Example 1: Basic binary Dataset


from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report

#Supervised Learning/ Classification / Y category 0/1
#Dataset
x = [[0,0]  ,  [1,1]  ,  [1,0]  ,  [0,1]]
y = [0          ,1         ,1       ,0  ]
Model = tree.DecisionTreeClassifier()
#Training
Model.fit(x,y) #information Gain

#Testing
y_pred = Model.predict(x)

print("Confusion Matrix:\n", confusion_matrix(y,y_pred))
print("\nClassification Report:\n",  (classification_report(y,y_pred)))

