import numpy as np 
import matplotlib.pyplot as plt

#samples
n= np.arange(-5,6,1, dtype=int)

#unit step sequence 
unit_step=np.where(n>=0,1,0)

scaling_factor = 2 
unit_step_scale=unit_step*scaling_factor

plt.stem(n,unit_step,label='unit step')
plt.stem(n,unit_step_scale,label='unit step scale',linefmt='r',markerfmt='ro')
plt.title('unit step sequence')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()



