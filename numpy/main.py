import numpy as np
array1=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
                ,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
                ,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

print(array1[0,0,3])


number=array1[0,0,3] + array1[0,1,2]
print(number)
# array1[start:end:step]
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print(array[0:3])

print (array[::-1])
print(array[:,::2])

print((array[0:3]+1))