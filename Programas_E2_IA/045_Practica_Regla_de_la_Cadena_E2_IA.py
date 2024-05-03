# Practica_045_Regla_de_la_Cadena_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Regla_de_la_Cadena

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def regla_de_la_cadena(eventos, probabilidades_condicionales):
    # Inicializamos la probabilidad conjunta como 1
    probabilidad_conjunta = 1
    
    # Iteramos sobre la lista de eventos
    for i in range(len(eventos) - 1):
        # Obtenemos el evento actual y el siguiente evento
        evento_actual = eventos[i]
        siguiente_evento = eventos[i+1]
        
        # Obtenemos la probabilidad condicional del siguiente evento dado el evento actual
        probabilidad_condicional = probabilidades_condicionales[evento_actual][siguiente_evento]
        
        # Actualizamos la probabilidad conjunta multiplicándola por la probabilidad condicional
        probabilidad_conjunta *= probabilidad_condicional
    
    return probabilidad_conjunta

# Definimos una lista de eventos
eventos = ['A', 'B', 'C']

# Definimos las probabilidades condicionales como un diccionario de diccionarios
probabilidades_condicionales = {
    'A': {'B': 0.6, 'C': 0.4},
    'B': {'C': 0.7}
}

# Calculamos la probabilidad conjunta utilizando la Regla de la Cadena
probabilidad_conjunta = regla_de_la_cadena(eventos, probabilidades_condicionales)

# Imprimimos el resultado
print("La probabilidad conjunta de los eventos", eventos, "es:", probabilidad_conjunta)
