# Practica_115_Logica_Modal_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Logica_Modal

class ModalLogic:
    def __init__(self, world):
        self.world = world
    
    def evaluate(self, formula):
        # Dividimos la fórmula en el operador modal y la proposición
        modal = formula[0]
        proposition = formula[1:]
        
        # Evaluamos la fórmula dependiendo del operador modal
        if modal == 'P':  # Posible
            return proposition in self.world
        elif modal == 'N':  # Necesario
            return all(proposition in w for w in self.world)
        else:
            raise ValueError("Operador modal desconocido")

# Definimos un mundo con posibles mundos
world = [{'p', 'q'}, {'p'}, {'q'}]

# Creamos una instancia de ModalLogic
modal_logic = ModalLogic(world)

# Formulas de lógica modal
formula_1 = 'Pp'  # Es posible que p sea verdadero
formula_2 = 'Np'  # Es necesario que p sea verdadero

# Evaluamos las fórmulas
result_1 = modal_logic.evaluate(formula_1)
result_2 = modal_logic.evaluate(formula_2)

# Imprimimos los resultados
print("Mundo:", world)
print(f"¿{formula_1} es verdadero?:", result_1)
print(f"¿{formula_2} es verdadero?:", result_2)

