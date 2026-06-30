import psycopg2

conexion = psycopg2.connect(
    #si trabajamos con una base de datos en la nube, aquí iría la dirección IP o el nombre del host
    host="localhost",
    port = 5432,
    #database es el nombre de la base de datos a la que queremos conectarnos, en este caso "test"
    database="test",
    user="postgres",
    password="admin"
)
print(conexion)
print("Conexión exitosa a la base de datos")


# Con el bloque try-except-finally, nos aseguramos de manejar cualquier error
# se usa with para manejar automáticamente la apertura y cierre de recursos,
# en este caso la conexión a la base de datos y el cursor.
# Esto nos ayuda a evitar problemas como conexiones abiertas o recursos no liberados,
# incluso si ocurre un error durante la ejecución. 
# En el bloque except, capturamos cualquier excepción que pueda ocurrir durante la ejecución de las operaciones con la base de datos,
# y garantizamos que la conexión se cierre correctamente al finalizar.

try:
    with conexion:
        with conexion.cursor() as cursor:   
            sentencia = "SELECT * FROM persona WHERE id_persona = %s"# Esto es un placeholder para evitar inyecciones SQL
            id_persona = input("Ingrese el ID de la persona a buscar: ")
            cursor.execute(sentencia, (1,)) #Ejecuta la sentencia SQL
            #registros = cursor.fetchall() #Obtiene todos los registros
            registros = cursor.fetchone() #Obtiene un solo registro
            print(registros)
            #esto nos devuelve una lista de tuplas, cada tupla representa un registro de la tabla persona
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close() #Cierra la conexión a la base de datos
#cursor.close() #Cierra el cursor