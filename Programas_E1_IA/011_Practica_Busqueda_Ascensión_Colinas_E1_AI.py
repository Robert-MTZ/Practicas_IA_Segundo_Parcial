# Practica_011_Búsqueda_Ascensión_Colinas_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Ascensión_Colinas

import random # Importa el módulo random de la biblioteca estándar de Python, que se utiliza para generar números aleatorios

def hill_climbing(problem, max_iterations=1000): # Esta línea define una función llamada hill_climbing que toma dos argumentos: problem, que representa un problema que deseamos resolver utilizando el algoritmo de escalada de colinas, y max_iterations, que define el número máximo de iteraciones permitidas en el algoritmo (por defecto 1000)
    current_state = problem.initial_state() # Esta línea inicializa el estado actual con el estado inicial del problema, utilizando el método initial_state() del objeto problem
    for _ in range(max_iterations): # Este bucle for ejecuta el algoritmo de escalada de colinas durante un número máximo de iteraciones determinado por max_iterations
        neighbors = problem.neighbors(current_state) # Esta línea genera todos los vecinos del estado actual utilizando el método neighbors() del objeto problem
        if not neighbors: # Esta condición verifica si no hay vecinos disponibles
            break
        next_state = max(neighbors, key=problem.value) # Esta línea selecciona el vecino con el mayor valor utilizando la función max() y especificando la función de evaluación value() del objeto problem
        if problem.value(next_state) <= problem.value(current_state): # Esta condición verifica si el valor del vecino seleccionado es menor o igual al valor del estado actual. Si es así, significa que el vecino no mejora la solución, por lo que el algoritmo termina la búsqueda y sale del bucle for
            break
        current_state = next_state # Esta línea actualiza el estado actual con el vecino seleccionado como el nuevo estado actual
    return current_state # Finalmente, esta línea devuelve el estado actual, que representa la solución encontrada por el algoritmo de escalada de colinas

class Problem: # Sirve como interfaz para representar un problema en el algoritmo de escalada de colinas
    def initial_state(self):
        raise NotImplementedError()

    def value(self, state):
        raise NotImplementedError()

    def neighbors(self, state):
        raise NotImplementedError()

class ExampleProblem(Problem): # Define una subclase ExampleProblem de la clase Problem. Esta subclase implementa los métodos initial_state(), value(), y neighbors() para representar un problema específico que minimiza la suma de los elementos en un estado
    def __init__(self, initial_state):
        self.initial = initial_state

    def initial_state(self):
        return self.initial

    def value(self, state):
        return -sum(state)  # Minimize the sum of elements

    def neighbors(self, state):
        neighbors = []
        for i in range(len(state)):
            for delta in (-1, 1):
                neighbor = list(state)
                neighbor[i] += delta
                neighbors.append(tuple(neighbor))
        return neighbors

def main():
    initial_state = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
    problem = ExampleProblem(initial_state)
    solution = hill_climbing(problem)
    print("Initial State:", initial_state)
    print("Solution Found:", solution)
    print("Value of Solution:", problem.value(solution))

if __name__ == "__main__":
    main()
