
import numpy as np

Var_w = np.load(r'C:\Users\M S I\PycharmProjects\ass_TEST\Lab\Data\w.npy')
Var_x = np.load(r'C:\Users\M S I\PycharmProjects\ass_TEST\Lab\Data\x.npy')
Var_y = np.load(r'C:\Users\M S I\PycharmProjects\ass_TEST\Lab\Data\y.npy')
Var_z = np.load(r'C:\Users\M S I\PycharmProjects\ass_TEST\Lab\Data\z.npy')

print(Var_w)
print('COUNT OF w : ' , Var_w.shape,np.count_nonzero(Var_w == 0,),np.count_nonzero(Var_w == 1,))

print(Var_x)
print('ATTRIBUTE OF x : ' , Var_x.shape,np.count_nonzero(Var_x == 0,),np.count_nonzero(Var_x == 1,))

print(Var_y)
print('ATTRIBUTE OF y : ' , Var_y.shape,np.count_nonzero(Var_y == 0,),np.count_nonzero(Var_y == 1,))

print(Var_z)
print('ATTRIBUTE OF z : ' , Var_z.shape,np.count_nonzero(Var_z == 0,),np.count_nonzero(Var_z == 1,))


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
f00 , f01 , f10 , f11 = contingency(Var_w , Var_x)
print(f00 , f01)
print(f10 , f11)

print('---------- CONTINGENCY TABLE (x , y) -----------')
f00 , f01 , f10 , f11 = contingency(Var_x , Var_y)
print(f00 , f01)
print(f10 , f11)

print('---------- CONTINGENCY TABLE (y , z) -----------')
f00 , f01 , f10 , f11 = contingency(Var_y , Var_z)
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
similarity_matrix([Var_w , Var_x , Var_y , Var_z])

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
dissimilarity_matrix([Var_w , Var_x , Var_y , Var_z])
