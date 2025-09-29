import numpy as np 
#/// Saving and loading ////
array = np.array([[1,2,3],[4,5,6],[7,8,9]])

np.savetxt('array.txt', array, delimiter=',')
print("Array saved to 'array.txt'")

loaded_array = np.loadtxt('array.txt', delimiter =',')
print(loaded_array)

#/// Saving and loading binary files ////
np.save("array.npy", array)

loaded_binary_array = np.load("array.npy")
print(loaded_binary_array)