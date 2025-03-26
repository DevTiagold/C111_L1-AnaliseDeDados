
dicionario = []

soma_idade = 0
cont = 0
pessoas_cadastradas = 0

veri = True
while veri ==True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M/F): ")
    dicionario.append({'nome':nome, 'idade':idade, 'sexo':sexo})

    soma_idade = soma_idade + idade
    if sexo == 'F' and idade < 20:
        cont = cont + 1
    pessoas_cadastradas = pessoas_cadastradas + 1

    decisao = input('Deseja inserir alguma pessoa? (s/n) -->')
    if decisao == 's':
        veri = True
    else:
        veri = False

print('\n')
print('Media de idade do grupo = {}' .format(soma_idade / pessoas_cadastradas))
print('Quantidade de mulheres com menos de 20 anos = {}'.format(cont))




