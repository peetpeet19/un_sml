# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('play_store_top_app_category_wise.csv')
data.head()
data.info()

data.drop(['name','app_id','rated_for','category','publisher','tags','updated_on','price',], 1, inplace=True)

data.info()

data['review_count'] = data['review_count'].str.rstrip('reviews')
data['downloads'] = data['downloads'].str.rstrip('+')
data['review'] = data['review'].astype(str).str.replace('nan', '0')
data['review_count'] = data['review_count'].astype(str).str.replace('nan', '0')
data['downloads'] = data['downloads'].astype(str).str.replace('nan', '0')

print(data)

data.info()

print(data['review_count'].iloc[0])

def translate_number(number):
    if isinstance(number, int) or isinstance(number, float):
        return number
    number = number.replace(' ', '')
    if 'K' in number:
        return int(float(number.replace('K', '' )) * 1000)
    elif 'M' in number:
        return int(float(number.replace('M', '' )) * 1000000)
    elif 'B' in number:
        return int(float(number.replace('B', '' )) * 1000000000)
    else:
        return int(float(number))

data['review_count'] = data['review_count'].apply(translate_number)
data['downloads'] = data['downloads'].apply(translate_number)

print(data)

data1 = data

fig = plt.figure(1,figsize=(6,4))
plt.scatter(data['review_count'],data['review'])
plt.xlabel("review_count")
plt.ylabel('review')
plt.show()

fig = plt.figure(1,figsize=(6,4))
plt.scatter(data['review_count'],data['downloads'])
plt.xlabel("review_count")
plt.ylabel('downloads')
plt.show()

fig = plt.figure(1,figsize=(6,4))
plt.scatter(data['review'],data['downloads'])
plt.xlabel("review")
plt.ylabel('downloads')
plt.show()

from sklearn.cluster import AgglomerativeClustering
clustering2 = AgglomerativeClustering(n_clusters=5).fit(data)
print("n_clusters=2",clustering2)
print(clustering2.labels_)

df = pd.DataFrame(clustering2.labels_)
df.to_csv('Agglomerative.csv')

from sklearn.cluster import KMeans
kmeans_c2 = KMeans(n_clusters=5, random_state=440).fit(data)
print("kmeans labels",kmeans_c2.labels_)
print("kmeans cluster_centers",kmeans_c2.cluster_centers_)

df = pd.DataFrame(kmeans_c2.labels_)
df.to_csv('kmeans_c2.csv')

print(data)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Get the cluster labels
labels = kmeans_c2.labels_

# Get the cluster centers
centers = kmeans_c2.cluster_centers_

# Scatter plot the data points with color-coded clusters
ax.scatter(data1['review'], data1['review_count'], data1['downloads'], c=labels)

# Plot the cluster centers as black stars
ax.scatter(centers[:, 0], centers[:, 1], centers[:, 2], marker='*', c='black', s=200)

# Set the axis labels
ax.set_xlabel('Review')
ax.set_ylabel('Review Count')
ax.set_zlabel('Downloads')

# Show the plot
plt.show()

import plotly.express as px
import pandas as pd
import numpy as np

# create some sample data
np.random.seed(440)
data3 = pd.DataFrame(np.random.randn(894, 3), columns=['x', 'y', 'z'])

# fit k-means clustering model
kmeans_c2 = KMeans(n_clusters=5, random_state=440).fit(data)

# add cluster labels to data
data3['cluster'] = kmeans_c2.labels_

# create 3D scatter plot
fig = px.scatter_3d(data3, x='x', y='y', z='z', color='cluster')
fig.show()