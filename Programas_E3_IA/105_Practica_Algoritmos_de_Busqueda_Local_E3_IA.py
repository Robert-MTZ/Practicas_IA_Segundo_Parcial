# Practica_105_Algoritmos_de_Busqueda_Local_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Algoritmos_de_Busqueda_Local

import random

def objective_function(x): # Función objetivo que queremos maximizar
    
    return -(x ** 2)  # Función objetivo simple: queremos maximizar el valor negativo de x al cuadrado

def hill_climbing(max_iterations, step_size): #  Algoritmo de escalada (hill climbing) para encontrar el máximo de una funcion

    current_solution = random.uniform(-10, 10)  # Genera una solución inicial aleatoria
    current_value = objective_function(current_solution)  # Calcula el valor de la función objetivo para la solución actual

    for _ in range(max_iterations):
        new_solution = current_solution + random.uniform(-step_size, step_size)  # Genera una nueva solución vecina
        new_value = objective_function(new_solution)  # Calcula el valor de la función objetivo para la nueva solución

        if new_value > current_value:  # Si la nueva solución es mejor que la actual
            current_solution = new_solution  # Actualiza la solución actual
            current_value = new_value  # Actualiza el valor de la función objetivo

    return current_solution

if __name__ == "__main__":
    max_iterations = 1000  # Número máximo de iteraciones
    step_size = 0.1  # Tamaño del paso

    # Ejecutamos el algoritmo de escalada
    best_solution = hill_climbing(max_iterations, step_size)

    # Imprimimos el resultado
    print("La mejor solución encontrada es:", best_solution)
    print("El valor máximo de la función objetivo es:", objective_function(best_solution))

