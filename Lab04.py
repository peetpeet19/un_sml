
#hierarchical algorithm

from sklearn import datasets

from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy

iris = datasets.load_iris()
X = iris.data
y = iris.target

clustering2 = AgglomerativeClustering(n_clusters=2).fit(X)
print("n_clusters=2",clustering2)
print(clustering2.labels_,"\n")

#agglo_result2 = clustering2.labels_
#for i in range(len(y)) :
    #print(agglo_result2[i] , "\t" ,y[i] )

clustering3 = AgglomerativeClustering(n_clusters=3).fit(X)
print(clustering3.labels_,"\n")

clustering4 = AgglomerativeClustering(n_clusters=4).fit(X)
print(clustering4.labels_,"\n")

clustering5 = AgglomerativeClustering(n_clusters=5).fit(X)
print(clustering5.labels_,"\n")

clustering6 = AgglomerativeClustering(n_clusters=6).fit(X)
print(clustering6.labels_,"\n")

clustering7 = AgglomerativeClustering(n_clusters=7).fit(X)
print(clustering7.labels_,"\n")

def plot_dendrogram(X) :
    linkage_iris =  linkage(X ,"ward")
    dendrogram(linkage_iris)

plt.title("Agnee clusters dendrogram")
plot_dendrogram(X)
plt.show()


#Z = hierarchy.linkage(X, 'ward')
#
## method 1: lastp
#hierarchy.dendrogram(Z, truncate_mode='lastp', p=4)  # -> you will have 4 leaf at the bottom of the plot
#plt.show()
#
## method 2: level
#hierarchy.dendrogram(Z, truncate_mode='level',p=5)  # -> No more than ``p`` levels of the dendrogram tree are displayed.
#plt.show()



'''''

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)
    
clustering1 = AgglomerativeClustering(distance_threshold=1, n_clusters=None).fit(X)

plt.title("Hierarchical Clustering Dendrogram 2")
# plot the top three levels of the dendrogram
plot_dendrogram(clustering1, truncate_mode="level", p=2)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
'''''