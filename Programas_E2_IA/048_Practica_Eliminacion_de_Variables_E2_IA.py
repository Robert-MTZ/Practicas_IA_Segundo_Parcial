# Practica_048_Eliminacion_de_Variables_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Eliminacion_de_Variables

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def eliminacion_de_variables(variables_eliminar, variables_observadas, red_bayesiana):
    # Crear una copia de la red bayesiana
    red_bayesiana_reducida = red_bayesiana.copy()
    
    # Eliminar las variables irrelevantes de la red bayesiana
    for variable in variables_eliminar:
        del red_bayesiana_reducida[variable]
    
    # Calcular la distribución marginal de las variables observadas en la red bayesiana reducida
    distribucion_marginal = inferencia_por_enumeracion(variables_observadas, {}, red_bayesiana_reducida)
    
    return distribucion_marginal

def inferencia_por_enumeracion(variables, evidencia, red_bayesiana):
    # Inicializar la distribución conjunta como 1
    distribucion_conjunta = 1
    
    # Iterar sobre todas las variables
    for variable in variables:
        # Si la variable no está en la evidencia, calcular su probabilidad marginal
        if variable not in evidencia:
            distribucion_conjunta *= inferencia_variable(variable, evidencia, red_bayesiana)
    
    return distribucion_conjunta

def inferencia_variable(variable, evidencia, red_bayesiana):
    # Obtener los padres de la variable
    padres = red_bayesiana[variable]['padres']
    
    # Calcular la probabilidad condicional de la variable dado los valores de sus padres
    probabilidad_condicional = red_bayesiana[variable]['probabilidad_condicional'][tuple([evidencia[variable] for variable in padres])]
    
    return probabilidad_condicional

# Definir la red bayesiana
red_bayesiana = {
    'A': {
        'padres': [],
        'probabilidad_condicional': {'': 0.3}
    },
    'B': {
        'padres': ['A'],
        'probabilidad_condicional': {'0': 0.6, '1': 0.4}
    }
}

# Definir las variables a eliminar y las variables observadas
variables_eliminar = ['A']
variables_observadas = ['B']

# Calcular la distribución marginal de las variables observadas
distribucion_marginal = eliminacion_de_variables(variables_eliminar, variables_observadas, red_bayesiana)

# Imprimir el resultado
print("La distribución marginal de las variables observadas es:", distribucion_marginal)
