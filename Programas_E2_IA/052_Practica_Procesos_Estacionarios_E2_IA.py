# Practica_052_Procesos_Estacionarios_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Procesos_Estacionarios

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def proceso_AR(phi, sigma, n):
  
    # Inicializamos la serie temporal con ruido blanco
    serie = np.random.normal(0, sigma, n)
    
    # Iteramos sobre el número de puntos a generar
    for i in range(len(phi), n):
        # Calculamos el valor autoregresivo como una combinación lineal de los valores anteriores
        valor_AR = np.sum(np.array(phi) * serie[i-len(phi):i])
        # Agregamos ruido blanco al valor autoregresivo
        valor = valor_AR + np.random.normal(0, sigma)
        # Agregamos el valor a la serie temporal
        serie = np.append(serie, valor)
    
    return serie

# Parámetros del proceso AR
phi = [0.5, -0.2]  # Coeficientes autoregresivos
sigma = 1  # Desviación estándar del ruido blanco
n = 100  # Número de puntos a generar

# Generamos la serie temporal del proceso AR
serie_AR = proceso_AR(phi, sigma, n)

# Imprimimos los primeros 10 valores de la serie temporal
print("Primeros 10 valores de la serie temporal:")
print(serie_AR[:10])

