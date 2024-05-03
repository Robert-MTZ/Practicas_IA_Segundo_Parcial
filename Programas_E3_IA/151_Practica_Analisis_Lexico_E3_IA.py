# Practica_151_Analisis_Lexico_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Analisis_Lexico

import re

# Definimos los tokens que queremos reconocer y sus correspondientes expresiones regulares
tokens = [
    ('NUMBER', r'\d+'),         # Números enteros
    ('PLUS', r'\+'),            # Suma
    ('MINUS', r'\-'),           # Resta
    ('TIMES', r'\*'),           # Multiplicación
    ('DIVIDE', r'/'),           # División
    ('LPAREN', r'\('),          # Paréntesis izquierdo
    ('RPAREN', r'\)'),          # Paréntesis derecho
]

# Creamos una expresión regular que reconocerá todos los tokens
lexer = re.compile('|'.join('(?P<%s>%s)' % pair for pair in tokens))

# Función principal para analizar una cadena de entrada
def lex(input_string):
    # Iteramos sobre cada coincidencia en la cadena de entrada
    for match in lexer.finditer(input_string):
        # Iteramos sobre los grupos nombrados en la coincidencia
        for name, value in match.groupdict().items():
            if value is not None:
                # Si el valor no es None, significa que hemos encontrado un token
                yield name, value

if __name__ == '__main__':
    # Cadena de entrada
    input_string = '3 + 4 * ( 2 - 1 )'
    print("Cadena de entrada:", input_string)
    # Llamamos a la función lex para analizar la cadena
    for token in lex(input_string):
        # Imprimimos cada token encontrado
        print(token)
