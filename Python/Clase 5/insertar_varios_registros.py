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
            sentencia = "INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)" # Insertamos un nuevo registro en la tabla persona
            
            # Pedimos al usuario que ingrese los datos de la persona a insertar
            nombre = input("Ingrese el nombre de la persona: ")
            apellido = input("Ingrese el apellido de la persona: ")
            email = input("Ingrese el email de la persona: ")
            
            #Tambien podemos crearlos directamente en el código, sin pedir al usuario
            #valores = (
                # ("Carlos", "Lara", "carloslara@gmail.com")
                # ("Ana", "García", " anagarcia@gmail.com")
                # ("Luis", "Pérez", " luisperez@gmail.com")
            #) #Lista de tuplas con los datos de las personas a insertar
            
            cursor.executemany(sentencia, [(nombre, apellido, email)]) #El comando executemany permite ejecutar la misma sentencia SQL varias veces con diferentes valores,
            #en este caso insertamos varias personas a la vez
            
            #conexion.commit() #Guarda los cambios en la base de datos
            registros_insertados = cursor.rowcount #Obtiene la cantidad de registros insertados
            print(f"Registro insertado correctamente. Cantidad de registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close() #Cierra la conexión a la base de datos
#cursor.close() #Cierra el cursor