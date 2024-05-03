# Practica_107_Reglas_de_Diagnostico_y_Causales_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Reglas_de_Diagnostico_y_Causales

class Rule: # Clase para representar una regla de diagnóstico o causal

    def __init__(self, conditions, diagnosis): #   Inicializa la regla con las condiciones y el diagnóstico asociado
 
        self.conditions = conditions
        self.diagnosis = diagnosis

    def match(self, symptoms): # Verifica si los síntomas dados cumplen con las condiciones de la regla
   
        return all(symptom in symptoms for symptom in self.conditions)


class DiagnosticRules: # Clase para representar un conjunto de reglas de diagnóstico

    def __init__(self): # Inicializa el conjunto de reglas vacío
       
        self.rules = []

    def add_rule(self, conditions, diagnosis): # Agrega una nueva regla al conjunto de reglas
  
        rule = Rule(conditions, diagnosis)
        self.rules.append(rule)

    def diagnose(self, symptoms): # Realiza un diagnóstico basado en los síntomas presentados por el paciente
    
        diagnoses = []
        for rule in self.rules:
            if rule.match(symptoms):
                diagnoses.append(rule.diagnosis)
        return diagnoses

if __name__ == "__main__":
    # Creamos un conjunto de reglas de diagnóstico
    diagnostic_rules = DiagnosticRules()

    # Agregamos algunas reglas de diagnóstico
    diagnostic_rules.add_rule(["fiebre", "tos"], "Resfriado común")
    diagnostic_rules.add_rule(["dolor de cabeza", "náuseas"], "Migraña")
    diagnostic_rules.add_rule(["dolor de garganta", "ganglios inflamados"], "Amigdalitis")

    # Síntomas presentados por el paciente
    patient_symptoms = {"fiebre", "tos"}

    # Realizamos el diagnóstico
    diagnoses = diagnostic_rules.diagnose(patient_symptoms)

    # Imprimimos los diagnósticos posibles
    print("Diagnósticos posibles:", diagnoses)

