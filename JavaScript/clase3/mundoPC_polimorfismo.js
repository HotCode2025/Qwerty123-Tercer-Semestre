// Tarea Clase 3


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
        this.computadoras = [];         //arreglo vacio 
    }

    agregarComputadora(computadora) {
        this.computadoras.push(computadora);        //agrego los objetos
    }

    mostrarOrden() {
        console.log(`Orden: ${this.idOrden}`); //muestro id o num de la orden por consola
        this.computadoras.forEach(comp => {     // recorro cada elemento del array con forEach donde estan las computadoras
            console.log(comp.toString());       // cada computadora individual (comp) la convierto en texto e imprimo en consola
        });
    }
}

// Ejemplo 1 basico 
let monitor1 = new Monitor("Samsung", "24 pulgadas");
let teclado1 = new Teclado("USB", "Logitech");
let raton1 = new Raton("USB", "HP");

let computadora1 = new Computadora("PC Gamer", monitor1, teclado1, raton1);

let orden1 = new Orden();
orden1.agregarComputadora(computadora1);
orden1.mostrarOrden();

//Ejemplo 2 varias computadoras en misma orden

let monitor2 = new Monitor("LG", "27 pulgadas");
let teclado2 = new Teclado("Bluetooth", "Redragon");
let raton2 = new Raton("USB", "Logitech");

let computadora2 = new Computadora("PC Oficina", monitor2, teclado2, raton2);

let orden2 = new Orden();
orden2.agregarComputadora(computadora2);
orden2.agregarComputadora(computadora1); // reutilizo objetos de la anterior

orden2.mostrarOrden();

// Ejemplo3 Ordenes independientes o vacias donde no mezclan datos y con id propias

let orden3 = new Orden();
let orden4 = new Orden();

orden3.agregarComputadora(computadora1);
orden4.agregarComputadora(computadora2);

orden3.mostrarOrden();
orden4.mostrarOrden();

// ================= POLIMORFISMO =================

// En este caso aplicamos el concepto de polimorfismo utilizando el método toString().
// Todas las clases (Raton, Teclado, Monitor y Computadora) implementan este método,
// pero cada una lo define de manera diferente.
//
// Creamos una función llamada "probarPolimorfismo" que recibe un arreglo de objetos
// y ejecuta el método toString() sin importar el tipo específico de cada objeto.
// Esto demuestra el polimorfismo, ya que distintos objetos responden de forma diferente
// al mismo método.

function probarPolimorfismo(objetos) {
    objetos.forEach(obj => {
        console.log(obj.toString());
    });
}

// Ejemplo de uso:
console.log("=== PRUEBA DE POLIMORFISMO ===");
probarPolimorfismo([monitor1, teclado1, raton1, computadora1]);


// ================= EXPLICACIÓN CLASE ORDEN =================

// La clase Orden ya aplica polimorfismo en su método mostrarOrden().
// Esto ocurre cuando recorre el arreglo de computadoras y llama al método toString()
// de cada objeto.
//
// this.computadoras.forEach(comp => {
//     console.log(comp.toString());
// });
//
// En este caso, no importa la composición interna de cada computadora,
// ya que todas responden al mismo método. Esto es un ejemplo claro de polimorfismo,
// donde se utiliza una misma interfaz (toString) para operar con diferentes objetos.