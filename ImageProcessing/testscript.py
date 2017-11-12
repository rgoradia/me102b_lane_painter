# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:39:38 2017

@author: Ymubarak
"""

import proofofConcept 
#path = '/home/ymubarak/ME102B/me102b_lane_painter/ImageProcessing/Square.txt'
path = "C://Users//Ymubarak//Documents//ME102B//me102b_lane_painter//ImageProcessing//Square.txt"

f= open(path,'r')

# get info about shit 
lines = f.readlines 

lines = f.readlines()
mat = np.array(lines)

nodelist = list() 

n0 =nodelist[100]
ns = n0.findneighbors(nodelist,3) 
x = [n.xloc for n in ns]
y = [n.yloc for n in ns]
plt.scatter(x,y)    

x1 = [n.xloc for n in nodelist]
x2 = [n.yloc for n in nodelist]
plt.scatter(x1,x2)  
        
[n,error]=n0.gettangent(ns)
plt.figure()  
plt.scatter(x , n[0]*x) 
plt.scatter(x,y) 

