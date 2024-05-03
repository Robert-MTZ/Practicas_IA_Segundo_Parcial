# Practica_111_Programacion_Logica_Prolog_y_CLIPS_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Logica_Prolog_y_CLIPS

from pyke import knowledge_engine # Importar las bibliotecas necesarias

engine = knowledge_engine.engine(__file__) # Crear un motor de conocimiento

# Cargar el archivo de reglas de Prolog
engine.reset()
engine.activate('coin_flip')

# Definir la cantidad de lanzamientos
num_lanzamientos = 1000
cara_count = 0
cruz_count = 0

# Realizar los lanzamientos y contar los resultados
for _ in range(num_lanzamientos):
    result = engine.prove_1_goal('coin_flip($result)')['result']
    if result == 'cara':
        cara_count += 1
    else:
        cruz_count += 1

# Calcular la probabilidad de cara y cruz
probabilidad_cara = cara_count / num_lanzamientos
probabilidad_cruz = cruz_count / num_lanzamientos

# Imprimir los resultados
print(f"Probabilidad de cara: {probabilidad_cara}")
print(f"Probabilidad de cruz: {probabilidad_cruz}")


