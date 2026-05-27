function seleccionarPersonajeJugador(){
    // Obtenemos los elementos de los radio buttons por su ID
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');

    // Evaluamos cuál está seleccionado
    if (inputZuko.checked) {
        alert('SELECCIONASTE A ZUKO 🔥');
    } else if (inputKatara.checked) {
        alert('SELECCIONASTE A KATARA 💧');
    } else if (inputAang.checked) {
        alert('SELECCIONASTE A AANG 🌪️');
    } else if (inputToph.checked) {
        alert('SELECCIONASTE A TOPH 🌎');
    } else {
        alert('Por favor, selecciona un personaje primero.');
    };
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
