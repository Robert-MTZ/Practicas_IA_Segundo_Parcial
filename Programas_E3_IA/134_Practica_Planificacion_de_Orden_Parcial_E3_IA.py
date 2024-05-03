# Practica_134_Planificacion_de_Orden_Parcial_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Planificacion_de_Orden_Parcial

import networkx as nx

# Creamos un grafo dirigido para representar las acciones y sus dependencias
grafo = nx.DiGraph()

# Añadimos nodos al grafo, que representan las acciones en el problema de planificación
grafo.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Añadimos aristas al grafo para representar las dependencias entre las acciones
grafo.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])

# Calculamos el orden parcial de las acciones utilizando el algoritmo topológico de ordenación
orden_parcial = list(nx.topological_sort(grafo))

# Imprimimos el orden parcial de las acciones
print("Orden parcial de las acciones:", orden_parcial)

