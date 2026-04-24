package paquete1;

public class TestPaquete1 {
    public static void main(String[] args) {
        Clase2 clase2 = new Clase2();
        System.out.println(clase2.atributoDefault);
        clase2.metodoDefault();
        /*Al ser un atributo default, solo es accesible desde la misma clase o paquete */

        ClaseHija2 claseHija2 = new ClaseHija2();
        claseHija2.atributoDefault = "Modificando el atributo default desde TestPaquete1";
        System.out.println(claseHija2.atributoDefault);
        //claseHija2.metodoDefault(); // No se puede acceder al método default desde TestPaquete1
        //Se puede acceder al atributo default porque ClaseHija2 hereda de Clase2, pero no se puede acceder al método default 
        //porque TestPaquete1 no es parte del mismo paquete ni es una subclase de Clase2.
    }
}
