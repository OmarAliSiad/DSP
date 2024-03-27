#draw unit Sample sequence
import numpy as np 
import matplotlib.pyplot as plt

#samples 
n= np.arange(-5,6,1, dtype=int)#range from -5 to 5 and increase by 1
print(n)#print values of n
unit_ramp = np.where(n>=0,n,0) #Draw Ramp unit
print(unit_ramp)#print values of unit_sample

plt.stem(n,unit_ramp,label="unit_ramp")#draw axis x and y 
plt.title('unit Ramp sequence')#Title
plt.xlabel('n')#x axis is n
plt.ylabel('unit_ramp')#y axis is unit_sample
plt.legend()#To Draw Label
plt.grid(True)#To draw Sqaures