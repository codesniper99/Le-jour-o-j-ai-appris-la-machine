

print ("done not")
import sklearn
from sklearn import tree

#Height Weight Index
x=[[174,	96,		4],[189,	87,		2],[185,	110,	4],[195,	104,	3],
[149,	61,		3],[189,	104,	3],[147,	92,		5],[154,	111,	5],
[174,	90,		3]
]

y= ['Male','Male','Female','Female','Male','Male','Male','Male','Male']
print(sklearn.__path__)
clf = tree.DecisionTreeClassifier()
clf= clf.fit(x,y)
print("wait")
prediction = clf.predict([[169,103,4]])

print (prediction)

print ("done")


