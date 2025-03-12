#Realizando reshape de numpy arrays
import numpy as np
#isso permite transformar um array em uma matriz
mtz = np.arange(9).reshape((3,3))
print(mtz)

# #numero de elementos -->size
# print(mtz.size)
# #proporção da matriz -->shape
# print(mtz.shape)
# #numero de dimensões -->ndim
# print(mtz.ndim)

#Operações nas linhas e colunas da matriz
#realiza a somas das colunas
print(mtz.sum(axis=0))
#soma das linhas
print(mtz.sum(axis=1))

#soma apenas da primeira linha
print(mtz.sum(axis=0)[0])

