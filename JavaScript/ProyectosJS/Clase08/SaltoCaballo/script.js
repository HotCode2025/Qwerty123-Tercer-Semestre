const N = 8;
let tablero;
let rutaGanadora = []; 
let coordenadasMostradas = []; 

const despX = [2, 1, -1, -2, -2, -1, 1, 2];
const despY = [1, 2, 2, 1, -1, -2, -2, -1];

const tableroHTML = document.getElementById("tablero");
const resultadoHTML = document.getElementById("resultado");
const tituloHTML = document.getElementById("titulo");

function dibujarPasoAnimacion(currX, currY) {
    tableroHTML.innerHTML = "";
    tableroHTML.style.gridTemplateColumns = "repeat(" + N + ", 55px)";

    for (let x = 0; x < N; x++) {
        for (let y = 0; y < N; y++) {
            const casilla = document.createElement("div");
            casilla.classList.add("casilla");

            if ((x + y) % 2 === 0) {
                casilla.classList.add("blanca");
            } else {
                casilla.classList.add("negra");
            }

            if (x === currX && y === currY) {
                casilla.classList.add("caballo-actual");
                casilla.innerHTML = "♞";
            } 
            else if (tablero[x][y] > 0) {
                casilla.classList.add("rastro");
                casilla.innerHTML = "✕";
            }

            tableroHTML.appendChild(casilla);
        }
    }
}

function dibujarTableroVacio() {
    tableroHTML.innerHTML = "";
    tableroHTML.style.gridTemplateColumns = "repeat(" + N + ", 55px)";

    for (let x = 0; x < N; x++) {
        for (let y = 0; y < N; y++) {
            const casilla = document.createElement("div");
            casilla.classList.add("casilla");

            if ((x + y) % 2 === 0) {
                casilla.classList.add("blanca");
            } else {
                casilla.classList.add("negra");
            }
            tableroHTML.appendChild(casilla);
        }
    }
}

function esValido(x, y) {
    return (x >= 0 && x < N && y >= 0 && y < N && tablero[x][y] === 0);
}

function obtenerGrado(x, y) {
    let conteo = 0;
    for (let i = 0; i < 8; i++) {
        if (esValido(x + despX[i], y + despY[i])) {
            conteo++;
        }
    }
    return conteo;
}

function resolverTour(x, y, paso) {
    if (paso === N * N + 1) {
        return true;
    }

    let candidatos = [];
    for (let i = 0; i < 8; i++) {
        let sigX = x + despX[i];
        let sigY = y + despY[i];

        if (esValido(sigX, sigY)) {
            let grado = obtenerGrado(sigX, sigY);
            candidatos.push({ x: sigX, y: sigY, grado: grado });
        }
    }

    if (candidatos.length === 0) {
        return false;
    }

    candidatos.sort((a, b) => a.grado - b.grado);

    for (let candidato of candidatos) {
        let nxtX = candidato.x;
        let nxtY = candidato.y;

        tablero[nxtX][nxtY] = paso;
        rutaGanadora.push({ x: nxtX, y: nxtY, paso: paso });

        if (resolverTour(nxtX, nxtY, paso + 1)) {
            return true;
        }

        tablero[nxtX][nxtY] = 0;
        rutaGanadora.pop();
    }

    return false;
}

function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function reproducirCamino() {
    tablero = Array.from({ length: N }, () => Array(N).fill(0));
    
    tablero[0][0] = 1;
    coordenadasMostradas = ["[0,0]"]; 
    
    resultadoHTML.innerHTML = "Historial de saltos [x, y]:<br><strong>" + coordenadasMostradas.join(" → ") + "</strong>";
    dibujarPasoAnimacion(0, 0);
    await esperar(300);

    for (let i = 0; i < rutaGanadora.length; i++) {
        let coordenada = rutaGanadora[i];
        
        tablero[coordenada.x][coordenada.y] = coordenada.paso;
        coordenadasMostradas.push("[" + coordenada.x + "," + coordenada.y + "]");
        
        resultadoHTML.innerHTML = "Historial de saltos [x, y]:<br><strong>" + coordenadasMostradas.join(" → ") + "</strong>";
        dibujarPasoAnimacion(coordenada.x, coordenada.y);
        
        await esperar(200); 
    }

    resultadoHTML.innerHTML = "¡Desafío completado!<br>El caballo recorrió las 64 casillas con éxito.<br><br>Coordenadas utilizadas en orden:<br><strong>" + coordenadasMostradas.join(" → ") + "</strong>";
}

function iniciar() {
    tituloHTML.innerHTML = "✨ El Camino Animado del Caballo";
    resultadoHTML.style.display = "inline-block";
    resultadoHTML.innerHTML = "Buscando la solución óptima...";

    tablero = Array.from({ length: N }, () => Array(N).fill(0));
    rutaGanadora = [];

    tablero[0][0] = 1;

    const solucionado = resolverTour(0, 0, 2);

    if (solucionado) {
        resultadoHTML.innerHTML = "¡Ruta encontrada! Iniciando recorrido...";
        reproducirCamino();
    } else {
        dibujarTableroVacio();
        resultadoHTML.innerHTML = "No se pudo calcular un recorrido completo.";
    }
}

function prepararPantallaInicial() {
    tituloHTML.innerHTML = "♞ El Desafío del Salto del Caballo";
    tablero = Array.from({ length: N }, () => Array(N).fill(0));
    dibujarTableroVacio();
    resultadoHTML.innerHTML = "";
    resultadoHTML.style.display = "none";
}

prepararPantallaInicial();