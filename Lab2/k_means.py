import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn import metrics
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('winequality-white.csv')
x = dataset.iloc[:,3:]
y = dataset.iloc[:-1]
print(dataset['quality'].value_counts())
sns.FacetGrid(dataset,hue='quality',size=5).map(plt.scatter,'pH','total sulfur dioxide').add_legend()
plt.show()


#scaling the feature down
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
x_scaled_array = scaler.transform(x)
x_scaled = pd.DataFrame(x_scaled_array,columns=x.columns)

nclusters,seed = 3,0
km=KMeans(n_clusters=nclusters,random_state=seed)
km.fit(x_scaled)
y_cluster_kmeans = km.predict(x_scaled)
wcss=[]

#elbow method used to figure out amount of clusters
for i in range(1,13):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,13),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()
silhouette_avg = metrics.silhouette_score(x,y_cluster_kmeans)
print("The silhouette score is: {}".format(silhouette_avg))

