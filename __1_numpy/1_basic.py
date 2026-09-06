import numpy as np 
# print(np.__version__) this just used to get the version of the numpy

array=np.array([[1,2,3],
                [2,3,4],
                [2,3,4]])
# array=array*2
print(array)
print(type(array))
print(array.ndim)
print(array.shape)
print(array[0][0])
number=array[0,0]+array[1,0]+array[1,2]
print(number)