# Practica_146_Mejor_Hipotesis_Actual_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Mejor_Hipotesis_Actual

# Definición de la clase de la Mejor Hipótesis Actual
class BestHypothesis:
    def __init__(self):
        self.best_hypothesis = None  # La mejor hipótesis actual
        self.best_accuracy = 0  # La precisión de la mejor hipótesis actual

    # Función para entrenar el modelo y encontrar la mejor hipótesis
    def train(self, X_train, y_train):
        unique_classes = set(y_train)  # Obtenemos las clases únicas en los datos de entrenamiento

        # Iteramos sobre todas las clases únicas para encontrar la mejor hipótesis
        for target_class in unique_classes:
            # Contamos la frecuencia de la clase en los datos de entrenamiento
            class_frequency = sum(1 for label in y_train if label == target_class)
            
            # Calculamos la precisión de la hipótesis que predice la clase mayoritaria
            accuracy = class_frequency / len(y_train)
            
            # Si esta hipótesis es mejor que la actual, actualizamos la mejor hipótesis
            if accuracy > self.best_accuracy:
                self.best_accuracy = accuracy
                self.best_hypothesis = target_class

    # Función para predecir la clase de nuevos ejemplos
    def predict(self, X_test):
        return [self.best_hypothesis] * len(X_test)  # Devolvemos la mejor hipótesis para todos los ejemplos

# Conjunto de datos de entrenamiento
X_train = [[2, 's'], [3, 'm'], [4, 'm'], [5, 'l'], [6, 'l']]
y_train = ['-', '-', '+', '+', '+']

# Creamos una instancia del clasificador de Mejor Hipótesis Actual
bha_classifier = BestHypothesis()

# Entrenamos el clasificador con los datos de entrenamiento
bha_classifier.train(X_train, y_train)

# Realizamos predicciones sobre los mismos datos de entrenamiento
predictions = bha_classifier.predict(X_train)

# Imprimimos las predicciones
print("Predicciones:", predictions)

