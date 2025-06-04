
function createHeader() {
  
  const header = document.createElement('header');
  header.className = 'header';

  
  const logo = document.createElement('div');
  logo.className = 'logo';
  logo.textContent = '👑'; 


  
  const gameTitle = document.createElement('h1');
  gameTitle.className = 'game-title';
  gameTitle.textContent = 'Raspberry Pi Pico';

  
  const buttonsDiv = document.createElement('div');
  buttonsDiv.className = 'buttons';

  
  const buttonInicio = document.createElement('button');
  buttonInicio.textContent = 'Inicio';
  buttonInicio.onclick = () => handleInicio();

  const buttonOpciones = document.createElement('button');
  buttonOpciones.textContent = 'Opciones';
  buttonOpciones.onclick = () => handleOpciones();

  const buttonSalir = document.createElement('button');
  buttonSalir.textContent = 'Salir';
  buttonSalir.onclick = () => handleSalir();

  
  buttonsDiv.appendChild(buttonInicio);
  buttonsDiv.appendChild(buttonOpciones);
  buttonsDiv.appendChild(buttonSalir);

  
  header.appendChild(logo);
  header.appendChild(gameTitle);
  header.appendChild(buttonsDiv);


  document.body.appendChild(header);
}


function handleInicio() {
  alert("Has hecho clic en Inicio");
}

function handleOpciones() {
  alert("Has hecho clic en Opciones");
}

function handleSalir() {
  alert("Has hecho clic en Salir");
}


window.onload = createHeader;

  