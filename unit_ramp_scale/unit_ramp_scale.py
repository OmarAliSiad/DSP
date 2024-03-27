import numpy as np 
import matplotlib.pyplot as plt

#samples
n= np.arange(-5,6,1, dtype=int)

#unit ramp sequence
unit_ramp=np.where(n>=0,n,0)

scaling_factor = 2
unit_ramp_scale=unit_ramp*scaling_factor

plt.stem(n,unit_ramp,label='unit ramp')
plt.stem(n,unit_ramp_scale,label='unit ramp scale',linefmt='r',markerfmt='ro')
plt.title('unit ramp sequence')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()