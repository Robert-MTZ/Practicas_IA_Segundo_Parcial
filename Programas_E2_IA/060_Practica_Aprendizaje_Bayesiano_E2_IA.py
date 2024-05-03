# Practica_060_Aprendizaje_Bayesiano_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Aprendizaje_Bayesiano

import numpy as np # Genera numeros aleatorios y realizar calculos matriciales de manera eficiente

class NaiveBayesClassifier: # Define una clase llamada NaiveBayesClassifier
    def __init__(self): # Define el método de inicialización de la clase
        self.class_prior = None # Inicializa el atributo class_prior como None
        self.mean = None  # Inicializa el atributo mean como None
        self.std = None # Inicializa el atributo std como None

    def fit(self, X, y): # Define el método fit para ajustar el modelo
        self.class_prior = {} # Inicializa un diccionario vacío para almacenar las probabilidades a priori de las clases
        self.mean = {} # Inicializa un diccionario vacío para almacenar las medias de las características por clase
        self.std = {} # Inicializa un diccionario vacío para almacenar las desviaciones estándar de las características por clase

        classes = np.unique(y) # Obtiene las clases únicas en el conjunto de etiquetas y las guarda en la variable classes

        for c in classes: # Itera sobre cada clase única
            X_c = X[y == c]  # Filtra los datos de entrenamiento correspondientes a la clase c y los guarda en X_c
            self.class_prior[c] = len(X_c) / len(X) # Calcula y guarda la probabilidad a priori de la clase c
            self.mean[c] = np.mean(X_c, axis=0) # Calcula y guarda la media de las características para la clase c
            self.std[c] = np.std(X_c, axis=0) # Calcula y guarda la desviación estándar de las características para la clase c

    def predict(self, X):  # Define el método predict para hacer predicciones
        predictions = [] # Inicializa una lista para almacenar las predicciones

        for x in X: # Itera sobre cada instancia de datos en X
            posteriors = [] # Inicializa una lista para almacenar las probabilidades posteriores

            for c in self.class_prior: # Itera sobre cada clase y su probabilidad a priori
                prior = np.log(self.class_prior[c]) # Calcula el logaritmo de la probabilidad a priori de la clase c
                likelihood = np.sum(np.log(self._pdf(c, x)))  # Calcula el logaritmo de la verosimilitud para la clase c y la instancia x
                posterior = prior + likelihood # Calcula la probabilidad posterior para la clase c y la instancia x
                posteriors.append(posterior) # Agrega la probabilidad posterior a la lista de probabilidades posteriores

            predictions.append(np.argmax(posteriors)) # Agrega la clase con la probabilidad posterior más alta como predicción

        return predictions  # Devuelve la lista de predicciones

    def _pdf(self, class_label, x): # Define un método privado para calcular la densidad de probabilidad
        mean = self.mean[class_label] # Obtiene la media correspondiente a la clase class_label
        std = self.std[class_label] # Obtiene la desviación estándar correspondiente a la clase class_label
        numerator = np.exp(-((x - mean) ** 2) / (2 * std ** 2)) # Calcula el numerador de la densidad de probabilidad
        denominator = np.sqrt(2 * np.pi * std ** 2) # Calcula el denominador de la densidad de probabilidad
        return numerator / denominator # Devuelve la densidad de probabilidad

X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) # Datos de entrenamiento
y_train = np.array([0, 0, 0, 1, 1, 1]) # Etiquetas de clase correspondientes a los datos de entrenamiento

X_test = np.array([[1, 2], [5, 6]]) # Datos de prueba

model = NaiveBayesClassifier() # Crea una instancia del clasificador de Bayes ingenuo
model.fit(X_train, y_train)# Entrena el modelo con los datos de entrenamiento

predictions = model.predict(X_test) # Realiza predicciones sobre los datos de prueba
print("Predictions:", predictions) # Imprime las predicciones
