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
            sentencia = "UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s" # Actualizamos un registro en la tabla persona
            
            # Pedimos al usuario que ingrese los datos de la persona a actualizar
            id_persona = input("Ingrese el ID de la persona a actualizar: ")
            nombre = input("Ingrese el nombre de la persona: ")
            apellido = input("Ingrese el apellido de la persona: ")
            email = input("Ingrese el email de la persona: ")
            #Tambien podemos crearlos directamente en el código, sin pedir al usuario
            #valores = (1,"Carlos", "Lara", "carloslara@gmail.com")
            
            #De la misma forma que ingresamos,podemos modificar varios registros a la vez, con el comando executemany
            cursor.execute(sentencia, (id_persona, nombre, apellido, email)) #Ejecuta la sentencia SQL
            #conexion.commit() #Guarda los cambios en la base de datos
            registros_insertados = cursor.rowcount #Obtiene la cantidad de registros insertados
            print(f"Registro actualizado correctamente. Cantidad de registros actualizados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close() #Cierra la conexión a la base de datos
#cursor.close() #Cierra el cursor
