class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __enter__(self):
        print("Abriendo el archivo...")
        print("obtenemos el recurso".center(50, "-"))
        self.nombre = open(self.nombre, "r", encoding="utf-8")#encapsulamos la apertura del archivo en el método __enter__,
        #así se asegura que el archivo se abra correctamente y se maneje el recurso de forma segura
        return self.nombre
    
    def __exit__(self, tipo_exception, valor_exception, traza_exception):
        print("Cerrando el archivo...")
        self.nombre.close()
        print("liberamos el recurso".center(50, "-"))
        if self.nombre:
            self.nombre.close()#con esto se asegura que el archivo se cierre correctamente, aunque haya un error, el archivo se cerrará correctamente,
            #es una buena práctica usar with open() para manejar archivos en Python, ya que es más seguro y eficiente que usar open() sin with.