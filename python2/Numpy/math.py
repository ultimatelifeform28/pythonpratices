import numpy as np

# #///// angles////

angles = np.array([0,np.pi/2, np.pi, 3*np.pi/2])

result_sine = np.sin(angles)

print("Sine of angles:", result_sine)

#//// exponential ////

array = np.array([1,2,3,4,5,])

result_exp = np.exp(array)

print("Exponential of array:", result_exp)

#//// multidimensional ////

array_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])

array_3d = np.array([[1,2], [3,4], [5,6], [7,8]])


print(array_2d)
print(array_3d)

#//// element in multidimensional ////

array_2d = np.array([[10,20,30], [40,50,60], [70,80,90]])
array_3d = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])

element_2d = array_2d[1,2]  # Accessing element in 2D array (row 1, column 2)
element_3d = array_3d[1,0,1]  # Accessing element in 3D array (row 2, column 1)

print("Element in 2D array at (1,2):", element_2d)
print("Element in 3D array at (1,0,1):", element_3d)