# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:04:45 2017

@author: Ymubarak
"""

# Instructions : 
# - orient your picture such that the car positive movement (forward) is in the y direction 
# - use the test.ipynb to see if the path you drew is binarized accurately enough 
# - if not either try giving a more magnified picture or trying increasing the neighborsize 


import numpy as np 
import math as m 
class node() : 
    
    def __init__(self,xloc,yloc):
        self.yloc = yloc
        self.xloc =xloc
        
    def findneighbors(self,nodelist,size):
        x =np.array( [n.xloc for n in nodelist ])
        y = np.array([n.yloc for n in nodelist]) 
        
        x_upper = self.xloc + size 
        x_lower = self.xloc - size 
        y_upper = self.yloc + size 
        y_lower = self.yloc - size 
        
        boolx = np.logical_and(x <= x_upper, x >= x_lower)
        booly = np.logical_and(y <= y_upper, y >= y_lower)       

        boolfin= np.logical_and(boolx,booly)  
        
        l = np.array(nodelist)
        neighbors = l[boolfin]
        neighbors= list(neighbors)
        if len(neighbors) > 1 : 
            i=  self.where(neighbors)
            neighbors.remove(neighbors[i])
            return neighbors 
        else : 
            return []
        
    def equals(self,node):
        n1 = False 
        n2 = False 
        if node.xloc == self.xloc :
            n1= True 
        if node.yloc == self.yloc :
            n2 = True 
        if n2 & n1: 
            return True 
        else : 
            return False 
        
    def where(self, nodelist) : 
        i = [x for x in range(0,len(nodelist)) if self.equals(nodelist[x])]
        return i[0]
    

class Image() :
    def __init__(self, filepath):
        f= open(filepath,'r')
        self.linearray = np.array(f.readlines())
        self.dataarray = self.makenumpy() 
        self.centroids = self.columncentroids()

    def makenumpy(self):
        nump =np.array(self.linearray)
        empty = []
        for i in range(1,len(nump)): 
            column = [int(x) for x in nump[i] if x!= "\n"]
            empty.append(column)
        return np.array(empty)

    def columncentroids(self):
        #x_averages[colum_number] =[cetroid1, centroid2, ....]
        mat = self.dataarray 
        x_averages = dict()         
 
        for i in range(0, mat.shape[0]) :
            x_averages[i] = list() 
            number_of_entries = 0 
            aggregate_pos = 0 
            for j in range(0,mat.shape[1]):
                if aggregate_pos !=0 and mat[i,j] == 0 : 
                    x_averages[i].append(aggregate_pos/float(number_of_entries))
                    aggregate_pos = 0 
                    number_of_entries = 0 
                elif mat[i,j] != 0 : 
                    number_of_entries = number_of_entries + 1 
                    aggregate_pos = aggregate_pos + j 
                   # print(aggregate_pos !=0 and mat[i,j] == 0 )
        x,y = tolist(x_averages)

        return x,y 
    
    def getNodes(self) :
        nodelist = list() 
        mat= self.centroids
        for i in range(0,len(mat[0])):
            x = mat[0][i]
            y = mat[1][i]
            nodelist.append(node(x,y)) 
        return nodelist 
    
    def NearestNode(self, point,nodelist):
        xlocs = [n.xloc for n in nodelist]
        ylocs = [n.yloc for n in nodelist]
        distx = np.array(xlocs)- point[0]
        disty = np.array(ylocs) - point[1]
        
        dists = (distx**2 + disty**2)**0.5
        non_zero = dists[dists!=0]
        ind1 = np.argmin(non_zero)
        min_val = non_zero[ind1]

        ind = np.where(dists == min_val)[0][0]
        
        return nodelist[ind] , dists[ind]

    def getNextStates(self,neighborhood_size) :
        #returns for each node in self.getNodes() 
        # array [angle_to_next_node, distance_to_next_node, paint_state]

        total_unpainted = self.getNodes() 
        painted = list() 
        Instructs = list () 
        n0 = total_unpainted[0]
        i = 1 
        
        while  len(total_unpainted) > 1 : 
            neighbors = n0.findneighbors(total_unpainted,neighborhood_size) 
            [n1,dist_2_n1] = self.NearestNode([n0.xloc, n0.yloc],total_unpainted)
            ang = getangle(n0,n1) 

            # if you can't find neighbors that need to be painted. 
            if not neighbors : # empty neighbors  
                paint_state = 0 
            else :
                paint_state = 1 
            
            Instructs.append([ang, dist_2_n1, paint_state])
            painted.append(n0)
            total_unpainted.remove(total_unpainted[n0.where(total_unpainted)])
            n0 = n1 
            i = i + 1 

    
        return Instructs 



def tolist(xdict):
    y = []
    x = []
    for key, values in xdict.items() : 
        if not not xdict[key]:
            for i in range(0,len(xdict[key])):
                y.append( key )
                x.append(xdict[key][i])

    x=np.array(x)
    y=np.array(y)
    x=x.reshape(x.size)
    y=y.reshape(y.size)
    return x,y 

def getangle(node1, node2):
    deltx = node2.xloc - node1.xloc 
    delty= node2.yloc - node1.yloc 

    #print("delta x is " + str(deltx )) 
    #print("delta y is "+ str(delty)) 
    angle = m.atan2(delty,deltx) 
    #print("angle from the negative x axsis : " + str(angle)) 

    return angle 
