#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 12:37:13 2017

@author: ymubarak
"""

import numpy as np 
import matplotlib.pyplot as plt
 
path = '/home/ymubarak/ME102B/me102b_lane_painter/ImageProcessing/Square.txt'


f= open(path,'r')

# get info about shit 
lines = f.readlines 

lines = f.readlines()
mat = np.array(lines)

nodelist = list() 



class node():
    def __init__(self,xloc,yloc):
        self.yloc = yloc
        self.xloc =xloc
        self.state = 0 
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
        return neighbors 
            
        
    def gettangent(self,neighors):
        
        x = [n.xloc for n in neighbors]
        y = [n.yloc for n in neighbors]
        m = np.linalg.lstsq(x,y)
        error = m*x - y ; 
        return m,error 
    
        
        
    
class image() :
    def __init__(self, binary,nodelist):
        self.nodelist = nodelist 
        self.startnode = nodelist[0]
        self.binaryImage = binary 
    def gettangents (self) : 
        
        pass 
 
for i in range(0,len(mat)):
    for j in range(0,len(mat[i])): 
        if mat[i][j]== '1' :
            nodelist.append(node(i,j))       

n0 =nodelist[100]
ns = n0.findneighbors(nodelist,3) 
x = [n.xloc for n in ns]
y = [n.yloc for n in ns]
plt.scatter(x,y)    

x1 = [n.xloc for n in nodelist]
x2 = [n.yloc for n in nodelist]
plt.scatter(x1,x2)  
        
n0.gettangent(ns) 



