import numpy as np
mtz = np.arange(1,10,1).reshape((3,3))


print(mtz>5)#mostra as posiçõas em que os elementos são maiores que 5, sendo false os menores e true os maiores
print(mtz[mtz>5])#retorna os elementos que são maiores

#mostrando apenas os elementos pares
print(mtz%2==0)
print(mtz[mtz%2==0])