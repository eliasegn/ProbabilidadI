################################################################################
# Leyes de los Grandes Números
# Autor: Elías González Nieto
# Afil : Facultad de Ciencias - UNAM
# Curso : Probabilidad I
################################################################################

################################################################################
# Librerías
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd
import random
import math
################################################################################

################################################################################
# Aproximación Poisson a Binomial

# Definimos los parámetros
n = 10000
p = 0.001
lam = n * p
Nsim = 5000
sims = np.random.binomial(n, p, size=Nsim)

# Histograma de la normal
counts, bins = np.histogram(sims, bins=range(0, int(max(sims))+2), density=True)

# Soporte de la Poisson
xs = np.arange(len(counts))

# Evaluamos la masa poisson en xs
pmf_poisson = st.poisson.pmf(xs, mu=lam)

# Graficamos
plt.bar(xs, counts, alpha=0.6, label=f'Binomial$({n},{p})$')
plt.plot(xs, pmf_poisson, marker='o', linestyle='-', label=f'Poisson($\\lambda$={lam})')
plt.legend()
plt.xlabel('k')
plt.title('Aproximación')
plt.ylabel('Probabilidad')
plt.title(f'Aproximación Poisson a Binomial con $n$={n} y $p$={p}')
plt.show()

# Función para visualizar la Aproximación Poisson a Binomial
def aprox(n,p):
  # Parámetros
  lam = n*p
  Nsim = 5000
  # Simulación de binomial
  sims = np.random.binomial(n, p, size=Nsim)
  # Histograma
  counts, bins = np.histogram(sims, bins=range(0, int(max(sims))+2), density=True)
  # Poisson
  xs = np.arange(len(counts))
  pmf_poisson = st.poisson.pmf(xs, mu=lam)

  # Gráfico de histogramas
  plt.figure()
  plt.bar(xs, counts, alpha=0.6, label=f'Binomial$({n},{p})$')
  plt.plot(xs, pmf_poisson, marker='o', linestyle='-', label=f'Poisson($\\lambda$={lam})')
  plt.title(f'Aproximación Poisson a Binomial con $n$={n} y $p$={p}')
  plt.legend()
  plt.xlabel('k')
  plt.ylabel('Probabilidad')
  plt.show()
  
  return None

# Ejemplos
aprox(1000, 0.5)
aprox(400, 0.2)
aprox(1,0.2)

################################################################################
# Ley Fuerte de los Grandes Números

# Distribución Bernoulli

# Tamaño de la muestra aleatoria
N = 1000
p = 0.3

# Muestra ber(p)
ber1 = np.random.binomial(n=1, p=p, size=N)

# Aquí guardaremos las medias truncadas
S1 = [] 
# Calculamos las medias truncadas y las guardamos en la lista S
for i in range(len(ber1)):
  S1.append(sum(ber1[:i+1])/len(ber1[:i+1]))

# Graficamos la convergencia de la sucesión
plt.figure()
plt.plot(S1, color = 'darkblue', linewidth = 2, label = 'Medias Truncadas')
plt.axhline(y=p, color='indigo', ls = '--', label = 'Esperanza de la Distribución')
plt.xlabel('m')
plt.ylabel('S_m')
plt.grid()
plt.show()

# Función para visualizar la convergencia
def bernoulli_lfgn(p, N):
  ber1 = np.random.binomial(n=1, p=p, size=N)
  S1 = [] 
  for i in range(len(ber1)):
    S1.append(sum(ber1[:i+1])/len(ber1[:i+1]))
  plt.figure()
  plt.plot(S1, color = 'darkblue', linewidth = 2, label = 'Medias Truncadas')
  plt.axhline(y=p, color='indigo', ls = '--', label = 'Esperanza de la Distribución')
  plt.xlabel('m')
  plt.ylabel('S_m')
  plt.grid()
  plt.show()
  return None

# Ejemplos
bernoulli_lfgn(0.5, 1000)

# Distribución Geométrica

# Función para visualizar la convergencia
def geo_lfgn(p, N):
  # Muestra geométrica(p)
  geo1 = np.random.geometric(p=p, size=N)

  # Aquí guardaremos las medias truncadas
  S2 = [] 
  # Calculamos las medias truncadas y las guardamos en la lista S
  for i in range(len(geo1)):
    S2.append(sum(geo1[:i+1])/len(geo1[:i+1]))

  # Graficamos la convergencia de la sucesión
  plt.figure()
  plt.plot(S2, color = 'darkblue', linewidth = 2, label = 'Medias Truncadas')
  plt.axhline(y=1/p, color='indigo', ls = '--', label = 'Esperanza de la Distribución')
  plt.xlabel('m')
  plt.ylabel('S_m')
  plt.grid()
  plt.show()
  return None

# Ejemplo
geo_lfgn(0.5, 1000)

# Distribución Exponencial

# Función para visualizar la convergencia
def exp_lfgn(N, lam): # Recibe la media de la distribución
  # Muestra exp(1/lam)
  exp1 = np.random.exponential(scale=lam, size=N) 

  # Aquí guardaremos las medias truncadas
  S = [] 
  # Calculamos las medias truncadas y las guardamos en la lista S
  for i in range(len(exp1)):
    S.append(sum(exp1[:i+1])/len(exp1[:i+1]))

  # Graficamos la convergencia de la sucesión
  plt.figure()
  plt.plot(S, color = 'darkblue', linewidth = 2, label = 'Medias Truncadas')
  plt.axhline(y=lam, color='indigo', ls = '--', label = 'Esperanza de la Distribución')
  plt.xlabel('m')
  plt.ylabel('S_m')
  plt.grid()
  plt.show()
  return None

# Ejemplo
exp_lfgn(2000, 2)

# Distribución Normal

# Función para visualizar la convergencia
def normal_lfgn(mu, sigma, N):
  nor = np.random.normal(mu, sigma, size=N) # Muestra normal(mu, sigma^2)
  S = []
  # Medias truncadas
  for i in range(len(nor)):
    S.append(sum(nor[:i+1])/len(nor[:i+1]))
  # Gráfico
  plt.figure()
  plt.plot(S, color = 'darkblue', linewidth = 2, label = 'Medias Truncadas')
  plt.axhline(y=mu, color='indigo', ls = '--', label = 'Esperanza de la Distribución')
  plt.xlabel('m')
  plt.ylabel('S_m')
  plt.grid()
  plt.show()
  return None

# Ejemplos
normal_lfgn(0, 1, 1000)
normal_lfgn(-2312, 2045, 1000)