#with open("prueba.txt", "r", encoding="utf-8") as archivo: # con with open() se asegura que el archivo se cierre automáticamente después de usarlo, no es necesario usar finally para cerrar el archivo
#    print(archivo.read()) #imprime el contenido del archivo, pero como el archivo se abrió en modo lectura, se puede leer el contenido del archivo sin problemas
    #si el archivo se hubiera abierto en modo escritura, no se podría leer el contenido del archivo y se generaría un error
    
    #no hace falta el try ni finally para manejar el archivo, con with open() se maneja automáticamente el cierre del archivo, aunque haya un error, el archivo se cerrará correctamente, 
    # es una buena práctica usar with open() para manejar archivos en Python, ya que es más seguro y eficiente que usar open() sin with.
    #los metodos que ahorramos con with open() son: try, except, finally, close(), etc. que se usan para manejar archivos de forma segura y eficiente.
    
    # __enter__ y __exit__ son los métodos que se usan para manejar el contexto del archivo,
    # con with open() se llama automáticamente a estos métodos para manejar el archivo de forma segura y eficiente. 
    
from ManejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo: #con with ManejoArchivos() se maneja el archivo de forma segura y eficiente, se llama automáticamente a los métodos __enter__ y __exit__ para manejar el archivo de forma segura y eficiente.
    print(archivo.read()) #imprime el contenido del archivo, pero como el archivo se abrió en modo lectura, se puede leer el contenido del archivo sin problemas