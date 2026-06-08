const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Estado global de las torres
let torres = {
    'A': [],
    'B': [],
    'C': []
};

let movimientos = []; // Lista para guardar los pasos del algoritmo
let totalDiscos = 0;

// --- ALGORITMO RECURSIVO (Solo calcula, no dibuja todavía) ---
function calcularHanoi(n, origen, destino, auxiliar) {
    if (n === 1) {
        movimientos.push({ origen, destino });
        return;
    }
    calcularHanoi(n - 1, origen, auxiliar, destino);
    movimientos.push({ origen, destino });
    calcularHanoi(n - 1, auxiliar, destino, origen);
}

// --- FUNCIÓN PARA DIBUJAR LAS TORRES EN LA CONSOLA ---
function dibujarTorres() {
    // Limpia la pantalla de la terminal para el efecto de animación
    console.clear();
    console.log(`🎮 Animación de Torres de Hanoi - ${totalDiscos} discos\n`);

    // Dibujamos de arriba hacia abajo (desde la altura máxima hasta la base)
    for (let i = totalDiscos - 1; i >= 0; i--) {
        let linea = "";
        
        // Renderizar cada una de las 3 torres (A, B, C)
        ['A', 'B', 'C'].forEach(torre => {
            const disco = torres[torre][i];
            if (disco) {
                // Si hay un disco, dibuja bloques "█" proporcionales a su tamaño
                const bloques = "█".repeat(disco * 2);
                const espacio = " ".repeat(totalDiscos - disco);
                linea += espacio + bloques + espacio + "\t";
            } else {
                // Si no hay disco, dibuja el poste central "|"
                const espacio = " ".repeat(totalDiscos);
                linea += espacio + "|" + espacio + "\t";
            }
        });
        console.log(linea);
    }

    // Dibujar la base y las etiquetas
    const baseTorre = "═".repeat(totalDiscos * 2 + 1);
    console.log(`${baseTorre}\t${baseTorre}\t${baseTorre}`);
    console.log(" ".repeat(totalDiscos) + "Poste A" + " ".repeat(totalDiscos) + "\t" +
                " ".repeat(totalDiscos) + "Poste B" + " ".repeat(totalDiscos) + "\t" +
                " ".repeat(totalDiscos) + "Poste C");
    console.log("\n");
}

// --- ANIMADOR DE MOVIMIENTOS ---
function animar(index) {
    // Si ya no hay más movimientos, terminamos
    if (index >= movimientos.length) {
        console.log(`✅ ¡Animación terminada con éxito en ${movimientos.length} movimientos!`);
        rl.close();
        return;
    }

    // Obtener el movimiento actual
    const { origen, destino } = movimientos[index];
    
    // Sacar el disco del poste origen y ponerlo en el destino
    const discoMoviendose = torres[origen].pop();
    torres[destino].push(discoMoviendose);

    // Redibujar la pantalla
    dibujarTorres();
    console.log(`Progreso: Movimiento ${index + 1} de ${movimientos.length}`);
    console.log(`Moviendo disco desde ${origen} hasta ${destino}...`);

    // Esperar 800 milisegundos antes de hacer el siguiente movimiento
    setTimeout(() => {
        animar(index + 1);
    }, 800);
}

// --- FUNCIÓN PRINCIPAL ---
function iniciarJuego() {
    rl.question('Ingresa la cantidad de discos (entre 3 y 7): ', (input) => {
        const discos = parseInt(input);

        if (isNaN(discos) || discos < 3 || discos > 7) {
            console.log('❌ Error: Por favor, ingresa un número válido entre 3 y 7.\n');
            iniciarJuego();
        } else {
            totalDiscos = discos;
            
            // Inicializar el poste A con los discos (los más grandes abajo)
            for (let i = discos; i >= 1; i--) {
                torres['A'].push(i);
            }

            // Calcular todos los movimientos recursivamente
            calcularHanoi(discos, 'A', 'C', 'B');

            // Mostrar el estado inicial antes de empezar a mover
            dibujarTorres();
            console.log("Presiona cualquier tecla en la terminal para iniciar la animación...");
            
            // Esperar 2 segundos y arrancar la animación de forma automática
            setTimeout(() => {
                animar(0);
            }, 2000);
        }
    });
}

iniciarJuego();