# Practica_152_Analisis_Sintactico_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Analisis_Sintactico

# Definimos la lista de tokens y su índice actual
tokens = []
current_token_index = 0

# Función para obtener el siguiente token
def get_next_token():
    global current_token_index
    if current_token_index < len(tokens):
        token = tokens[current_token_index]
        current_token_index += 1
        return token
    return None

# Funciones para el análisis sintáctico de cada tipo de expresión
def factor():
    global current_token_index
    token = get_next_token()
    if token[0] == 'NUMBER':
        return int(token[1])
    elif token[0] == 'LPAREN':
        result = expression()
        if get_next_token()[0] != 'RPAREN':
            raise SyntaxError("Expected ')' after expression")
        return result
    else:
        raise SyntaxError("Invalid token")

def term():
    result = factor()
    while True:
        token = get_next_token()
        if token and token[0] in ('TIMES', 'DIVIDE'):
            factor_value = factor()
            if token[0] == 'TIMES':
                result *= factor_value
            else:
                result /= factor_value
        else:
            current_token_index -= 1
            break
    return result

def expression():
    result = term()
    while True:
        token = get_next_token()
        if token and token[0] in ('PLUS', 'MINUS'):
            term_value = term()
            if token[0] == 'PLUS':
                result += term_value
            else:
                result -= term_value
        else:
            current_token_index -= 1
            break
    return result

# Función principal para analizar una cadena de entrada
def parse(input_tokens):
    global tokens, current_token_index
    # Reiniciamos el índice de tokens
    tokens = input_tokens
    current_token_index = 0
    # Llamamos a la función de análisis sintáctico inicial
    return expression()

if __name__ == '__main__':
    # Definimos una cadena de tokens de ejemplo
    input_tokens = [
        ('NUMBER', '3'),
        ('PLUS', '+'),
        ('NUMBER', '4'),
        ('TIMES', '*'),
        ('LPAREN', '('),
        ('NUMBER', '2'),
        ('MINUS', '-'),
        ('NUMBER', '1'),
        ('RPAREN', ')')
    ]
    print("Cadena de tokens de entrada:", input_tokens)
    # Llamamos a la función de análisis sintáctico para analizar la cadena de tokens
    result = parse(input_tokens)
    print("Resultado del análisis sintáctico:", result)
