package domain;

public class Persona {
    private int idPersona;
    private static int contadorPersonas;

    static {//bloque estático (se ejecuta una sola vez al cargar la clase)
        System.out.println("Inicializando el bloque estático...");
        ++Persona.contadorPersonas;
        // idPersona = 10; // No se puede acceder a variables de instancia en un 
        // bloque estático
    }

    {// Bloque de instancia(se ejecuta antes del constructor y se ejecuta cada vez que se crea un nuevo objeto)
        System.out.println("Inicializando el bloque de instancia...");
        this.idPersona = Persona.contadorPersonas++;
    }

    public Persona() {
        System.out.println("Ejecutando el constructor...");
    }// El orden de ejecución es: bloque estático, bloque de instancia, constructor

    public int getIdPersona() {
        return idPersona;
    }
}
