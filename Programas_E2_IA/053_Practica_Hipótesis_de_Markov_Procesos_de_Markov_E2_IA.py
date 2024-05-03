# Practica_053_Hipótesis_de_Markov_Procesos_de_Markov_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Hipótesis_de_Markov_Procesos_de_Markov

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class ProcesoMarkov:
    def __init__(self, matriz_transicion, estados):
        
        self.matriz_transicion = np.array(matriz_transicion)
        self.estados = estados
    
    def generar_secuencia(self, estado_inicial, longitud_secuencia):
     
        secuencia = [estado_inicial]
        estado_actual = estado_inicial
        
        for _ in range(longitud_secuencia - 1):
            # Calcula la probabilidad de transición desde el estado actual
            probabilidades_transicion = self.matriz_transicion[self.estados.index(estado_actual), :]
            # Elige un nuevo estado basado en las probabilidades de transición
            estado_nuevo = np.random.choice(self.estados, p=probabilidades_transicion)
            # Agrega el nuevo estado a la secuencia
            secuencia.append(estado_nuevo)
            # Actualiza el estado actual
            estado_actual = estado_nuevo
        
        return secuencia

# Definimos la matriz de transición y los estados
matriz_transicion = [[0.7, 0.3], [0.4, 0.6]]  # Ejemplo de matriz de transición para dos estados
estados = ['A', 'B']  # Ejemplo de estados

# Creamos una instancia del proceso de Markov
proceso = ProcesoMarkov(matriz_transicion, estados)

# Generamos una secuencia de estados
secuencia_generada = proceso.generar_secuencia('A', 10)

# Imprimimos la secuencia generada
print("Secuencia generada:", secuencia_generada)
