#trabalhando com padrões textuais com numpy
import numpy as np

arr = np.array(['Goku', 'Gohan', 'Bulma', 'Vegeta', 'Goten'])
print(np.char.find(arr, 'Go') >= 0)
print(arr[np.char.find(arr, 'Go') >= 0])

print(np.char.find(arr, 'a')>=0)
print(arr[np.char.find(arr, 'a')>0])

