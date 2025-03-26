import numpy as np
import random

arr1 = np.ones(8)
arr2 = np.random.randint(0,9,8)

arr3 = arr1 + arr2
print(arr3)

if arr3.sum() >= 40:
   print(np.reshape(arr3, (4,2)))
else:
   print(np.reshape(arr3, (2,4)))

