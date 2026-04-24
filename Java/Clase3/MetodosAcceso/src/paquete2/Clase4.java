package paquete2;

public class Clase4 {
    private String atributoprivate  = "atributo privado";

    private Clase4() {
        System.out.println("Constructor privado");
    }

    // Constructor publico con parametro para poder crear objetos de esta clase desde otras clases
    public Clase4(String parametro) {
        System.out.println("Constructor publico con parametro: " + parametro);
    }

    private  void metodoprivate() {
        System.out.println("Metodo privado");
    }

    // Getters y Setters para el atributo privado
    public String getAtributoprivate() {
        return atributoprivate;
    }
    public void setAtributoprivate(String atributoprivate) {
        this.atributoprivate = atributoprivate;
    }
}
