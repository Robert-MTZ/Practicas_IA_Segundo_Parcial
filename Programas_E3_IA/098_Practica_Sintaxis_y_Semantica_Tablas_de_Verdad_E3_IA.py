# Practica_098_Sintaxis_y_Semantica_Tablas_de_Verdad_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Sintaxis_y_Semantica_Tablas_de_Verdad

import itertools

def generate_truth_table(variables):

    table = []
    permutations = itertools.product([True, False], repeat=len(variables)) # Genera todas las combinaciones posibles de True y False para las variables
    for perm in permutations:
        row = {}
        for i, var in enumerate(variables):
            row[var] = perm[i] # Asigna el valor de verdad actual a la variable correspondiente
        table.append(row) # Agrega la fila a la tabla
    return table

def evaluate_expression(expression, values):

    # Reemplaza los valores de las variables en la expresión
    expression = expression.replace('and', 'and_').replace('or', 'or_').replace('not', 'not_')
    for var, value in values.items():
        expression = expression.replace(var, str(value))
    
    # Evalúa la expresión y devuelve el resultado
    return eval(expression)

def print_truth_table(expression, variables):
    """
    Print the truth table for the given logical expression.
    
    Args:
    - expression: String representing the logical expression
    - variables: List of strings representing variable names
    """
    # Genera la tabla de verdad
    table = generate_truth_table(variables)
    
    # Imprime el encabezado de la tabla
    header = '\t'.join(variables + [expression])
    print(header)
    print('-' * len(header))
    
    # Imprime cada fila de la tabla
    for row in table:
        values = [str(row[var]) for var in variables]
        result = evaluate_expression(expression, row)
        values.append(str(result))
        print('\t'.join(values))

expression = 'not A or B and C'
variables = ['A', 'B', 'C']
print_truth_table(expression, variables)

