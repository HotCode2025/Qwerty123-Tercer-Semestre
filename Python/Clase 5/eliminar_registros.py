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

try:
    with conexion:
        with conexion.cursor() as cursor:   
            sentencia = "DELETE FROM persona WHERE id_persona = %s" # Eliminamos un registro en la tabla persona
            
            # Pedimos al usuario que ingrese el ID de la persona a eliminar
            id_persona = input("Ingrese el ID de la persona a eliminar: ")
            #Tambien podemos eliminarlo directamente en el código, sin pedir al usuario, por ejemplo, eliminando el registro con ID 1
            #id_persona = 1
            
            # Ejecutamos la sentencia SQL
            cursor.execute(sentencia, (id_persona,))
            #Se puede eliminar directamente sin pedir al usuario, por ejemplo, eliminando el registro con ID 1
            #cursor.execute(sentencia, (1,))
            
            #Y tambien se pueden eliminar varios registros a la vez, por ejemplo, eliminando los registros con ID 2 y 3
            #cursor.executemany(sentencia, (2,3))
            
            #conexion.commit() #Guarda los cambios en la base de datos
            registros_eliminados = cursor.rowcount #Obtiene la cantidad de registros eliminados
            print(f"Registro eliminado correctamente. Cantidad de registros eliminados: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close() #Cierra la conexión a la base de datos
#cursor.close() #Cierra el cursor
