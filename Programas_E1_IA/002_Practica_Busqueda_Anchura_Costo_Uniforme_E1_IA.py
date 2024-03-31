# Practica_002_Busqueda_Anchura_Costo_Uniforme_E1_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica 

# Programa_Busqueda_Anchura_Costo_Uniforme_IA

import heapq # se utiliza este componente gracias a sus caracteristicas de busqueda, las cuales permiten  ser priorizados y procesados en orden de su prioridad

def bacu(graf, inic, fin): # definimos la funcion def bacu ya que es una abreviatura al titulo de Busqueda Anchura Costo Uniforme, donde ademas se declaran las variables con las cuales estaremos trabajando en el programa 

    priority_queue = [(0,inic)] # Establecemos nuestra prioridad
    visit = set() # seguira los elementos buscando el camino mas rapido

    while priority_queue: # creamos un bucle 
        cost, nodo = heapq.heappop(priority_queue) # Con esta linea estamos especificando que se extraera un elemento con la menor prioridad de la cola

        if nodo == fin: # Esta linea comprueba si el nodo a sido extraido
            return cost # Si el nodo extraído es igual al nodo de destino, entonces se devuelve el costo asociado con ese nodo 

        visit.add(nodo) # Agrega al nodo actual (nodo) el conjunto de nodos visitados (visit)

        for neighbor, neighbor_cost in graf[nodo].items(): # Esto itera sobre todos los elementos del diccionario asociado al nodo actual 
            total_cost= cost + neighbor_cost #  Aquí se calcula el costo total para alcanzar el vecino actual desde el nodo actual

            if neighbor not in visit: # Este bloque verifica si el vecino actual no ha sido visitado previamente. Si esto es cierto, significa que el algoritmo no ha explorado este vecino antes y es necesario agregarlo a la cola de prioridad para futuras exploraciones
                heapq.heappush(priority_queue, (total_cost, neighbor)) # Si el vecino no ha sido visitado, se agrega a la cola de prioridad con su costo total (total_cost) y se asocia con el vecino correspondiente. Esto permite que el algoritmo continúe explorando desde este vecino en futuras iteraciones
            elif total_cost < cost: # Este bloque se ejecuta si el vecino ya ha sido visitado, pero se ha encontrado un camino más corto para alcanzarlo. En este caso, se actualiza el costo total en la cola de prioridad con el nuevo costo más bajo (total_cost) y se vuelve a agregar a la cola de prioridad. Esto asegura que el algoritmo tenga en cuenta el camino más corto hacia este vecino en futuras exploraciones
                heapq.heappush(priority_queue, (total_cost, neighbor)) # Si el vecino no ha sido visitado, se agrega a la cola de prioridad con su costo total (total_cost) y se asocia con el vecino correspondiente. Esto permite que el algoritmo continúe explorando desde este vecino en futuras iteraciones

    return None # Cuando se ejecuta return None, la función termina su ejecución y devuelve explícitamente None como resultado

if __name__ == "__main__": #  se utiliza para determinar si el script de Python está siendo ejecutado como un programa principal o si está siendo importado como un módulo en otro script
    graf = { # Le asignamos valores a nuestro grafo y lo estructuramos 
        'I': {'J': 3, 'K': 2},
        'J': {'I': 3, 'L': 5, 'M': 2},
        'K': {'I': 2, 'N': 8},
        'L': {'J': 5},
        'M': {'J': 2, 'O': 1},
        'N': {'K': 8},
        'O': {'M': 1}
    }

    inic_nodo = 'I' # Establecemos nuestro nodo inicial
    fin_nodo = 'O' # Establecemos nuestro nodo final 

    shortest_cost = bacu(graf, inic_nodo, fin_nodo) # Se buscara el camino mas corto entre los nodos 

    # Imprimimos nuestros resultados
    if shortest_cost is not None: #  se utiliza para verificar si la variable shortest_cost no es None. En Python, None se utiliza comúnmente para representar la ausencia de un valor o un valor nulo
        print(f"El costo de la distancia mas corta entre el nodo {inic_nodo} hasta el nodo {fin_nodo} es: {shortest_cost}" ) # Se imprime este mensaje si se cumple la condicion
    else: # Si no se cumple entonces 
        print(f"No se encontro un camino desde el nodo {inic_nodo} hasta el nodo {fin_nodo} ") # se imprimira este mensaje si no se cumple la condicion





