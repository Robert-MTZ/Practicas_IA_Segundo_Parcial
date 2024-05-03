# Practica_096_Dinamica_y_Control_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Dinamica_y_Control

import numpy as np
import matplotlib.pyplot as plt

# Definimos las constantes del sistema
m = 1.0  # Masa (kg)
k = 10.0  # Constante del resorte (N/m)
b = 0.5  # Coeficiente de amortiguamiento (N.s/m)

# Definimos la función de la dinámica del sistema
def dinamica(x, v, F):

    a = (F - k*x - b*v) / m  # Segunda Ley de Newton
    return a

# Definimos el controlador proporcional (P)
Kp = 20.0  # Ganancia proporcional

# Definimos la posición deseada
x_deseada = 1.0  # Posición deseada (m)

# Definimos las condiciones iniciales
x_0 = 0.0  # Posición inicial
v_0 = 0.0  # Velocidad inicial

# Definimos los parámetros de la simulación
tiempo_simulacion = 10.0  # Tiempo total de simulación (s)
dt = 0.01  # Paso de tiempo (s)
num_pasos = int(tiempo_simulacion / dt)  # Número de pasos de tiempo

# Creamos arrays para almacenar los resultados de la simulación
t = np.linspace(0.0, tiempo_simulacion, num_pasos)  # Array de tiempo
x = np.zeros(num_pasos)  # Array de posición
v = np.zeros(num_pasos)  # Array de velocidad
F_control = np.zeros(num_pasos)  # Array de fuerza de control

# Simulamos la dinámica del sistema con control proporcional
for i in range(num_pasos):
    # Calculamos el error de posición
    error = x_deseada - x_0
    
    # Calculamos la fuerza de control utilizando el controlador proporcional (P)
    F_control[i] = Kp * error
    
    # Calculamos la aceleración utilizando la dinámica del sistema
    a = dinamica(x_0, v_0, F_control[i])
    
    # Actualizamos la velocidad y la posición utilizando la integración numérica
    v_1 = v_0 + a * dt
    x_1 = x_0 + v_0 * dt
    
    # Almacenamos los resultados
    x[i] = x_1
    v[i] = v_1
    
    # Actualizamos las condiciones iniciales para el próximo paso de tiempo
    x_0 = x_1
    v_0 = v_1

# Visualizamos los resultados
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Posición')
plt.plot(t, v, label='Velocidad')
plt.plot(t, F_control, label='Fuerza de Control')
plt.axhline(y=x_deseada, color='r', linestyle='--', label='Posición Deseada')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor')
plt.title('Control Proporcional de un Sistema Masa-Resorte-Amortiguador')
plt.legend()
plt.grid(True)
plt.show()
