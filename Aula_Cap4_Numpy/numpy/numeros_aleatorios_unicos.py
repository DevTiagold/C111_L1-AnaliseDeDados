#Elementos aleatórios e únicos
import numpy as np
import random

#semente de dados para gerar os mesmo numeros laatórios
np.random.seed(10)

#Entre 20 e 50 sorteamos 10 numeros aleatórios colocados em um array unidimensional
arr = np.random.randint(20, 50, 10)
print(arr)

#para BIDIMENSIONAL
arr = np.random.randint(20, 50, [2,2])
print(arr)

#Connceito de UNICOS
arr = np.random.randint(20, 50, [5,5])
print(arr)
#etrido elementos unicos com o unique
print(np.unique(arr, return_counts=True))



