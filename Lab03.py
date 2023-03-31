
import numpy as np

def euclidean(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

def kmean(a1_list,a2_list,centroid_1,centroid_2):
    if(len(a1_list)==len(a2_list)) and len(centroid_1)==len(centroid_2):
        distance = np.zeros((len(a1_list),len(centroid_1)))
        new_c1 = np.zeros(len(centroid_1))
        new_c2 = np.zeros(len(centroid_2))
        cluster_no = []
        c_cnt = np.zeros(len(centroid_1))
        for i in range(len(a1_list)):
            for j in range(len(centroid_1)):
                distance[i,j] = euclidean(a1_list[i],a2_list[i],centroid_1[j],centroid_2[j])

        for i in range(len(a1_list)):
            min_val = min(distance[i, :])
            cluster_no.append(list(distance[i, :]).index(min_val))
            print("point:"+str(i+1), "\t",
                  '{:.2f}'.format(distance[i,0]), "\t",
                  '{:.2f}'.format(distance[i,1]), "\t",
                  '{:.2f}'.format(distance[i,2]), "\t",
                  cluster_no[i]+1)

        for i in range(len(a1_list)):
            new_c1[cluster_no[i]] += a1_list[i]
            new_c2[cluster_no[i]] += a2_list[i]
            c_cnt[cluster_no[i]] += 1

        for i in range(len(new_c1)):
            new_c1[i] /= c_cnt[i]
            new_c2[i] /= c_cnt[i]
        print(new_c1,new_c2)
        return new_c1,new_c2
    else:
        print("Dimension error")

a1 = [0,2,3,5,7,11,13,15,16,19]
a2 = [0,5,1,4,7,1,5,2,6,4]
c1 = [0,7,19]
c2 = [0,7,4]

new_c1,new_c2 = kmean(a1,a2,c1,c2)
_, _ = kmean(a1,a2,new_c1,new_c2)

#for i in range(10):
    #print("รอบ", i)
    #c1,c2 = kmean(a1,a2,c1,c2)

#probability measurement
#Centroid

from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()

X = iris.data
y = iris.target
print(len(y))

kmeans_c2 = KMeans(n_clusters=2, random_state=440, n_init="auto").fit(X)
print("kmeans labels",kmeans_c2.labels_)
print("kmeans cluster_centers",kmeans_c2.cluster_centers_)

print("predict",kmeans_c2.predict([[1,2,3,4]]))


kmeans_c3 = KMeans(n_clusters=3, random_state=640, n_init="auto").fit(X)
print("kmeans_c3",kmeans_c3.labels_)

kmeans_c4 = KMeans(n_clusters=4, random_state=640, n_init="auto").fit(X)
print("kmeans_c4",kmeans_c4.labels_)

kmeans_c5 = KMeans(n_clusters=5, random_state=640, n_init="auto").fit(X)
print("kmeans_c5",kmeans_c5.labels_)

kmeans_c6 = KMeans(n_clusters=6, random_state=640, n_init="auto").fit(X)
print("kmeans_c6",kmeans_c6.labels_)

kmeans_c7 = KMeans(n_clusters=7, random_state=640, n_init="auto").fit(X)
print("kmeans_c7",kmeans_c7.labels_)



