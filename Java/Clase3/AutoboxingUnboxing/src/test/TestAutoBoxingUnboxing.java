package test;

public class TestAutoBoxingUnboxing {
    /**
     * Clases envolventes de tipos primitivos o wrapper classes
     * Tipos primitivos: byte, short, int, long, float, double, char, boolean
     * tipos envolventes: Byte, Short, Integer, Long, Float, Double, Character, Boolean
     * AutoBoxing: proceso de convertir un tipo primitivo a su clase envolvente
     * Unboxing: proceso de convertir un objeto de una clase envolvente a su tipo primitivo
     */

    public static void main(String[] args) {
        Integer entero = 10; // AutoBoxing: se convierte el int 10 a un Integer
        System.out.println("Valor del entero (Integer): " + entero);
        //declarar un primitivo a partir una clase envolvente,convierte
        //el tipo de variable primitivo a un tipo objeto
        System.out.println("entero = " + entero.toString());
        /*Esto se conoce como AutoBoxing, y es una característica de Java que facilita la conversión entre tipos primitivos 
        y sus clases envolventes. Al convertir un tipo primitivo a un tipo objeto,
        puedes acceder a métodos específicos de la clase envolvente,
        como toString(), compareTo(), etc., lo que te permite realizar operaciones adicionales con el valor.
        */

        int numero = entero; // Unboxing: se convierte el tipo objeto a un tipo primitivo,en este caso de Integer a int
        System.out.println("Valor del número (int): " + numero);
    }

}
