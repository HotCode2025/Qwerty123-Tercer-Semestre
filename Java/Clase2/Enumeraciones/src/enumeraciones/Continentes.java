package enumeraciones;

public enum Continentes {
    AMERICA(53, "1,2 billones"),
    EUROPA(46, "740 millones"),
    AFRICA(54, "1,34 billones"),
    ASIA(48, "4,62 billones"),
    OCEANIA(14, "42 millones");

    private final int paises;
    private final String habitantes;

    Continentes(int paises, String habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }

    public int getPaises() {
        return paises;
    } 

    public String getHabitantes() {
        return habitantes;
    }
}