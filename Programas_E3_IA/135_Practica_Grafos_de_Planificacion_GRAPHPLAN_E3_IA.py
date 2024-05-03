# Practica_135_Grafos_de_Planificacion_GRAPHPLAN_Parcial_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Grafos_de_Planificacion_GRAPHPLAN

import pygraphviz as pgv

# Definimos una función para crear el grafo de planificación
def crear_grafo_planificacion(problema, acciones):
    # Creamos un nuevo grafo dirigido
    grafo = pgv.AGraph(strict=False, directed=True)

    # Añadimos los nodos correspondientes a las acciones
    for accion in acciones:
        grafo.add_node(accion)

    # Añadimos las aristas que representan las precondiciones y efectos de las acciones
    for accion, precondiciones, efectos in problema:
        for precondicion in precondiciones:
            grafo.add_edge(precondicion, accion)
        for efecto in efectos:
            grafo.add_edge(accion, efecto)

    return grafo

# Definimos el problema de planificación (acciones, precondiciones y efectos)
problema = [
    ('MoverA', ['Libre(A)', 'En(A, Mesa)'], ['En(A, B)']),
    ('MoverB', ['Libre(B)', 'En(B, Mesa)'], ['En(B, A)'])
]

# Definimos las acciones posibles en el problema
acciones = ['MoverA', 'MoverB']

# Creamos el grafo de planificación
grafo_planificacion = crear_grafo_planificacion(problema, acciones)

# Dibujamos el grafo de planificación y lo guardamos en un archivo
grafo_planificacion.draw('grafo_planificacion.png', prog='dot')

# Imprimimos el grafo de planificación en la consola
print("Grafo de planificación:")
print(grafo_planificacion)
 
