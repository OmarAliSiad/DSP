import numpy as np 
import matplotlib.pyplot as plt

#samples
n= np.arange(-5,6,1, dtype=int)

#unit sample sequence 
unit_sample =np.where(n==0,1,0)

#scaling sequence
scaling_factor =2 
unit_sample_scale=unit_sample*scaling_factor

plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.stem(n,unit_sample,label='unit sample')
plt.stem(n,unit_sample_scale,label='unit sample scale',linefmt='r',markerfmt='ro')
plt.title('unit sample sequence')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.legend()

