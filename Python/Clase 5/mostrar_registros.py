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
            sentencia = "SELECT * FROM persona WHERE id_persona in %s"# Esto es un placeholder para evitar inyecciones SQL(parametro posicional)
            entrada = input("Ingrese los ID de las personas a buscar, separados por comas: ")
            # Convertimos la entrada en una tupla de enteros
            llaves_primarias = (tuple( entrada.split(',')),) # Esto es necesario porque el placeholder espera una tupla, incluso si solo hay un valor
            cursor.execute(sentencia, (llaves_primarias,)) #Ejecuta la sentencia SQL
            registros = cursor.fetchall() #Obtiene todos los registros
            for registro in registros:# Iteramos sobre la lista de tuplas y mostramos cada registro
                print(registro)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close() #Cierra la conexión a la base de datos
#cursor.close() #Cierra el cursor