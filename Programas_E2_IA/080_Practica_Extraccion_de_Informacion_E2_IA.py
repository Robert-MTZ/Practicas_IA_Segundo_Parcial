# Practica_080_Recuperacion_del_Datos_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Extraccion_de_Informacion

import spacy

# Cargar el modelo pre-entrenado de spaCy para el idioma en cuestión
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo para la extracción de información
texto = "El presidente de Estados Unidos, Joe Biden, se reunió con el primer ministro británico, Boris Johnson, en la cumbre del G7."

# Procesar el texto con spaCy
doc = nlp(texto)

# Iterar sobre las entidades nombradas en el texto y mostrarlas
print("Entidades nombradas encontradas:")
for entity in doc.ents:
    print("Texto:", entity.text)
    print("Etiqueta:", entity.label_)

# Imprimir el árbol de dependencias sintácticas del texto
print("\nÁrbol de dependencias sintácticas:")
for token in doc:
    print(token.text, "-->", token.dep_, "-->", token.head.text)
