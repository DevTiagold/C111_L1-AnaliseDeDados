import pandas as pd
import numpy as np
#Pandas "series"

#labels
labels = ['a', 'b', 'c']
dados = [10,20,30]

#Criando series com dua listas
s1 = pd.Series(index=labels , data=dados)
# print(s1)
# print(type(s1))#verificando o tipo

#criando series com um dicionario
s2 = pd.Series({'a':10, 'c':50, 'd':80})

# #chamando o valor da series
# print(s1['b'])
#Realizando operações entre series
# print(s1 + s2)
#
# #refazendo a soma acima, tratando aos valores que não foram atribuídos a um dos indexes equivalentes como 0
# print(s1.add(s2, fill_value=0))

#Acessar apenas o que precisamos
# print(s1[['a', 'c']]) # se queremos trazer multiplas colunas precisamos usar uma lista

#condicionais no pandas(identico ao numpy)
print(s1 > s1.mean())
print(s1[s1 > s1.mean()])



































