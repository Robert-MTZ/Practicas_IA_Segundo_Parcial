# Practica_012_Búsqueda_Tabu_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Busqueda_Tabu

import random
import copy

class TSPProblem:
    def __init__(self, distances): # Este es el constructor de la clase. Recibe una matriz de distancias que representa las distancias entre todas las ciudades en el problema TSP y la almacena en el atributo self.distances
        self.distances = distances

    def initial_solution(self): # Este método genera una solución inicial aleatoria para el problema TSP. Crea una lista de ciudades en orden secuencial y luego la mezcla aleatoriamente utilizando random.shuffle()
        cities = list(range(len(self.distances)))
        random.shuffle(cities)
        return cities

    def evaluate(self, solution): # Este método calcula la evaluación de una solución dada, es decir, la distancia total recorrida para completar la ruta. Itera sobre las ciudades en la solución y suma las distancias entre cada par de ciudades consecutivas. Utiliza la matriz de distancias almacenada en self.distances para obtener las distancias entre las ciudades
        total_distance = 0
        for i in range(len(solution)):
            total_distance += self.distances[solution[i-1]][solution[i]]
        return total_distance

    def neighbors(self, solution): # Este método genera todos los vecinos de una solución dada intercambiando dos ciudades en la ruta. Itera sobre todas las combinaciones únicas de dos ciudades en la solución y genera un nuevo vecino intercambiando esas dos ciudades. Utiliza copy.deepcopy() para crear una copia profunda de la solución original y evitar modificarla directamente
        neighbors = []
        for i in range(len(solution)):
            for j in range(i + 1, len(solution)):
                neighbor = copy.deepcopy(solution)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighbors.append(neighbor)
        return neighbors

def tabu_search(problem, max_iterations=1000, tabu_size=10):
    current_solution = problem.initial_solution()
    best_solution = current_solution
    tabu_list = []

    for _ in range(max_iterations): # Esta función toma un objeto problem que representa un problema TSP, así como parámetros opcionales como el número máximo de iteraciones y el tamaño de la lista tabu
        neighbors = problem.neighbors(current_solution)
        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                neighbor_value = problem.evaluate(neighbor)
                if neighbor_value < best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        if not best_neighbor:
            break

        current_solution = best_neighbor
        if problem.evaluate(best_neighbor) < problem.evaluate(best_solution):
            best_solution = best_neighbor

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution

def main():
    # Distancias entre ciudades 
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    problem = TSPProblem(distances)
    best_solution = tabu_search(problem)

    print("Mejor solución encontrada:", best_solution)
    print("Distancia de la mejor solución:", problem.evaluate(best_solution))

if __name__ == "__main__":
    main()
