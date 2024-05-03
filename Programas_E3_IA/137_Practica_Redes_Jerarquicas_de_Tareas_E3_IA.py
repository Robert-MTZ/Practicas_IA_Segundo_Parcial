# Practica_137_Redes_Jersrquicas_de_Tareas_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Redes_Jersrquicas_de_Tareas

# Definimos la red de tareas como un diccionario
red_tareas = {
    'Tarea A': ['Tarea B', 'Tarea C'],  # Tarea A tiene como dependencias las tareas B y C
    'Tarea B': ['Tarea D'],              # Tarea B tiene como dependencia la tarea D
    'Tarea C': ['Tarea D'],              # Tarea C tiene como dependencia la tarea D
    'Tarea D': ['Tarea E'],              # Tarea D tiene como dependencia la tarea E
    'Tarea E': []                        # Tarea E no tiene dependencias
}

# Función para imprimir la red de tareas de manera jerárquica
def imprimir_red_tareas(red, tarea, nivel=0):
    print('\t' * nivel + tarea)  # Imprimir la tarea con la indentación correspondiente
    # Recorrer las tareas dependientes de la tarea actual
    for dependencia in red[tarea]:
        imprimir_red_tareas(red, dependencia, nivel + 1)  # Llamar recursivamente a la función con la tarea dependiente

# Imprimir la red de tareas
print("Red de tareas:")
imprimir_red_tareas(red_tareas, 'Tarea A')

