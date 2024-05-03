# Practica_108_Ingeniería_del_Conocimiento_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Ingeniería_del_Conocimiento

class Rule: #  Clase para representar una regla de produccion
    
    def __init__(self, condition, action): # Inicializa la regla con una condición y una accion
  
        self.condition = condition
        self.action = action

    def apply(self): # Aplica la regla si la condición se cumple
  
        if self.condition():
            return self.action()
        else:
            return None


class KnowledgeBase: # Clase para representar la base de conocimiento del sistema

    def __init__(self): #  Inicializa la base de conocimiento con una lista vacía de reglas
       
        self.rules = []

    def add_rule(self, rule): # Agrega una regla a la base de conocimiento
     
        self.rules.append(rule)

    def infer(self): #  Realiza la inferencia basada en las reglas en la base de conocimiento
  
        actions = []
        for rule in self.rules:
            result = rule.apply()
            if result is not None:
                actions.append(result)
        return actions

# Definimos algunas funciones de condición
def sunny_condition():
    return input("¿Está soleado hoy? (sí/no): ").lower() == "sí"


def warm_condition():
    return input("¿La temperatura es cálida? (sí/no): ").lower() == "sí"


# Definimos algunas funciones de acción
def picnic_action():
    return "Ve de picnic al parque."


def hike_action():
    return "Ve de excursión a la montaña."

if __name__ == "__main__":
    # Creamos la base de conocimiento
    kb = KnowledgeBase()

    # Agregamos reglas a la base de conocimiento
    kb.add_rule(Rule(sunny_condition, picnic_action))
    kb.add_rule(Rule(warm_condition, hike_action))

    # Realizamos la inferencia
    print("Recomendaciones:")
    for action in kb.infer():
        print("-", action)

