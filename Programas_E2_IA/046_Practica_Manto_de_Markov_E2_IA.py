# Practica_046_Manto_de_Markov_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Manto_de_Markov

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente 

def modelo_markov(estado_inicial, transiciones, longitud_secuencia):
    # Creamos una lista para almacenar la secuencia de estados
    secuencia = [estado_inicial]
    
    # Iteramos para generar la secuencia de estados
    for _ in range(longitud_secuencia - 1):
        # Obtenemos el último estado en la secuencia
        estado_actual = secuencia[-1]
        
        # Obtenemos las probabilidades de transición desde el estado actual
        probabilidades = transiciones[estado_actual]
        
        # Generamos el siguiente estado basado en las probabilidades de transición
        siguiente_estado = np.random.choice(list(probabilidades.keys()), p=list(probabilidades.values()))
        
        # Añadimos el siguiente estado a la secuencia
        secuencia.append(siguiente_estado)
    
    return secuencia

# Definimos los estados posibles
estados = ['A', 'B', 'C']

# Definimos las probabilidades de transición entre estados como un diccionario de diccionarios
transiciones = {
    'A': {'A': 0.7, 'B': 0.2, 'C': 0.1},
    'B': {'A': 0.3, 'B': 0.4, 'C': 0.3},
    'C': {'A': 0.5, 'B': 0.1, 'C': 0.4}
}

# Definimos el estado inicial
estado_inicial = 'A'

# Definimos la longitud de la secuencia deseada
longitud_secuencia = 10

# Generamos la secuencia de estados utilizando el modelo de Manto de Markov
secuencia = modelo_markov(estado_inicial, transiciones, longitud_secuencia)

# Imprimimos la secuencia generada
print("Secuencia de estados generada:", secuencia)

