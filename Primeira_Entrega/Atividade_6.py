import math

numero = float(input("Digite um valor: "))
print("Vamos aplicar algumas funções sobre este valor...")

raiz = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
pt_inteira = math.trunc(numero)

print("Raiz: {:.2f} \nFunção teto: {} \nFunção chão: {} \npt_inteira: {}".format(raiz, teto, chao, pt_inteira))