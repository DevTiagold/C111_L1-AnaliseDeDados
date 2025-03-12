#Criando um numpy arrays com mais facilidade
#Estruturando rapidamente uma matriz de 1's

import numpy as np
#cria matriz 5 por 5 só de 1
mtz = np.ones([5,5])
print(mtz)

# arange --> cria um array de 0 a 10
mtz = np.arange(10)
print(mtz)

#de forma mais detalhada que exprime o inicio, fim e taxa de crescimento
arr = np.arange(10,30,2)
print(arr)