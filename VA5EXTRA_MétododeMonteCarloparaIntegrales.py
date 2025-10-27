################################################################################
# Extra: Método de Monte Carlo para Integrales
# Autor: Elías González Nieto
# Afil : Facultad de Ciencias - UNAM
# Curso : Probabilidad I
################################################################################

################################################################################
# Librerías
import numpy as np
import matplotlib.pyplot as plt
import math
################################################################################

################################################################################
# Funciones Sencillas

# Gráfica de la identidad
xpoints = np.linspace(0,1,10000)
plt.plot(xpoints, xpoints, color = 'darkblue')
plt.fill_between(xpoints, xpoints, color='cyan', alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x')
plt.grid()
plt.show()

# Simulación de vectores aleatorios
u1 = np.random.uniform(0,1,1000)
u2 = np.random.uniform(0,1,1000)

# Visualización
xpoints = np.linspace(0,1,10000)
plt.plot(xpoints, xpoints, color = 'darkblue')
plt.fill_between(xpoints, xpoints, color='cyan', alpha=0.5)
plt.scatter(u1, u2, color='indigo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = x')
plt.grid()
plt.show()

# Aproximación a la integral
u1 = np.random.uniform(0,1,1000)
u2 = np.random.uniform(0,1,1000)
contador = 0
for i in range(len(u1)):
  if u2[i] <= u1[i]:
    contador += 1
  else:
    0
print(contador / len(u1))

# Función para aproximar la integral en [0,1] de x^n
def integral_polinomio(n, N=1000):
  # Simulamos las uniformes
  unif1 = np.random.uniform(0,1,N)
  unif2 = np.random.uniform(0,1,N)

  # Graficamos la función
  xpoints = np.linspace(0,1,10000)
  plt.figure()
  plt.plot(xpoints, xpoints**n, color = 'darkblue')
  plt.fill_between(xpoints, xpoints**n, color='cyan', alpha=0.5)
  plt.scatter(unif1, unif2, color='indigo')
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.title(f'f(x) = x^{n}')
  plt.grid()
  plt.show()

  # Aproximamos la integral
  contador = 0
  for i in range(len(unif1)):
    if unif2[i] <= unif1[i]**n:
      contador += 1
    else:
      0
  print(f'La integral de 0 a 1 de x^{n} es', contador / N)

# Ejemplos
integral_polinomio(2)
integral_polinomio(3)

################################################################################
# Integral sobre R de e^{-x^2/2}

xpoints3 = np.linspace(-100,100,10000)
plt.figure()
plt.plot(xpoints3, np.exp(-xpoints3**2/2), color = 'darkblue')
plt.fill_between(xpoints3, np.exp(-xpoints3**2/2), color='cyan', alpha=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'f(x) = $e^{-x^2/2}$')
plt.grid()
plt.show()

# Estimación de la integral por medio de Monte Carlo
def f(x):
  return math.exp(-x**2/2)

N = 10000
unif31 = np.random.uniform(-100,100,N)
unif32 = np.random.uniform(0,1,N)

plt.figure()
plt.plot(xpoints3, np.exp(-xpoints3**2/2), color = 'darkblue')
plt.fill_between(xpoints3, np.exp(-xpoints3**2/2), color='cyan', alpha=0.5)
plt.scatter(unif31, unif32, color='indigo')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'f(x) = $e^{-\frac{x^2}{2}}$')
plt.grid()
plt.show()

contador3 = 0
for i in range(len(unif31)):
  if unif32[i] <= f(unif31[i]):
    contador3 += 1
  else:
    0
print(200*contador3 / len(unif31), math.sqrt(2*math.pi))

# Una función para hacer este proceso
def aproximar_integral3(N=10000, grafico = True):
  # Las uniformes
  unif31 = np.random.uniform(-100,100,N)
  unif32 = np.random.uniform(0,1,N)

  # Las gráficas
  if grafico:
    xpoints3 = np.linspace(-100,100,N)
    plt.figure()
    plt.plot(xpoints3, np.exp(-xpoints3**2/2), color = 'darkblue')
    plt.fill_between(xpoints3, np.exp(-xpoints3**2/2), color='cyan', alpha=0.5)
    plt.scatter(unif31, unif32, color='indigo')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(r'f(x) = $e^{-x^2}$')
    plt.grid()
    plt.show()

  # Aproximamos la integral
  contador3 = 0
  for i in range(len(unif31)):
    if unif32[i] <= f(unif31[i]):
      contador3 += 1
    else:
      0

  # Imprimimos la aproximación
  #print('La aproximación de la integral es:', 200*contador3 / len(unif31))
  return 200*contador3 / len(unif31)

# Obtenemos la media de 1000 aproximaciones
aproximaciones = [aproximar_integral3(1000, False) for i in range(1000)]
print(np.mean(aproximaciones))

# Verificación con el valor real
math.sqrt(2*math.pi)

################################################################################
# Caso general

# Clase para aplicar el método de Monte Carlo
class MonteCarlo:

  def __init__(self, f, a, b, M, N=1000):
    '''
    f: función a integrar
    a: límite inferior
    b: límite superior
    M: cota para la función
    N: número de iteraciones
    '''
    self.f = f
    self.a = a
    self.b = b
    self.N = N
    self.M = M

  def aproximar_integral(self):
    # Las uniformes
    unif31 = np.random.uniform(self.a,self.b,self.N)
    unif32 = np.random.uniform(0,self.M,self.N)
    # Aproximación
    indicadora = 0
    for i in range(len(unif31)):
      if unif32[i] <= self.f(unif31[i]):
        indicadora += 1
      else:
        0
    return unif31, unif32, (self.b-self.a)*indicadora / self.N

  def graficar(self):
    xpoints = np.linspace(self.a,self.b, self.N)
    u1, u2, app = self.aproximar_integral()
    plt.figure()
    plt.plot(xpoints, self.f(xpoints), color = 'darkblue')
    plt.fill_between(xpoints, self.f(xpoints), color='cyan', alpha=0.5)
    plt.scatter(u1, u2, color='indigo')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'f(x) = {self.f.__name__}')
    plt.grid()
    plt.show()
    print('La aproximación de esta iteración fue', app)


# Ejemplo
def f1(x):
  return 1/x

clase1 = MonteCarlo(f1, 1, math.exp(1), 1)
clase1.graficar()

