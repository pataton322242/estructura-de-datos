import numpy as np
import pandas as pd
df = pd.read_csv('PRACTICA_2/Housing.csv')
lista =df ['price']

def housingStarts(str):
    lista=lista=df ['price']
suma = 0
moda = 0
for i in lista:
        suma+= i
Media = suma/len(lista)
print('\nMedia:', Media)
m= {}
for i in lista:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
        moda = max(m, key=m.get)
print('Moda:', moda)
varianza_sum = 0
for i in lista:
    varianza_sum += (i - Media) ** 2/(len(lista) - 1)
print('Varianza:',  varianza_sum)
desviacion_muestral = np.sqrt(varianza_sum)
print('Desviacion estandar muestral:', desviacion_muestral)
 