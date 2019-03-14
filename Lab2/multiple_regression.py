import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv('basketball_csv.csv')
# print(data.isnull().sum())

#we want to predict the occupancy at a certain time of the day
#print(data.Occupancy.describe())
    

#check for skewness
print("Skew is: ", data.ppg.skew())
plt.hist(data.ppg, color='red')
plt.show()

target = np.log(data.ppg+10)
print('Skew is: ', target.skew())
plt.hist(target, color='blue')
plt.show()

numeric_features = data.select_dtypes(include=[np.number])

corr = numeric_features.corr()

print(corr['ppg'].sort_values(ascending=False)[:5], '\n')
print(corr['ppg'].sort_values(ascending=False)[-5:])

quality_pivot = data.pivot_table(index='percent of successful field goals',
                                  values='ppg', aggfunc=np.median)
print(quality_pivot)

quality_pivot.plot(kind='bar', color='green')
plt.xlabel("Percent of successful field goals")
plt.ylabel("PPG")
plt.show()

y = data.ppg
x = data.drop(['ppg'],axis=1)
from sklearn.model_selection import train_test_split

xTrain,xTest,yTrain,yTest = train_test_split(x,y,random_state=42,test_size=.5)
lr = linear_model.LinearRegression()
model = lr.fit(xTrain,yTrain)
print('R^2 is: ',model.score(xTest,yTest))

from sklearn.metrics import mean_squared_error
predictions = model.predict(xTest)
print('RMSE is: ',mean_squared_error(yTest,predictions))
