package paquete1;

public class Clase1 {
    public String atributoPublic = "Atributo Público";
    protected String atributoProtected = "Atributo Protegido";

    public Clase1() {
        System.out.println("Constructor publico de Clase1");
    }
    protected Clase1(String mensaje) {
        System.out.println("Constructor protegido de Clase1: " + mensaje);
    }
    protected void metodoProtegido() {
        System.out.println("Método protegido de Clase1");
    }

    public void metodoPublico() {
        System.out.println("Método público de Clase1");
    }
}
