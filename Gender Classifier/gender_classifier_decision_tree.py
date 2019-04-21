'''loading the dataset 
	Converting the categorical values
	Nan values
	Outliers 
	normalize
	train test split
	classifier / model
'''


import sklearn
from sklearn import tree
import pandas as pd

#Height Weight Index
data = pd.read_csv(r"C:\\Users\\Akhil\\Desktop\\Le-jour-o-j-ai-appris-la-machine\\Datasets\\500_Person_Gender_Height_Weight_Index.csv")
print(data)

x = data.iloc[: , 1:].values
y = data.iloc[: , 0].values

from sklearn.model_selection import train_test_split
x_train , x_test  , y_train , y_test = train_test_split (x , y,test_size = 0.25 ,random_state = 0)

print(data.info())
print(data.describe())

print ("done not")


print(sklearn.__path__)
clf = tree.DecisionTreeClassifier()
clf= clf.fit(x_train,y_train)
print("wait")
prediction = clf.predict(x_test)
print (y_test)

print (prediction)

print ("done")


