import enumeraciones.Dias;

public class TestEnumeraciones {
    public static void main(String[] args) {
        //System.out.println("Dias.LUNES = " + Dias.LUNES);
        //indicarDiaDeSemana(Dias.LUNES);//las enumaraciones se tratan como cadenas
        //Ahora no se debe agregar comillas a los dias de la semana, ya que se tratan como constantes y no como cadenas, lo que hace que el codigo sea mas legible y menos propenso a errores.
        
        
        for (Dias dias : Dias.values()) {
            //con values() se obtiene un arreglo con todos los valores de la enumeracion, 
            // y con el for each se recorre ese arreglo para mostrar cada dia de la semana.
            indicarDiaDeSemana(dias);
        }//hice un for each para recorrer los dias de la semana,
        //y asi no tener que escribir un switch para cada dia de la semana, lo que hace que el codigo sea mas limpio y legible.

        System.out.println("------------------------------");


        for (enumeraciones.Continentes continente : enumeraciones.Continentes.values()) {
            System.out.println("Continente = " + continente);
            System.out.println("paises de este continente = " + continente.getPaises());
            System.out.println("habitantes de este continente = " + continente.getHabitantes());
            System.out.println("------------------------------");
        }
    }

    private static void indicarDiaDeSemana(Dias dias) {
        switch (dias) {
            case LUNES:
                System.out.println("Lunes - Primer dia de la semana");
                break;
            case MARTES:
                System.out.println("Martes - Segundo dia de la semana");
                break;
            case MIERCOLES:
                System.out.println("Miercoles - Tercer dia de la semana");
                break;
            case JUEVES:
                System.out.println("Jueves - Cuarto dia de la semana");
                break;
            case VIERNES:
                System.out.println("Viernes - Quinto dia de la semana");
                break;
            case SABADO:
                System.out.println("Sabado - Sexto dia de la semana");
                break;
            case DOMINGO:
                System.out.println("Domingo - Septimo dia de la semana");
                break;
        }
    }
}
