################################################################################
# Simulación de Variables Aleatorias Discretas con Soporte Finito
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
# Simular Bernoulli

p = 0.3
u = random.random()
if u < p:
    x = 1
else:
    x = 0
print(x)

# Función para simular una muestra de Bernoullis
def bernoulli(p, n):
    x = []
    for i in range(n):
        u = random.random()
        if u < p:
            x.append(1)
        else:
            x.append(0)
    return x

muestra = bernoulli(0.3, 1000)
plt.hist(muestra, color='indigo')
plt.title('Histograma de la muestra')
plt.xlabel('Valores de X')
plt.ylabel('Frecuencia')
plt.show()

################################################################################
# Simular v.a. discretas con soporte finito

def simular_discretas(x, p):
  # Guardamos en un df los datos
  df = pd.DataFrame({'x': x, 'p': p})
  # La suma acumulada y la uniforme
  df['p_acum'] = df['p'].cumsum()
  u = random.random()

  for i in range(len(df)):
      if u <= df['p_acum'][i]: # La condición
          return df['x'][i]
  return np.random.choice(x, p=p) # A veces no llega por problemas numéricos
  
# Ejemplo 1
equis = [1,2,3]
probas = [0.05, 0.9, 0.05]
X = [simular_discretas(equis, probas) for i in range(1000)]

plt.figure(figsize=(10,5))
plt.hist(X, color = 'indigo', bins=range(5),edgecolor = 'black', align = 'left', rwidth=1)
plt.title('Histograma de la muestra')
plt.xlabel('Valores de X')
plt.ylabel('Frecuencia')
plt.show()

################################################################################
# Ejemplo 2: Binomial

import math
def masa_binomial(n, p, j):
  # Devuelve P(Bin(n,p)=j)
  return (math.comb(n, j))*(p**j)*((1-p)**(n-j))

# Los parámetros de la Binomial
n = 10
p = 0.3
soporte_binomial = range(1, 11)
proba_binomial = [masa_binomial(n, p, j) for j in soporte_binomial]

# Normalizamos para asegurar suma 1, puede haber errores numéricos de redondeo
suma = sum(proba_binomial)
proba_binomial = [q/suma for q in proba_binomial]

# Simulamos la v.a.
Binomial = [simular_discretas(soporte_binomial, proba_binomial) for i in range(1000)]

# Graficamos la v.a.
plt.figure(figsize=(10,5))
plt.hist(Binomial, bins=range(n+2), align='left', rwidth=1, edgecolor='black', color = 'indigo')
plt.title('Histograma de la muestra')
plt.xlabel('Valores de X')
plt.ylabel('Frecuencia')
plt.show()

# Clase de una binomial
class Binomial:

  def __init__(self, n, p):
    self.n = n
    self.p = p
    # Calculamos la binomial como antes
    self.soporte_binomial = range(1, n+1)
    self.proba_binomial = [masa_binomial(n, p, j) for j in self.soporte_binomial]
    suma = sum(self.proba_binomial)
    self.proba_binomial = [q/suma for q in self.proba_binomial] # Normalizamos por errores numéricos

  def simular(self):
    return simular_discretas(self.soporte_binomial, self.proba_binomial)

  def graficar(self, N=1000):
    # Visualizamos el histograma
    Binom = [self.simular() for i in range(N)]
    plt.figure(figsize=(10,5))
    plt.hist(Binom, bins=range(n+2), align='left', rwidth=1, edgecolor='black', color = 'indigo')
    plt.title(f'Histograma de una muestra binomial de {N} elementos')
    plt.xlabel('Valores de X')
    plt.ylabel('Frecuencia')
    plt.show

  def masa(self, j):
    return masa_binomial(n, p, j)

  def __str__(self):
    return f'Binomial({n, p})'

# Ejemplos
Y = Binomial(10, 0.25)
Y.graficar()

Z = Binomial(10, 0.5)
Z.graficar()

W = Binomial(10, 0.75)
W.graficar()

D = Binomial(10, 1)
D.graficar()
