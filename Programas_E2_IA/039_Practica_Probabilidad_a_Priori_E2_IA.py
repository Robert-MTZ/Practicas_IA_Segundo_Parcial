# Practica_039_Probabilidad_a_Priori_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Probabilidad_a_Priori

class ProbabilidadAPriori:
    def __init__(self, datos):
        self.datos = datos

    def calcular_probabilidad(self, evento):
        """
        Calcula la probabilidad a priori de un evento dado en el conjunto de datos.

        Args:
        - evento: El evento del cual se desea calcular la probabilidad a priori.

        Returns:
        - probabilidad: La probabilidad a priori del evento.
        """
        # Contamos el número de veces que aparece el evento en los datos
        conteo_evento = sum(1 for muestra in self.datos if muestra == evento)

        # Calculamos la probabilidad dividiendo el número de ocurrencias del evento entre el tamaño del conjunto de datos
        probabilidad = conteo_evento / len(self.datos)

        return probabilidad

# Ejemplo de conjunto de datos de juguete
datos = ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B', 'C', 'A']

# Creamos una instancia de la clase ProbabilidadAPriori con el conjunto de datos
prob_apriori = ProbabilidadAPriori(datos)

# Calculamos la probabilidad a priori de varios eventos
evento_a = 'A'
evento_b = 'B'
evento_c = 'C'
prob_a = prob_apriori.calcular_probabilidad(evento_a)
prob_b = prob_apriori.calcular_probabilidad(evento_b)
prob_c = prob_apriori.calcular_probabilidad(evento_c)

# Imprimimos los resultados
print(f"Probabilidad a priori de {evento_a}: {prob_a}")
print(f"Probabilidad a priori de {evento_b}: {prob_b}")
print(f"Probabilidad a priori de {evento_c}: {prob_c}")
