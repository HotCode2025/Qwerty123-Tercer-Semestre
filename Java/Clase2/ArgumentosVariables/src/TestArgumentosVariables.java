public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(1,2,3,4,5);
        imprimirNumeros(3,5,6);
        variosParametros("Juan","Gimenez", 1, 2, 3, 4, 5);
}

    // El método con argumentos variables debe ser el último parámetro
    private static void variosParametros(String nombre, String apellido, int... numeros) {
    System.out.println("Nombre: " + nombre + ", Apellido: " + apellido);
    imprimirNumeros(numeros);
    }
    // El método con argumentos variables debe ser el último parámetro
    //los parametros con argumentos variables se tratan como un arreglo dentro del método
    //y un arreglo es un objeto, por lo que se puede pasar un arreglo directamente al método con argumentos variables
    public static void imprimirNumeros(int... numeros) {
        for (int i = 0 ;i < numeros.length; i++) {
            System.out.println("Elemento "+ numeros[i]);
        }
    }
}
