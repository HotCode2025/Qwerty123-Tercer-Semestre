# Juego de Aang: Avatar

## Uso del DOM para crear un juego interactivo
En esta práctica, se ha desarrollado un juego basado en la serie "La Leyenda de Aang: Avatar". El juego permite a los jugadores seleccionar un personaje y luego elegir ataques para enfrentarse a un enemigo. A continuación, se describen los aspectos clave del código y cómo se utiliza el DOM para crear una experiencia interactiva.
### Estructura del Código
El código se divide en dos archivos principales:
1. **LaLeyendadeAang.html**: Este archivo contiene la estructura HTML del juego, incluyendo secciones para seleccionar personajes, mostrar ataques y reiniciar el juego.
2. **Aang.js**: Este archivo contiene la lógica del juego, incluyendo funciones para iniciar el juego, seleccionar personajes y manejar los ataques.

## Documentacion sobre html y js
### HTML
- Se utiliza una estructura básica de HTML con etiquetas como `<section>`, `<h2>`, `<p>`, y `<button>` para organizar el contenido del juego.
- Se incluyen elementos con IDs específicos (como `boton-personaje`, `personaje-seleccionado`, `enemigo-seleccionado`, etc.) para facilitar la manipulación del DOM desde JavaScript.
### JavaScript
- Se utiliza `window.addEventListener("load", iniciarJuego);` para asegurarse de que el juego se inicialice correctamente una vez que la página esté completamente cargada.
-**getElementById** se utiliza para acceder a los elementos del DOM y actualizar su contenido o agregar event listeners.
-**innerHTML** se utiliza para actualizar el contenido de los elementos del DOM, como mostrar el personaje seleccionado y las vidas restantes.

## Cambios Realizados
- Se define una función `iniciarJuego()` que se ejecuta cuando la página se carga, agregando un event listener al botón de selección de personaje.
- La función `seleccionarPersonaje()` maneja la lógica para seleccionar un personaje y actualizar la interfaz del juego en consecuencia.
- Se creo una función `seleccionAleatioriaEnemigo()` para seleccionar un enemigo de manera aleatoria cada vez que se selecciona un personaje.
- Se mejoró la legibilidad del código al organizar las funciones y agregar comentarios explicativos.