import numpy as np

array_1 = np.array([1,1,1,1,1,1,1,1])
array_2 = np.array([2,4,5,6,9,9,1,8])

soma_array = array_1 + array_2

if soma_array.sum() >= 40:
    soma_array = soma_array.reshape(8,1)
else:
    soma_array = soma_array.reshape(1,8)

print(soma_array)