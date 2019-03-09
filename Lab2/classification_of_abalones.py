from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
import pandas as pd


#read in csv
data = pd.read_csv('abalone.csv')

#describe the rings data
#print(data.rings.describe())

data = data.drop(['sex'],axis=1)

xTrain, xTest, yTrain, yTest = train_test_split(data,data['rings'],test_size=.6,random_state=0)

# combine=[data]
#
# for dataset in combine:
#     dataset['sex']=dataset['sex'].map({'M': 0,'F':1,'I':2}).astype(int)

#differenct classifiers
clf_svm = svm.SVC(kernel='linear').fit(xTrain,yTrain)
knn = KNeighborsClassifier().fit(xTrain,yTrain)
gnb = GaussianNB().fit(xTrain,yTrain)

print("SVC score is {}".format(clf_svm.score(xTest,yTest)))
print("KNN score is {}".format(knn.score(xTest,yTest)))
print("GNB score is {}".format(gnb.score(xTest,yTest)))