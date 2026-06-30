try:
    archivo = open("prueba.txt", "w" ,encoding="utf-8") #la "w" es para escribir, si el archivo no existe lo crea, si existe lo sobreescribe
    #Para que no hayan errores de codificación, es importante especificar la codificación al abrir el archivo, en este caso usamos utf-8
    archivo.write("Programamos con diferentes tipos de escritura. Ahora escribimos en formato txt \n") #escribe en el archivo
    archivo.write("Podemos escribir varias lineas usando el salto de linea, con Alt + 92 \n") #escribe otra línea en el archivo
    archivo.write("Es importante cerrar el archivo después de usarlo para liberar recursos y evitar errores \n") 
    archivo.write("las letras para manejar archivos son: \nr (leer)\n w (escribir)\n a (agregar) \n x (crear)") 
    archivo.write("\nSi queremos escribir sin sobreescribir el archivo, usamos la letra a (agregar) en lugar de w (escribir)") 
    archivo.write("\nSi queremos crear un archivo nuevo, usamos la letra x (crear), si el archivo ya existe da error")
    archivo.write("\nTexto para leer con readlines()y acceder a una línea específica usando el índice de la lista devuelta por readlines()")
    archivo.write("\nTambien podemos usar el tipo de archivo que queramos,por ejemplo: \narchivo.csv, \narchivo.json, \narchivo.xml, etc.")
    archivo.write("\nTambien podemos usar las letras : \nt (texto) \nb (binario) \n+ (lectura y escritura) \na+ (agregar y leer) \nw+ (escribir y leer) \nx+ (crear y leer)")
except Exception as e:
    print(e)
finally:
    archivo.close()# con esto se asegura que el archivo se cierre aunque haya un error, es una buena práctica usar finally para cerrar archivos
    