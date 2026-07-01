package test;

import domain.*;

public class testInstanceOf {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Jose", 200000);
        determinartipo(empleado1);
        empleado1 = new Gerente("Jose", 50000, "Sistemas");
        determinartipo(empleado1);
    }

    public static void determinartipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es una instancia de tipo Gerente");
            
            //De estas 2 forma podemos determinar la instancia de departamento
            Gerente gerente = (Gerente) empleado;
            //((Gerente) empleado).getDepartamento();
            System.out.println("gerente = " + gerente.getDepartamento());
        }
        else if(empleado instanceof Empleado){
            System.out.println("Es una instancia de tipo Empleado");
        }
        else if (empleado instanceof Object){
            System.out.println("Es una instancia de tipo Object");
        }
        //Con esto podemos determinar que el objeto pertenece a "x" instancia
    }
}
