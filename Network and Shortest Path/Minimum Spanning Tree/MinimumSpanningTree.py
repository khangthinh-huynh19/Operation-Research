'''The code is used for Minimum Spanning Tree Network, which is very common in Operation Research'''

import numpy as np
node=6
#Create matrix D among nodes in the network
# node=int(input('Input the number of nodes: '))
# matrixD=[]
# for row in range(node):
#     D_row=[]
#     for col in range(node):
#         print('If there are no directed arc between two node or node-to-node, please input a big value')
#         dij=int(input('Distance between node' + str(row) + 'and' + str(col)+ ': '))
#         D_row.append(dij)
#     matrixD.append(D_row)
# matrixD=np.array(matrixD)
matrixD=np.array([[10000,1,5,7,9,10000],[1,10000,6,4,3,10000],
[5,6,10000,5,10000,10],[7,4,5,10000,8,3],
[9,3,10000,8,10000,10000],[10000,10000,10,3,10000,10000]])

#Create a replicated version of matrixD for drawing the network
matrixD_cop=matrixD.copy()

#Choose the starting node
starting_node=int(input('Choose your starting node: '))
print('Note: In this system, the starting node must be (order of node - 1)')
C=[starting_node]
#C_bar=[0,2,3,4,5]
#pairs contains the minimum arc
pairs=[]
for k in range(node-1):
    print('Iteration ',k)
    unconnected_matrix=[] #Operation matrix
    for selected_node in C:
        unconnected_matrix.append(matrixD[selected_node ,:])
    unconnected_matrix=np.array(unconnected_matrix)
    #print(unconnected_matrix)

    #Find the nearest node of C
    nearest_node=np.where(unconnected_matrix==np.min(unconnected_matrix))
    min_row=unconnected_matrix[nearest_node[0][0],:]
    print('The new node added to the spanning tree is: ',nearest_node[1][0])

    #Indexing from the matrix D
    connected_node=np.where(np.all(matrixD==min_row,axis=1)) #trả ra node có điểm gần nhất
    print('The connected node is: ',connected_node[0][0])
    #3
    # =np.array(index)
    r=connected_node[0][0] #Connected node
    c=nearest_node[1][0] #New nearest node

    #Repecling the added value dij with BIG M to avoiding the repitition
    matrixD[r,c]=10000
    matrixD[c,r]=10000
    
    #Adding the new arc the tree
    pairs.append([r,c])
    #Adding new nearest node for the next iteration
    C.append(c)

print('The minimum spanning tree is: ',pairs)
C.sort()
print('The C set is: ',C)

#Create data for creating the spanning tree network
spanning=[]
for node in C:
    connect_nodes=[]
    for pair in pairs:
        if pair[0]==node:
            connect_nodes.append(pair[1])
    if connect_nodes==[]:
        connect_nodes=[None]
    spanning.append(connect_nodes)
print('Spanning list: ',spanning)

