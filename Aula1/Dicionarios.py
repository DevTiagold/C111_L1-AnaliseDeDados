#Dicionários também usa {}, bem como os conjuntos. No entanto, a cada elemento usamos uma chave e um valor --> {chave:valor}
pessoa = {
          'nome':'Goku',
          'idade':42
         }
print(pessoa)

# Acessar elementos
print(pessoa['nome'])

#Insert
pessoa['sexo'] = 'M'
print(pessoa)
#Update
pessoa['nome'] = 'Vegeta'

#Delete
del pessoa['sexo']

print(pessoa)