package Test;

import domain.Persona;
public class test_bloque {
    public static void main(String[] args) {
        System.out.println("Creando la persona 1...");
        Persona persona1 = new Persona();
        System.out.println("ID Persona 1: " + persona1.getIdPersona());

        System.out.println("\nCreando la persona 2...");
        Persona persona2 = new Persona();
        System.out.println("ID Persona 2: " + persona2.getIdPersona());
    }
}
