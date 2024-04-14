# Practica_003_Busqueda_Profundidad_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica 

# Programa_Busqueda_Profundidad_IA

class Grafo: # Se crea la clase grafo
    def __init__(self): #se crea una funcion en la cual se creara un objeto para poder trabajar con sus atributos
        self.grafo = {} # estamos defininiendo el atributo llamado grafo

    def add_vert(self, vert): # Creamos una funcion para trabajar con los vertices
        if vert not in self.grafo: # Esra linea de codigo es una condicion que verifica si un vertive dado no esta presente 
            self.grafo[vert] = [] # Esta linea esta asignada a una lista vacia donde se almacenaran nuestros valores 

    def add_edge(self, vert01, vert02): # Creamos esta funcion para trabajar con nuestros aristas
        if vert01 in self.grafo and vert02 in self.grafo: # Esta linea nos ayuda a verificar si el vertice 01 y el vertice 02 estan presentes en el diccionario
            self.grafo[vert01].append(vert02) # Esta linea le permite a nuestro atributo acceder a los datos almacenados en nuestro diccionario
            self.grafo[vert02].append(vert01) # Esta linea le permite a nuestro atributo acceder a los datos almacenados en nuestro diccionario

    def dfs(self, inic): # Creamos una funcion nueva que nos permitira hacer la busqueda en profundidad
        visit = set() # Con esta linea vamos a visitar los vertices 
        self._dfs_recursivo(inic, visit)  # Esta linea manda llamar a un metodo el cual nos permitira hacer la busqueda en profundidad

    def _dfs_recursivo(self, vert, visit): # Este metodo o funcion nos ayudara a visitar los vertices del grafo
        visit.add(vert) # Visitara y recopilara informacion de los vertices
        print(vert) # imprimira lo que tenga almacenado vertice

        for vec in self.grafo[vert]: # Se crea un bucle con un for el cual crea una lista adyacente del vertice
            if vec not in visit: # Esta linea verifica si el vertice adyacnte no esta presente en el conjunto
                self._dfs_recursivo(vec, visit) # Esta linea tiene la funcion de hacer que la busqueda se empiece desde el vertice adyacente y ir registrando los conjuntos visitados

if __name__ == "__main__": # Verifica si hay una igualdad
    g = Grafo() # Creamos nuestro grafo en donde almacenaremos muestros nodos
    g.add_vert('I') # Agregamos el vertice llamado I al grafo 
    g.add_vert('J') # Agregamos el vertice llamado J al grafo
    g.add_vert('K') # Agregamos el vertice llamado K al grafo
    g.add_vert('L') # Agregamos el vertice llamado L al grafo
    g.add_vert('M') # Agregamos el vertice llamado M al grafo
    g.add_edge('I', 'J') # Definimos el trazo del arista en el grafo
    g.add_edge('I', 'K') # Definimos el trazo del arista en el grafo
    g.add_edge('J', 'L') # Definimos el trazo del arista en el grafo
    g.add_edge('K', 'M') # Definimos el trazo del arista en el grafo

    print("Se imprime el recorrido de la busqueda en profundidad: ") # Imprimimos el recorrido de busqueda en profundidad
    g.dfs('I') # Definimos desde que nodo iniciaremos la busqueda 
    

