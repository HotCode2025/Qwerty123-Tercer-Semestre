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
    conexion.autocommit = False #Desactivamos el autocommit para manejar las transacciones manualmente
    cursor = conexion.cursor()
    sentencia = "INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)"
    valores = ("Maria", "Esparza", "maria.esparza@email.com")
    cursor.execute(sentencia, valores)
    print("Registro insertado, pero aún no se ha confirmado la transacción")
    # Si queremos confirmar la transacción, usamos commit
    conexion.commit()
    print("Transacción confirmada, los cambios se han guardado en la base de datos")
except Exception as e:
    conexion.rollback() #Si ocurre un error, revertimos la transacción para mantener la integridad de los datos
    print(f"Ocurrió un error: {e}")
finally:    conexion.close()