#Program to find the inverse of a matrix.
#Developed by: Rohith S
#RegisterNumber: 25008317
import numpy as np
a = np.array([[2,1,1],[1,1,1],[1,-1,2]])
b = np.linalg.inv(a)
print(b)