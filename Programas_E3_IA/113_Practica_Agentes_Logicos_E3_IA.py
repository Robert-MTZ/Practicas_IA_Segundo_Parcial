# Practica_113_Agentes_Logicos_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Agentes_Logicos

from itertools import product

def is_satisfiable(formula):
    # Generar todas las posibles asignaciones de valores de verdad a las variables
    variables = set()
    for token in formula:
        if token.isalpha():
            variables.add(token)
    truth_values = product([False, True], repeat=len(variables))
    
    # Probar cada posible asignación de valores de verdad
    for values in truth_values:
        valuation = dict(zip(variables, values))
        if evaluate(formula, valuation):
            return True
    return False

def evaluate(formula, valuation):
    stack = []
    for token in formula:
        if token.isalpha():
            stack.append(valuation[token])
        elif token == '¬':
            stack.append(not stack.pop())
        elif token == '∧':
            stack.append(stack.pop() and stack.pop())
        elif token == '∨':
            stack.append(stack.pop() or stack.pop())
    return stack[0]

# Fórmula de lógica proposicional
formula = ['p', '∧', 'q', '∨', 'r', '∧', '¬', 'p']

# Verificar si la fórmula es satisfacible
satisfacible = is_satisfiable(formula)

# Imprimir el resultado
if satisfacible:
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
