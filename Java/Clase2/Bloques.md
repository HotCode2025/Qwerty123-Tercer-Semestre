
# 1. Reemplazar Bloques static (Inicialización de clase)

    Los bloques static se ejecutan una sola vez cuando la clase se carga.

## Alternativa 1: Inicialización directa en el campo (Recomendado para casos simples)

java
// En lugar de: static { mapa = new HashMap<>(); ... }

    private static final Map<String, String> mapa = new HashMap<>();

## Alternativa 2: Métodos estáticos auxiliares (Recomendado para lógica compleja)

Si necesitas try-catch u otra lógica, usa un método private static.
java

    private static int val = initVal();
    private static int initVal() {
    // Lógica compleja aquí
    return 10;
    }

## Alternativa 3: Inicialización perezosa (Lazy Initialization) 

Si la inicialización es costosa y no siempre se necesita, puedes usar un método que se llame solo cuando sea necesario.

java

    private static Connection connection;
    public static Connection getConnection() {
    if (connection == null) {
    connection = createConnection(); // Se ejecuta solo la primera vez
    }
    return connection;
    }

# 2. Reemplazar Bloques No Static / Instancia (Inicialización de objeto)

Estos bloques se ejecutan cada vez que se crea una instancia (objeto) de la clase.
    
    Baeldung
    Baeldung
    +1

## Alternativa 1: Inicialización directa en el campo

java
// En lugar de: { lista = new ArrayList<>(); }

    private List<String> lista = new ArrayList<>();

## Alternativa 2: Constructor (Recomendado)

Si el bloque es para inicializar variables, el constructor es el lugar adecuado.
java
    public MiClase() {
    // Inicialización aquí
    }

## Alternativa 3: Constructores encadenados (Constructor Chaining)

Si tienes varios constructores y quieres compartir código de inicialización, llama a un constructor principal usando this().
