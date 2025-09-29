import numpy as np

#/// Basic operations ////
a = np.array([1,2,3,])
b = np.array([4,5,6,])

sum_result = a + b
product_result = a * b

print("Sum:", sum_result)
print("Product:", product_result)

#/// Broadcasting addition ////

a = np.array([[1,2,3], [4,5,6], [7,8,9]])
b = np.array([10,20,30])

result = a + b

print("Broadcasted Addition Result:\n", result)

#/// Universal functions ////

data = np.array([[ 10, 20], [30, 40], [50, 60]])

print("total sum:", np.sum(data))
print("mean per column:", np.mean(data, axis=0))
print("mean per row:", np.mean(data, axis=1))

#/// Boolean indexing ////

arr = np.array([10,15,20,25])
mask = arr > 15
filtered= arr[mask]

print("Filtered array (elements > 15):", filtered)