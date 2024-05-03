# Practica_112_Resolucion_Skolem_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Resolucion_Skolem

from sympy import symbols, Or, And, Not, satisfiable

# Definir los símbolos para las variables
x, y, z = symbols('x y z')

# Definir la fórmula lógica de ejemplo
formula = Or(And(x, y), And(Not(x), z))

# Mostrar la fórmula original
print("Fórmula original:", formula)

# Convertir la fórmula a cláusulas de Horn
clausulas_horn = formula.to_cnf()

# Mostrar las cláusulas de Horn
print("Cláusulas de Horn:", clausulas_horn)

# Verificar si la fórmula es satisfacible
satisfacible = satisfiable(clausulas_horn)

# Imprimir el resultado
if satisfacible:
    print("La fórmula es satisfacible.")
else:
    print("La fórmula no es satisfacible.")
