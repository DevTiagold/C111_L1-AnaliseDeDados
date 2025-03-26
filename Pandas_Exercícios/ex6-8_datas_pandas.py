import pandas as pd  

# Criando os dados do DataFrame  
data = {  
    'W': [10, 29, 30, 43, 37],  
    'X': [37, 26, 9, 41, 48],  
    'Y': [16, 30, 10, 12, 12],  
    'Z': [1, 49, 1, 17, 25]  
} 
# Criando o DataFrame com os índices A e B  
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D', 'E'])  

# Exibindo o DataFrame  
print(df)  

# Mostrando os valores da coluna 'X' que são menores que 30
print("------------------------Valores da coluna 'X' menores que 30------------------------")
print(df[df['X'] < 30]['X'])
print("------------------------------------------------------------------------------------")

#Apresentando a média da linha D usando loc e a soma da linha usando iloc
print("------------------------Média da linha D usando loc------------------------")
print(df.loc['D'].mean())
print("------------------------Soma da linha E usando iloc------------------------")
print(df.iloc[4].sum())
print("------------------------------------------------------------------------------------")

#Fazendo slicing nas linhas A, C e E junto com as colunas X e Y.
print("------------------------Slicing nas linhas A, C e E junto com as colunas X e Y------------------------")
print(df.loc[['A', 'C', 'E'], ['X', 'Y']])
print("------------------------------------------------------------------------------------")

#mostre qual seria a soma dos elementos de cada uma destas linhas em cada uma destas colunas.
print("------------------------Soma dos elementos de cada uma destas linhas em cada uma destas colunas------------------------")
print(df.loc[['A', 'C', 'E'], ['X', 'Y']].sum())