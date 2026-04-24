package paquete1;

public class ClaseHija2 extends Clase2 {
    public ClaseHija2() {
        super(); // Calls the default constructor of Clase2
        this.atributoDefault = "Atributo Default modificado en ClaseHija2";
        System.out.println("atributoDefault: " + this.atributoDefault);
        this.metodoDefault();
    }
}
