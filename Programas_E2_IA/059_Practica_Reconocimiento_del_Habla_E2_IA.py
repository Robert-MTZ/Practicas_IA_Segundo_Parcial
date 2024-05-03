# Practica_059_Reconocimiento_del_Habla_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria en Mecatronica

# Programa_Reconocimiento_del_Habla

import speech_recognition as sr  # Importamos la biblioteca SpeechRecognition

# Creamos un objeto recognizer
recognizer = sr.Recognizer()

# Definimos la fuente de audio como el micrófono del sistema
fuente_audio = sr.Microphone()

# Definimos una función para reconocer el habla
def reconocer_habla():
    with fuente_audio as source:  # Abrimos la fuente de audio
        print("Escuchando...")  # Imprimimos un mensaje para indicar que estamos escuchando
        audio = recognizer.listen(source)  # Escuchamos el audio desde el micrófono
    try:
        print("Reconociendo...")  # Imprimimos un mensaje para indicar que estamos reconociendo el habla
        texto = recognizer.recognize_google(audio, language='es-ES')  # Reconocemos el habla utilizando Google Speech Recognition
        return texto  # Retornamos el texto reconocido
    except sr.UnknownValueError:  # Manejamos la excepción si no se puede entender el habla
        print("No se pudo entender el habla")
        return ""  # Retornamos una cadena vacía
    except sr.RequestError as e:  # Manejamos la excepción si hay un error en el servicio de reconocimiento
        print(f"Error al solicitar el servicio de reconocimiento; {e}")
        return ""  # Retornamos una cadena vacía

# Llamamos a la función para reconocer el habla
texto_reconocido = reconocer_habla()

# Imprimimos el texto reconocido
print("Texto reconocido:", texto_reconocido)

