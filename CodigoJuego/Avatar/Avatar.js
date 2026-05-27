function iniciarJuego(){
    let botonSeleccionar = document.getElementById("boton-personaje");
botonSeleccionar.addEventListener("click", seleccionarPersonaje);
}

function seleccionAleatioriaEnemigo() {
    let enemigoSeleccionado = document.getElementById("enemigo-seleccionado");
    let enemigos = ["Azula", "Ozai", "Combustion"];
    let enemigoAleatorio = enemigos[Math.floor(Math.random() * enemigos.length)];
    enemigoSeleccionado.innerHTML = enemigoAleatorio;
}

function seleccionarPersonaje() {
//MODIFICACION DE CODIGO PARA MEJOR LEGIBILIDAD
//Declaramos variables para cada personaje
    let inputAang = document.getElementById("aang");
    let inputKatara = document.getElementById("katara");
    let inputZuko = document.getElementById("zuko");
    let inputToph = document.getElementById("toph");
    let personajeSeleccionado = document.getElementById("personaje-seleccionado");
//Verificamos cuál personaje ha sido seleccionado y mostramos el mensaje correspondiente
    if (inputAang.checked) {
        personajeSeleccionado.innerHTML = "Aang";
        alert("Has seleccionado a Aang");
    } else if (inputKatara.checked) {
        personajeSeleccionado.innerHTML = "Katara";
        alert("Has seleccionado a Katara");
    } else if (inputZuko.checked) {
        personajeSeleccionado.innerHTML = "Zuko";
        alert("Has seleccionado a Zuko");
    } else if (inputToph.checked) {
        personajeSeleccionado.innerHTML = "Toph";
        alert("Has seleccionado a Toph");
    } else {
        alert("Por favor, selecciona un personaje");
    }

    if (inputAang.checked || inputKatara.checked || inputZuko.checked || inputToph.checked) {
        seleccionAleatioriaEnemigo();
    }

//    if (document.getElementById("aang").checked) {
//        alert("Has seleccionado a Aang");
//    } else if (document.getElementById("katara").checked) {
//        alert("Has seleccionado a Katara");
//    } else if (document.getElementById("zuko").checked) {
//        alert("Has seleccionado a Zuko");
//    } else if (document.getElementById("toph").checked) {
//        alert("Has seleccionado a Toph");
//    } else {
//        alert("Por favor, selecciona un personaje");
}



window.addEventListener("load", iniciarJuego);