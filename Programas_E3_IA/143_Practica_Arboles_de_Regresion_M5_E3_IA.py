# Practica_143_Arboles_de_Regresion_M5_ID3_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Arboles_de_Regresion_M5

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import numpy as np

# Cargamos el conjunto de datos de Boston Housing
boston = load_boston()
X = boston.data
y = boston.target

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un árbol de regresión
reg_tree = DecisionTreeRegressor(max_depth=4)
reg_tree.fit(X_train, y_train)

# Función para realizar la poda M5
def m5_prune(tree, X, y, threshold=0.05):
    if tree.children_left[0] == tree.children_right[0]:
        return

    for i in range(tree.node_count):
        if tree.children_left[i] != tree.children_right[i]:
            m5_prune(tree.children_left[i], X, y)
            m5_prune(tree.children_right[i], X, y)

            y_pred = tree.value[i].flatten()[0]
            y_actual = y[tree.apply(X) == i]

            mse_child_left = np.mean((y[tree.apply(X) == tree.children_left[i]] - y_pred[0]) ** 2)
            mse_child_right = np.mean((y[tree.apply(X) == tree.children_right[i]] - y_pred[1]) ** 2)
            mse_total = np.mean((y_actual - np.mean(y_actual)) ** 2)

            if mse_child_left + mse_child_right - mse_total < threshold:
                tree.children_left[i] = tree.children_right[i] = -1

# Realizamos la poda M5
m5_prune(reg_tree.tree_, X_train, y_train)

# Evaluamos el rendimiento del modelo en el conjunto de prueba
y_pred = reg_tree.predict(X_test)
mse = np.mean((y_test - y_pred) ** 2)
print("Error cuadrático medio:", mse)

