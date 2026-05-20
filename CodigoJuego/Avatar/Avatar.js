function seleccionarPersonaje() {
    if (document.getElementById("aang").checked) {
        alert("Has seleccionado a Aang");
    } else if (document.getElementById("katara").checked) {
        alert("Has seleccionado a Katara");
    } else if (document.getElementById("zuko").checked) {
        alert("Has seleccionado a Zuko");
    } else if (document.getElementById("toph").checked) {
        alert("Has seleccionado a Toph");
    } else {
        alert("Por favor, selecciona un personaje");
    }
}

let botonSeleccionar = document.getElementById("boton-personaje");
botonSeleccionar.addEventListener("click", seleccionarPersonaje);