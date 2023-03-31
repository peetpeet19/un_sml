
import numpy as np

#def euclidean(x1,y1,x2,y2) :
#   return  ((x1-x2)^2+(y1-y2)^2)^2

#print(euclidean(2,5,3,1,5,4))

def euclidean(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

'''
def kmean(a1_list,a2_list,centroid_1,centroid_2) :
    if len(a1_list) == len(a2_list) and len(centroid_1) == len(centroid_2):
        distance = np.zeros((len(a1_list), len(centroid_1)))
        new_c1 = np.zeros(len(a1_list), len(centroid_1))
        new_c1 = np.zeros(len(a1_list), len(centroid_1))
        cluster_no = []
        for i in range(len(a1_list)) :
            for j in range(len(centroid_1)) :
                distance[i,j] = euclidean(a1_list[i],a2_list[i],centroid_1[j],centroid_2[j])

        for i in range(len(a1_list)):
            min_val = min(distance[i,:])
            cluster_no.append(list(distance[i,:]).index(min_val))
            print("POINT"+str(i+1),"\t",
                  '{:.3f}',format(distance[i, 0]), '\n',
                  '{:.3f}',format(distance[i, 1]), '\n',
                  '{:.3f}',format(distance[i, 2]), '\n',
                  cluster_no[i]+1)
    else : print("error")

a1 = [0,2,3,5,7,11,13,15,16,19]
a2 = [0,5,1,4,7,1,5,2,6,4]
c1 = [0,7,19]
c2 = [0,7,4]
kmean(a1,a2,c1,c2)

'''
def kmean(a1_list,a2_list,centroid_1,centroid_2):
    if(len(a1_list) == len(a2_list)) and len(centroid_1) == len(centroid_2):

        distance = np.zeros((len(a1_list),len(centroid_1)))
        new_c1 = np.zeros(len(centroid_1))
        new_c2 = np.zeros(len(centroid_2))
        cluster_no = []
        c_cut = np.zeros(len(centroid_1))

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
            c_cut[cluster_no[i]] += 1

        for i in range(len(new_c1)):
            new_c1[i] /= c_cut[i]
            new_c2[i] /= c_cut[i]
        print(new_c1,new_c2)
        return new_c1,new_c2

    else:
        print("Dimension error")



a1 = [0,2,3,5,7,11,13,15,16,19]
a2 = [0,5,1,4,7,1,5,2,6,4]
c1 = [0,7,19]
c2 = [0,7,4]

new_c1 ,new_c2 = kmean(a1,a2,c1,c2)
_, _ = kmean(a1,a2,new_c1,new_c2)
