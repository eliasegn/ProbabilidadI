################################################################################
# El Problema de Monty Hall
# Autor: Elías González Nieto
# Afil : Facultad de Ciencias - UNAM
# Curso : Probabilidad I
################################################################################

################################################################################
# Librerías
import random
import numpy as np
import matplotlib.pyplot as plt
import math
################################################################################

################################################################################
# Método de la Función Inversa 

# Simular la exponencial
lam = 1
u = random.random() # Simulamos la uniforme
x = -(1/lam)*math.log(u) # Aplicamos la transformación
x

# Función para simular una v.a. exponencial
def simular_exp(lam):
  u = random.random()
  return -(1/lam)*math.log(u)

# Vemos el histograma de la muestra
lam = 2
N = 1000
xpoints = [simular_exp(2) for _ in range(N)]
plt.figure()
plt.hist(xpoints, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid')
plt.title(f'Distribución exponencial {lam}')
plt.show()

# Agregamos la densidad exponencial
lam = 2 # Parámetro
N = 1000 # Tamaño de muestra
xpoints = [simular_exp(2) for _ in range(N)] # Muestra
plt.figure()
plt.hist(xpoints, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid', density = True)
x = np.linspace(0, 10, 200) # Dominio de la densidad
y = lam * np.exp(-lam * x) # Densidad
plt.plot(x, y, color='red', label=f'Densidad exp({lam})') # Gráfico de la densidad
plt.title(f'Distribución exponencial {lam}')
plt.legend()
plt.show()

# Clase para simular la exponencial
class Exponencial:
  def __init__(self, lam):
    '''
    lam: Parámetro de la distribución
    '''
    self.lam = lam

  def graficar(self, N = 1000, dens = True):
    plt.figure()
    xpoints = [simular_exp(self.lam) for _ in range(N)]
    plt.hist(xpoints, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid', density = True)
    if dens:
      x = np.linspace(0, 10, 200)
      y = self.lam * np.exp(-self.lam * x)
      plt.plot(x, y, color='red', label=f'Densidad exp({self.lam})')
    plt.title(f'Distribución exponencial {self.lam}')
    plt.legend()
    plt.show()

# Ejemplos
exp1 = Exponencial(3)
exp1.graficar()

exp2 = Exponencial(5)
exp2.graficar(N = 10000, dens = False)

################################################################################
# Simular la Cauchy

# Función para simular Cauchy
def simular_cauchy(x0=0, gamma=1):
    u = random.random()
    return x0 + gamma * math.tan(math.pi * (u - 0.5))

# Clase para variable aleatoria Cauchy
class Cauchy:
    def __init__(self, x0=0, gamma=1):
        '''
        x0: parámetro de localización
        gamma: parámetro de escala (>0)
        '''
        self.x0 = x0
        self.gamma = gamma

    def graficar(self, N=1000, dens=True, rango=(-10,10)):
        plt.figure()
        xpoints = [simular_cauchy(self.x0, self.gamma) for _ in range(N)] # simulamos valores de Cauchy
        plt.hist(xpoints, bins=100, density=True, edgecolor='darkblue',
                 color='turquoise', align='mid', alpha=0.7, range=rango) # graficamos el histograma

        if dens: # si esto es verdadero grafica la densidad también
            x = np.linspace(rango[0], rango[1], 500)
            y = 1/(math.pi * self.gamma * (1 + ((x - self.x0)/self.gamma)**2))
            plt.plot(x, y, color='red', label=f'Cauchy(x0={self.x0}, γ={self.gamma})')

        plt.title(f'Distribución Cauchy (x0={self.x0}, γ={self.gamma})')
        plt.legend()
        plt.show()

# Ejemplos
cauchy1 = Cauchy(x0=0, gamma=1)
cauchy1.graficar()

cauchy2 = Cauchy(x0=2, gamma=3)
cauchy2.graficar()

################################################################################
# Método de Aceptación Rechazo

# Simular una normal

# Parámetros del método
u = random.random()
Y = np.random.exponential(1)
c = math.sqrt(2*math.e/math.pi)

# Método de aceptación rechazo
while u >= c*math.exp(-Y**2):
  u = random.random()
  Y = np.random.exponential(1)
X = Y
X # imprimimos el valor

def ar_normal():
  # Parámetros del método
  u = random.random()
  Y = np.random.exponential(1)
  c = math.sqrt(2*math.e/math.pi)
  # Método de aceptación rechazo
  while u > c*math.exp(-(Y-1)**2/2):
    u = random.random()
    Y = np.random.exponential(1)
  # Elección del signo
  ber = np.random.binomial(1, 0.5)
  if ber == 0:
    X = Y
  else:
    X = -Y
  return X

# Graficamos los resultados
N = 10000
muestra_normal = [ar_normal() for _ in range(N)]
x = np.linspace(-5, 5, 200)
y = 1/math.sqrt(2*math.pi)*np.exp(-x**2/2)
plt.figure()
plt.hist(muestra_normal, density= True, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid') # Histograma de la muestra
plt.plot(x, y, color='red', label='Densidad normal estándar') # Densidad normal
plt.title(f'Distribución normal estándar')
plt.legend()
plt.show()

# Ejemplos
sigma = 100
mu = -300
N = 100000

# Simulamos una normal estándar y la transformamos
estandar = np.array([ar_normal() for _ in range(N)])
normal = sigma*estandar + mu

# Graficamos
xn = np.linspace(mu-3*sigma, mu+3*sigma, 200)
yn = 1/math.sqrt(2*math.pi*sigma**2)*np.exp(-(xn-mu)**2/(2*sigma**2))
plt.figure()
plt.hist(normal, density= True, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid')
plt.plot(xn, yn, color='red', label=f'Densidad normal({mu}, {sigma})')
plt.title(f'Distribución normal({mu}, {sigma})')
plt.show()

# Clase para simular la normal
class Normal():

  def __init__(self, mu, sigma):
    '''
    mu: media de la normal
    sigma: desviación estándar de la normal
    '''
    self.mu = mu
    self.sigma = sigma

  def simular(self, N = 10000):
    estandar = np.array([ar_normal() for _ in range(N)])
    normal = self.sigma*estandar + self.mu
    return normal

  def graficar(self, N = 10000, dens = True):
    normal = self.simular(N)
    plt.figure()
    plt.hist(normal, density= True, bins = 50, edgecolor = 'darkblue', color = 'turquoise', align='mid')
    if dens:
      xn = np.linspace(self.mu-3*self.sigma, self.mu+3*self.sigma, 200)
      yn = 1/math.sqrt(2*math.pi*self.sigma**2)*np.exp(-(xn-self.mu)**2/(2*self.sigma**2))
      plt.plot(xn, yn, color='red', label=f'Densidad normal({self.mu}, {self.sigma})')
    plt.title(f'Distribución normal({self.mu}, {self.sigma})')
    plt.show()

# Ejemplos
n1 = Normal(0, 1)
n1.graficar()

n2 = Normal(0, 10000)
n2.graficar()

n3 = Normal(-6123, 0.1)
n3.graficar()