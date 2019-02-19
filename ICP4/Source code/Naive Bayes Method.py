# importing the necessary python libraries for machine learning and importing the data sets
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

# Loading our data set
iris = datasets.load_iris()

# splitting the training(60%) and test(40%) data
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

# Picking a type of training model
clf1 = svm.SVC(kernel="linear", C=1).fit(x_train,y_train)
clf2 = svm.SVC(kernel="rbf", C=1).fit(x_train,y_train)
clf3 = GaussianNB(None, 1e-9).fit(x_train,y_train)

# Testing each classifier and print out it's score
print("SVM classifier score: %s" % (clf1.score(x_test,y_test)))
print("SVM classifier with RBE Kernel score: %s" % (clf2.score(x_test,y_test)))
print("Gaussian classifier score: %s" % (clf3.score(x_test,y_test)))
