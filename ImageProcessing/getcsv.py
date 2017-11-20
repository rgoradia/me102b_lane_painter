import Process as p 
import sys 
import csv 
import math as m 
import matplotlib.pyplot as plt 
import numpy as np 

def main() : 
    path = sys.argv[1]
    n_size  = float(sys.argv[2])

    Im = p.Image(path) 
    commands = Im.getNextStates(n_size)
    filename = path.replace("txt","csv")
    x = np.array(commands)
    np.savetxt(filename,x, delimiter=',')

   # plot and make sure if the all the path is painted 
    nodelist= Im.getNodes()
    n0 = nodelist[0]
    p0 = [n0.xloc , n0.yloc]
    for i in range(0,len(commands)):
        theta = commands[i][0]
        dist = commands[i][1]
        pn = [dist*m.cos(theta) + p0[0], dist*m.sin(theta) + p0[1]] 
        if  commands[i][2] : 
            plt.plot([p0[0], pn[0]],[p0[1], pn[1]] )
        p0= pn


    plt.show() 


if __name__ == "__main__":
	main() 



