// Tarea 6 Abril JavaScript CLASE 01 PROYECTO MundoPC Programacion III Lunes


// Clase DispositivoEntrada
class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }
}


// Clase Raton (mouse)
class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this.idRaton = ++Raton.contadorRatones;
    }

    toString() {
        return `Raton [id=${this.idRaton}, tipo=${this.tipoEntrada}, marca=${this.marca}]`;
    }
}

// Clase Teclado
class Teclado extends DispositivoEntrada {
    static contadorTeclados = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this.idTeclado = ++Teclado.contadorTeclados;
    }

    toString() {
        return `Teclado [id=${this.idTeclado}, tipo=${this.tipoEntrada}, marca=${this.marca}]`;
    }
}

// Clase Monitor
class Monitor {
    static contadorMonitores = 0;

    constructor(marca, tamanio) {
        this.idMonitor = ++Monitor.contadorMonitores;
        this.marca = marca;
        this.tamanio = tamanio;
    }

    getIdMonitor() {
        return this.idMonitor;
    }

    toString() {
        return `Monitor [id=${this.idMonitor}, marca=${this.marca}, tamaño=${this.tamanio}]`;
    }
}

// Clase Computadora
class Computadora {
    static contadorComputadoras = 0;

    constructor(nombre, monitor, teclado, raton) {
        this.idComputadora = ++Computadora.contadorComputadoras;
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }

    toString() {
        return `
Computadora [id=${this.idComputadora}, nombre=${this.nombre}]
  ${this.monitor.toString()}
  ${this.teclado.toString()}
  ${this.raton.toString()}
        `;
    }
}

// Clase Orden
class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadoras = [];
    }

    agregarComputadora(computadora) {
        this.computadoras.push(computadora);
    }

    mostrarOrden() {
        console.log(`Orden: ${this.idOrden}`);
        this.computadoras.forEach(comp => {
            console.log(comp.toString());
        });
    }
}

// Ejemplo
let monitor1 = new Monitor("GigaByte", "27 pulgadas");
let teclado1 = new Teclado("USB", "Logitech");
let raton1 = new Raton("USB", "Razer");

let computadora1 = new Computadora("PC Gamer", monitor1, teclado1, raton1);

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.mostrarOrden();