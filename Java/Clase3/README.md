## Autoboxing y Unboxing
En Java, el autoboxing es el proceso automático de convertir un tipo de dato primitivo en su correspondiente clase envolvente (wrapper class). Por ejemplo, convertir un `int` en un `Integer`. El unboxing es el proceso inverso, donde una clase envolvente se convierte automáticamente en su tipo de dato primitivo correspondiente.

## Ciclo For Each
El ciclo for-each, también conocido como "enhanced for loop", es una forma simplificada de iterar sobre colecciones y arreglos en Java. Permite recorrer elementos sin necesidad de usar un índice explícito. La sintaxis es la siguiente:

```java
for (TipoElemento elemento : coleccion) {
    // Código a ejecutar con cada elemento
}
```
En este ejemplo, `TipoElemento` es el tipo de los elementos en la colección, `elemento` es la variable que representa cada elemento durante la iteración, y `coleccion` es la colección o arreglo que se está iterando. Este tipo de ciclo es especialmente útil para mejorar la legibilidad del código y reducir errores relacionados con índices.

## Métodos de Acceso
Los métodos de acceso, también conocidos como getters y setters, son métodos que permiten acceder y modificar los atributos de una clase de manera controlada. Un getter es un método que devuelve el valor de un atributo, mientras que un setter es un método que establece el valor de un atributo. Estos métodos son fundamentales para encapsular los datos y proteger la integridad de los objetos.
Tenemos 3 tipos de métodos de acceso: Public, Private y Protected.
- **Public**: Los métodos públicos pueden ser accedidos desde cualquier clase. Son los más comunes para getters y setters, ya que permiten que otras clases interactúen con los atributos de la clase de manera segura.
- **Private**: Los métodos privados solo pueden ser accedidos dentro de la misma clase. Se utilizan para ocultar la implementación interna de la clase y proteger los datos de accesos no autorizados.
- **Protected**: Los métodos protegidos pueden ser accedidos dentro de la misma clase, por clases del mismo paquete y por subclases. Son útiles para permitir cierto nivel de acceso a los atributos mientras se mantiene un control sobre quién puede modificarlos.
En resumen, los métodos de acceso son esenciales para mantener la encapsulación y la integridad de los objetos en Java, permitiendo un control adecuado sobre cómo se acceden y modifican los atributos de una clase.

Existe un cuarto tipo de método de acceso llamado "default" o "package-private", que no tiene un modificador de acceso explícito. Estos métodos solo pueden ser accedidos por clases dentro del mismo paquete, lo que proporciona un nivel de acceso intermedio entre public y private.(son pocos usados, pero es importante mencionarlos para tener una comprensión completa de los niveles de acceso en Java).