import keras
from keras.layers.core import Dense, Activation
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tensorboard
from keras.models import Model
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import numpy as np

data = pd.read_csv('heart.csv')
#check our features to see if there are any nulls
print(data.isnull().sum())
#get the counts for our
print(data['target'].value_counts())
#print(data.head(10))
numeric_features = data.select_dtypes(include=[np.number])

corr = numeric_features.corr()

print(corr['target'].sort_values(ascending=False)[:5], '\n')
print(corr['target'].sort_values(ascending=False)[-5:])

quality_pivot = data.pivot_table(index='cp',
                                  values='target', aggfunc=np.median)
print(quality_pivot)
quality_pivot.plot(kind='bar', color='green')
plt.xlabel("cp")
plt.ylabel("target")
plt.show()

y = data.target
x = data.drop(['target'],axis=1)
# set seed for numpy and tensorflow
# set for reproducible results

from sklearn.model_selection import train_test_split
xTrain,xTest,yTrain,yTest = train_test_split(x,y,random_state=42,test_size=.5)


tbCallBack = keras.callbacks.TensorBoard(log_dir='./Graph', write_graph=True, write_images=True)



from sklearn.model_selection import train_test_split
tbCallBack = keras.callbacks.TensorBoard(log_dir='./Graph', write_graph=True, write_images=True)


lr = LogisticRegression()
model = lr.fit(xTrain,yTrain)
print('R^2 is: ',model.score(xTest,yTest))
