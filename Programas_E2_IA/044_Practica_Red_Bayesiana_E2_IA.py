# Practica_044_Red_Bayesiana_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Red_Bayesiana


import networkx as nx
import matplotlib.pyplot as plt # Es una interfaz que proporciona funciones para crear graficos

# Creamos un nuevo gráfico dirigido
red_bayesiana = nx.DiGraph()

# Añadimos los nodos (variables) al gráfico
red_bayesiana.add_node("Lluvia")
red_bayesiana.add_node("Tráfico")

# Añadimos una relación entre "Lluvia" y "Tráfico"
red_bayesiana.add_edge("Lluvia", "Tráfico")

# Dibujamos la red bayesiana
nx.draw(red_bayesiana, with_labels=True, node_size=1000, node_color="lightblue", font_size=20, font_weight="bold")

# Mostramos el gráfico
plt.show()
