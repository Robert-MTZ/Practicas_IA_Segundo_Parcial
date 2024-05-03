# Practica_100_Inferencia_Logica_Proposicional_Base_de_Conocimiento_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Inferencia_Logica_Proposicional_Base_de_Conocimiento

class InferenceEngine:
    """
    Motor de inferencia lógica proposicional.
    """

    def __init__(self):
        """
        Inicializa el motor de inferencia con una lista vacía de reglas.
        """
        self.rules = []

    def add_rule(self, rule):
        """
        Agrega una regla al motor de inferencia.

        Args:
        - rule: Una instancia de la clase Rule que representa una regla.
        """
        self.rules.append(rule)

    def infer(self, query):
        """
        Infere si una consulta es verdadera o falsa.

        Args:
        - query: Una instancia de la clase Literal que representa una consulta.

        Returns:
        - True si la consulta es verdadera, False si es falsa.
        """
        for rule in self.rules:
            # Si la regla es activada por la consulta
            if rule.is_triggered_by(query):
                # Verifica si todas las premisas de la regla son verdaderas
                if all(self.infer(premise) for premise in rule.antecedents):
                    # Si todas las premisas son verdaderas, la conclusión también es verdadera
                    return True
        # Si ninguna regla se activa o ninguna regla tiene premisas verdaderas, la consulta es falsa
        return False


class Literal:

    def __init__(self, name, value=True):

        self.name = name
        self.value = value

    def __str__(self):
     
        return self.name


class Rule:
   
    def __init__(self, antecedents, consequent):

        self.antecedents = antecedents
        self.consequent = consequent

    def is_triggered_by(self, query):

        return self.consequent.name == query.name
    
if __name__ == "__main__":
    # Creamos un motor de inferencia
    engine = InferenceEngine()

    # Creamos algunas premisas y conclusiones
    p, q, r = Literal("p"), Literal("q"), Literal("r")
    s = Literal("s", value=False)

    # Creamos algunas reglas y las agregamos al motor de inferencia
    engine.add_rule(Rule([p], q))
    engine.add_rule(Rule([q, r], s))

    # Consultamos si "s" es verdadero
    print("¿s es verdadero?", engine.infer(s))

