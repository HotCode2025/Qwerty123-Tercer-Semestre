# La Leyenda de Aang: Juego de Combate 

## 📖 Descripción del Juego
Es un juego web de combate por turnos donde el jugador se enfrenta a la computadora. El jugador debe elegir a su personaje favorito del universo de Avatar y enfrentarse a un enemigo seleccionado de forma totalmente aleatoria por el sistema. 

Una vez definidos los combatientes, el juego se desarrolla mediante una mecánica de combate inspirada en el clásico "Piedra, Papel o Tijera", pero utilizando ataques físicos. 

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
* **HTML5:** Estructuración semántica en dos columnas (`<main>`, `<section>`).
* **JavaScript (Vanilla):** Manipulación del DOM, manejo de eventos, funciones matemáticas aleatorias y lógica de control.
* **CSS3:** Rediseño completo de la interfaz utilizando Flexbox para una distribución fluida, tarjetas con sombras, bordes redondeados y fondos con degradados.

---

## 🎯 Objetivos y Tareas del Proyecto

### Punto 1: Estructura Base y Selección de Personaje (Completado)
* [x] Crear la estructura HTML base.
* [x] Identificar cada opción de personaje con un `id` único.
* [x] Implementar estructura de control en JS para verificar qué opción fue marcada.
* [x] Validar que el usuario no pueda avanzar sin elegir un personaje.

### Punto 2: Manipulación del DOM y Carga de Página (Completado)
* [x] Agrupar la asignación de eventos en `iniciarJuego()`.
* [x] Implementar `window.addEventListener('load')` para asegurar la carga.
* [x] Inyectar el nombre del personaje seleccionado en el HTML usando `.innerHTML`.

### Punto 3: Botones de Ataque y Enemigo Aleatorio (Completado)
* [x] Configurar botones de "Puño", "Patada" y "Barrida".
* [x] Crear función `aleatorio(min, max)`.
* [x] Asignar automáticamente un personaje al enemigo y mostrarlo en el DOM (`seleccionarPersonajeEnemigo()`).
* [x] Registrar la elección del jugador en variables globales.
* [x] Crear función `ataqueAleatorioEnemigo()` para la respuesta de la PC.

### Punto 4: Lógica de Combate y Rediseño UI/UX (Completado)
El objetivo de esta etapa fue definir al ganador de la ronda y mejorar la experiencia visual del usuario.
* [x] Crear la función `combate()` para comparar `ataqueJugador` y `ataqueEnemigo`.
* [x] Implementar las reglas de combate mediante condicionales lógicos para definir victoria, derrota o empate.
* [x] Rediseñar la interfaz utilizando CSS Flexbox, dividiendo la pantalla en dos columnas (Juego y Reglas).
* [x] Aplicar estilos modernos: fondo degradado, tarjetas blancas con sombras (`box-shadow`), bordes redondeados y botones interactivos.
* [x] Integrar la sección interactiva de "Reglas de Combate" visible para el usuario.

### Punto 5: Interfaz Dinámica Final y Sistema de Vidas (Pendiente)
* [ ] Modificar el texto de los `<span>` de vidas en el HTML para restar puntos al perdedor de cada turno.
* [ ] Crear una función que inyecte los resultados dinámicamente en el DOM sin usar alertas.
* [ ] Ocultar y mostrar dinámicamente las secciones de la interfaz (ej. ocultar la sección de ataques al iniciar).
* [ ] Determinar la condición de "Fin del juego" cuando las vidas lleguen a 0.
* [ ] Habilitar y programar el botón de Reiniciar (`location.reload()`).