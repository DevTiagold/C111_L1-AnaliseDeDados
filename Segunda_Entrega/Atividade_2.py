MagazineLuiza = {'Apple', 'Samsung', 'Xiaomi', 'Motorola', 'Oppo', 'Nokia', 'LG'}
CasasBahia = {'Samsung', 'Poco', 'Motorola', 'Oppo', 'Realme', 'LG', 'Honor'}

#Quais modelos estão disponíveis nas duas lojas
uniao = MagazineLuiza | CasasBahia
uniao_alfabetica = sorted(uniao)
print('Os modelos disponíveis são: \n', uniao_alfabetica)
print('\n')
#Quais modelos são iguais nas duas lojas
intersecao = MagazineLuiza & CasasBahia
intercecao_alfabetica = sorted(intersecao)
print('Modelos iguais nas duas lojas: \n', intercecao_alfabetica)


