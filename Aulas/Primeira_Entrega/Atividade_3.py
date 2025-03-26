sexo = input('Digite seu sexo (M/F): ')
adapt = sexo.upper()
while adapt != 'M' and adapt != 'F':
    adapt = input('Digite seu sexo (M/F): ')

if adapt == 'M':
    print('Masculino')
else :
    print('Feminino')

