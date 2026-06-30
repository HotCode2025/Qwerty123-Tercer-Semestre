# CLASES DE PYTHON
Cree un solo entorno para toda la carpeta de Python...lo que hace que todos los archivos creados no queden en sus correspondientes carpetas de CLASE.

## CLASE 1

### Excepciones Personalizadas
Para hacer una excepsion personalizada, se debe crear una clase que herede de la clase Exception
Dentro de un bloque try, se puede lanzar una excepcion personalizada utilizando la palabra clave raise
```python
class MiExcepcionPersonalizada(Exception):
    pass
try:
    raise MiExcepcionPersonalizada("Este es un mensaje de error personalizado")
except MiExcepcionPersonalizada as e:
    print(e)
```
### numeros iguales exception
 la excepcion personalizada para numeros iguales se puede crear de la siguiente manera:

```python
class NumerosIgualesException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje
```

## CLASE 2

### Manejo de archivos
Para manejar archivos en Python, se pueden utilizar las funciones integradas como open(), read(), write() y close().
Se usa la funcion with para abrir un archivo, lo que garantiza que el archivo se cierre correctamente después de su uso, incluso si ocurre una excepción.
Hay que especificar el formato de lectura para evitar errores...normalmente es UTF-8
Y para manipularlo con python se crean metodos para escribir, leer y cerrar el archivo. 

```python
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = None

    def escribir(self, contenido):
        with open(self.nombre, 'w') as self.archivo:
            self.archivo.write(contenido)

    def leer(self):
        with open(self.nombre, 'r') as self.archivo:
            return self.archivo.read()

    def cerrar(self):
        if self.archivo:
            self.archivo.close()
```

## CLASE 3

Catalogo de peliculas utilizando lo aprendido en manejo de archivos

## CLASE 4

Aprendiendo el uso de postgreSQL y el uso de python para su manipulacion

## CLASE 5

### Bloque try-except-finally
Con el bloque try-except-finally, nos aseguramos de manejar cualquier error
se usa with para manejar automáticamente la apertura y cierre de recursos,
en este caso la conexión a la base de datos y el cursor.
Esto nos ayuda a evitar problemas como conexiones abiertas o recursos no liberados,
incluso si ocurre un error durante la ejecución. 
En el bloque except, capturamos cualquier excepción que pueda ocurrir durante la ejecución de las operaciones con la base de datos,
y garantizamos que la conexión se cierre correctamente al finalizar.
### Manipulando PostgreSQL

Aprendemos el uso de PlaceHolder(parametros posicionales)
Los datos se crean,modifican en forma de tuplas siendo las mas comunes
 *Tuplas de un solo elemento: Si solo vas a pasar un dato, recuerda poner la coma final: (valor,) no (valor).

*conexion.commit() Sin llamar a este método, es posible que sus actualizaciones, inserciones o eliminaciones solo existan en un estado "preparado" temporal y se perderán una vez que se cierre la conexión.

## CLASE 6
Trabajando con transacciones en PostgreSQL utilizando Python
*Transacción: Es una unidad de trabajo que se ejecuta de manera atómica, es decir, todas las operaciones dentro de la transacción se completan exitosamente o ninguna de ellas se aplica a la base de datos. Esto garantiza la integridad de los datos y evita estados inconsistentes.

### Transacciones manuales
En este ejemplo, se realizan dos operaciones en la base de datos: una inserción y una actualización. Si ambas operaciones se ejecutan correctamente, se llama a commit() para confirmar la transacción y guardar los cambios en la base de datos. Si ocurre un error en cualquiera de las operaciones, se llama a rollback() para revertir la transacción y mantener la integridad de los datos. Finalmente, se cierra la conexión a la base de datos.
### Transacciones con bloque with
Con el bloque with, se hace de manera automática el commit de la transacción al finalizar el bloque, o un rollback si ocurre una excepción.

## CLASE 7

Seguimos trabajando con transacciones en PostgreSQL utilizando Python, ahora vemos el metodo logging para registrar eventos y errores en un archivo de log, lo que nos ayuda a monitorear el comportamiento de nuestra aplicación y a depurar problemas de manera más eficiente.
Creamos las clases "conexion" y "cursor" para manejar la conexión a la base de datos y las operaciones con el cursor, respectivamente.Tambien creamos la clase "Persona"

### Logging
El módulo logging de Python proporciona una forma flexible de registrar eventos y errores en un archivo de log. En este ejemplo, se configura el logging para escribir en un archivo llamado 'capa_datos.log' con un nivel de log de ERROR.

## CLASE 8

Trabajando con la capa de datos en Python utilizando PostgreSQL
En esta clase, se implementa una capa de datos para manejar la conexión a la base de datos y las operaciones con la base de datos de manera más estructurada y modular. Se crean las clases "Conexion" y "Cursor" para manejar la conexión a la base de datos y las operaciones con el cursor, respectivamente. También se crea la clase "Persona" para representar una entidad en la base de datos.
### Capa de datos
La capa de datos es una parte fundamental de la arquitectura de software que se encarga de manejar la interacción con la base de datos. En este ejemplo, se implementa una capa de datos utilizando clases para encapsular la lógica de conexión y operaciones con la base de datos. Esto permite una mejor organización del código, facilita el mantenimiento y mejora la reutilización de la lógica relacionada con la base de datos en toda la aplicación.

## CLASE 9

Implementacion de una clase CursorPool, optimizando codigo creando un pool