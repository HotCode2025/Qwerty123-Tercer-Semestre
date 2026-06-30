archivo = open("prueba.txt", "r", encoding="utf-8") # la "r" es para leer, si el archivo no existe da error
#archivo = open("c:\\prueba.txt", "r", encoding="utf-8") # de esta forma se puede especificar la ruta completa del archivo, es importante usar doble barra invertida para evitar errores de escape

#print(archivo.read()) #imprime el contenido del archivo

#print(archivo.read(15)) #si le agregamos un número entre paréntesis, lee esa cantidad de caracteres
#print(archivo.readline()) #lee una línea del archivo, cada vez que se llama a readline() lee la siguiente línea
#print(archivo.readlines()) #lee todas las líneas del archivo y las devuelve como una lista

#for linea in archivo: #también podemos usar un ciclo for para leer el archivo línea por línea
#    print(linea)
    
#print(archivo.readlines()[10]) #si queremos acceder a una línea específica, podemos usar el índice de la lista devuelta por readlines(), en este caso se imprime la línea 17 (índice 16)

#archivo2 = open("copia.txt", "a", encoding="utf-8") # la "a" es para agregar, si el archivo no existe lo crea, si existe lo agrega al final del archivo
archivo2 = open("copia.txt", "w", encoding="utf-8")
archivo2.write(archivo.read()) #escribe el contenido del archivo original en el nuevo archivo
archivo.close() # cerramos el archivo original
archivo2.close() # cerramos el archivo de copia
#las veces que se ejecute este código, se agregará el contenido del archivo original al final del archivo de copia, si queremos evitar esto, podemos usar la letra "w" en lugar de "a" para escribir en el archivo de copia, así se sobreescribirá el archivo cada vez que se ejecute el código
print("Archivo copiado exitosamente")