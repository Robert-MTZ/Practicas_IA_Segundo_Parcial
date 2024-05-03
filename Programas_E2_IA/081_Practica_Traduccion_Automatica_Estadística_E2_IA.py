# Practica_081_Traduccion_Automatica_Estadística_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_Traduccion_Automatica_Estadística

from googletrans import Translator

def translate_text(text, target_language='en'):
    """
    Función para traducir texto a otro idioma utilizando Google Translate.

    Args:
    - text: El texto que se va a traducir.
    - target_language: El idioma al que se va a traducir el texto. Por defecto, 'en' (inglés).

    Returns:
    - translated_text: El texto traducido.
    """
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

# Texto de ejemplo para traducir
texto_a_traducir = "Hola, ¿cómo estás?"

# Traducción del texto
texto_traducido = translate_text(texto_a_traducir)

# Imprimir el texto original y el texto traducido
print("Texto original:", texto_a_traducir)
print("Texto traducido:", texto_traducido)
