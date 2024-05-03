# Practica_040_Probabilidad_Condicionada_y_Normalizacion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Probabilidad_Condicionada_y_Normalizacion

import numpy as np # Generar numeros aleatorios y realizar cálculos matriciales de manera eficiente

def probabilidad_condicionada_y_normalizacion(evento_a, evento_b):
    # Crear una matriz de probabilidades aleatorias para el evento A dado B
    probabilidades = np.random.rand(len(evento_a), len(evento_b))
    
    # Normalizar las probabilidades para que sumen 1
    probabilidades /= np.sum(probabilidades)
    
    return probabilidades

# Evento B: lanzar un dado
evento_b = [1, 2, 3, 4, 5, 6]

# Evento A: obtener un número par en el lanzamiento del dado
evento_a = [2, 4, 6]

# Calcular probabilidades condicionadas y normalizadas
prob_condicionada_normalizada = probabilidad_condicionada_y_normalizacion(evento_a, evento_b)

# Imprimir las probabilidades
print("Probabilidades condicionadas y normalizadas:")
print(prob_condicionada_normalizada)
