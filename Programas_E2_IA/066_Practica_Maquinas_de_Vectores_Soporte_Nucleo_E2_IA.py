# Practica_066_Maquinas_de_Vectores_Soporte_Nucleo_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Maquinas_de_Vectores_Soporte_Nucleo

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generamos datos de ejemplo con dos características y dos clases
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_clusters_per_class=1, random_state=42)

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador SVM con un núcleo RBF (Radial Basis Function)
svm_classifier = SVC(kernel='rbf', random_state=42)

# Entrenamos el clasificador SVM con los datos de entrenamiento
svm_classifier.fit(X_train, y_train)

# Realizamos predicciones sobre los datos de prueba
y_pred = svm_classifier.predict(X_test)

# Calculamos la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo SVM:", accuracy)

