# Practica_102_Resolucion_y_Forma_Normal_Conjuntiva_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Resolucion_y_Forma_Normal_Conjuntiva

from sympy import symbols, Or, And, Not, to_cnf, satisfiable

def resolution(clause_a, clause_b):

    resolvents = []
    for literal in clause_a:
        if Not(literal) in clause_b:  # Si el complemento del literal está en la otra cláusula
            # Elimina el par de literales opuestos y une las cláusulas
            resolvent = [l for l in clause_a if l != literal] + [l for l in clause_b if l != Not(literal)]
            resolvents.append(resolvent)
    return resolvents

def to_cnf_resolution(expr):
 
    cnf = to_cnf(expr)  # Convierte la expresión a CNF utilizando la biblioteca sympy

    # Obtiene las cláusulas de la CNF
    clauses = list(cnf.args) if isinstance(cnf, Or) else [cnf]

    while True:
        new_clauses = []  # Almacena las nuevas cláusulas generadas por la resolución

        for i in range(len(clauses)):
            for j in range(i+1, len(clauses)):
                resolvents = resolution(clauses[i].args, clauses[j].args)  # Realiza la resolución entre pares de cláusulas
                new_clauses.extend(resolvents)

        # Verifica si hay cláusulas nuevas, si no hay, termina
        if not new_clauses:
            break

        # Elimina cláusulas redundantes
        new_clauses = [clause for clause in new_clauses if clause not in clauses]

        # Une las cláusulas nuevas con las existentes
        clauses.extend(new_clauses)

    return And(*[Or(*clause) for clause in clauses])  # Combina las cláusulas en una única expresión lógica conjuntiva

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos algunas variables simbólicas
    p, q, r = symbols('p q r')

    # Expresión lógica para probar
    expr = Or(And(p, q), And(Not(p), r))

    # Convertimos la expresión a CNF utilizando resolución
    cnf_resolution = to_cnf_resolution(expr)

    # Verificamos si la CNF es satisfacible
    print("¿La CNF es satisfacible?", satisfiable(cnf_resolution))
    print("Forma normal conjuntiva:", cnf_resolution)
