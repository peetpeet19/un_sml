
#Lab01
#640710440
#พีท อ่อนทอง


from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
X = iris.data
y = iris.target

print("shape",X.shape)
print("target_names == ",list(iris.target_names))

#ข้อ b iris 2 Feature
fig = plt.figure(1,figsize=(6,4))
plt.clf()
plt.cla()
plt.scatter(X[:,0],X[:,1], c=y)
plt.title('iris 2 Feature')
plt.show()

#ข้อ c PCA iris
pca1 = PCA(n_components=2)
pca_X1 = pca1.fit_transform(X)
print(pca_X1.shape)
print(pca1.explained_variance_ratio_)

#ข้อ d กราฟ PCA 2 มิติ
fig = plt.figure(1,figsize=(6,4))
plt.clf()
plt.cla()
plt.scatter(pca_X1[:,0],pca_X1[:,1],c=y)
plt.title('PCA n_components_ == 2')
plt.show()

#ข้อ e PCA 4 มิติ
pca2 = PCA(n_components=4)
pca_X2 = pca2.fit_transform(X)
print(pca2.explained_variance_ratio_)
print(pca2.n_components_)

# กราฟ PCA 4 มิติ
#Bar plot of explained_variance
ex_pca = pca2.explained_variance_
fig = plt.figure(1,figsize=(6,4))
plt.bar(range(1,len(ex_pca)+1),ex_pca)
plt.title('PCA n_components_ == 4')
plt.show()

#Scree Plot of explained_variance
fig = plt.figure(1,figsize=(6,4))
plt.plot(1,len(ex_pca)+1,ex_pca)
plt.title('PCA n_components_ == 4')
plt.show()

# My data --------------------------------------------------------------------

my_data = pd.read_csv("PLACES.csv")

X_mydata = my_data[['log(climate)','log(housing)','log(health)','log(crime)','log(trans)','log(edu)',
'log(arts)','log(recre)','log(economics)']]
#X_mydata.head()
y_mydata = my_data["id"]

#กราฟ ของ mydata
fig = plt.figure(1,figsize=(6,4))
plt.clf()
plt.cla()
plt.scatter(X_mydata["log(climate)"],X_mydata["log(housing)"])
plt.title('mtcar 2 Feature')
plt.show()

#PCA 4 มิติ ของ mydata
pca_mydata = PCA(n_components=4)
pca_mydata_X1 = pca_mydata.fit_transform(X_mydata)
print(pca_mydata_X1.shape)
print(pca_mydata.explained_variance_ratio_)

#กราฟ ของ mydata
fig = plt.figure(1,figsize=(6,4))
plt.clf()
plt.cla()
plt.scatter(pca_mydata_X1[:,0],pca_mydata_X1[:,1])
plt.title('Pca mydata 4 Feature')
plt.show()

#Scree Plot  PCA 4 มิติ ของ mydata
ex_pca_mydata = pca_mydata.explained_variance_
fig = plt.figure(1,figsize=(6,4))
plt.plot(1,len(ex_pca_mydata)+1,ex_pca_mydata)
plt.title('PCA n_components_ == 4')
plt.show()
