let N;
let tablero;
let posiciones;

const tableroHTML = document.getElementById("tablero");
const resultadoHTML = document.getElementById("resultado");
const tituloHTML = document.getElementById("titulo");

function dibujarTablero() {
    tableroHTML.innerHTML = "";
    tableroHTML.style.gridTemplateColumns = "repeat(" + N + ", 60px)";

    for (let fila = 0; fila < N; fila++) {
        for (let columna = 0; columna < N; columna++) {
            const casilla = document.createElement("div");
            casilla.classList.add("casilla");

            if ((fila + columna) % 2 === 0) {
                casilla.classList.add("blanca");
            } else {
                casilla.classList.add("negra");
            }

            // Si hay una reina calculada en esa posición, la dibuja
            if (tablero[fila][columna] === 1) {
                if ((fila + columna) % 2 !== 0) {
                    casilla.innerHTML = "♕";
                } else {
                    casilla.innerHTML = "♛";
                }
            }
            tableroHTML.appendChild(casilla);
        }
    }
}

function esSeguro(fila, columna) {
    for (let i = 0; i < fila; i++) {
        if (posiciones[i] === columna) {
            return false;
        }
        if (Math.abs(i - fila) === Math.abs(posiciones[i] - columna)) {
            return false;
        }
    }
    return true;
}

function resolver(fila) {
    if (fila === N) {
        return true;
    }

    for (let columna = 0; columna < N; columna++) {
        if (esSeguro(fila, columna)) {
            tablero[fila][columna] = 1;
            posiciones[fila] = columna;

            if (resolver(fila + 1)) {
                return true;
            }

            tablero[fila][columna] = 0;
            posiciones[fila] = undefined;
        }
    }
    return false;
}

function iniciar() {
    N = parseInt(document.getElementById("valorN").value);

    if (N < 8) {
        alert("El valor mínimo de N debe ser 8");
        return;
    }

    tituloHTML.innerHTML = "✨ Desafío Resuelto: " + N + " Reinas";
    resultadoHTML.style.display = "inline-block";
    resultadoHTML.innerHTML = "Calculando solución...";

    tablero = Array.from({ length: N }, () => Array(N).fill(0));
    posiciones = [];

    const solucion = resolver(0);

    if (solucion) {
        dibujarTablero();
        resultadoHTML.innerHTML = "¡Solución encontrada!<br>Arreglo de columnas por fila: <strong>[ " + posiciones.join(" , ") + " ]</strong>";
    } else {
        tableroHTML.innerHTML = "";
        resultadoHTML.innerHTML = "No se encontró una solución para este valor de N.";
    }
}

// Nueva función que prepara el tablero vacío al cargar el sitio
function prepararPantallaInicial() {
    N = parseInt(document.getElementById("valorN").value) || 8;
    tituloHTML.innerHTML = "👑 El Desafío de las " + N + " Reinas";
    
    // Genera una matriz vacía (llena de ceros) temporal para dibujar el tablero inicial
    tablero = Array.from({ length: N }, () => Array(N).fill(0));
    dibujarTablero();
    
    resultadoHTML.innerHTML = "";
    resultadoHTML.style.display = "none";
}

prepararPantallaInicial();