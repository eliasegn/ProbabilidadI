################################################################################
# Experimentos Aleatorios
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
# La librería random

# Definimos la lista
lista = [0,1,2,3,4,5,6,7,8,9]

# Elegimos un elemento aleatorio con la función
u = random.choice(lista)

# Imprimimos el elemento
print(u)

# Simular 10 números aleatorios entre 0 y 1
print([random.random() for _ in range(10)])

################################################################################
# Elegir aleatoriamente de una muestra de 2 (un volado)

# Definimos la lista
lista = [0,1]

# Generamos un número aleatorio entre 0 y 1
u = random.random()

# Verificamos la condición y elegimos
eleccion = None
if u < 0.5:
  eleccion = lista[0]
else:
  eleccion = lista[1]

# Imprimos la elección
print(eleccion)

# Función para elegir de una lista de dos elementos
def elegirdedos(lista):

  # Si la lista no contiene dos elementos, lanza un error
  if len(lista) != 2:
    raise Exception("La lista debe tener 2 elementos")

  # Genera un número aleatorio entre 0 y 1
  u = random.random()

  # Verifica la condición y regresa la elección
  eleccion = None
  if u < 0.5:
    eleccion = lista[0]
  else:
    eleccion = lista[1]
  return eleccion

# Definimos los parámetros para la gráfica
intentos = 100
dominio = range(intentos)
codominio = [elegirdedos([0,1]) for _ in dominio]

# Graficamos
plt.figure()
plt.scatter(dominio, codominio, color = 'indigo')
plt.grid()
plt.show()

# Prueba con algunas listas
lista1 = ['uno', 1]
lista2 = [{1: 'superior 1', 2: 'superior 2', 3: 'lineal 1', 4: 'lineal 2'}, 'ciencias']
lista3 = [[1,2,3], 912312323]

elegirdedos(lista1), elegirdedos(lista2), elegirdedos(lista3)

################################################################################
# Elegir aleatoriamente de una muestra de n

# Definimos la lista
lista10 = [1,2,3,4,5,6,7,8,9,10]
n = len(lista10)
# División del [0,1] en n+1 pedazos
division = np.linspace(0,1,n+1)
# Número aleatorio entre 0 y 1
u = random.random()
k = None

# Verificamos la condición de la partición
for i in range(len(division)):
  if division[i] <= u < division[i+1]:
    k = i

# Imprimimos el valor elegido
print(lista10[k])

# Definimos una función análoga al procedimiento anterior
def elegirde(lista):
  n = len(lista)
  division = np.linspace(0,1,n+1)
  u = random.random()
  k = None
  for i in range(len(division)):
    if division[i] <= u < division[i+1]:
      k = i
  return lista[k]

# Definimos dominio y rango para el experimento
lista = [1,2,3,4,5,6]
intentos2 = 100
dominio2 = range(intentos2)
codominio2 = [elegirde(lista) for _ in dominio2]

# Graficamos los resultados
plt.figure()
plt.scatter(dominio2, codominio2, color = 'indigo')
plt.grid()
plt.show()

# Definimos un df con el número y las veces que fue lanzado
lanzamientos = pd.DataFrame(codominio2)

# Contamos el número de veces que aparece cada número
conteos = lanzamientos.value_counts().sort_index()

# Graficamos
plt.figure()
conteos.plot(kind='bar', color='indigo')
plt.axhline(y = 0.1666*intentos2, linestyle = '--', color = 'purple')
plt.title('Distribución de los lanzamientos')
plt.xlabel('Número')
plt.ylabel('Frecuencia')
plt.show()

################################################################################
# Un Experimento Aleatorio

# Definimos las variables para comenzar
gain = 0
iter = 100
urna = [0,1,2]

# Simulamos la elección y la ganancia o pérdida de dinero
for i in range(iter):
  res = elegirde(urna)
  if res == 0 or res == 1:
    gain = gain + 1500
  else:
    gain = gain - 1000

# Imprimimos la ganancia total
print(gain)

def experimento(iter):
  # Definimos las variables asociadas
  gain = 0
  urna = [0,1,2]
  ganancias = []
  # Simulamos el experimento
  for i in range(iter):
    res = elegirde(urna)
    if res == 0 or res == 1:
      gain = gain + 1500
    else:
      gain = gain - 1000
    # Guardamos la ganancia en cada paso
    ganancias.append(gain)
  return ganancias

# Graficamos el desarollo del experimento
plt.figure()
plt.plot(experimento(100), color = 'indigo')
plt.xlabel('Iteraciones')
plt.ylabel('Ganancia')
plt.grid()
plt.show()

# Definimos un experimento con parámetros móviles
def experimento_mejorado(iter, u, d, num_urna=int):
  # Definimos las variables asociadas
  gain = 0
  ganancias = []
  # urna = [0,1,2,...,num_urna]
  urna = list(range(num_urna))
  # Simulamos el experimento
  for i in range(iter):
    res = elegirde(urna)
    if res == 0:
      gain = gain + u
    else:
      gain = gain - d
    ganancias.append(gain)
  return ganancias

# Graficamos las ganancias
plt.figure()
plt.plot(experimento_mejorado(1000, 1,1,2), color = 'indigo')
plt.xlabel('Iteraciones')
plt.ylabel('Ganancia')
plt.grid()
plt.show()