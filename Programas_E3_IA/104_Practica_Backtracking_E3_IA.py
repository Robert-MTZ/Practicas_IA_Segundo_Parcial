# Practica_104_Backtracking_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Backtracking

def is_valid_solution(candidate): # Verifica si una solución candidata es valida

    return sum(candidate) == 10

def backtrack(candidate, depth, max_depth): # Función recursiva para realizar el backtracking.

    if depth == max_depth:  # Verifica si se alcanzó la profundidad máxima
        if is_valid_solution(candidate):  # Verifica si la solución candidata es válida
            print("Solución encontrada:", candidate)  # Imprime la solución encontrada
    else:
        for choice in range(1, 5):  # Genera todas las opciones posibles (en este caso, del 1 al 4)
            # Realiza una elección y agrega el elemento a la solución candidata
            candidate.append(choice)
            # Realiza una llamada recursiva con la solución candidata actualizada y aumenta la profundidad
            backtrack(candidate, depth + 1, max_depth)
            # Deshace la última elección para explorar otras posibilidades
            candidate.pop()

if __name__ == "__main__":
    # Llamamos a la función de backtracking con una solución candidata vacía, profundidad inicial 0 y profundidad máxima 4
    backtrack([], 0, 4)

