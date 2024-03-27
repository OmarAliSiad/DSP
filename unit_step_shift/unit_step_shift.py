#draw unit Sample sequence
import numpy as np 
import matplotlib.pyplot as plt

#samples 
shift_amount = 2
n= np.arange(-5,6,1, dtype=int)#range from -5 to 5 and increase by 1
print(n)#print values of n
unit_step = np.where(n>=0,1,0) # Draw unit_step
unit_step_shift=np.roll(unit_step,shift_amount)# Draw unit_step_shift 
print(unit_step)#print values of unit_sample

plt.stem(n,unit_step,label="unit_step")#draw axis x and y 
plt.stem(n,unit_step_shift,label="unit_step_shift",linefmt="r",markerfmt="co")#draw axis x and y 
plt.title('unit step sequence')#Title unit step sequence
plt.xlabel('n')#x axis is n
plt.ylabel('sample_unit')#y axis is unit_sample
plt.legend()#To Draw Label
plt.grid(True)#To draw Sqaures