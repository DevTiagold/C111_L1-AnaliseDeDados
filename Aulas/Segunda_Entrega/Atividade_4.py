pessoas = []  # Lista para armazenar os dicionários de cada pessoa

for _ in range(3):  # Loop para ler os dados de 3 pessoas
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas.append({'nome': nome, 'peso': peso})  # Adiciona um dicionário na lista
    print('\nOutra pessoa...')

peso_max = 0
peso_min = 99999
# Encontrando a pessoa mais pesada e a mais leve
for c in range(3):
    if pessoas[c]['peso'] > peso_max:
        peso_max = pessoas[c]['peso']
        nome_mais_pesado = pessoas[c]['nome']
for c in range(3):
    if pessoas[c]['peso'] < peso_min:
        peso_min = pessoas[c]['peso']
        nome_min_peso = pessoas[c]['nome']


print(f'A pessoa mais pesada é {nome_mais_pesado} com {peso_max} kg.')
print(f'A pessoa mais leve é {nome_min_peso} com {peso_min} kg.')
