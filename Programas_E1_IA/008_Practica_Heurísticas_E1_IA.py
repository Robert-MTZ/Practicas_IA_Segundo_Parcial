# Practica_008_Heurísticas_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Heurísticas

import heapq # Se manda llamr la biblioteca heapq para usar la cola de prioridad

class Grafo: # Se crea la clase Grafo
    def __init__(self): 
        self.vertices = {} # # Inicializa el diccionario de vértices del grafo

    def agregar_vertice(self, v): # Esta funcion se encarga de agregar un vertice al grafo
        if v not in self.vertices: # Verifiva si el vertice no esta presente en el diccionario
            self.vertices[v] = {} #  # Agrega un nuevo vértice al grafo si no existe

    def agregar_arista(self, v1, v2, peso): # Esta funcion se encarga de agregar un arista al grafo
        self.agregar_vertice(v1) # Verifica que el vertice este presente en el grafo antes de agregar el arista
        self.agregar_vertice(v2) # Verifica que el vertice este presente en el grafo antes de agregar el arista
        self.vertices[v1][v2] = peso # Agrega una arista entre dos vértices con un peso dado


    def heuristic(self, v, objetivo): # Este metodo  es responsable de calcular la heuristica entre un vertice dado y un objetivo dado
        return abs(v[0] - objetivo[0]) + abs(v[1] - objetivo[1]) # Calcula la distancia Manhattan entre el vértice dado v y el objetivo dado

    def a_estrella(self, inicio, objetivo): # Implementa el algoritmo A* para encontrar el camino más corto desde un nodo inicial 
        frontera = [] # Inicializa la cola de prioridad para almacenar los nodos a explorar
        heapq.heappush(frontera, (0, inicio))  # Agrega el nodo inicial a la frontera con prioridad 0
        padres = {} # Diccionario para almacenar los padres de los nodos
        costo_g = {inicio: 0} # Diccionario para almacenar los costos g(n) de los nodos

        while frontera: # Mientras la frontera no esté vacía
            costo, actual = heapq.heappop(frontera) # Obtiene el nodo actual con el menor costo
            if actual == objetivo: # Si el nodo actual es el objetivo, termina y devuelve el camino
                camino = [] # Se inicializa una lista vacia 
                while actual in padres: # Se crea un bucle que se ejecutara mientras el nodo actual este presente en el diccionario padres
                    camino.append(actual) # Se utiliza para agregar el nodo actual al camino más corto
                    actual = padres[actual] # Se utiliza para actualizar el nodo actual con su nodo padre
                camino.append(inicio) #  Agrega el nodo inicial al final del camino asegura que el camino completo
                return list(reversed(camino)) # finaliza la ejecución del método a_estrella y devuelve el camino más corto encontrado desde el nodo inicial hasta el nodo objetivo en forma de lista, con el orden correcto de nodos desde el inicio hasta el objetivo

            for vecino in self.vertices[actual]: # Para cada vecino del nodo actual
                nuevo_costo = costo_g[actual] + self.vertices[actual][vecino] # Calcula el nuevo costo g(n)
                if vecino not in costo_g or nuevo_costo < costo_g[vecino]:  # Si el nuevo costo es menor 
                    costo_g[vecino] = nuevo_costo  # Actualiza el costo g(n) del vecino
                    prioridad = nuevo_costo + self.heuristic(vecino, objetivo)  # Calcula la prioridad
                    heapq.heappush(frontera, (prioridad, vecino)) # Agrega el vecino a la frontera
                    padres[vecino] = actual # Actualiza el padre del vecino

        return None  # Si no se encuentra un camino, devuelve None


grafo = Grafo() # Se crea un objeto grafo
grafo.agregar_arista((0, 0), (1, 0), 1) # Se agrega arista al grafo
grafo.agregar_arista((0, 0), (0, 1), 1) # Se agrega arista al grafo
grafo.agregar_arista((1, 0), (1, 1), 1) # Se agrega arista al grafo
grafo.agregar_arista((1, 1), (2, 1), 1) # Se agrega arista al grafo
grafo.agregar_arista((0, 1), (0, 2), 1) # Se agrega arista al grafo
grafo.agregar_arista((2, 1), (2, 2), 1) # Se agrega arista al grafo
grafo.agregar_arista((0, 2), (1, 2), 1) # Se agrega arista al grafo
grafo.agregar_arista((1, 2), (2, 2), 1) # Se agrega arista al grafo

inicio = (0, 0) # Se pone el punto de inicio
objetivo = (2, 2) # se pone el objetivo de la busqueda
camino = grafo.a_estrella(inicio, objetivo) # # Encuentra el camino más corto usando A*
print("Camino más corto:", camino) # Se imprime el camino encontrado
