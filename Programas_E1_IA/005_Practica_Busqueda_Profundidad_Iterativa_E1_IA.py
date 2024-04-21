# Practica_005_Busqueda_Profundidad_Iterativa_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Profundidad_Iterativa 

class Nodo: # Se crea una clase llamada Nodo
    def __init__(self, valor): # Cuando se crea un nuevo objeto de la clase Nodo, se espera que se pase un valor como argumento, y este valor se utilizará para inicializar el objeto de acuerdo con la lógica definida dentro del método __init__
        self.valor = valor #  Esta línea de código establece el valor inicial del atributo valor para el objeto que está siendo creado
        self.izquierda = None # Se está inicializando el atributo izquierda del objeto actual
        self.derecha = None # Se está inicializando el atributo derecha del objeto actual

def BPI_arbol(raiz, objetivo): # Utilizamos el algoritmo  de Busqueda en profundidad iterativa recibiendo dos parametros que son raiz y objetivo
    for limite in range(1, 100):  # Límite arbitrario para evitar bucles infinitos
        if DFS_arbol(raiz, objetivo, limite): # Esta linea verifica si se cumple una condicion antes de ejecutar un bloque de codigo 
            return True # indica que la condicion es verdadera
    return False # indica que la condicion es falsa

def DFS_arbol(nodo, objetivo, limite): # La función realiza una búsqueda en profundidad recursiva a partir del nodo actual
    if nodo is None: # verifica si el nodo actual es None
        return False # Retorna una vez llegado al nodo final
    if nodo.valor == objetivo: # verifica si el valor del nodo actual es igual al valor del objetivo
        return True # Retorna una vez llegado al nodo final
    if limite <= 0: # Verifica si el límite de profundidad ha alcanzado cero o ha caído por debajo de cero
        return False # Retorna una vez llegado al nodo final
    return (DFS_arbol(nodo.izquierda, objetivo, limite - 1) or
            DFS_arbol(nodo.derecha, objetivo, limite - 1)) # Busca recursivamente el objetivo tanto en el subárbol izquierdo como en el derecho del nodo actual, dentro del límite de profundidad especificado. Si el objetivo se encuentra en alguna de estas ramas, la función retorna True, de lo contrario, retorna False

raiz = Nodo(10) # Se crea un nodo raiz y se le asigna un valor
raiz.izquierda = Nodo(5) # Se crea un nodo hijo izquierdo y se le asigna un valor
raiz.derecha = Nodo(15) # Se crea un nodo hijo derecho y se le asigna un valor
raiz.izquierda.izquierda = Nodo(3) # se empieza a construir el arbol binario,  Se crea otro nodo hijo izquierdo con un valor de 3 y se asigna al nodo hijo izquierdo del nodo raíz 
raiz.izquierda.derecha = Nodo(7) # Se crea un nodo hijo derecho con un valor de 7 y se le asigna al nodo hijo izquierdo del nodo raíz
raiz.derecha.izquierda = Nodo(11) # Se crea un nodo hijo izquierdo con un valor de 11 y se le asigna al nodo hijo derecho del nodo raíz
raiz.derecha.derecha = Nodo(20) # Se crea un nodo hijo derecho con un valor de 20 y se le asigna al nodo hijo derecho del nodo raíz

objetivo = 11 # Se establece el objetivo de la busqueda en profundidad iterativa
print("El elemento que estas buscando: ", objetivo, "esta en el árbol?") # Imprimimos el resultado
print(BPI_arbol(raiz, objetivo)) # Se manda llamar la funcion y sus parametros para poder imprimir el objetivo


        
