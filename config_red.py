import network
import time
from machine import Pin

def conectar_wifi(lista_redes):
    wlan = network.WLAN(network.STA_IF) #se crea una instancia con el adaptador fisico
    wlan.active(True)
    
    # Desconectar la red si es que está conectada.
    if wlan.isconnected():
        wlan.disconnect()
        
    for red in lista_redes:
        #prin("\nIntentando conectar a: {red['ssid']}...")
        wlan.connect(red['ssid'], red['password'])
        
        timeout = 0
        while not wlan.isconnected() and timeout < 10:
            print(".", end = "")
            time.sleep(1)
            timeout += 1
            
            return True
    
tiempo_rojo = 20
tiempo_amarillo = 1
tiempo_verde = 0
        