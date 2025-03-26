times = ['Santos', 'Corinthians', 'Palmeiras', 'Barcelona', 'Real Madrid']

#Primeiros colocados
print('Primeiros colocados: ', times[:3])

#Dois últimos colocdos
print('Dois últimos colocados ', times[3:])

#Lista em ordem alfabética
times_ordered = sorted(times)
print('Em ordem alfabética: ',times_ordered)

#Buscando posição de um time
if 'Barcelona' in times:
    position = times.index('Barcelona')
    position_podio = position+1
    print('O Barcelona está em {}º lugar!'.format(position_podio))