# Practica_010_Búsquedas_A*_AO*_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Búsquedas_A*_AO*

import heapq # Se manda llamr la biblioteca heapq para usar la cola de prioridad

class Node:  # Creamos la clase Grafo
    def __init__(self, position): # Se inicializa el atributo
        self.position = position
        self.g = 0
        self.h = 0
        self.parent = None

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

class Grid: # representa un objeto que modela una cuadrícula o rejilla bidimensional
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]

    def set_obstacle(self, x, y): # Este método permite establecer un obstáculo en una posición específica de la cuadrícula. Recibe las coordenadas x y y del obstáculo y establece el valor de la celda correspondiente en 1
        self.grid[y][x] = 1

    def is_obstacle(self, x, y): # Este método comprueba si una determinada celda de la cuadrícula contiene un obstáculo. Recibe las coordenadas x y y de la celda y devuelve True si contiene un obstáculo (valor 1), de lo contrario devuelve False
        return self.grid[y][x] == 1

    def heuristic(self, a, b): #  Este método calcula una heurística simple para estimar el costo del camino más corto entre dos nodos a y b. Utiliza la distancia de Manhattan entre las posiciones de los nodos
        return abs(a.position[0] - b.position[0]) + abs(a.position[1] - b.position[1])

    def neighbors(self, node): # Este método calcula los nodos vecinos de un nodo dado en la cuadrícula. Recibe un objeto Node que representa el nodo actual y devuelve una lista de nodos vecinos alcanzables desde el nodo actual. Los nodos vecinos son los nodos adyacentes (arriba, abajo, izquierda, derecha) en la cuadrícula, siempre y cuando estén dentro de los límites de la cuadrícula
        x, y = node.position
        neighbors = []
        if x > 0:
            neighbors.append(Node((x - 1, y)))
        if x < self.width - 1:
            neighbors.append(Node((x + 1, y)))
        if y > 0:
            neighbors.append(Node((x, y - 1)))
        if y < self.height - 1:
            neighbors.append(Node((x, y + 1)))
        return neighbors

def reconstruct_path(node): # define una función llamada reconstruct_path que toma un nodo final en un grafo y reconstruye el camino desde el nodo inicial hasta ese nodo final
    path = [] # Se inicializa una lista vacía llamada path que almacenará las posiciones de los nodos en el camino
    current = node #  Se inicializa una variable current con el nodo final pasado como argumento a la función
    while current is not None: # Se inicia un bucle while que continuará hasta que current sea None, lo que significa que hemos alcanzado el nodo inicial
        path.append(current.position) # En cada iteración del bucle, la posición del nodo actual se agrega a la lista path
        current = current.parent # Se actualiza el nodo actual (current) para que sea el nodo padre del nodo actual. Esto se hace para retroceder en el camino desde el nodo final hasta el nodo inicial
    return path[::-1] # Una vez que hemos reconstruido todo el camino, se devuelve la lista path, pero se invierte usando la técnica de "slicing" [::-1] para obtener el orden correcto del camino desde el nodo inicial hasta el nodo final

def astar_search(grid, start, end): # Define una función llamada astar_search que toma tres argumentos: grid, que representa el grafo en el que se realiza la búsqueda, start, que es el nodo de inicio, y end, que es el nodo de destino
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == end.position:
            return reconstruct_path(current)

        closed_set.add(current)

        for neighbor in grid.neighbors(current):
            if grid.is_obstacle(*neighbor.position) or neighbor in closed_set:
                continue

            tentative_g = current.g + 1
            if neighbor not in open_list or tentative_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = grid.heuristic(neighbor, end)
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)

    return None

def ao_search(grid, start, end):
    open_list = [] # Se inicializa una lista abierta que almacenará los nodos que se están explorando pero aún no se han evaluado completamente
    closed_set = set() # Se inicializa un conjunto cerrado que almacenará los nodos que ya han sido completamente evaluados
    heapq.heappush(open_list, start) # Se agrega el nodo inicial a la lista abierta usando una cola de prioridad (heap) proporcionada por el módulo heapq. Esto asegura que el nodo con el menor valor de la función de evaluación f se extraiga primero de la lista abierta

    while open_list: #  Se inicia un bucle while que continuará mientras la lista abierta no esté vacía
        current = heapq.heappop(open_list) # Se extrae y asigna el nodo actual de la lista abierta. Este será el nodo que se está evaluando actualmente

        if current.position == end.position: # Se comprueba si el nodo actual es el nodo final. Si lo es, se devuelve el camino reconstruido desde el nodo inicial hasta el nodo final utilizando la función reconstruct_path
            return reconstruct_path(current) # Se agrega el nodo actual al conjunto cerrado, lo que indica que ha sido completamente evaluado

        closed_set.add(current)

        for neighbor in grid.neighbors(current): # Se itera sobre los vecinos del nodo actual en el grafo
            if grid.is_obstacle(*neighbor.position) or neighbor in closed_set: # Se comprueba si el vecino es un obstáculo o si ya está en el conjunto cerrado. Si cualquiera de estas condiciones se cumple, se pasa al siguiente vecino
                continue

            tentative_g = current.g + 1 # Se calcula el costo acumulado (g) del vecino si se llega a él desde el nodo actual
            if neighbor not in open_list or tentative_g < neighbor.g: # Se comprueba si el vecino no está en la lista abierta o si el nuevo costo acumulado es menor que el costo acumulado anteriormente registrado para el vecino
                neighbor.parent = current # Se actualiza el padre del vecino para que sea el nodo actual
                neighbor.g = tentative_g # Se actualiza el costo acumulado (g) del vecino con el nuevo valor calculado
                neighbor.h = grid.heuristic(neighbor, end) + neighbor.g # Se calcula la función heurística del vecino (h) sumando su costo acumulado al costo heurístico estimado para llegar desde él hasta el nodo final
                if neighbor not in open_list: #  Si el vecino no está en la lista abierta, se agrega a la lista abierta
                    heapq.heappush(open_list, neighbor) 

    return None # Si no se encuentra un camino desde el nodo inicial hasta el nodo final (por ejemplo, si la lista abierta se vacía y no se alcanza el nodo final), se devuelve None

def print_path(path, grid):
    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) in path:
                print("x", end=" ")
            elif grid.is_obstacle(x, y):
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

def main():
    # Crear el tablero
    grid = Grid(10, 10)
    grid.set_obstacle(2, 1)
    grid.set_obstacle(2, 2)
    grid.set_obstacle(2, 3)
    grid.set_obstacle(2, 4)
    grid.set_obstacle(4, 3)
    grid.set_obstacle(5, 3)
    grid.set_obstacle(6, 3)
    grid.set_obstacle(7, 3)

    # Definir el punto de inicio y el punto de destino
    start = Node((1, 1))
    end = Node((8, 8))

    # Ejecutar búsqueda A*
    path_astar = astar_search(grid, start, end)
    if path_astar:
        print("Path found using A*:")
        print_path(path_astar, grid)
    else:
        print("No path found using A*")

    # Ejecutar búsqueda AO*
    path_ao = ao_search(grid, start, end)
    if path_ao:
        print("\nPath found using AO*:")
        print_path(path_ao, grid)
    else:
        print("\nNo path found using AO*")

if __name__ == "__main__":
    main()
