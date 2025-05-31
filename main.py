from config_red import conectar_wifi
import luces_semaforo 
import urequests


REDES = [
    # nombre de la red, su contraseña
    {'ssid': 'E-Learning-SCL-2025', 'password': 'Educ@cion.2024'},
    {'ssid': 'POCO X3 Pro', 'password': 'Shaday88'}
]

if conectar_wifi(REDES):
    print("Conectado a Wifi - Ejecutando programa principal")
    luces_semaforo.luz_verde()
else:
    print("Modo offline - Funcionalidades limitadas")
    


def enviar_datos():
    try:
        json = config_red.tiempo_rojo
        response = urequests.put('https://semaforo-cd648-default-rtdb.firebaseio.com/rojo.json')
        response.close()

    except Exception as e:
        print('Error al enviar datos:', e)