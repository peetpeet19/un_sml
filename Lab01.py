
#Lab01
#640710440
#พีท อ่อนทอง

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import datasets

# load features and targets separately
iris = datasets.load_iris()
X = iris.data
y = iris.target

print("shape",X.shape)
print("target_names == ",list(iris.target_names))

#ข้อ b
fig = plt.figure(1,figsize=(6,4))
plt.clf()
plt.cla()
plt.scatter(X[:,0],X[:,1], c=y)
plt.title('iris 2 Feature')
plt.show()

#ข้อ c
pca1 = PCA(n_components=2)
pca_X1 = pca1.fit_transform(X)
print(pca_X1.shape)
print(pca1.explained_variance_ratio_)

#ข้อ d
fig = plt.figure(1,figsize=(6,4))
#plt.clf()
#plt.cla()
plt.scatter(pca_X1[:,0],pca_X1[:,1],c=y)
plt.title('PCA n_components_ == 2')
plt.show()

#ข้อ e
pca2 = PCA(n_components=4)
pca_X2 = pca2.fit_transform(X)
print(pca2.explained_variance_ratio_)
print(pca2.n_components_)

#Bar plot of explained_variance
ex_pca = pca2.explained_variance_
fig = plt.figure(1,figsize=(6,4))
plt.bar(range(1,len(ex_pca)+1),ex_pca)
plt.title('PCA n_components_ == 2')
plt.show()

#Bar plot of explained_variance
plt.plot(1,len(ex_pca)+1,ex_pca)
plt.title('PCA n_components_ == 2')
plt.show()


