# Practica_050_Ponderacion_de_Verosimilitud_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Ponderacion_de_Verosimilitud

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def ponderacion_verosimilitud(datos, parametros, modelo):
    # Inicializamos una lista para almacenar los pesos de cada observacion
    pesos = []
    
    # Iteramos sobre cada observación en los datos
    for observacion in datos:
        # Calculamos la verosimilitud de la observación bajo los parámetros dados
        verosimilitud = modelo(observacion, parametros)
        # Agregamos la verosimilitud a la lista de pesos
        pesos.append(verosimilitud)
    
    # Normalizamos los pesos dividiendo por la suma total de verosimilitudes
    pesos_normalizados = pesos / np.sum(pesos)
    
    return pesos_normalizados

# Definimos un modelo simple que devuelve la diferencia entre la observación y el parámetro
def modelo_simple(observacion, parametro):
    return np.abs(observacion - parametro)

# Generamos datos de ejemplo y parámetros de ejemplo
datos = [1, 2, 3, 4, 5]
parametro = 3

# Calculamos los pesos de cada observación usando el método de Ponderación de Verosimilitud
pesos = ponderacion_verosimilitud(datos, parametro, modelo_simple)

# Imprimimos los pesos resultantes
print("Pesos de las observaciones:", pesos)
