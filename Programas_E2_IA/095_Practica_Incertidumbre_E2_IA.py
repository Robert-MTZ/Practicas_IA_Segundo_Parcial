# Practica_095_Incertidumbre_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Incertidumbre

import numpy as np

# Definimos las incertidumbres de las mediciones
incertidumbre_medicion_1 = 0.1
incertidumbre_medicion_2 = 0.2

# Regla de la suma para combinar las incertidumbres
incertidumbre_suma = np.sqrt(incertidumbre_medicion_1**2 + incertidumbre_medicion_2**2)

# Regla del producto para combinar las incertidumbres
incertidumbre_producto = np.sqrt(incertidumbre_medicion_1**2 + incertidumbre_medicion_2**2)

# Imprimimos los resultados
print("Incertidumbre combinada por la regla de la suma:", incertidumbre_suma)
print("Incertidumbre combinada por la regla del producto:", incertidumbre_producto)
