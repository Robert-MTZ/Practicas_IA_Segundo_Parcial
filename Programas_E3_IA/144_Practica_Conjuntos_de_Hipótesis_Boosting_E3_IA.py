# Practica_144_Conjuntos_de_Hipótesis_Boosting_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Conjuntos_de_Hipótesis_Boosting

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador de árbol de decisión como clasificador base
base_classifier = DecisionTreeClassifier(max_depth=1)

# Creamos un clasificador AdaBoost con el clasificador base
adaboost_classifier = AdaBoostClassifier(base_estimator=base_classifier, n_estimators=50, learning_rate=1.0)

# Entrenamos el clasificador AdaBoost
adaboost_classifier.fit(X_train, y_train)

# Realizamos predicciones en el conjunto de prueba
y_pred = adaboost_classifier.predict(X_test)

# Calculamos la precisión del clasificador AdaBoost
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador AdaBoost:", accuracy)

