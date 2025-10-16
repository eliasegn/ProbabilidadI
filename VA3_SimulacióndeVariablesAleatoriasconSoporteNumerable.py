################################################################################
# Simulación de Variables Aleatorias Discretas con Soporte Numerable
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
import math
################################################################################

################################################################################
# Simular una Poisson

# Función de masa de una Poisson
def masa_poisson(lam, j):
  return (math.exp(-lam) * lam**j) / math.factorial(j)

# Variables iniciales
F = 0
lam = 2
u = random.random()
Z = []
# Condición del método
while F < u:
  Z.append(len(Z))
  F += masa_poisson(lam,Z[-1])
# El valor será el último de la lista Z
print(Z[-1])

# Función para simular 
def simular_poisson(lam):
  F = 0
  u = random.random()
  Z = []
  # Verificamos la condición con el bucle while
  while F < u:
    Z.append(len(Z))
    F += masa_poisson(lam,Z[-1])
  return Z[-1]

# Visualizamos el histograma
xpoints = [simular_poisson(2) for i in range(1000)]
plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left')
plt.title('Distribución Poisson')
plt.xlabel('X')
plt.show()

# Clase de la distribución Poisson
class Poisson:
  def __init__(self, lam):
    '''
    lam: parámetro de la distribución Poisson
    '''
    self.lam = lam
  def masa(self, j):
    return masa_poisson(self.lam, j) # Función de masa
  def graficar(self, N=1000):
    xpoints = [simular_poisson(self.lam) for i in range(N)] # Lista de valores de X
    plt.figure()
    plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left') # Histograma
    plt.title(f'Distribución Poisson de parámetro {self.lam}')
    plt.xlabel('X')

# Ejemplos
poi1 = Poisson(10)
poi1.graficar()

po2 = Poisson(100)
po2.graficar()

################################################################################
# Simular Binomial

# Función de masa de una Binomial
def masa_binomial(n, p, j):
  return math.comb(n,j) * p**j * (1-p)**(n-j)

# Variables iniciales
F = 0
n = 10
p = 0.5
u = random.random()
Z = []
# Condición del método
while F < u:
  Z.append(len(Z))
  F += masa_binomial(n, p,Z[-1])
# El valor será el último de la lista Z
print(Z[-1])

# Función para simular una binomial
def simular_binomial(n, p):
  F = 0
  u = random.random()
  Z = []
  # Condición del método
  while F < u:
    Z.append(len(Z))
    F += masa_binomial(n, p, Z[-1])
  return Z[-1]

# Visualizamos el histograma
xpoints = [simular_binomial(n, p) for i in range(1000)]
plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left')
plt.title('Distribución Poisson')
plt.xlabel('X')
plt.show()

# Clase para simular una binomial
class Binomial:
  def __init__(self, n, p):
    '''
    n: número de ensayos
    p: probabilidad de éxito
    '''
    self.n = n
    self.p = p
  def masa(self, j):
    return masa_binomial(self.n, self.p, j) # Función de masa
  def graficar(self, N=1000):
    xpoints = [simular_binomial(self.n, self.p) for i in range(N)] # Lista de valores de X
    plt.figure()
    plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left') # Histograma
    plt.title(f'Distribución Binomial {self.n, self.p}')
    plt.xlabel('X')

# Ejemplos
binom1 = Binomial(10, 0.5)
binom1.graficar()

binom2 = Binomial(100, 0.3)
binom2.graficar()

binom3 = Binomial(500, 0.9)
binom3.graficar()

################################################################################
# Simular Geométrica

# Función de masa geométrica
def masa_geometrica(p, j):
  return p * (1-p)**j

# Variables iniciales
F = 0
p = 0.5
u = random.random()
Z = []
# Condición del método
while F < u:
  Z.append(len(Z))
  F += masa_geometrica(p, Z[-1])
# El valor será el último de la lista Z
print(Z[-1])

# Función para simular geométrica
def simular_geometrica(p):
  F = 0
  u = random.random()
  Z = []
  # Condición del método
  while F < u:
    Z.append(len(Z))
    F += masa_geometrica(p, Z[-1])
  return Z[-1]

# Visualizamos el histograma
plt.figure()
xpoints = [simular_geometrica(p) for i in range(1000)]
plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left')
plt.title('Distribución Geométrica')
plt.xlabel('X')
plt.show()

# Clase para simular geométricas
class geometrica:
  def __init__(self, p):
    '''
    p: probabilidad de éxito
    '''
    self.p = p
  def masa(self, j):
    return masa_geometrica(self.p, j) # Función de masa
  def graficar(self, N=1000):
    xpoints = [simular_geometrica(self.p) for i in range(N)] # Lista de valores de X
    plt.figure()
    plt.hist(xpoints, bins = range(max(xpoints)+2), edgecolor = 'black', color = 'indigo', align='left') # Histograma
    plt.title(f'Distribución Geométrica {self.p}')
    plt.xlabel('X')
    plt.show()

# Ejemplos
geo1 = geometrica(0.5)
geo1.graficar()

geo2 = geometrica(0.3)
geo2.graficar()

geo3 = geometrica(0.9)
geo3.graficar()

geo4 = geometrica(0.01)
geo4.graficar()
