#draw unit Sample sequence
import numpy as np 
import matplotlib.pyplot as plt

#samples 
n= np.arange(-5,6,1, dtype=int)#range from -5 to 5 and increase by 1
print(n)#print values of n
unit_sample = np.where(n==0,1,0) #Draw unit_sample
print(unit_sample)#print values of unit_sample

plt.stem(n,unit_sample,label="unit_sample")#draw axis x and y 
plt.title('unit sample sequence')#Title
plt.xlabel('n')#x axis is n
plt.ylabel('unit_sample')#y axis is unit_sample
plt.legend()#To Draw Label
plt.grid(True)#To draw Sqaures