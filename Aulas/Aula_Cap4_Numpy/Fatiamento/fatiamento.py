#slicing de numpy arrays
import numpy as np

mtz = np.arange(1,10,1).reshape((3,3))
print(mtz)


# slicing em uma unica linha
print(mtz[2]) #linha de indice 2

#slicing de multiplas linhas
print(mtz[1:]) #pega a partir da linha 1 e vai até o fim, no caso 2

#slicing de uma coluna
print(mtz[:, 1])

#slicing de multiplas colunas
print(mtz[:,1:])