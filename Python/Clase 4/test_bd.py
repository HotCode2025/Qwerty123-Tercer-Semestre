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

cursor = conexion.cursor()
sentencia = "SELECT * FROM persona"
cursor.execute(sentencia) #Ejecuta la sentencia SQL
registros = cursor.fetchall() #Obtiene todos los registros
print(registros)
#esto nos devuelve una lista de tuplas, cada tupla representa un registro de la tabla persona

cursor.close() #Cierra el cursor
conexion.close() #Cierra la conexión a la base de datos