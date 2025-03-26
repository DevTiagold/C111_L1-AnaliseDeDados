nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print(nomes)

#Slicing de dados --> fatiamento de uma estrutura
#No python, o primeito incide de uma coleção é INCLUSIVE e o segundo EXCLUSIVE
#Tuplas é um tipo de coleção imutável

print(nomes[0])  #Goku
print(nomes[:2]) #Goku e Vegeta
print(nomes[2:]) #Trunks e Gohan
print(nomes[1:3])#Vegeta e Trunks
print(nomes[-1]) #Gohan

#tentando alterar um tupla
nomes[0] = 'Bulma'
print(nomes)

#First Jump of the catkkk ---> Para que trabalhar com uma coleção imutável? Para trabalhar com coisas, ou melhor, informações que não são necessárias alterações
#Tuplas aceitam elementos Heteregêneos, embora em DataScience é importante trabalhar com dados homogêneos

