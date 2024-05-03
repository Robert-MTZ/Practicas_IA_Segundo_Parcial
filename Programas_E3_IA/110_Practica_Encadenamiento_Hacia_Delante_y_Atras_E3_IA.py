# Practica_110_Encadenamiento_Hacia_Delante_y_Atras_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Encadenamiento_Hacia_Delante_y_Atras

class Rule: # Clase para representar una regla de produccion
 
    def __init__(self, conditions, conclusion): # Inicializa la regla con condiciones y una conclusion
        self.conditions = conditions
        self.conclusion = conclusion

    def apply(self, facts): #  Aplica la regla si se cumplen todas las condiciones
       
        if all(condition in facts for condition in self.conditions):
            return self.conclusion
        else:
            return None


class ForwardChaining: #  Clase para representar el encadenamiento hacia adelante
  
    def __init__(self, rules, facts): # Inicializa el encadenamiento hacia adelante con reglas y hechos iniciales
     
        self.rules = rules
        self.facts = facts

    def infer(self): # Realiza la inferencia hacia adelante
   
        new_facts = set()
        while True:
            inferred = False
            for rule in self.rules:
                conclusion = rule.apply(self.facts)
                if conclusion is not None and conclusion not in self.facts:
                    new_facts.add(conclusion)
                    inferred = True
            if not inferred:
                break
            self.facts.update(new_facts)
        return self.facts

if __name__ == "__main__":
    # Definimos las reglas y los hechos iniciales
    rules = [
        Rule(["P", "Q"], "R"),
        Rule(["S"], "P"),
        Rule(["T"], "Q"),
    ]
    initial_facts = {"S", "T"}

    # Realizamos la inferencia hacia adelante
    fc = ForwardChaining(rules, initial_facts)
    inferred_facts = fc.infer()

    # Imprimimos los hechos inferidos
    print("Hechos inferidos:", inferred_facts)

