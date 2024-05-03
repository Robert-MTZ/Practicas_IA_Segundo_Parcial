# Practica_116_Logica_Temporal_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Programacion_Logica_Temporal

class TemporalLogic:
    def __init__(self, world):
        self.world = world
    
    def evaluate(self, formula):
        # Dividimos la fórmula en el operador temporal y las variables proposicionales
        temporal_operator = formula[0]  # Operador temporal ("<" o ">")
        proposition = formula[1:]  # Variables proposicionales
        
        # Evaluamos la fórmula dependiendo del operador temporal
        if temporal_operator == '<':  # Antes
            return all(self.world.index(proposition[i]) < self.world.index(proposition[i+1])
                       for i in range(len(proposition)-1))
        elif temporal_operator == '>':  # Después
            return all(self.world.index(proposition[i]) > self.world.index(proposition[i+1])
                       for i in range(len(proposition)-1))
        else:
            raise ValueError("Operador temporal desconocido")

# Definimos una secuencia de eventos (mundo)
world = ['p', 'q', 'r']

# Creamos una instancia de TemporalLogic
temporal_logic = TemporalLogic(world)

# Formulas de lógica temporal
formula_1 = '<pq'  # p ocurre antes que q
formula_2 = '>rp'  # r ocurre después que p

# Evaluamos las formulas
result_1 = temporal_logic.evaluate(formula_1)
result_2 = temporal_logic.evaluate(formula_2)

# Imprimimos los resultados
print("Mundo (secuencia de eventos):", world)
print(f"¿{formula_1} es verdadero?:", result_1)
print(f"¿{formula_2} es verdadero?:", result_2)

