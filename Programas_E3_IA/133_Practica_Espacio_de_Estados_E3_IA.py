# Practica_133_Espacio_de_Estados_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Espacio_de_Estados

from collections import deque

# Definimos la función que representa el problema y sus operadores
def problema(estado):
    return estado == 8

def operadores(estado):
    return [estado + 1, estado * 2]

# Implementamos el algoritmo de búsqueda en amplitud (BFS)
def bfs(inicial):
    # Creamos una cola para almacenar los estados a explorar
    cola = deque()
    cola.append((inicial, [inicial]))  # Inicializamos la cola con el estado inicial y el camino

    while cola:
        estado_actual, camino_actual = cola.popleft()  # Extraemos el primer estado de la cola
        print("Explorando estado:", estado_actual)
        
        if problema(estado_actual):  # Verificamos si hemos encontrado una solución
            return camino_actual
        
        # Generamos los nuevos estados a partir de los operadores y los añadimos a la cola
        for op in operadores(estado_actual):
            nuevo_estado = op
            nuevo_camino = camino_actual + [nuevo_estado]
            cola.append((nuevo_estado, nuevo_camino))

    return None

# Definimos el estado inicial
estado_inicial = 1

# Ejecutamos el algoritmo BFS
camino_solucion = bfs(estado_inicial)

# Imprimimos el camino de solución encontrado
print("Camino de solución:", camino_solucion)
