# Practica_051_Monte_Carlo_para_Cadenas_de_Markov_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Monte_Carlo_para_Cadenas_de_Markov

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def funcion_objetivo(x):
    # Función objetivo que queremos muestrear
    return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)

def metropolis_hastings(func_objetivo, propuesta, n_iter, sigma=1):
    # Algoritmo Metropolis-Hastings para muestrear la función objetivo
    muestras = []
    aceptadas = 0
    x_actual = np.random.randn()  # Inicializamos la cadena con un valor aleatorio
    
    for _ in range(n_iter):
        # Generamos una propuesta de movimiento
        x_propuesto = propuesta(x_actual, sigma)
        
        # Calculamos la probabilidad de aceptación
        prob_aceptacion = min(1, func_objetivo(x_propuesto) / func_objetivo(x_actual))
        
        # Aceptamos o rechazamos la propuesta
        if np.random.rand() < prob_aceptacion:
            x_actual = x_propuesto
            aceptadas += 1
        
        # Agregamos la muestra a la lista
        muestras.append(x_actual)
    
    tasa_aceptacion = aceptadas / n_iter
    return muestras, tasa_aceptacion

def propuesta_normal(x_actual, sigma):
    """Genera una propuesta de movimiento usando una distribución normal."""
    return x_actual + np.random.normal(scale=sigma)

# Parámetros del algoritmo
n_iter = 10000  # Número de iteraciones
sigma = 1  # Desviación estándar de la distribución de propuesta

# Ejecutamos el algoritmo Metropolis-Hastings
muestras, tasa_aceptacion = metropolis_hastings(funcion_objetivo, propuesta_normal, n_iter, sigma)

# Imprimimos la tasa de aceptación
print("Tasa de aceptación:", tasa_aceptacion)

# Imprimimos el valor medio de las muestras
print("Valor medio de las muestras:", np.mean(muestras))
