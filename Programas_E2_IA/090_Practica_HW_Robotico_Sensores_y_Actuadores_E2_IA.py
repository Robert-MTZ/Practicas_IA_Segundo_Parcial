# Practica_090_HW_Robotico_Sensores_y_Actuadores_E2_IA
# Roberto_Martinez_Bailon_21310216_6E
# Ingenieria_en_Mecatronica

# Programa_HW_Robotico_Sensores_y_Actuadores

import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
TRIGGER_PIN = 18
ECHO_PIN = 24

# Configuramos el modo de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def medir_distancia():
    # Generamos un pulso corto en el pin de activación del sensor
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, False)
    
    # Esperamos a que el pin de eco se active
    inicio_tiempo = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        inicio_tiempo = time.time()
    
    # Esperamos a que el pin de eco se desactive
    fin_tiempo = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        fin_tiempo = time.time()
    
    # Calculamos la duración del pulso de eco
    duracion = fin_tiempo - inicio_tiempo
    
    # Calculamos la distancia utilizando la fórmula de velocidad * tiempo / 2
    distancia = (34300 * duracion) / 2
    
    return distancia

try:
    while True:
        # Medimos la distancia
        distancia = medir_distancia()
        print("Distancia:", distancia, "cm")
        time.sleep(1)  # Esperamos 1 segundo entre cada medición

except KeyboardInterrupt:
    # En caso de interrupción del teclado, limpiamos los pines GPIO y salimos del programa
    GPIO.cleanup()
