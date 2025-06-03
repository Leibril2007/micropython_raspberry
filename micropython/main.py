from config_red import conectar_wifi
import config_red
import luces_semaforo 


REDES = [
    # nombre de la red, su contraseña
    {'ssid': 'POCO X3 Pro', 'password': 'Shaday88'},
    {'ssid': 'E-Learning-SCL-2025', 'password': 'Educ@cion.2024'},
    
]



if conectar_wifi(REDES):
    print("Conectado a Wifi - Ejecutando programa principal")
    
    ledRojo = 15
    ledAmar = 14
    ledVerde = 13
    
    while True:
        luces_semaforo.luz_roja(ledRojo, config_red.tiempo_rojo)
        luces_semaforo.luz_amarillo(ledAmar, config_red.tiempo_amarillo)
        luces_semaforo.luz_verde(ledVerde, config_red.tiempo_verde)
    
else:
    print("Modo offline - Funcionalidades limitadas")