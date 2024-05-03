# Practica_150_Gramaticas_Jerarquía_de_Chomsky_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Gramaticas_Jerarquía_de_Chomsky


# Función para verificar si una gramática es de tipo 3 (regular)
def es_regular(gramatica):
    for produccion in gramatica:
        # Verificar si cada producción tiene la forma A -> aB o A -> a
        if len(produccion) > 3 or (len(produccion) == 3 and produccion[1] != '->'):
            return False
        if len(produccion) == 3 and (not produccion[0].isupper() or not produccion[2].isupper()):
            return False
    return True

# Función para verificar si una gramática es de tipo 2 (libre de contexto)
def es_libre_de_contexto(gramatica):
    for produccion in gramatica:
        # Verificar si cada producción tiene la forma A -> α donde α es una cadena de símbolos terminales o no terminales
        if len(produccion) != 3 or produccion[1] != '->':
            return False
    return True

# Función para verificar si una gramática es de tipo 1 (sensible al contexto)
def es_sensible_al_contexto(gramatica):
    # Por simplicidad, asumiremos que todas las gramáticas son sensibles al contexto
    return True

# Función para verificar si una gramática es de tipo 0 (recursivamente enumerable)
def es_recursivamente_enumerable(gramatica):
    # Por simplicidad, asumiremos que todas las gramáticas son recursivamente enumerables
    return True

# Gramática
gramatica = [
    "S -> aS",
    "S -> b"
]

# Verificar el tipo de la gramática
if es_regular(gramatica):
    print("La gramática es de tipo 3 (regular)")
elif es_libre_de_contexto(gramatica):
    print("La gramática es de tipo 2 (libre de contexto)")
elif es_sensible_al_contexto(gramatica):
    print("La gramática es de tipo 1 (sensible al contexto)")
elif es_recursivamente_enumerable(gramatica):
    print("La gramática es de tipo 0 (recursivamente enumerable)")
else:
    print("La gramática no pertenece a ninguna categoría conocida de la jerarquía de Chomsky")
