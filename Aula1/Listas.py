#Listas ---> diferentemente das tuplas que usa (), as listas usan []
nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

#As mesmas funcionalidades de slicing para tuplas são aplicadas a Listas
#As listas são mutáveis

# INSERT and APPEND
nomes.append('Bulma') #--> appendar, inserir no final expressão de programador
nomes.insert(2, 'Piccolo') #insert, coloca na posição do index desejado jogando o elemento do index para "frente"
print(nomes)

# UPDATE
nomes[0] = 'Goten' #Atualiza/suubstitui o elemento

# DELETE
del nomes[1] #Excluindo pelo indice / nomes.pop(1)
nomes.remove('Trunks')
print(nomes)

if 'Piccolo' in nomes:   # Podemos fazer verificações tanto com listas como também com tuplas, mas as listas possuem um leque maior de manipulaçao!
    print('Piccolo is here!!')