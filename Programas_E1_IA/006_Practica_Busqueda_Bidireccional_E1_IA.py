# Practica_006_Busqueda_Bidireccional_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Bidireccional

from collections import deque # Se implementa una cola

class Grafo: # Se crea la clase Grafo
    def __init__(self): # Se crea un nuevo objeto en esta clase, este método se ejecuta automáticamente, permitiendo la inicialización de la instancia de la clase según sea necesario
        self.vertices = {} # Inicializa el atributo vertices de la instancia de la clase como un diccionario vacío

    def agregar_vertice(self, vertice): # Este método agregara un vértice a una estructura de datos de grafo
        if vertice not in self.vertices: #  Verifica si el vértice que se va a agregar aún no está presente en la estructura de datos del grafo
            self.vertices[vertice] = [] # Asigna una lista vacía como el valor asociado al vértice en el diccionario 

    def agregar_arista(self, vertice1, vertice2): # Este método agregara un arista entre dos vértices en un grafo
        self.vertices[vertice1].append(vertice2) # Agregara un arista entre vertice1 y vertice2 en el grafo
        self.vertices[vertice2].append(vertice1) # Agregara un arista entre vertice2 y vertice1 en el grafo

def buscar_bidireccional(grafo, inicio, objetivo): # Se define una funcion llamada busqueda bidireccional
    frontera_inicio = deque([inicio]) # Frontera desde el inicio
    frontera_objetivo = deque([objetivo]) # Frontera desde el objetivo
    visitados_inicio = {inicio} # Conjunto para almacenar los nodos visitados desde el inicio
    visitados_objetivo = {objetivo} # Conjunto para almacenar los nodos visitados desde el objetivo

    while frontera_inicio and frontera_objetivo: # inicia un bucle while que continuará ejecutándose mientras ambas fronteras, frontera_inicio y frontera_objetivo, contengan al menos un elemento
        actual_inicio = frontera_inicio.popleft() # Expandir desde el inicio
        for vecino in grafo.vertices[actual_inicio]: # Esta línea itera sobre todos los vecinos del nodo
            if vecino not in visitados_inicio: # Verifica si el vecino actual del nodo actual_inicio no ha sido visitado anteriormente desde el nodo de inicio en el grafo
                frontera_inicio.append(vecino) # Agrega el nodo vecino al final de la cola
                visitados_inicio.add(vecino) # Agrega el nodo vecino al conjunto 
            if vecino in visitados_objetivo: # Verifica si el nodo vecino actual ha sido visitado anteriormente desde el nodo objetivo en el grafo
                return True #  Indica que se ha encontrado una ruta entre el nodo de inicio y el nodo objetivo en el grafo

        actual_objetivo = frontera_objetivo.popleft() # Expandir desde el objetivo
        for vecino in grafo.vertices[actual_objetivo]: # Itera sobre los vecinos del nodo actual_objetivo en el grafo
            if vecino not in visitados_objetivo: #  Verifica si el vecino actual del nodo actual_objetivo no ha sido visitado anteriormente desde el nodo objetivo en el grafo
                frontera_objetivo.append(vecino) # Agrega el nodo vecino al final de la cola 
                visitados_objetivo.add(vecino) #  Agrega el nodo vecino al conjunto visitados_objetivo
            if vecino in visitados_inicio: # verifica si el nodo vecino actual ha sido visitado anteriormente desde el nodo de inicio en el grafo
                return True # Indica que se ha encontrado una ruta entre el nodo de inicio y el nodo objetivo en el grafo

    return False # Indica que no se ha encontrado una ruta entre el nodo de inicio y el nodo objetivo en el grafo

grafo = Grafo() # Se crea un nuevo objeto
grafo.agregar_vertice('I') # Agrega un vértice al grafo
grafo.agregar_vertice('J') # Agrega un vértice al grafo
grafo.agregar_vertice('K') # Agrega un vértice al grafo
grafo.agregar_vertice('L') # Agrega un vértice al grafo
grafo.agregar_arista('I', 'J') # Se agrega un arista entre los dos vertices en el grafo
grafo.agregar_arista('J', 'K') # Se agrega un arista entre los dos vertices en el grafo
grafo.agregar_arista('K', 'L') # Se agrega un arista entre los dos vertices en el grafo

inicio = 'I' # Se pone desde donde iniciara la busqueda
objetivo = 'L' # Se pone donde finalizara
print(buscar_bidireccional(grafo, inicio, objetivo)) # Se imprime el resultado de la busqueda
