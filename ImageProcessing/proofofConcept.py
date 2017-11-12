#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# work on variable starting point using the where module in the node class 
"""
Created on Mon Oct 23 12:37:13 2017

@author: ymubarak
"""

import numpy as np 
import math 


class node():
    def __init__(self,xloc,yloc):
        self.yloc = yloc
        self.xloc =xloc
        self.state = 0 
        self.angle = 0 
        self.slope = 0 
    def paint(self ): 
        self.state = 1 
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
        i=  self.where(neighbors)
        neighbors.remove(neighbors[i])
        return neighbors 
    
    def nextorientation(self,current_theta, linewidth ):
        pass 
    def findnodepos(self, current_theta):
        pass 
    def getdistance(self, another_node):
        x = self.xloc - another_node.xloc 
        y = self.yloc - another_node.yloc 
        dist = (x**2 + y**2) ** 0.5 
        return dist 
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
    
            
    
#doesnt work     
    def gettangent(self,neighbors):
        
        x = np.array([n.xloc for n in neighbors]).reshape(len(neighbors),1) 
        y = np.array([n.yloc for n in neighbors]).reshape(len(neighbors),1)
        #shift 
        x = x- self.xloc 
        y = y - self.yloc 
        m = np.linalg.lstsq(x,y)[0]
        error = m*x - y ; 
        self.slope = m 
        return m, error, x, y 
    def getangle(self):
        op_ad = self.slope[0][0]
        self.angle = math.atan(op_ad**-1)
        return self.angle
        
    
    
    

class car(): 
    def __init__(self):
        self.theta = 0 
        self.paint_state = False 
    
    
    
class Image() :
    def __init__(self, filepath, pixelscale = [1,1], 
                 starting_orientation = 0 ): #startingpoint = [])  : 
        f= open(filepath,'r')
        
        self.linearray = np.array(f.readlines())
        self.dataarray = self.makenumpy() 
        self.path = filepath 
        self.pixelscale = pixelscale 
        self.centroids = self.columncentroids()
        self.nodelist = self.getNodes()
        #if startingpoint == []: 
           # self.startingpoint = self.startnode()
            
        self.orientation0 = starting_orientation 
        
    def startnode(self) : 
        return self.nodelist[0]
    
    def makenumpy(self):
        nump =np.array(self.linearray)
        empty = []
        for i in range(1,len(nump)): 
            column = [int(x) for x in nump[i] if x!= "\n"]
            empty.append(column)
        return np.array(empty)

    def getNodes(self) :
        nodelist = list() 
        mat= self.centroids
        for i in range(0,len(mat[0])):
            x = mat[0][i]
            y = mat[1][i]
            nodelist.append(node(x,y)) 
        return nodelist 
    

    def setpixelscale(self, ps) : 
        self.pixelscale = ps

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
    
    def NearestNode(self, point):
        distx = self.centroids[0] - point[0]
        disty = self.centroids[1] - point[1]
        
        dists = (distx**2 + disty**2)**0.5
        non_zero = dists[dists!=0]
        min_val = np.argmin(non_zero)
        
        ind = np.where(dists == min_val)[0][0]
        return self.nodelist[ind] , dists[ind]
    
    
    def getNextStates(self,neighborhood_size) :
        #returns for each node in self.getNodes() 
        # array [angle_to_next_node, distance_to_next_node, paint_state]
        total_unpainted = self.getNodes() 
        painted = list() 
        Instructs = list () 
        n0 = total_unpainted[0]
        i = 1 
        
        while not not total_unpainted : 
            i =+ 1 
            neighbors = n0.findneighbors(total_unpainted,neighborhood_size) 
            [n1,dist_2_n1] = self.NearestNode([n0.xloc, n0.yloc])
            tan = n0.gettangent([n1])
            ang = n0.getangle()
            # if you can't find neighbors that need to be painted. 
            if not neighbors : # empty neighbors  
                paint_state = 0 
            else :
                paint_state = 1 
            
            Instructs.append([ang, dist_2_n1, paint_state])
            n0.paint()
            painted.append(n0)
            total_unpainted.remove(n0)
            n0 = n1 
    
        return Instructs 
                
                
    
def tolist(xdict):
    y = []
    x = []
    for key, values in xdict.items() : 
        if not not xdict[key]:
            y.append( key*np.ones(len(xdict[key])) )
            x.append([j for j in xdict[key]])
    x=np.array(x)
    y=np.array(y)
    x=x.reshape(x.size)
    y=y.reshape(y.size)
    return x,y 
            
        
      



