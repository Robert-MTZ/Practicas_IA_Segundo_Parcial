# Practica_099_Base_de_Conocimiento_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Base_de_Conocimiento

class KnowledgeBase: #  Una base de conocimiento simple que almacena hechos y reglas.

    def __init__(self):
       
        self.facts = []  # Lista para almacenar hechos
        self.rules = []  # Lista para almacenar reglas

    def add_fact(self, fact):
  
        self.facts.append(fact)

    def add_rule(self, antecedent, consequent):
 
        self.rules.append((antecedent, consequent))

    def query(self, fact):
 
        if fact in self.facts:  # Verifica si el hecho está presente en los hechos conocidos
            return True
        for antecedent, consequent in self.rules:  # Itera sobre todas las reglas
            if all(self.query(ante) for ante in antecedent) and fact == consequent:  # Verifica si se cumplen todas las premisas y el consecuente coincide
                return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    kb = KnowledgeBase()  # Crea una nueva base de conocimiento

    # Agrega algunos hechos
    kb.add_fact("Gato")
    kb.add_fact("Perro")
    kb.add_fact("Mamífero")
    kb.add_fact("Felino")
    kb.add_fact("Canino")

    # Agrega algunas reglas
    kb.add_rule(["Gato", "Mamífero"], "Es un gato mamífero")
    kb.add_rule(["Perro", "Mamífero"], "Es un perro mamífero")
    kb.add_rule(["Felino", "Mamífero"], "Es un felino mamífero")
    kb.add_rule(["Canino", "Mamífero"], "Es un canino mamífero")

    # Realiza algunas consultas
    print("¿El gato es un mamífero?", kb.query("Es un gato mamífero"))
    print("¿El perro es un mamífero?", kb.query("Es un perro mamífero"))
    print("¿El perro es un felino?", kb.query("Es un perro felino"))
