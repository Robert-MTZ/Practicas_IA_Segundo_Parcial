# Practica_043_Regla_de_Bayes_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Regla_de_Bayes

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

def regla_de_bayes(probabilidad_a, probabilidad_b_dado_a, probabilidad_b):
    # Calculamos la probabilidad de no A
    probabilidad_no_a = 1 - probabilidad_a
    
    # Calculamos la probabilidad de no B
    probabilidad_no_b = 1 - probabilidad_b
    
    # Calculamos la probabilidad de B dado no A
    probabilidad_b_dado_no_a = 1 - probabilidad_b_dado_a
    
    # Aplicamos la Regla de Bayes
    probabilidad_a_dado_b = (probabilidad_b_dado_a * probabilidad_a) / ((probabilidad_b_dado_a * probabilidad_a) + (probabilidad_b_dado_no_a * probabilidad_no_a))
    
    return probabilidad_a_dado_b

# Definimos las probabilidades
probabilidad_a = 0.3  # Probabilidad de A
probabilidad_b_dado_a = 0.7  # Probabilidad de B dado A
probabilidad_b = 0.5  # Probabilidad de B

# Calculamos la probabilidad de A dado B usando la Regla de Bayes
probabilidad_a_dado_b = regla_de_bayes(probabilidad_a, probabilidad_b_dado_a, probabilidad_b)

# Imprimimos el resultado
print("La probabilidad de A dado B es:", probabilidad_a_dado_b)
