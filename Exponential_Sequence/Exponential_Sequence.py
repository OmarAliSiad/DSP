#Exponential Sequence 
#have 4 cases 
#First Case -> a > 1
#Second Case -> 1 > a >0
#Third Case -> a > -1
#Fourth Case ->0 > a < -1'

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6,1,dtype=int);#range from -5 to 5 and increase by 1

a1=0.8#case 1
a2=1.2#case 2
a3=-0.8#case 3
a4=-1.2#case 4

y1=a1**n#Exponential decreasing 
y2=a2**n#Exponential increasing 
y3=a3**n#Toggle from left to right
y4=a4**n#Toggle from right to left 

plt.figure(figsize=(10,5))#figure that will draw on it 
plt.subplot(2,2,1)#Draw in First plot
plt.stem(n,y1,label='0 < a < 1')#draw axis x and y 
plt.title('0 < a < 1')#Exponential decreasing 
plt.xlabel('n')#name x axis as n 
plt.ylabel('y(n)')#name y axis as y
plt.legend()#to draw label
plt.grid(True)#To draw Sqaures 

plt.subplot(2,2,2)#Draw in Second plot
plt.stem(n,y2,label='a > 1')#Draw Two axais
plt.title('a > 1')#Print Statment a > 1
plt.xlabel('n')#name x axis as n 
plt.ylabel('y(n)')#name y axis as y
plt.legend()#to draw label
plt.grid(True)#to draw squares in figure
         
plt.subplot(2,2,3)#Draw in Third plot
plt.stem(n,y3,label='0 > a > -1')#Draw Two axais
plt.title('0 > a > -1')#Print Statment 0 > a > -1
plt.xlabel('n')#name x axis as n 
plt.ylabel('y(n)')#name y axis as y
plt.legend()#to draw label
plt.grid(True)#to draw squares in figure
         
plt.subplot(2,2,4)#Draw in Fourth plot
plt.stem(n,y4,label='0 > a < -1')#Draw Two axais
plt.title('0 > a < -1' )#Print Statment 0 > a < -1
plt.xlabel('n')#name x axis as n
plt.ylabel('y(n)')#name y axis as y
plt.legend()#to draw label
plt.grid(True)#to draw squares in figure

plt.tight_layout()#to not intersect with each other
plt.show()#Display