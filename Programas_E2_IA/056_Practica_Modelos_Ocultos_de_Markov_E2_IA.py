# Practica_056_Modelos_Ocultos_de_Markov_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Modelos_Ocultos_de_Markov

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class HMM:
    def __init__(self, A, B, pi):
        
        self.A = np.array(A)  # Matriz de transición de estado
        self.B = np.array(B)  # Matriz de emisión
        self.pi = np.array(pi)  # Distribución inicial de estado
        self.N = len(pi)  # Número de estados
        self.M = len(B[0])  # Número de símbolos de observación
        
    def generar_secuencia(self, longitud):
      
        secuencia_estados = []
        secuencia_observaciones = []
        estado_actual = np.random.choice(range(self.N), p=self.pi)  # Escoge un estado inicial
        for _ in range(longitud):
            secuencia_estados.append(estado_actual)
            observacion = np.random.choice(range(self.M), p=self.B[estado_actual])  # Genera una observación
            secuencia_observaciones.append(observacion)
            estado_actual = np.random.choice(range(self.N), p=self.A[estado_actual])  # Cambia de estado
        return secuencia_observaciones, secuencia_estados

# Parámetros del HMM
A = [[0.7, 0.3],  # Matriz de transición de estado
     [0.4, 0.6]]
B = [[0.1, 0.4, 0.5],  # Matriz de emisión
     [0.6, 0.3, 0.1]]
pi = [0.6, 0.4]  # Distribución inicial de estado

# Creamos una instancia del HMM
hmm = HMM(A, B, pi)

# Generamos una secuencia de observaciones y estados ocultos
secuencia_observaciones, secuencia_estados = hmm.generar_secuencia(10)

# Imprimimos la secuencia de observaciones y estados ocultos
print("Secuencia de observaciones:", secuencia_observaciones)
print("Secuencia de estados ocultos:", secuencia_estados)

