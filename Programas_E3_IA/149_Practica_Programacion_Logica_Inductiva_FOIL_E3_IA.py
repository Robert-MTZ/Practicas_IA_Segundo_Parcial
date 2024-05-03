# Practica_149_Programacion_Logica_Inductiva_FOIL_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Logica_Inductiva_FOIL

from collections import defaultdict

# Función para calcular el número de veces que un literal aparece en los ejemplos positivos y negativos
def count_literals(examples_pos, examples_neg, literal):
    count_pos = sum(1 for example in examples_pos if literal in example)
    count_neg = sum(1 for example in examples_neg if literal in example)
    return count_pos, count_neg

# Función para calcular la ganancia de información de un literal
def information_gain(examples_pos, examples_neg, literal):
    count_pos, count_neg = count_literals(examples_pos, examples_neg, literal)
    total_pos = len(examples_pos)
    total_neg = len(examples_neg)
    
    # Calcular la ganancia de información utilizando la fórmula de FOIL
    gain = (count_pos / total_pos) * (count_neg / total_neg)
    return gain

# Función para encontrar el mejor literal en un conjunto de literales
def find_best_literal(examples_pos, examples_neg, literals):
    best_literal = None
    best_gain = 0
    
    # Iterar sobre cada literal y calcular su ganancia de información
    for literal in literals:
        gain = information_gain(examples_pos, examples_neg, literal)
        if gain > best_gain:
            best_gain = gain
            best_literal = literal
            
    return best_literal

# Función principal del algoritmo FOIL
def foil(examples_pos, examples_neg, literals):
    rule = []  # Inicializamos la regla vacía
    
    # Mientras haya ejemplos positivos y no haya ejemplos negativos
    while examples_pos and not examples_neg:
        # Encontramos el mejor literal
        best_literal = find_best_literal(examples_pos, examples_neg, literals)
        if best_literal is None:
            break  # Si no hay mejor literal, terminamos
            
        rule.append(best_literal)  # Añadimos el mejor literal a la regla
        
        # Filtramos los ejemplos que satisfacen la regla
        examples_pos = [example for example in examples_pos if best_literal in example]
        examples_neg = [example for example in examples_neg if best_literal not in example]
        
        # Removemos el literal de los literales disponibles
        literals.remove(best_literal)
        
    return rule

# Conjunto de datos de entrenamiento
examples_pos = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'same', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'],
    ['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']
]
examples_neg = [
    ['rainy', 'cold', 'high', 'strong', 'cool', 'change', 'no'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'no']
]

# Lista de literales disponibles
literals = ['sunny', 'rainy', 'warm', 'cold', 'normal', 'high', 'strong', 'cool', 'same', 'change']

# Ejecutamos el algoritmo FOIL
rule = foil(examples_pos, examples_neg, literals)

# Imprimimos la regla resultante
print("Regla resultante:", rule)

