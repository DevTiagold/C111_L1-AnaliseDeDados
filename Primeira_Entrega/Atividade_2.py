valor = int(input("De qual valor gostaria de ver a tabuada? "))
limite = int(input("Qual o limite que gostaria de ver? "))

for c in range(0, limite + 1):
    resultado = valor * c
    print("{} x {} = {}" .format(valor, c, resultado))

