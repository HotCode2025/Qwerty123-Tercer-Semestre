let ataqueJugador
let ataqueEnemigo

function iniciarJuego(){
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
    
    let botonPunio = document.getElementById('boton-punio')
    botonPunio.addEventListener('click', ataquePunio)

    let botonPatada = document.getElementById('boton-patada')
    botonPatada.addEventListener('click', ataquePatada)

    let botonBarrida = document.getElementById('boton-barrida')
    botonBarrida.addEventListener('click', ataqueBarrida)
}

function seleccionarPersonajeJugador(){
    // Obtenemos los elementos de los radio buttons por su ID
    let inputZuko = document.getElementById('zuko');
    let inputKatara = document.getElementById('katara');
    let inputAang = document.getElementById('aang');
    let inputToph = document.getElementById('toph');
    let personajeJugador = document.getElementById('personaje-jugador');

    // Evaluamos cuál está seleccionado
    if (inputZuko.checked) {
        personajeJugador.innerHTML = 'Zuko'
    } else if (inputKatara.checked) {
        personajeJugador.innerHTML = 'Katara'
    } else if (inputAang.checked) {
        personajeJugador.innerHTML = 'Aang'
    } else if (inputToph.checked) {
        personajeJugador.innerHTML = 'Toph'
    } else {
        alert('Por favor, selecciona un personaje primero.');
    };
    seleccionarPersonajeEnemigo()
}

function seleccionarPersonajeEnemigo(){
    let personajeAleatorio = aleatorio(1, 4) //Elige enemigo aleatoriamente
    let personajeEnemigo = document.getElementById('personaje-enemigo')

    // Comenzamos con la lógica
    if (personajeAleatorio == 1) {
        personajeEnemigo.innerHTML = 'Zuko'
    } else if (personajeAleatorio == 2) {
        personajeEnemigo.innerHTML = 'Katara'
    } else if (personajeAleatorio == 3) {
        personajeEnemigo.innerHTML = 'Aang'
    } else if (personajeAleatorio == 4) {
        personajeEnemigo.innerHTML = 'Toph'
    }
}

function ataquePunio(){
    ataqueJugador = 'Punio'
    ataqueAleatorioEnemigo()
}

function ataquePatada(){
    ataqueJugador = 'Patada'
    ataqueAleatorioEnemigo()
}

function ataqueBarrida(){
    ataqueJugador = 'Barrida'
    ataqueAleatorioEnemigo()
}

function ataqueAleatorioEnemigo(){
    let ataqueAleatorio = aleatorio(1, 3)
    // Comenzamos con la lógica
    if (ataqueAleatorio == 1) {
        ataqueEnemigo = 'Punio'
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = 'Patada'
    } else {
        ataqueEnemigo = 'Barrida'
    }
    combate()
}

function combate(){
    
    if (ataqueJugador == ataqueEnemigo) {
        crearMensaje("¡EMPATE! 🤝");
    } 
    
    else if (ataqueJugador == 'Punio' && ataqueEnemigo == 'Barrida') {
        crearMensaje("¡GANASTE! 👊 vence a 🧹");
    } else if (ataqueJugador == 'Patada' && ataqueEnemigo == 'Punio') {
        crearMensaje("¡GANASTE! 🦵 vence a 👊");
    } else if (ataqueJugador == 'Barrida' && ataqueEnemigo == 'Patada') {
        crearMensaje("¡GANASTE! 🧹 vence a 🦵")
    } else {
        crearMensaje("¡PERDISTE! 😢");
    }

}

function crearMensaje(resultado){
    let sectionMensaje = document.getElementById('mensaje')
    let parrafo = document.createElement('p')

    parrafo.innerHTML = 'Tu personaje atacó con '+ ataqueJugador +', el personaje del enemigo atacó con '+ ataqueEnemigo +' ' + resultado
    sectionMensaje.appendChild(parrafo)

}


function aleatorio(min, max){
    return Math.floor(Math.random() * (max - min + 1) + min)
}

window.addEventListener('load', iniciarJuego);
