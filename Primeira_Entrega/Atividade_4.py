dist = float(input("Qual a distância(KM) que será percorrida? "))
if dist <= 200:
    valor = dist * 0.50

else:
    valor = dist * 0.45

print("Valor da passagem = R$ {:.2f}".format(valor))
