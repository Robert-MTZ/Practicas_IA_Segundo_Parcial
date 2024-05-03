# Practica_038_Incertidumbre_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Incertidumbre

import numpy as np # Importamos NumPy para trabajar con matrices

def calcular_entropia(dataset): # Función para calcular la entropía de un conjunto de datos

    total_muestras = len(dataset)  # Calcula el numero total de muestras en el dataset
    
    # Contador para almacenar el numero de veces que aparece cada clase en el dataset
    conteo_clases = {}
    for muestra in dataset:
        clase = muestra[-1]  # Suponemos que la última columna contiene la clase
        if clase not in conteo_clases:
            conteo_clases[clase] = 0
        conteo_clases[clase] += 1
    
    # Calcula la entropía utilizando la fórmula de entropía de Shannon
    entropia = 0
    for clase, conteo in conteo_clases.items():
        probabilidad = conteo / total_muestras
        entropia -= probabilidad * np.log2(probabilidad)
    
    return entropia

dataset = np.array([ # Se crea un array de Numpy (Almacen de datos)
    [120, 45, 0],
    [140, 55, 1],
    [130, 60, 1],
    [125, 50, 0],
    [135, 65, 1],
    [128, 48, 0],
    [132, 52, 0],
    [138, 58, 1]
])

# Calcula la entropía del conjunto de datos
entropia = calcular_entropia(dataset)

# Imprime la entropía calculada
print("Entropía del conjunto de datos:", entropia)
