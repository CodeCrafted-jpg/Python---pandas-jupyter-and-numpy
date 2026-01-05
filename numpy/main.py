import numpy as np
# array=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#                 ,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#                 ,[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])

# print(array[0,0,3])


# number=array[0,0,3] + array[0,1,2]
# print(number)
#array[start:end:step]
array=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#print(array[0:3])

#print (array[::-1])
print(array[:,::2])

