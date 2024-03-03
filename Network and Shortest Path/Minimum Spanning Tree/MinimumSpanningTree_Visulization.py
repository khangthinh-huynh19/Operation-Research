
import cv2 as cv 
import numpy as np
import random 
import math
#random_y=[1,-1,1,-1,1,-1]
def randomize_y(x,center_x,center_y,radius):
    y=(radius**2-(x-center_x)**2)**0.5+center_y
    return y
blank=np.zeros((900,900,3),dtype='uint8')

matrixD_cop=np.array([[10000,1,5,7,9,10000],[1,10000,6,4,3,10000],
[5,6,10000,5,10000,10],[7,4,5,10000,8,3],
[9,3,10000,8,10000,10000],[10000,10000,10,3,10000,10000]])


connect_node=[0,0,0,0,0,0]
center_node=[[350,350],0,0,0,0,0]
spanning=[[1,2], [4,3], [None], [5], [None],[None]]
i=1

#Drawing the starting node
cv.circle(blank,(350,350),20,(255,255,255),2)
cv.putText(blank,str(0),(350-10,350+10),
cv.FONT_HERSHEY_COMPLEX,1,(255,255,255))

for node in connect_node:
    for near_node in spanning[node]:
        if near_node != None:
            connect_node[i]=near_node
            print('Connect node: ', connect_node)

            #Indexing dij, dij is also the radius of the node
            dij=matrixD_cop[node,near_node]*70

            #Calculating the center for node j
            x_random_node_j=random.choice(np.linspace(center_node[node][0]-dij,center_node[node][1]+dij,6))
            y_random_node_j=randomize_y(x_random_node_j,center_node[node][0],center_node[node][1],dij)
            #print('y_random_node_j: ',y_random_node_j)
            x_random_node_j=math.floor(x_random_node_j)
            y_random_node_j=math.ceil(y_random_node_j)

            #Drawing node in the blank image
            cv.circle(blank,(x_random_node_j,y_random_node_j),20,(255,255,255),2)
            cv.putText(blank,str(near_node),(x_random_node_j-10,y_random_node_j+10),
            cv.FONT_HERSHEY_COMPLEX,1,(255,255,255))

            #Drawing arc between node i and j
            cv.line(blank,(center_node[node][0],center_node[node][1]),(x_random_node_j,y_random_node_j),
            (255,255,255),2)

            #Adding the center of node j to the center_node list
            #It is used to calculate the next near node
            center_node[near_node]=[x_random_node_j,y_random_node_j]
            print('Center node: ',center_node)

            #Recursion for i
            i=i+1

cv.imshow('Minimum Spanning Tree Network',blank)
cv.waitKey(0)