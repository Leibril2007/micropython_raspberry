const luces = document.querySelectorAll('.luz');

async function obtenerDatosDeAPI() {
  try {
    const response = await fetch("https://semaforo-cd648-default-rtdb.firebaseio.com/semaforo.json");
    const data = await response.json();
    console.log(data);
    return data;
  } catch(error) {
    console.error("Error al obtener datos:", error);
    return null;
  }
}

function actualizarSemaforo(rojo, amarillo, verde) {
  
  luces.forEach(luz => luz.classList.remove('encendido'));

  if (rojo == 1 ) {
      luces[0].classList.add('encendido'); 
  } else if ( amarillo == 2) {
      luces[1].classList.add('encendido');
  } else if (verde == 3) {
      luces[2].classList.add('encendido'); 
  }

}

async function actualizarLuces() {
  const data = await obtenerDatosDeAPI();
  
  if (data && typeof data === "object") {
    const rojo = parseInt(data.rojo);
    const amarillo = parseInt(data.amarillo);
    const verde = parseInt(data.verde);

    actualizarSemaforo(rojo, amarillo, verde);
  } else {
    console.warn("Datos no válidos recibidos de Firebase:", data);
  }
}

setInterval(actualizarLuces, 200)

actualizarLuces();