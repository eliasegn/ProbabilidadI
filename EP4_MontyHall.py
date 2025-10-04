################################################################################
# El Problema de Monty Hall
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
# Clase para Monty Hall sin cambio de puerta

class MontyHall_SinCambio():

  def __init__(self):
    '''
    intentos: el número de veces que jugaremos
    puntaje_promedio: lista para guardar las medias de los lanzamientos
    contador: lista para guardar los intentos
    proba: probabilidad de ganar
    jugada: tipo de jugada
    '''
    intentos = 0
    while intentos < 1:
      intentos = int(input('¿Cuántas veces quieres intentar? '))
    self.intentos = intentos
    self.puntaje_promedio = []
    self.contador = [] #Se puede quitar
    self.proba = 0
    self.jugada = "Sin Cambio"

  def Intento(self):
    real = random.randint(0,2) # Aquí está el coche
    priori = random.randint(0,2) # Esta es la que yo elijo

    if real == priori: # Si donde elegí está el carro, gané
        return 1
    else: # Si donde elegí no está el carro, perdí
        return 0

  def Simular(self):
    # Guardamos los puntajes
      puntajes = []
      # Repetimos tantas veces como nos indican
      for i in range(1, self.intentos + 1):
          puntajes.append(self.Intento())  # Guardamos el resultado de esa jugada
          self.puntaje_promedio.append(np.mean(puntajes)) # Guardamos la estimación de la probabilidad
          self.contador.append(i)
      # Guardamos la última estimación y graficamos
      self.proba = self.puntaje_promedio[-1]
      print(self)
      self.GraficarResultados()

  def GraficarResultados(self):
    # Gráfica de las probabilidades
    plt.figure(figsize=(11,6))
    plt.plot(self.contador, self.puntaje_promedio, marker='o', linestyle='-', color='darkblue')
    plt.title(f"Monty Hall ({self.jugada}): {self.intentos}", fontsize=25)
    plt.xlabel('Intentos', fontsize=20)
    plt.ylabel('Probabilidad de ganar', fontsize=20)
    plt.grid(True)  # Simula el estilo "whitegrid" de seaborn
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


  def __str__(self):
    return "\n         Informe        \n**************************\nTipo de jugada: %s \nIntentos: %s \nProbabilidad de ganar: %s \n \
    " %(self.jugada, self.intentos, self.proba)

# Clase para Monty Hall con cambio de puerta
class MontyHall_ConCambio(MontyHall_SinCambio):

    def __init__(self):
        intentos = 0
        while intentos < 1:
            intentos = int(input('¿Cuántas veces quieres intentar? ' ))
        self.intentos = intentos
        self.puntaje_promedio = []
        self.contador = []
        self.proba = 0
        self.jugada = "Con Cambio" # Con cambio

    def Intento(self):
        real = random.randint(0,2) # Aquí está el carro
        priori = random.randint(0,2) # Este es la elección inicial

        opciones_posteriori = [0,1,2] #list(range(3))
        opciones_posteriori.remove(priori) # Quitamos la elegida (porque esa no elige el presentador)

        # Quitamos la puerta donde no haya carro
        if opciones_posteriori[0] == real:
            del opciones_posteriori[1]
        elif opciones_posteriori[1] == real:
            del opciones_posteriori[0]
        else:
            del opciones_posteriori[random.randint(0,1)]

        posteriori = opciones_posteriori[0] # Aquí hacemos el cambio de puerta

        # Puntajes
        if posteriori == real:
            return 1
        else:
            return 0


# Menú interactivo
def Menu():
    # Menu desplegado
    print("     Monty Hall     ")
    print("**************************")
    print("(1) Jugar sin cambio")
    print("(2) Jugar con cambio")
    print("(3) Terminar")
    print("**************************")

    # Preguntamos cómo quieren jugar
    eleccion = int(input("¿Cómo quieres jugar? "))

    # Jugar como quiere el usuario
    if eleccion == 1:
        juego = MontyHall_SinCambio()
    elif eleccion == 2:
        juego = MontyHall_ConCambio()
    else:
        print('¡Gracias por jugar!')
        return None

    # Simular el juego
    juego.Simular()

    return None

# Ejemplos
Menu()

