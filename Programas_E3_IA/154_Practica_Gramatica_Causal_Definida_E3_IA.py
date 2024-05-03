# Practica_154_Gramatica_Causal_Definida_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Gramatica_Causal_Definida

import random

# Definimos la gramática como un diccionario donde las llaves son los símbolos no terminales y los valores son las reglas de producción
grammar = {
    'sentence': ['noun_phrase verb_phrase'],
    'noun_phrase': ['article noun', 'article adjective noun'],
    'verb_phrase': ['verb', 'verb noun_phrase'],
    'article': ['the', 'a'],
    'noun': ['cat', 'dog', 'man', 'woman'],
    'adjective': ['big', 'small', 'friendly'],
    'verb': ['runs', 'jumps', 'sleeps']
}

# Función para generar una cadena aleatoria a partir de la gramática
def generate_sentence(grammar, symbol):
    if symbol not in grammar:
        return symbol
    else:
        production = random.choice(grammar[symbol])
        return ' '.join(generate_sentence(grammar, s) for s in production.split())

if __name__ == '__main__':
    # Generamos una oración aleatoria utilizando la gramática definida
    random_sentence = generate_sentence(grammar, 'sentence')
    print("Oración generada:", random_sentence)
