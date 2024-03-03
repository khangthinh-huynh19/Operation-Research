import numpy as np
'This code is used for Floyd Algorithm, which determine the shortest path between any two nodes in a network'
#Creating matrix D (Distance Matrix)
rows=int(input("Number of nodes in the network: "))
cols=rows
matrixD=[]
for i in range(rows):
    D_row=[]
    for j in range(rows):
        dij=int(input("Input the distance from "+str(i) +" to " + str(j)+ ": "))
        D_row.append(dij)
    matrixD.append(D_row)
matrixD=np.array(matrixD)
print("The distance matrix D is: \n",matrixD)

#Iteration k
for k in range(rows):
    #pivot row k and pivot column k
    pivot=k
    for row in range(rows):
        for col in range(cols):
            dij = matrixD[row,col]

            #Ignoring the node(k,k)
            if row != k and col != k:
                #Triple Operation
                triple_sum=matrixD[row,k]+matrixD[k,col]
                if triple_sum<dij:
                    matrixD[row,col]=triple_sum
print("The shortest path matrix is:  \n",matrixD)

