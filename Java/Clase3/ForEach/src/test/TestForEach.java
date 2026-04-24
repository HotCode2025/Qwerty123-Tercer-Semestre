package test;

import dominio.Persona;

public class TestForEach {
    public static void main(String[] args) {
        int edades[] = {5, 10, 15, 20, 25};
        for (int edad : edades) {
            System.out.println("edad: " + edad);
        }
        //el for each es una forma mas sencilla de recorrer un arreglo, no se necesita un indice para acceder a cada elemento del arreglo,
        //se puede usar una variable temporal para almacenar el valor de cada elemento del arreglo en cada iteracion del ciclo for each.

    Persona personas[] = {new Persona("Juan"), new Persona("Maria"), new Persona("Pedro")};

    for (Persona persona : personas) {
        System.out.println(persona);
        }
    }
}