# Practica_131_Modelo_Probabilista_Racional_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Modelo_Probabilista_Racional

import numpy as np

# Definimos una función para calcular la utilidad esperada de una acción
def utilidad_esperada(probabilidades, utilidades):
    return np.dot(probabilidades, utilidades)

# Definimos las probabilidades y utilidades de cada acción
probabilidades = np.array([0.3, 0.5, 0.2])  # Probabilidades de las acciones
utilidades = np.array([100, 50, 0])  # Utilidades de las acciones

# Calculamos la utilidad esperada de cada acción
utilidad_esperada_accion = utilidad_esperada(probabilidades, utilidades)

# Imprimimos la utilidad esperada de cada acción
for i, utilidad in enumerate(utilidad_esperada_accion):
    print(f"Utilidad esperada de la acción {i+1}: {utilidad}")

# Seleccionamos la acción con la mayor utilidad esperada
mejor_accion = np.argmax(utilidad_esperada_accion)
print(f"La mejor acción es la acción {mejor_accion + 1}")
