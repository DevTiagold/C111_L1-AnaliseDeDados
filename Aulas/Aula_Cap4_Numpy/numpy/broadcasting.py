import numpy as np
#isso permite transformar um array em uma matriz
mtz = np.arange(9).reshape((3,3))
print(mtz)

#broadcasting(espalhar) --> fazendo uma operação em cada um dos elementos
print(mtz/2)
print(mtz*5)