import psycopg2 as bd

conexion = bd.connect(
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

try:
    with conexion:
    #con el bloque with, se hace de manera automática el commit de la transacción al finalizar el bloque, o un rollback si ocurre una excepción
        with conexion.cursor() as cursor:
    #Primera transacción: Insertar un nuevo registro en la tabla persona
            sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = ("Alex", "Rojas", "alex.rojas@email.com")
            cursor.execute(sentencia, valores)
            print("Registro insertado")
    
    #Segunda transacción: Actualizar el email de un registro existente en la tabla persona
            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s"
            valores = ("Juan Carlos","Roldan", "jc.roldan@email.com",1)
            cursor.execute(sentencia, valores)
            print("Registro actualizado")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:    
    conexion.close()
    
print("Transacción confirmada, los cambios se han guardado en la base de datos")