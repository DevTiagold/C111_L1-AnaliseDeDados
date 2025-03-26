registro = {}
nome = input('Digite seu nome: ')
media = float(input('Sua média: '))

registro['nome'] = nome
registro['media'] = media
if media >= 50:
    registro['Situacao'] = 'AP'
else:
    registro['Situacao'] = 'RP'
print ('O aluno {} possui média = {} \nLogo o aluno está {}' .format(registro['nome'], registro['media'], registro['Situacao']))
