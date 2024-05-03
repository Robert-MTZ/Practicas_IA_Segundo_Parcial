# Practica_061_Naïve_Bayes_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Naïve_Bayes

import numpy as np  # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class NaiveBayesClassifier: # Se crea la clase 
    def __init__(self):
        self.class_priors = {}  # Diccionario para almacenar las probabilidades a priori de cada clase
        self.word_counts = {}   # Diccionario para contar la frecuencia de cada palabra en cada clase
        self.class_totals = {}  # Diccionario para almacenar el número total de palabras en cada clase

    def train(self, X, y):
        # X es una lista de documentos (cada uno representado como una lista de palabras)
        # y es una lista de etiquetas de clase correspondientes a cada documento en X
        num_documents = len(X)

        # Calcular las probabilidades a priori de cada clase
        for label in set(y):
            self.class_priors[label] = sum(1 for label_i in y if label_i == label) / num_documents

        # Inicializar el conteo de palabras para cada clase
        for label in set(y):
            self.word_counts[label] = {}
            self.class_totals[label] = 0

        # Contar la frecuencia de cada palabra en cada clase
        for i in range(num_documents):
            document = X[i]
            label = y[i]
            for word in document:
                if word not in self.word_counts[label]:
                    self.word_counts[label][word] = 0
                self.word_counts[label][word] += 1
                self.class_totals[label] += 1

    def predict(self, X):
        # X es una lista de documentos (cada uno representado como una lista de palabras)
        predictions = []
        for document in X:
            max_prob = -np.inf
            predicted_class = None
            for label in self.class_priors:
                log_prob = np.log(self.class_priors[label])  # Log de la probabilidad a priori de la clase
                for word in document:
                    # Calcular la probabilidad condicional de cada palabra en el documento dado la clase
                    # y sumar los logs para obtener la probabilidad conjunta
                    log_prob += np.log((self.word_counts[label].get(word, 0) + 1) / (self.class_totals[label] + len(self.word_counts[label])))
                if log_prob > max_prob:
                    max_prob = log_prob
                    predicted_class = label
            predictions.append(predicted_class)
        return predictions

X_train = [["happy", "fun", "joy"], ["sad", "tears"], ["happy", "smile", "joy"]]
y_train = ["positive", "negative", "positive"]

classifier = NaiveBayesClassifier()
classifier.train(X_train, y_train)

X_test = [["happy", "fun"], ["sad", "tears", "joy"]]
predictions = classifier.predict(X_test)
print(predictions)  # Imprimir las predicciones
