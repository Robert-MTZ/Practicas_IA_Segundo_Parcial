# Practica_047_Inferencia_por_Enumeracion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Inferencia_por_Enumeracion

import numpy as np

def inferencia_por_enumeracion(evento, evidencia, red_bayesiana):
    # Inicializamos la probabilidad conjunta como 1
    probabilidad_conjunta = 1
    
    # Iteramos sobre todos los valores posibles del evento
    for valor_evento in red_bayesiana[evento]:
        # Inicializamos la probabilidad condicional como 1
        probabilidad_condicional = 1
        
        # Iteramos sobre todas las variables de evidencia
        for variable, valor_evidencia in evidencia.items():
            # Obtenemos la probabilidad condicional de la variable dada la evidencia
            prob_condicional = red_bayesiana[variable][valor_evento][valor_evidencia]
            
            # Actualizamos la probabilidad condicional multiplicándola por la probabilidad conjunta acumulada
            probabilidad_condicional *= prob_condicional
        
        # Actualizamos la probabilidad conjunta multiplicándola por la probabilidad condicional
        probabilidad_conjunta *= probabilidad_condicional
    
    return probabilidad_conjunta

# Definimos la red bayesiana como un diccionario de diccionarios de diccionarios
red_bayesiana = {
    'A': {
        '1': {'1': 0.3, '2': 0.7},
        '2': {'1': 0.6, '2': 0.4}
    },
    'B': {
        '1': {'1': 0.5, '2': 0.2},
        '2': {'1': 0.5, '2': 0.8}
    },
    'C': {
        '1': {'1': {'1': 0.1, '2': 0.2}, '2': {'1': 0.3, '2': 0.4}},
        '2': {'1': {'1': 0.9, '2': 0.8}, '2': {'1': 0.7, '2': 0.6}}
    }
}

# Definimos el evento de interés y la evidencia observada
evento = 'A'
evidencia = {'B': '1', 'C': '2'}

# Calculamos la probabilidad del evento dado la evidencia utilizando la inferencia por enumeración
probabilidad = inferencia_por_enumeracion(evento, evidencia, red_bayesiana)

# Imprimimos el resultado
print("La probabilidad de", evento, "dado la evidencia", evidencia, "es:", probabilidad)


