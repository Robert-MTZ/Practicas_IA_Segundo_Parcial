# Practica_136_Planificacion_Logica_Proposicional_SATPLAN_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Planificacion_Logica_Proposicional_SATPLAN

from pysat.solvers import MinisatSolver

# Definimos una función para convertir el problema de planificación en una fórmula CNF
def convertir_a_cnf(problema):
    cnf = []

    # Iteramos sobre las acciones del problema de planificación
    for accion, precondiciones, efectos in problema:
        # Cada acción se representa como una cláusula en la CNF
        clausula = []

        # Añadimos los literales positivos para las precondiciones
        for precondicion in precondiciones:
            clausula.append(precondicion)

        # Añadimos los literales negativos para los efectos
        for efecto in efectos:
            clausula.append("-" + efecto)

        # Añadimos la cláusula al conjunto de cláusulas CNF
        cnf.append(clausula)

    return cnf

# Definimos el problema de planificación (acciones, precondiciones y efectos)
problema = [
    ('MoverA', ['Libre(A)', 'En(A, Mesa)'], ['En(A, B)']),
    ('MoverB', ['Libre(B)', 'En(B, Mesa)'], ['En(B, A)'])
]

# Convertimos el problema de planificación a una fórmula CNF
cnf = convertir_a_cnf(problema)

# Creamos un solucionador SAT (Minisat en este caso)
solver = MinisatSolver()

# Añadimos las cláusulas CNF al solucionador SAT
for clausula in cnf:
    solver.add_clause(clausula)

# Resolvemos el problema de satisfacibilidad
resultado = solver.solve()

# Si el problema es satisfacible, imprimimos la solución
if resultado:
    print("Plan encontrado:")
    for accion, _, _ in problema:
        if solver.solve([accion]):
            print(accion)
else:
    print("No se encontró solución")

