# 2. load data .npy
# input is binary
import numpy as np

w = np.load(r'E:/mystudy/3 term 2/unsupervised/lab after midterm/lab 2/Dataset_L02/w.npy')
print(w)
print('COUNT OF w : ' , w.shape) # or len(w)
print('COUNT OF 0 : ' , np.count_nonzero(w == 0))
print('COUNT OF 1 : ' , np.count_nonzero(w == 1))

x = np.load(r'E:/mystudy/3 term 2/unsupervised/lab after midterm/lab 2/Dataset_L02/x.npy')
print(x)
print('ATTRIBUTE OF x : ' , x.shape)
print('COUNT OF 0 : ' , np.count_nonzero(x == 0))
print('COUNT OF 1 : ' , np.count_nonzero(x == 1))

y = np.load(r'E:/mystudy/3 term 2/unsupervised/lab after midterm/lab 2/Dataset_L02/y.npy')
print(y)
print('ATTRIBUTE OF y : ' , y.shape)
print('COUNT OF 0 : ' , np.count_nonzero(y == 0))
print('COUNT OF 1 : ' , np.count_nonzero(y == 1))

z = np.load(r'E:/mystudy/3 term 2/unsupervised/lab after midterm/lab 2/Dataset_L02/z.npy')
print(z)
print('ATTRIBUTE OF z : ' , z.shape)
print('COUNT OF 0 : ' , np.count_nonzero(z == 0))
print('COUNT OF 1 : ' , np.count_nonzero(z == 1))

# 3. contingency table
def contingency(input1 , input2) :
    if (len(input1) == len(input2)) :
        f00 = 0    # input1 = 0 input2 = 0
        f01 = 0    # input1 = 0 input2 = 1
        f10 = 0    # input1 = 0 input2 = 0
        f11 = 0    # input1 = 1 input2 = 1

        for i in range(len(input1)) :
            if input1[i] == 0 and input2[i] == 0 :
                f00 += 1
            elif input1[i] == 0 and input2[i] == 1 :
                f01 += 1
            elif input1[i] == 1 and input2[i] == 0 :
                f10 += 1
            elif input1[i] == 1 and input2[i] == 1 :
                f11 += 1

        return f00 , f01 , f10 , f11

    else :
        print('SIZE ERROR')

print('---------- CONTINGENCY TABLE (w , x) -----------')
f00 , f01 , f10 , f11 = contingency(w , x)
print(f00 , f01)
print(f10 , f11)

print('---------- CONTINGENCY TABLE (x , y) -----------')
f00 , f01 , f10 , f11 = contingency(x , y)
print(f00 , f01)
print(f10 , f11)

print('---------- CONTINGENCY TABLE (y , z) -----------')
f00 , f01 , f10 , f11 = contingency(y , z)
print(f00 , f01)
print(f10 , f11)

# 5. similarity matrix
def sym_binary_coef(input1 , input2) :
    f00 , f01 , f10 , f11 = contingency(input1 , input2)
    return (f00 + f11) / (f00 + f01 + f10 + f11)

def similarity_matrix(list_of_input) :
    n = len(list_of_input)
    output = np.zeros((n , n))

    for i in range(n - 1) :
        for j in range(i + 1 , n , 1) :
            output[j][i] = sym_binary_coef(list_of_input[i] , list_of_input[j])

    print(output)

print('---------- SIMILARITY MATRIX -----------')
similarity_matrix([w , x , y , z])

#  6. dissimilarity matrix
def sym_binary_coef(input1 , input2) :
    f00 , f01 , f10 , f11 = contingency(input1 , input2)
    return (f01 + f10) / (f00 + f01 + f10 + f11)

def dissimilarity_matrix(list_of_input) :
    n = len(list_of_input)
    output = np.zeros((n , n))

    for i in range(n - 1) :
        for j in range(i + 1 , n , 1) :
            output[j][i] = sym_binary_coef(list_of_input[i] , list_of_input[j])

    print(output)

print('---------- DISSIMILARITY MATRIX -----------')
dissimilarity_matrix([w , x , y , z])





