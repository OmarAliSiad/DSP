#draw unit Sample sequence
import numpy as np 
import matplotlib.pyplot as plt

#samples 
shift_amount = 2
n= np.arange(-5,6,1, dtype=int)#range from -5 to 5 and increase by 1
print(n)#print values of n
unit_ramp = np.where(n>=0,n,0) #Draw unit Ramp 
unit_ramp_shift=np.roll(unit_ramp,shift_amount)##Draw unit Ramp shift 
print(unit_ramp)#print values of unit_sample

plt.stem(n,unit_ramp,label="unit_ramp")#draw axis x and y 
plt.stem(n,unit_ramp_shift,label='unit ramp shift',linefmt='r',markerfmt='ro')
plt.title('unit Ramp sequence')#Title
plt.xlabel('n')#x axis is n
plt.ylabel('unit_ramp')#y axis is unit_sample
plt.legend()#To Draw Label
plt.grid(True)#To draw Sqaures