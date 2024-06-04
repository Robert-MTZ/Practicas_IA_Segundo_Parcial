# Practica_097_Sintaxis_y_Semantica_Tablas_de_Verdad_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Sintaxis_y_Semantica_Tablas_de_Verdad


import itertools

def generate_truth_table(variables):
    
    table = []
    # itertools.product genera todas las posibles combinaciones de valores True y False para las variables
    permutations = itertools.product([True, False], repeat=len(variables))
    for perm in permutations:
        row = {}
        for i, var in enumerate(variables):
            row[var] = perm[i]
        table.append(row)
    return table

def evaluate_expression(expression, values):
 
    # Reemplaza los valores de las variables en la expresión
    expression = expression.replace('and', 'and_').replace('or', 'or_').replace('not', 'not_')
    for var, value in values.items():
        expression = expression.replace(var, str(value))

    # Evalúa la expresión y devuelve el resultado
    return eval(expression)

def print_truth_table(expression, variables):

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

# Ejemplo de uso
expression = 'not A or B and C'
variables = ['A', 'B', 'C']
print_truth_table(expression, variables)

