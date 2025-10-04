################################################################################
# Números Pseudo-Aleatorios
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
# Simular una Uniforme en (0,1)

# En una dimensión
N = 100 # Números de puntos
xpoints = [random.random() for _ in range(N)] #list comprehension
plt.figure()
plt.scatter(xpoints, np.zeros(len(xpoints)), color = 'indigo')
plt.axline((0,0), (1,0), color = 'purple')
plt.title('Puntos aleatorios')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# En dos dimensiones
xpoints = [random.random() for _ in range(N)] #list comprehension
ypoints = [random.random() for _ in range(N)]
plt.figure()
plt.scatter(xpoints, ypoints, color = 'darkblue')
plt.title('Puntos aleatorios')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Función para construir un gráfico como el anterior
def plot_unif01(N, imp = True):
  xpoints = [random.random() for _ in range(N)]
  ypoints = [random.random() for _ in range(N)]

  plt.figure()
  plt.scatter(xpoints, ypoints, color = 'indigo')
  plt.title('Puntos aleatorios')
  plt.xlabel('x')

  if imp:
    return xpoints, ypoints
  else:
    return None

# Ejemplo
plot_unif01(100, False)

################################################################################
# Simular una Uniforme en (a,b)

a = 3
b = 8
X = random.random()
Y = (b-a)*X+a # Aplicamos la transformación
Y

# Función para simular uniforme en (0,1)
def simular_u01(N):
  return np.array([random.random() for _ in range(N)])

# Función para simular uniforme en (a,b)
def simular_unif(a, b, N):
  X = simular_u01(N)
  return (b-a)*X + a

# Simulación de uniforme en dos dimensiones
N = 100
xpoints2 = simular_unif(a, b, N)
ypoints2 = simular_unif(a, b, N)

plt.figure()
plt.scatter(xpoints2, ypoints2, color = 'indigo')
plt.title(f'Puntos aleatorios en {(a,b)}')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

################################################################################
# Método de MonteCarlo para aproximar áreas

# Gráfica del círculo unitario
plt.plot(np.linspace(-1, 1, 1000), np.sqrt(1-np.linspace(-1, 1, 1000)**2), color = 'darkblue')
plt.plot(np.linspace(-1, 1, 1000), -np.sqrt(1-np.linspace(-1, 1, 1000)**2), color = 'darkblue')
plt.fill_between(np.linspace(-1, 1, 1000), -np.sqrt(1-np.linspace(-1, 1, 1000)**2), np.sqrt(1-np.linspace(-1, 1, 1000)**2), color='cyan', alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid()
plt.show()

# Genreamos uniformes en [-1,1]x[-1,1]
N = 10000 # Número de uniformes

# Generamos las uniformes
xmuestra = simular_unif(-1, 1, N)
ymuestra = simular_unif(-1, 1, N)

# Graficamos el círculo unitario y los puntos aleatorios
plt.plot(np.linspace(-1, 1, 1000), np.sqrt(1-np.linspace(-1, 1, 1000)**2), color = 'darkblue')
plt.plot(np.linspace(-1, 1, 1000), -np.sqrt(1-np.linspace(-1, 1, 1000)**2), color = 'darkblue')
plt.fill_between(np.linspace(-1, 1, 1000), -np.sqrt(1-np.linspace(-1, 1, 1000)**2), np.sqrt(1-np.linspace(-1, 1, 1000)**2), color='cyan', alpha=0.5)
plt.scatter(xmuestra, ymuestra, color = 'navy', alpha = 0.25)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.grid()
plt.show()

# Aproximación del área del círculo unitario
contador = 0
for j in range(N):
  if xmuestra[j]**2 + ymuestra[j]**2 <= 1: # Condición de estar en el círculo
    contador = contador + 1

print(f'El área aproximada es {4*contador/N}')

# Función para aproximar pi con números aleatorios
def aprox_pi(N):
  contador = 0
  x = simular_unif(-1, 1, N)
  y = simular_unif(-1, 1, N)
  for j in range(N):
    if x[j]**2 + y[j]**2 <= 1: # Condición de estar en el círculo
      contador = contador + 1
  return 4*contador/N

N = 100000
print(f'El área aproximada es {aprox_pi(N)}')