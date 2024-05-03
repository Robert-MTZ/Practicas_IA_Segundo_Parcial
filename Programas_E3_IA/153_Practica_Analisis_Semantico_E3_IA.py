# Practica_153_Analisis_Semantico_E3_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Analisis_Semantico

# Definimos la clase para los nodos del árbol de sintaxis abstracta (AST)
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

# Definimos la función recursiva para construir el AST
def build_ast(tokens):
    root = Node('expression')
    current_node = root

    for token in tokens:
        if token[0] in ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE'):
            current_node.children.append(Node(token))
        elif token[0] == 'LPAREN':
            new_node = Node(token)
            current_node.children.append(new_node)
            current_node = new_node
        elif token[0] == 'RPAREN':
            current_node = current_node.parent
        else:
            raise ValueError("Invalid token")
    
    return root

# Definimos la función para realizar el análisis semántico del AST
def semantic_analysis(node):
    if node.value[0] in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE'):
        for child in node.children:
            semantic_analysis(child)
    elif node.value[0] == 'NUMBER':
        if not node.value[1].isdigit():
            raise ValueError("Invalid number")
    else:
        raise ValueError("Invalid node")

if __name__ == '__main__':
    # Definimos una lista de tokens de ejemplo
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
    # Construimos el AST a partir de los tokens de entrada
    ast_root = build_ast(input_tokens)
    print("AST construido:")
    print(ast_root)
    # Realizamos el análisis semántico del AST
    try:
        semantic_analysis(ast_root)
        print("Análisis semántico completado sin errores.")
    except ValueError as e:
        print("Error durante el análisis semántico:", e)
 
