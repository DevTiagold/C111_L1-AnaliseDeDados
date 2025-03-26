#Importando arquivos externos no numpy
import numpy as np
dataset = np.loadtxt('space.csv', delimiter=';' ,
            dtype='str', encoding='utf-8')
#observando o dataset
print(dataset[1,:])

#apresente a porcentagem de missões que deram certo
status = (dataset[:,7])
# print(status[np.char.find(status,'Success')>=0].size) #quantas deram sucesso
# print(status[np.char.find(status,'Failure')>=0].size) #quantas deram errado
success = status[np.char.find(status,'Success')>=0].size
#print(success)
porcentagem = success*100/4323
print("Porcentagem de sucesso de missões = {}%".format(porcentagem))

#quantas missões foram realizadas pelos EUA -->USA
location = (dataset[:,2])
location_usa = location[np.char.find(location,'USA')>=0].size
print("{} missões foram realizadas pelos USA".format(location_usa))

#qual a missão mais cara da Spacex
mission_spacex = (dataset[:,1]),(dataset[:,6])
print(mission_spacex)
# print(mission_spacex[np.char.find(mission_spacex,'SpaceX')>=0])