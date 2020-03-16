import numpy as np 

gps_x = np.loadtxt('Graph1.txt',delimiter=',',dtype='Float64',skiprows=1)[:,1]
gps_x_std = np.std(gps_x)
accelo_x = np.loadtxt('Graph2.txt',delimiter=',',dtype='Float64',skiprows=1)[:,1]
accelo_x_std = np.std(accelo_x)

print(f'GPS X Std:{gps_x_std}')
print(f'ACCELEROMETER X Std:{accelo_x_std}')

