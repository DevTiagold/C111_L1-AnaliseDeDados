import pandas as pd
import numpy as np
#Pandas DataFrame

#Plantando a semente aleatória
np.random.seed(10)

#Criando um DataFrame
df = pd.DataFrame(index=['a', 'b', 'c', 'd', 'e'],
                  columns=['w', 'x', 'y', 'z'],
                  data=np.random.randint(1,50,[5, 4]))
# print(df)
#
# #slicing com multiplas colunas
# print(df[['w','z']])

#acessando um elemento do dataframe --> coluna x linha
# print(df['x']['b'])

#Fazendo Slicing com loc()-->labels ou iloc()-->notação do numpy
#Slicing com loc()-->Localization
print(df.loc[['a', 'b'], ['w', 'x', 'z']])

#Slicing com Iloc-->index localization
print(df.iloc[0:2, :])
#Um dataframe é como uma planilha do excel dentro do python
print(df.loc[['a', 'b'], ['w', 'x', 'z']])