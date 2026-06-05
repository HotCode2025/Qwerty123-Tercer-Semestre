# La Leyenda de Aang: Juego de Combate 

## 📖 Descripción del Juego
Es un juego web de combate por turnos donde el jugador se enfrenta a la computadora. El jugador debe elegir a su personaje favorito del universo de Avatar y enfrentarse a un enemigo seleccionado de forma totalmente aleatoria por el sistema. 

Una vez definidos los combatientes, el juego se desarrolla mediante una mecánica de combate inspirada en el clásico "Piedra, Papel o Tijera", pero utilizando movimientos físicos. 

### 🥷 Personajes Disponibles
Tanto el jugador como la computadora podrán jugar con uno de los siguientes personajes:
* Zuko 🔥
* Katara 💧
* Aang 🌪️
* Toph 🌎

### ⚔️ Reglas de Combate
En cada turno, el jugador y el enemigo elegirán un ataque. Las interacciones y resoluciones de los ataques son las siguientes:

* **Puño** vence a **Barrida**.
* **Patada** vence a **Puño**.
* **Barrida** vence a **Patada**.

**Resolución del turno:**
* **Empate:** Si ambos eligen el mismo ataque.
* **Ganaste:** Si el ataque del jugador vence al del enemigo.
* **Perdiste:** Si el ataque del enemigo vence al del jugador.

---

## 🛠️ Herramientas y Tecnologías
* **HTML5:** Para estructurar el contenido y los botones de la interfaz.
* **JavaScript (Vanilla):** Para manipular el DOM, manejar eventos y programar la lógica de control.
* **CSS3 (Próximamente):** Para estilizar la interfaz.

---

## 🎯 Objetivos y Tareas del Proyecto

### Punto 1: Estructura Base y Selección de Personaje (Completado)
* [x] Crear la estructura HTML (selección de personaje, ataques, mensajes y reinicio).
* [x] Identificar cada opción de personaje con un `id` único.
* [x] Implementar la estructura de control en JavaScript para verificar qué opción fue marcada.
* [x] Validar que el usuario no pueda avanzar sin elegir un personaje.

### Punto 2: Manipulación del DOM y Carga de Página (Completado)
* [x] Agrupar la asignación de eventos dentro de la función `iniciarJuego()`.
* [x] Implementar `window.addEventListener('load', iniciarJuego)` para asegurar la carga del script.
* [x] Inyectar el nombre del personaje seleccionado directamente en el HTML utilizando `.innerHTML`.

### Punto 3: Botones de Ataque y Enemigo Aleatorio (Completado)
El objetivo de esta etapa fue configurar las opciones de ataque y darle vida a las decisiones de la computadora.
* [x] Modificar los botones de ataque en el HTML para que correspondan a "Puño", "Patada" y "Barrida".
* [x] Crear la función `aleatorio(min, max)` para generar números al azar.
* [x] Crear una función que asigne automáticamente un personaje al enemigo y mostrarlo en el DOM (`seleccionarPersonajeEnemigo()`).
* [x] Añadir eventos a los botones de ataque del jugador para guardar su elección en variables globales.
* [x] Generar una función (`ataqueAleatorioEnemigo()`) que decida el ataque de la PC cada vez que el jugador ataca.

### Punto 4: Lógica de Combate y Mensajes (En Desarrollo / Pendiente)
El objetivo de la siguiente fase es cruzar los ataques elegidos para definir al ganador de la ronda.
* [ ] Crear una función que compare el `ataqueJugador` con el `ataqueEnemigo`.
* [ ] Implementar las reglas de combate (Puño > Barrida, etc.) mediante condicionales `if-else` para definir quién gana, pierde o empata el turno.
* [ ] Crear una función que construya y muestre un mensaje en la sección `<section id="mensajes">` indicando qué ataque usó cada uno y el resultado ("GANASTE", "PERDISTE", "EMPATE").

### Punto 5: Interfaz Dinámica y Sistema de Vidas (Pendiente)
* [ ] Modificar el texto de los `<span>` de vidas en el HTML para restar puntos al perdedor de cada turno.
* [ ] Ocultar y mostrar dinámicamente las secciones de la interfaz (ej. ocultar la sección de ataques al iniciar y mostrarla solo cuando se elige el personaje).
* [ ] Determinar la condición de "Fin del juego" cuando las vidas lleguen a 0 (deshabilitar botones de ataque).
* [ ] Habilitar y programar el botón de Reiniciar para recargar la partida.