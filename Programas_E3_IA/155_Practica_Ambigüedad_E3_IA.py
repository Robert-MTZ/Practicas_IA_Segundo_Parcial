# Practica_155_Ambigüedad_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Ambigüedad

# Definimos la gramática como un diccionario donde las llaves son los símbolos no terminales y los valores son las reglas de producción
grammar = {
    'expr': ['expr + expr', 'expr - expr', 'expr * expr', 'expr / expr', '( expr )', 'number'],
    'number': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
}

# Función para generar todas las posibles interpretaciones de una expresión a partir de la gramática
def generate_expressions(grammar, symbol):
    if symbol not in grammar:
        return [symbol]
    else:
        expressions = []
        for production in grammar[symbol]:
            expressions.extend(generate_expression(grammar, s) for s in production.split())
        return expressions

# Función para evaluar una expresión aritmética
def evaluate_expression(expr):
    return eval(expr)

if __name__ == '__main__':
    # Definimos una expresión aritmética ambigua
    ambiguous_expr = '2 + 3 * 4'
    print("Expresión aritmética ambigua:", ambiguous_expr)
    # Generamos todas las posibles interpretaciones de la expresión
    interpretations = generate_expressions(grammar, 'expr')
    print("Posibles interpretaciones:")
    for interpretation in interpretations:
        print(interpretation, "=", evaluate_expression(interpretation))
