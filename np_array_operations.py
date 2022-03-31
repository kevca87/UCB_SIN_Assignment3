import numpy as np

a = np.zeros((8,8),dtype=int)
a[3,3] = -1
a[4,4] = -1
a[4,3] = 1
a[3,4] = 1

print(a[2:5,3])
print(a[2:5,3].shape)

v = np.array([1,2,0],dtype=int)

print(a)

a[2:5,3] = a[2:5,3] + v

print(a)

print(v.shape)
v = v.reshape(3,1)
print(v.shape)
print(v)