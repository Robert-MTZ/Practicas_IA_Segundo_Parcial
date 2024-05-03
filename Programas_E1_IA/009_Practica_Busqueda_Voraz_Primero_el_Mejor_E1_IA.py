# Practica_009_Busqueda_Voraz_Primero_el_Mejor_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Voraz_Primero_el_Mejor

import heapq # Se manda llamr la biblioteca heapq para usar la cola de prioridad

class Grafo: # Creamos la clase Grafo
    def __init__(self): # Se inicializa el atributo
        self.vertices = {} # Se crea un diccionario 

    def agregar_vertice(self, v): # Este metodo agrega un vertice al grafo
        if v not in self.vertices:
            self.vertices[v] = {}

    def agregar_arista(self, v1, v2, peso): # Este metodo se utiliza para agregar un arista entre dos vertices con un peso dado 
        self.agregar_vertice(v1)
        self.agregar_vertice(v2)
        self.vertices[v1][v2] = peso

    def heuristica(self, v, objetivo): # Se crea una funcion la cual calcula una heurística para el nodo v en relación con el nodo objetivo
        # En este ejemplo, usamos la distancia Euclidiana como heurística
        return ((v[0] - objetivo[0]) ** 2 + (v[1] - objetivo[1]) ** 2) ** 0.5

    def buscar_voraz_primero_mejor(self, inicio, objetivo): # Se esta implementando el metodo buscar_voraz_primero_mejor
        frontera = [] # se crea una lista vacia 
        heapq.heappush(frontera, (0, inicio)) # Se agregan elementos a la estructura de datos
        visitados = set() # Se crea un conjunto vacio el cual almacenara los nodos

        while frontera: # Se crea un bucle que delimitara
            _, actual = heapq.heappop(frontera) # Se usa la funcion heappop del modulo heapq de Python para extraer y obtener el elemento más pequeño de la lista frontera, que probablemente este organizada como un heap (montículo) mínimo

            if actual == objetivo: # Este if compara el nodo actual con el objetivo
                return True  # Se encontró el objetivo

            visitados.add(actual) # Agrega el nodo actual al conjunto de visitados

            for vecino in self.vertices[actual]:
                if vecino not in visitados:
                    heapq.heappush(frontera, (self.heuristica(vecino, objetivo), vecino)) # Se esta utilizando una cola de prioridad (implementada como un heap) para explorar los nodos de manera eficiente, priorizando aquellos que tienen la menor estimación del costo total desde el nodo actual hasta el nodo objetivo

        return False  # No se encontró el objetivo

grafo = Grafo() # Se esta creando una instancia de la clase 
grafo.agregar_arista((0, 0), (1, 0), 1) # Se agrega un arista al grafo
grafo.agregar_arista((0, 0), (0, 1), 1) # Se agrega un arista al grafo
grafo.agregar_arista((1, 0), (1, 1), 1) # Se agrega un arista al grafo
grafo.agregar_arista((1, 1), (2, 1), 1) # Se agrega un arista al grafo
grafo.agregar_arista((0, 1), (0, 2), 1) # Se agrega un arista al grafo
grafo.agregar_arista((2, 1), (2, 2), 1) # Se agrega un arista al grafo
grafo.agregar_arista((0, 2), (1, 2), 1) # Se agrega un arista al grafo
grafo.agregar_arista((1, 2), (2, 2), 1) # Se agrega un arista al grafo

inicio = (0, 0) # Se establece desde donde comenzara 
objetivo = (2, 2) # Se establece el objetivo 

if grafo.buscar_voraz_primero_mejor(inicio, objetivo): # Esta linea esta verificando si el metodo buscar_voraz_primero_mejor devuelve True (indicando que se encontro una solucion) y luego ejecuta el bloque de codigo dentro del if
    print("Se encontró un camino desde", inicio, "hasta", objetivo) # Se imprime si se encuentra el camino
else: # Cuando no se cumple
    print("No se encontró un camino desde", inicio, "hasta", objetivo) # Se imprime cuando no se cumple la condicion(No se encuentra el camino)
