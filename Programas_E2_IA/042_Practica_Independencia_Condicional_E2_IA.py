# Practica_042_Independencia_Condicional_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Independencia_Condicional

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def independencia_condicional(evento_a, evento_b, evento_c):
    # Generamos probabilidades aleatorias para los eventos A, B y C
    probabilidad_a = np.random.rand()
    probabilidad_b = np.random.rand()
    probabilidad_c = np.random.rand()
    
    # Verificamos la independencia condicional
    if probabilidad_a * probabilidad_b == probabilidad_c:
        resultado = "Los eventos A y B son independientes dado el evento C."
    else:
        resultado = "Los eventos A y B no son independientes dado el evento C."
    
    return resultado

# Definimos los eventos A, B y C
evento_a = "Lloverá"
evento_b = "Habrá tráfico"
evento_c = "El pronóstico del tiempo es soleado"

# Calculamos la independencia condicional
resultado = independencia_condicional(evento_a, evento_b, evento_c)

# Imprimimos el resultado
print(resultado)
