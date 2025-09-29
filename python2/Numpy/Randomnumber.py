import numpy as np

random_floats = np.random.rand(5)
print("Random floats:", random_floats)

#/// Random integers ////

random_integer = np.random.randint(10, 50, size=4)
print("Random integers between 10 and 50:", random_integer)

#/// Generate random numbers from a normal distribution ////

normal_distribution = np.random.randn(6)
print("normal distribution: ", normal_distribution)