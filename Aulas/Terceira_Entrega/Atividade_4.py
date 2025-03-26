import numpy as np
import random

# Criar uma matriz de tamanho qualquer
linhas = random.randint(2, 5)
colunas = random.randint(2, 5)
matriz = np.zeros((linhas, colunas), dtype=int)

print(matriz)
# Extrair número de linhas e colunas
total_elementos = linhas * colunas

# Determinar se o vetor unidimensional teria número par ou ímpar de elementos
paridade = "par" if total_elementos % 2 == 0 else "ímpar"

print(f"A matriz gerada tem {linhas} linhas e {colunas} colunas, totalizando {total_elementos} elementos.")
print(f"Se convertida para um vetor unidimensional, teria um número {paridade} de elementos.")
