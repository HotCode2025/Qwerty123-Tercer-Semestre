let N;
// Representamos las varillas como Pilas (arrays) de JS usando pop() y push()
let varillas = {
    'A': [],
    'B': [],
    'C': []
};
let listaMovimientos = [];
let historialTexto = [];

// Paleta de colores atractiva para diferenciar los diámetros de los discos
const coloresDiscos = ["#ef4444", "#3b82f6", "#10b981", "#f59e0b", "#8b5cf6", "#ec4899", "#14b8a6"];

const resultadoHTML = document.getElementById("resultado");
const tituloHTML = document.getElementById("titulo");

// Dibuja los discos en sus respectivas varillas respetando el orden de la pila
function dibujarHanoi() {
    ['A', 'B', 'C'].forEach(id => {
        const area = document.querySelector("#varilla-" + id + " .area-discos");
        area.innerHTML = ""; // Limpiamos la varilla para redibujarla

        varillas[id].forEach(diametroDisco => {
            const elementDisco = document.createElement("div");
            elementDisco.classList.add("disco");
            
            // Cálculo matemático para que el ancho sea proporcional a su tamaño
            let anchoPorcentaje = 30 + (diametroDisco * (70 / N));
            elementDisco.style.width = anchoPorcentaje + "%";
            elementDisco.style.backgroundColor = coloresDiscos[diametroDisco - 1] || "#64748b";

            area.appendChild(elementDisco);
        });
    });
}

// Algoritmo puramente Recursivo de las Torres de Hanoi
function calcularHanoi(discosActuales, origen, destino, auxiliar) {
    // Caso base: si solo queda un disco, se mueve directamente del origen al destino
    if (discosActuales === 1) {
        listaMovimientos.push({ desde: origen, hacia: destino });
        return;
    }

    // Paso 1: Mover los N-1 discos superiores al poste auxiliar usando el destino como apoyo
    calcularHanoi(discosActuales - 1, origen, auxiliar, destino);

    // Paso 2: Mover el disco grande restante al poste destino
    listaMovimientos.push({ desde: origen, hacia: destino });

    // Paso 3: Mover los N-1 discos del poste auxiliar al destino usando el origen como apoyo
    calcularHanoi(discosActuales - 1, auxiliar, destino, origen);
}

function esperar(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Ejecuta la reproducción visual controlada por tiempos
async function animarSolucion() {
    historialTexto = [];
    
    for (let i = 0; i < listaMovimientos.length; i++) {
        let mov = listaMovimientos[i];
        
        // Hacemos el movimiento físico en las Pilas de datos
        let discoRemovido = varillas[mov.desde].pop();
        varillas[mov.hacia].push(discoRemovido);
        
        // Registramos la acción en el texto inferior
        historialTexto.push("Disco " + discoRemovido + " de " + mov.desde + " → " + mov.hacia);
        resultadoHTML.innerHTML = "Movimiento " + (i + 1) + " de " + listaMovimientos.length + ":<br><strong>" + historialTexto.join(" | ") + "</strong>";
        
        // Redibujamos la pantalla
        dibujarHanoi();
        
        // Velocidad adaptativa: si son muchos discos, acelera un poquito
        let velocidad = N > 5 ? 400 : 700;
        await esperar(velocidad);
    }

    resultadoHTML.innerHTML = "🎉 ¡Acertijo Resuelto!<br>Se completó la mudanza de los " + N + " discos en <strong>" + listaMovimientos.length + " movimientos</strong> perfectos.<br><br>Secuencia ejecutada:<br><strong>" + historialTexto.join(" → ") + "</strong>";
}

function iniciar() {
    N = parseInt(document.getElementById("valorN").value);

    if (N < 3 || N > 7) {
        alert("Por favor, selecciona una cantidad de discos entre 3 y 7 para apreciar la animación fluidamente.");
        return;
    }

    tituloHTML.innerHTML = "✨ Solución en Curso: " + N + " Discos";
    resultadoHTML.innerHTML = "Calculando la estrategia recursiva óptima...";

    // Reiniciamos las estructuras de las varillas
    varillas = { 'A': [], 'B': [], 'C': [] };
    listaMovimientos = [];

    // Llenamos la varilla de Origen (A) colocando los discos más grandes primero (abajo de la pila)
    for (let i = N; i >= 1; i--) {
        varillas['A'].push(i);
    }

    // Ejecutamos el motor recursivo
    calcularHanoi(N, 'A', 'C', 'B');

    resultadoHTML.innerHTML = "¡Estrategia calculada! Iniciando mudanza automatizada...";
    animarSolucion();
}

function prepararPantallaInicial() {
    N = parseInt(document.getElementById("valorN").value) || 4;
    tituloHTML.innerHTML = "⛩️ Las Torres de Hanoi";
    
    varillas = { 'A': [], 'B': [], 'C': [] };
    listaMovimientos = [];
    
    for (let i = N; i >= 1; i--) {
        varillas['A'].push(i);
    }
    
    dibujarHanoi();
    resultadoHTML.innerHTML = "";
}

// Listener para que el escenario cambie de tamaño inmediatamente al tocar el número
document.getElementById("valorN").addEventListener("change", prepararPantallaInicial);

prepararPantallaInicial();