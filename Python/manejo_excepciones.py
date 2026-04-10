
from numeros_iguales_excepcion import NumerosIgualesException

#Para hacer una excepsion personalizada, se debe crear una clase que herede de la clase Exception
#Dentro de un bloque try, se puede lanzar una excepcion personalizada utilizando la palabra clave raise
#Ejemplo:

resultado = None #esto es una variable global, que se puede usar en cualquier parte del programa, incluso fuera del bloque try

try:
    #Se pueden crear las variables dentro del bloque try para que solo existan dentro de ese bloque y no afecten el resto del programa
#a = 10
#b = 0
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    if a == b:
        raise NumerosIgualesException("Los numeros son iguales")
    resultado = a / b
#Se pude agregar varias excepciones específicas para manejar diferentes tipos de errores
except TypeError as e:
    print(f"Ocurrió un error de tipo: {e}")

except ZeroDivisionError as e:
    print(f"Ocurrió un error de división por cero: {e}")

except Exception as e:
    print(f"Ocurrió un error: {e}")
    
else:
    print("no se produjo ningún error")
finally:
    print("Este bloque se ejecuta siempre, haya o no haya ocurrido una excepción")  

print(f"El resultado es: {resultado}")

print("El programa continúa ejecutándose...")

##Las excepciones tienen una jerarquía, lo que significa que se pueden capturar excepciones específicas o generales.
#Por ejemplo, se puede capturar una excepción ZeroDivisionError para manejar específicamente el error de división por cero