import numpy as np 

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(np.dot(array1, array2))
print(np.matmul(array1, array2))

print(array1 * array2)    # This is broadcasting
# Broadcasting is applied when the dimensions of columns starting from right are same or one value is 1

# NumPy broadcasts array1 to shape (4, 4) by repeating the row 4 times
# It broadcasts array2 to shape (4, 4) by repeating the column 4 times