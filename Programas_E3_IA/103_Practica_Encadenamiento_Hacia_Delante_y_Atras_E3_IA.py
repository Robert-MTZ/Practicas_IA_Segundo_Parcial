# Practica_103_Encadenamiento_Hacia_Delante_y_Atras_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Encadenamiento_Hacia_Delante_y_Atras

class KnowledgeBase:

    def __init__(self):
    
        self.rules = []  # Lista para almacenar reglas
        self.facts = set()  # Conjunto para almacenar hechos

    def add_rule(self, rule):
 
        self.rules.append(rule)

    def add_fact(self, fact):
   
        self.facts.add(fact)

    def forward_chaining(self):
      
        new_facts = True  # Bandera para indicar si se han inferido nuevos hechos

        while new_facts:
            new_facts = False
            for rule in self.rules:
                if rule.is_triggerable(self.facts):  # Verifica si la regla se puede activar
                    new_fact = rule.consequent
                    if new_fact not in self.facts:  # Verifica si el hecho es nuevo
                        self.facts.add(new_fact)
                        new_facts = True

    def backward_chaining(self, goal):
   
        if goal in self.facts:  # Si el objetivo ya es un hecho conocido, retorna True
            return True

        for rule in self.rules:
            if goal == rule.consequent:
                if all(self.backward_chaining(antecedent) for antecedent in rule.antecedents):  # Verifica si todas las premisas son alcanzables
                    return True

        return False

class Rule:
  

    def __init__(self, antecedents, consequent):
 
        self.antecedents = antecedents
        self.consequent = consequent

    def is_triggerable(self, known_facts):
  
        return all(antecedent in known_facts for antecedent in self.antecedents)


class Fact:

    def __init__(self, name):
    
        self.name = name

    def __eq__(self, other):
  
        return isinstance(other, Fact) and self.name == other.name

    def __hash__(self):
       
        return hash(self.name)

if __name__ == "__main__":
    # Creamos algunos hechos
    A = Fact("A")
    B = Fact("B")
    C = Fact("C")
    D = Fact("D")

    # Creamos algunas reglas
    rule1 = Rule([A], B)
    rule2 = Rule([B, C], D)

    # Creamos una base de conocimiento y agregamos las reglas y hechos
    kb = KnowledgeBase()
    kb.add_rule(rule1)
    kb.add_rule(rule2)
    kb.add_fact(A)
    kb.add_fact(C)

    # Realizamos encadenamiento hacia adelante para inferir nuevos hechos
    kb.forward_chaining()

    # Imprimimos los hechos inferidos
    print("Hechos inferidos después de encadenamiento hacia adelante:")
    for fact in kb.facts:
        print(fact.name)

    # Realizamos encadenamiento hacia atrás para verificar si se puede probar un objetivo
    print("¿Se puede probar el hecho D?")
    print(kb.backward_chaining(D))
