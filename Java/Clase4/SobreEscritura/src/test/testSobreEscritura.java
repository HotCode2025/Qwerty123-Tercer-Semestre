package test;

import dominio.*;

public class testSobreEscritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Jose", 200000);
        //System.out.println("Empleado : " + empleado1.obtenerDetalles());
        imprimir(empleado1);

        Gerente gerente1 = new Gerente("Alberto", 150000, "Sistemas");
        //System.out.println("gerente1 :" +gerente1.obtenerDetalles());
        imprimir(gerente1);
        //Aca podemos usar el polimorfismo para aplicar un metodo dirigido a la clase padre sobre la clase hija
    }
    public static void imprimir(Empleado empleado){
        //Aca podemos ver como funciona el polimorfismo
        String detalles = empleado.obtenerDetalles();//Uso del metodo de la clase padre para ambas
        System.out.println("detalles = " + detalles);
    }
}
