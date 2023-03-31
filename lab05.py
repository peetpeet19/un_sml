

from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:,0]
y = iris.target

plt.figure(figsize=(5, 4))
plt.hist(X)
plt.show()

for i in range(3):
    plt.hist(X[y == i], bins=10, color=["g","b","r"][i] ,alpha =0.5 , label=iris.target_names[i])
plt.title("class")
plt.xlabel("cm")
plt.ylabel("Count")
plt.legend()
plt.show()

from sklearn.cluster import DBSCAN
iris = datasets.load_iris()
dataX = iris.data
datay = iris.target

clustering_DBSCAN = DBSCAN(eps=0.5, min_samples=2).fit(dataX)
print(clustering_DBSCAN)
print(clustering_DBSCAN.labels_)
print(datay)



from sklearn.mixture import GaussianMixture
gm = GaussianMixture(n_components=2, random_state=0).fit(dataX)
gm.means_