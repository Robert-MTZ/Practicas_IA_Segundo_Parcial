# Practica_094_Cinematica_Inversa_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Cinematica_Inversa

import math

# Definimos la longitud de los eslabones del robot
L1 = 5  # Longitud del primer eslabón
L2 = 4  # Longitud del segundo eslabón

# Definimos la posición deseada del extremo del robot (x, y)
x = 2
y = 5

# Calculamos la distancia desde el origen al punto deseado
distancia = math.sqrt(x**2 + y**2)

# Calculamos el ángulo entre la línea que une el origen con el punto deseado y el primer eslabón
# Usamos la ley del coseno
alpha = math.acos((L1**2 + distancia**2 - L2**2) / (2 * L1 * distancia))

# Calculamos el ángulo de la articulación 1 con respecto al eje x
theta1 = math.atan2(y, x) - alpha

# Calculamos el ángulo de la articulación 2 con respecto al eje x
# Usamos la ley del coseno nuevamente
beta = math.acos((L1**2 + L2**2 - distancia**2) / (2 * L1 * L2))
theta2 = math.pi - beta

# Convertimos los ángulos a grados para mayor legibilidad
theta1_grados = math.degrees(theta1)
theta2_grados = math.degrees(theta2)

# Imprimimos los ángulos de las articulaciones
print("Ángulo de la articulación 1:", theta1_grados, "grados")
print("Ángulo de la articulación 2:", theta2_grados, "grados")
