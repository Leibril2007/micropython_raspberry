from machine import Pin
from enviar_datos import enviar_datos_fb
import time

def luz_roja(pin, tiempo):
    led1 = Pin(pin, Pin.OUT)
    dato = 1
    dato2 = 0
    dato3 = 0
    enviar_datos_fb(dato, dato2, dato3)
    
    led1.value(1)       # Enciende el LED
    print("corriendo")  # Muestra mensaje en consola
    time.sleep(tiempo)     # Espera 0.5 segundos
    led1.value(0)       # Apaga el LED
    time.sleep(tiempo)
    

def luz_amarillo(pin, tiempo):
    led2 = Pin(pin, Pin.OUT)
    dato = 0
    dato2 = 2
    dato3 = 0
    enviar_datos_fb(dato, dato2, dato3)
    
    led2.value(1)       # Enciende el LED
    print("corriendo2")  # Muestra mensaje en consolaa
    time.sleep(tiempo)     # Espera 0.5 segundos
    led2.value(0)       # Apaga el LED
    time.sleep(tiempo)

def luz_verde(pin, tiempo):
    led3 = Pin(pin, Pin.OUT)
    dato = 0
    dato2 = 0
    dato3 = 3
    enviar_datos_fb(dato, dato2, dato3)
    
    led3.value(1)       # Enciende el LED
    print("corriendo2")  # Muestra mensaje en consola
    time.sleep(tiempo)     # Espera 0.5 segundos
    led3.value(0)       # Apaga el LED
    time.sleep(tiempo)
    