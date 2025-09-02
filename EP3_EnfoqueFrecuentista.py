################################################################################
# Enfoque Frecuentista
# Autor: Elías González Nieto
# Afil : Facultad de Ciencias - UNAM
# Curso : Probabilidad I
################################################################################

################################################################################
# Librerías
import numpy as np 
import random
import pandas as pd
import matplotlib.pyplot as plt
################################################################################

################################################################################
# Elegir aleatoriamente un elemento de una lista
def elegirde(lista):
  '''
  Parámetros
  lista : lista de donde elegirá uno aleatoriamente
  '''
  n = len(lista) # Longitud de la lista
  division = np.linspace(0,1,n+1) # Partición del [0,1] de n espacios
  u = random.random() # Número aleatorio entre 0 y 1
  k = None # Valor a elegir
  for i in range(len(division)):
    if division[i] <= u < division[i+1]: # Elegimos dependiendo de la partición
      k = i # k será el índice donde cayó el número aleatorio
  return lista[k]

# Ejemplo de simular un dado
dado = [1,2,3,4,5,6]
elegirde(dado)

# Repetir 10 veces el lanzamiento de un dado justo
iter = 10 # El número de iteraciones
for i in range(iter):
  print(elegirde(dado))

# Aproximación de la probabilidad de que salga 4
iter = 100 # El número de iteraciones
contador4 = 0 # El contador
for i in range(iter):
  if elegirde(dado) == 4: # Si sale 4, agregamos al contador
    contador4 += 1

print('La aproximación es', contador4 / iter)

# Hacemos lo mismo para cada valor distinto del dado
# Definimos contadores por cada evento
contador1 = 0
contador2 = 0
contador3 = 0
contador5 = 0
contador6 = 0

# Guardamos los lanzamientos en cada iteración
lanzamientos = []
dado = [1,2,3,4,5,6]

# Hacemos el experimento y guardamos los resultados
for i in range(iter):
  lanzamiento = elegirde(dado)
  if lanzamiento == 1:
    contador1 += 1
  elif lanzamiento == 2:
    contador2 += 1
  elif lanzamiento == 3:
    contador3 += 1
  elif lanzamiento == 4:
    contador4 += 1
  elif lanzamiento == 5:
    contador5 += 1
  elif lanzamiento == 6:
    contador6 += 1
  lanzamientos.append(lanzamiento)

# Graficamos los resultados
dominio2 = range(iter)
plt.figure()
plt.scatter(dominio2, lanzamientos, color = 'indigo')
plt.grid()
plt.show()

# Vemos el histograma de resultados usando pandas

# Definimos un df con el número y las veces que fue lanzado
lanzamientos = pd.DataFrame(lanzamientos)

# Contamos el número de veces que aparece cada número
conteos = lanzamientos.value_counts().sort_index()

# Graficamos
plt.figure()
conteos.plot(kind='bar', color='indigo')
plt.axhline(y = 0.1666*iter, linestyle = '--', color = 'purple')
plt.title('Distribución de los lanzamientos')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

################################################################################
# Código completo para simular un dado justo y calcular las probabilidades de obtener cada número
iter = 100 # El número de iteraciones

# Definimos contadores para cada valor del dado
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

lanzamientos = [] # Lista de lanzamientos

for i in range(iter):
  lanzamiento = elegirde(dado) # Lanzamos el dado
  if lanzamiento == 1:
    contador1 += 1
  elif lanzamiento == 2:
    contador2 += 1
  elif lanzamiento == 3:
    contador3 += 1
  elif lanzamiento == 4:
    contador4 += 1
  elif lanzamiento == 5:
    contador5 += 1
  elif lanzamiento == 6:
    contador6 += 1
  lanzamientos.append(lanzamiento)

dominio = range(iter)

# Definimos un df con el número y las veces que fue lanzado
lanzamientos = pd.DataFrame(lanzamientos)

# Contamos el número de veces que aparece cada número
conteos = lanzamientos.value_counts().sort_index()

# Graficamos
plt.figure()
conteos.plot(kind='bar', color='indigo')
#plt.axhline(y = 0.1666*iter, linestyle = '--', color = 'purple')
plt.title(f'Distribución de los valores con {iter} lanzamientos')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.grid()
plt.show()

################################################################################
# Ejercicio de Aplicación
ejercicios = [1,2,3,4,5,6,7,8,9,10] # número de ejercicios
N = 100000 # número de iteraciones


# Inciso a
indicadora = 0 # contador
for i in range(N):
  estudiados = random.sample(ejercicios, 7)
  elegidos = random.sample(ejercicios, 5)
  # Calculamos el cardinal de la intersección
  bien = len(set(estudiados) & set(elegidos))
  if bien == 5: # Si el cardinal es 5, agregamos
      indicadora += 1

print(indicadora/N)

# Inciso b
indicadora2 = 0 # contador
for i in range(N):
  estudiados = random.sample(ejercicios, 7)
  elegidos = random.sample(ejercicios, 5)
  # Calculamos el cardinal de la intersección
  bien = len(set(estudiados) & set(elegidos))
  if bien == 5 or bien == 4: # Si el cardinal es 5 o 4, agregamos
      indicadora2 += 1

print(indicadora2/N)