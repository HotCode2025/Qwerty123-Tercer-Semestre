package test;

import paquete1.Clase1;
import paquete2.Clase3;
import paquete2.Clase4;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();//Creacion de un objeto a travez del constructor publico de la clase Clase1.
        System.out.println("Acceso a Clase1 desde TestModificadoresAcceso: " + clase1.atributoPublic);//acceso al objeto a traves del atributo publico de la clase Clase1.
        clase1.metodoPublico();//acceso al objeto a traves del metodo publico de la clase Clase1.
        Clase3 clase3 = new Clase3();//Creacion de un objeto a travez del constructor publico de la clase Clase3.
        System.out.println("Clase hija: " + clase3);//Acceso a Clase3 desde TestModificadoresAcceso: clase3.atributoPublic);
        //acceso al objeto a traves del atributo publico de la clase Clase3.


        Clase4 clase4 = new Clase4("Parametro para constructor publico");//Creacion de un objeto a travez del constructor publico con parametro de la clase Clase4.
        clase4.setAtributoprivate("Nuevo valor para atributo privado");//Acceso al objeto a traves del metodo setter privado de la clase Clase4.
        System.out.println("Valor del atributo privado: " + clase4.getAtributoprivate());//Acceso al objeto a traves del metodo getter privado de la clase Clase4.
    }

}
