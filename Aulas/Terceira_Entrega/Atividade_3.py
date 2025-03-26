
import numpy as np
import random

matriz = np.zeros((2, 2), dtype=int)
mina = (random.randint(0, 1), random.randint(0, 1))
matriz[mina] = 1
print(matriz)
while True:
    linha = int(input("Linha (0 ou 1): "))
    coluna = int(input("Coluna (0 ou 1): "))

    if matriz[linha, coluna] == 1:
        print("BOOM! Você perdeu!")
        break

    print("Seguro! Continue jogando.")
    if input("Jogar novamente? (s/n): ").lower() != 's':
        break
