# Practica_004_Busqueda_Profundidad_limitada_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Profundidad_Limitada

class Grafo: # Creamos la clase Grafo 
    def __init__(self): # Inicializamos el objeto creado
        self.grafo = {} # esta linea se usara para almacenar la informacion en el diccionario

    def add_vert(self, vert): # Definimos un metodo para agregar vertices
        if vert not in self.grafo: # esta linea verifica si el vertice no esta presente en el diccionario
            self.grafo[vert] = [] # Se inicializa una entrada en el diccionario y se le asigna una lista vacia 

    def add_edge(self, vert01, vert02): # Se crea un metodo para hacer una conexion entre los vertices
        if vert01 in self.grafo and vert02 in self.grafo: # esta linea verifica si los vertices estan presentes en el grafo
            self.grafo[vert01].append(vert02) # Agrega el vertice a la lista de los vertices adyacentes 
            self.grafo[vert02].append(vert01) # Agrega el vertice a la lista de los vertices adyacentes

    def dls(self, inic, profun_limit): # Se crea el metodo para buscar en profundidad
        visit = set() # Esta linea crea un conjunto vacio
        self._dls_recursivo(inic, visit, profun_limit, 0) # llama a un metodo dentro de la misma clase con parametros ya establecidos

    def _dls_recursivo(self, vert, visit, profun_limit, profun_actual): # se define un metodo que implementa una busqueda en profundidad limitada de manera recursiva en un grafo (explora los vertices adyacentes)
        if profun_actual > profun_limit: # Esta linea verifica la profundidad de la busqueda, basicamente ve si se cumple la profundidad especificada
            return # se devuelve el valor

        visit.add(vert) # visita y agrega al vertice
        print(vert) # imprime el vertice

        for vec in self.grafo[vert]: # Se utiliza para que recorra todos los vertices adyacentes al vertice
            if vec not in visit: # Se establece una condicion en caso de que no sea visitado que lo visite
                self._dls_recursivo(vec, visit, profun_limit, profun_actual + 1) # Hace una llamada recursiva al metodo continuando con la busqueda en profundidad desde el vertice adyacente y se incrementa la profundidad actual 

if __name__ == "__main__": # Se verifica si hay una igualdad
    g = Grafo() # Se crea nuestro grafo
    g.add_vert('I') # Agregamos el vertice llamado I al grafo
    g.add_vert('J') # Agregamos el vertice llamado J al grafo
    g.add_vert('K') # Agregamos el vertice llamado K al grafo
    g.add_vert('L') # Agregamos el vertice llamado L al grafo
    g.add_vert('M') # Agregamos el vertice llamado M al grafo
    g.add_edge('I', 'J') # Definimos el trazo del arista en el grafo
    g.add_edge('I', 'K') # Definimos el trazo del arista en el grafo
    g.add_edge('J', 'L') # Definimos el trazo del arista en el grafo
    g.add_edge('J', 'M') # Definimos el trazo del arista en el grafo

print("Se imprime el recorrido de la busqueda en profundidad limitada: ") # # Imprimimos el recorrido de busqueda en profundidad limitada
g.dls('I', 2) # llamamos al metodo dls en un objeto y establecemos el inicio de la busqueda que sera desde el vertice I hasta una profundidad maxima de 2
