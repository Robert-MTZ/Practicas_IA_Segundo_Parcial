# Practica_117_Logica_No_Monotonica_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Logica_No_Monotonica

# Definir una lista de bloques y sus relaciones
bloques = {
    'A': None,  # El bloque A está en la base
    'B': 'A',   # El bloque B está sobre el bloque A
    'C': 'B',   # El bloque C está sobre el bloque B
}

# Función para verificar si un bloque está en la cima de otro bloque
def en_la_cima(bloque_superior, bloque_inferior):
    return bloques.get(bloque_inferior) == bloque_superior

# Función para agregar una nueva relación de apilamiento entre bloques
def apilar(bloque_superior, bloque_inferior):
    if en_la_cima(bloque_superior, bloque_inferior):
        print(f"No se puede apilar {bloque_superior} sobre {bloque_inferior}. ¡Violación de la lógica no monotónica!")
    else:
        bloques[bloque_superior] = bloque_inferior
        print(f"{bloque_superior} se ha apilado sobre {bloque_inferior}.")

# Mostrar la configuración inicial de los bloques
print("Configuración inicial de los bloques:")
for bloque, soporte in bloques.items():
    if soporte:
        print(f"{bloque} está sobre {soporte}.")
    else:
        print(f"{bloque} está en la base.")

# Agregar una nueva relación de apilamiento
apilar('C', 'A')

# Mostrar la configuración actualizada de los bloques
print("\nConfiguración actualizada de los bloques:")
for bloque, soporte in bloques.items():
    if soporte:
        print(f"{bloque} está sobre {soporte}.")
    else:
        print(f"{bloque} está en la base.")

