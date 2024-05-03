# Practica_156_Induccion_Gramatical_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Induccion_Gramatical

from collections import defaultdict

# Función para convertir una cadena en una lista de símbolos
def tokenize(string):
    return string.split()

# Función para construir una gramática en FNC a partir de ejemplos
def inductive_grammar_learning(examples):
    # Inicializamos un diccionario para almacenar las reglas de producción
    productions = defaultdict(list)

    # Para cada ejemplo, convertimos la cadena en una lista de símbolos y agregamos las reglas de producción
    for example in examples:
        tokens = tokenize(example)
        if len(tokens) > 1:
            # Si la cadena tiene más de un símbolo, agregamos reglas para los pares de símbolos consecutivos
            for i in range(len(tokens) - 1):
                productions[tokens[i], tokens[i+1]].append(tokens[i] + " " + tokens[i+1])
        else:
            # Si la cadena tiene un solo símbolo, lo marcamos como terminal
            productions[tokens[0]].append(tokens[0])

    # Generamos un conjunto de reglas para los símbolos no terminales
    non_terminals = set(productions.keys())

    # Construimos las reglas de producción para cada símbolo no terminal
    for A, B in non_terminals:
        for C in non_terminals:
            for production1 in productions[A, C]:
                for production2 in productions[C, B]:
                    productions[A, B].append(production1 + " " + production2)

    # Eliminamos las reglas repetidas
    for key, value in productions.items():
        productions[key] = list(set(value))

    # Retornamos las reglas de producción en forma de gramática
    return productions

# Función para generar nuevas cadenas a partir de la gramática aprendida
def generate_from_grammar(grammar, start_symbol, length=10):
    # Inicializamos la cadena resultante con el símbolo inicial
    result = [start_symbol]

    # Iteramos para generar la cadena de acuerdo con la gramática
    for _ in range(length):
        # Elegimos aleatoriamente una producción para el símbolo actual
        production = random.choice(grammar.get(result[-1], [result[-1]]))
        # Dividimos la producción en símbolos y los agregamos a la cadena resultante
        result.extend(production.split())

    # Retornamos la cadena generada
    return ' '.join(result)

if __name__ == '__main__':
    # Definimos una lista de ejemplos de cadenas válidas en el lenguaje
    examples = [
        "a b c",
        "a d e f g",
        "a b c d e f"
    ]

    # Aplicamos el algoritmo de inducción gramatical para aprender la gramática
    learned_grammar = inductive_grammar_learning(examples)
    print("Gramática aprendida:")
    for key, value in learned_grammar.items():
        print(key, "->", value)

    # Generamos nuevas cadenas a partir de la gramática aprendida
    print("\nNuevas cadenas generadas:")
    for _ in range(5):
        generated_string = generate_from_grammar(learned_grammar, 'a')
        print(generated_string)
