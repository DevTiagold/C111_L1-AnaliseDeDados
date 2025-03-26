import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

#retorna o menor valor e maior valor
print(arr1.min(), arr1.max())
#retorna o indice do maior valor e indice do menor valor
print(arr1.argmin(), arr1.argmax())
#calcula media dos elementos de um numpy array
print(arr1.mean(), arr1.sum())


#realizando operações entre dois ou mais arrays
arr3 = arr1 + arr2
print(arr3)

#para concatenar dois ou mais arrays numpy
arr3 = np.concatenate((arr1, arr2))
print(arr3)
