#draw unit Sample sequence
import numpy as np 
import matplotlib.pyplot as plt

#samples 
shift_amount = 2
n= np.arange(-5,6,1, dtype=int)#range from -5 to 5 and increase by 1
print(n)#print values of n
unit_sample = np.where(n==0,1,0) #Draw unit_sample
unit_sample_shift = np.roll(unit_sample,shift_amount)#Draw unit_sample_shift
print(unit_sample)#print values of unit_sample

plt.stem(n,unit_sample,label="unit_sample")#draw axis x and y 
plt.stem(n,unit_sample_shift,label="unit_sample_shift",linefmt="r",markerfmt="ro")#draw axis x and y 
plt.title('unit sample sequence')#Title
plt.xlabel('n')#x axis is n
plt.ylabel('unit_sample')#y axis is unit_sample
plt.legend()#To Draw Label
plt.grid(True)#To draw Sqaures