# Practica_093_Movimiento_Espacio_de_Configuracion_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Movimiento_Espacio_de_Configuracion

import matplotlib.pyplot as plt

# Definimos las dimensiones del entorno
xmin, xmax = -5, 5
ymin, ymax = -5, 5

# Creamos una figura y ejes para el gráfico
fig, ax = plt.subplots()

# Establecemos los límites del gráfico
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])

# Dibujamos el entorno
ax.plot([xmin, xmin, xmax, xmax, xmin], [ymin, ymax, ymax, ymin, ymin], 'k-')

# Definimos la posición inicial del robot
robot_posicion_inicial = (0, 0)

# Dibujamos la posición inicial del robot
ax.plot(robot_posicion_inicial[0], robot_posicion_inicial[1], 'ro', label='Posición Inicial')

# Definimos una lista de posiciones candidatas para el robot
posiciones_candidatas = [(1, 1), (2, 2), (-1, 1), (-2, -2)]

# Dibujamos las posiciones candidatas del robot
for posicion in posiciones_candidatas:
    ax.plot(posicion[0], posicion[1], 'bo')

# Etiquetamos los ejes y añadimos una leyenda
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Mostramos el gráfico
plt.title('Espacio de Configuración del Robot')
plt.grid(True)
plt.show()

