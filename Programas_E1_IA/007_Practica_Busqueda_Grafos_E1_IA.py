# Practica_007_Busqueda_Grafos_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Grafos

class Grafo: # Creamos una clase llamada Grafo
    def __init__(self): # Se inicializan los atributos o variables de instancia de la clase
        self.vertices = {} # Se inicializa un diccionario vacío que se utilizará para almacenar los vértices y sus adyacencias en el grafo

    def agregar_vertice(self, vertice): # Este metodo se utiliza para agregar un nuevo vértice al grafo
        if vertice not in self.vertices: # Verifica si el vértice que se intenta agregar al grafo no existe en el diccionario de vértices actual
            self.vertices[vertice] = [] # Se inicializa una lista vacía en el diccionario de vértices del grafo

    def agregar_arista(self, vertice1, vertice2): # Este metodo se utiliza para agregar una arista (una conexión) entre dos vértices en el grafo
        self.vertices[vertice1].append(vertice2) # Esto representa la existencia de una arista que va desde vertice1 hasta vertice2
        self.vertices[vertice2].append(vertice1) # Esto representa la existencia de una arista que va desde vertice2 hasta vertice1

    def dfs(self, inicio): # Se implementa la busqueda en profundidad 
        visitados = set() # Se crea un conjunto vacio
        self._dfs_recursivo(inicio, visitados) # Se manda llamar un metodo

    def _dfs_recursivo(self, vertice, visitados): # Se crea una funcion que nos ayudara a hacer la busqueda en el grafo
        visitados.add(vertice) # Esta linea esta agregando el vertice actual al conjunto de nodos visitados
        print(vertice) # Se imprimira el vertice

        for vecino in self.vertices[vertice]: #  Esta línea esta recorriendo todos los vértices adyacentes al vértice actual y ejecutando el siguiente bloque de código 
            if vecino not in visitados: #  Verifica si el vértice adyacente vecino al vértice actual vertice no ha sido visitado previamente
                self._dfs_recursivo(vecino, visitados) # La llamada recursiva se realiza con dos argumentos: el vértice adyacente vecino, que se va a explorar, y el conjunto visitados

grafo = Grafo() # Se crea un objeto
grafo.agregar_vertice('I') # Se agrega un vertice al grafo
grafo.agregar_vertice('J') # Se agrega un vertice al grafo
grafo.agregar_vertice('K') # Se agrega un vertice al grafo
grafo.agregar_vertice('L') # Se agrega un vertice al grafo

grafo.agregar_arista('I', 'J') # Se agrega un arista entre dos vertices
grafo.agregar_arista('I', 'K') # Se agrega un arista entre dos vertices
grafo.agregar_arista('J', 'L') # Se agrega un arista entre dos vertices
grafo.agregar_arista('K', 'L') # Se agrega un arista entre dos vertices

print("Recorrido DFS:") # Se imprime el resultado de la busqueda en el grafo
grafo.dfs('I') # Se pone desde donde se iniciara la busqueda
