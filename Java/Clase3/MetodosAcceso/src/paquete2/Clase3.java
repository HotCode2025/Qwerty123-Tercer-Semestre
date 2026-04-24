package paquete2;

import paquete1.Clase1;

public class Clase3 extends Clase1 {
    public Clase3() {
        super("Acceso al constructor protegido desde Clase3");
        this.atributoProtected = "Acceso al atributo protegido desde Clase3(clase hija)";
        System.out.println("Acceso al atributo protegido desde Clase3: " + this.atributoProtected);
        this.atributoPublic = "Acceso al atributo público desde Clase3";
    }
}
