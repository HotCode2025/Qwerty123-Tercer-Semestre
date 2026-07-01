# 🚢 Batalla Naval — Proyecto Final

> Juego de Batalla Naval desarrollado en **Python 3.12**, como proyecto integrador del tercer semestre de la cátedra "Programación III".  
> Adaptación y reescritura del proyecto original en Java, aplicando principios de **POO**, **encapsulamiento**, **Enum** y **separación de responsabilidades**.  
> Incluye una **interfaz gráfica con Pygame** como extensión visual del proyecto de consola original.  
> Incorpora **persistencia de datos con SQLite** para ranking y historial de partidas.

---

## 📁 Estructura del proyecto

```
batalla_naval/
│
├── batalla_naval.py          # Punto de entrada — versión consola (menú y lógica de partida)
├── batallaNaval_pygame.py    # Punto de entrada — versión gráfica con Pygame
├── batalla_naval.db          # Base de datos SQLite (se genera automáticamente)
│
├── dominio/                  # Modelos principales del juego
│   ├── __init__.py
│   ├── jugadores.py          # Entidad Jugador (nombre + puntaje)
│   ├── tablero.py            # Lógica del tablero, barcos y disparos
│   └── tipo_barco.py         # Enum con los tipos de barcos
│
└── utilidades/               # Clases de soporte
    ├── __init__.py
    ├── db.py                  # Capa de acceso a datos SQLite (conexión, CRUD)
    ├── ranking.py             # Ranking Top 10 con respaldo en base de datos
    └── utilidades.py          # Métodos estáticos: parseo de coordenadas
```

> Los módulos `dominio/` y `utilidades/` son **compartidos** por ambas versiones. La versión Pygame reemplaza únicamente la capa de presentación.

---

## 🎮 Cómo jugar

### Requisitos

- Python **3.10 o superior** (se usa `list[int] | None` y f-strings avanzados)
- **Versión consola:** no requiere librerías externas
- **Versión gráfica:** requiere Pygame

```bash
pip install pygame
```

### Ejecutar el juego

```bash
# Versión consola (original)
python batalla_naval.py

# Versión gráfica con Pygame
python batallaNaval_pygame.py
```

### Mecánica

| Elemento          | Detalle                                      |
|-------------------|----------------------------------------------|
| Tablero           | 8 × 8 (columnas A–H, filas 1–8)             |
| Disparos totales  | 25 por partida                               |
| Puntaje inicial   | 125 puntos                                   |
| Penalización agua | −5 puntos por cada disparo fallido           |
| Barcos            | Submarino (1), Destructor (2), Crucero (3)   |

### Símbolos del tablero (versión consola)

| Símbolo | Significado               |
|---------|---------------------------|
| `?`     | Celda sin disparar        |
| `O`     | Agua (disparo fallido)    |
| `X`     | Impacto en barco          |
| `#`     | Barco completamente hundido |

### Formato de coordenadas (versión consola)

```
A5   → Columna A, Fila 5
H8   → Columna H, Fila 8
```

### Rendición (versión consola)

Cada **5 disparos válidos**, el juego habilita la opción de rendirse escribiendo `salir`, `rendirse` o `q`.

---

## 🖥️ Versión gráfica — Pygame

La versión Pygame reimplementa toda la interfaz del juego en una ventana gráfica, manteniendo intacta la lógica de dominio. Separa completamente la capa de presentación de la lógica de negocio.

### Pantallas

| Pantalla          | Descripción                                                                        |
|-------------------|------------------------------------------------------------------------------------|
| Menú principal    | Opciones Jugar, Ranking, Historial y Salir, con decoración de olas animadas        |
| Ingreso de nombre | Campo de texto con cursor parpadeante y validación en tiempo real                  |
| Tablero           | Grilla 8×8 interactiva con etiquetas, hover al pasar el mouse y clic para disparar |
| Resultado         | Pantalla con mensaje según desempeño, estadísticas y ranking actualizado            |
| Ranking Top 10    | Vista completa con medallas 🥇🥈🥉 y mejor puntaje por jugador                    |
| Historial         | Tabla con las últimas 20 partidas: jugador, puntaje, disparos, resultado y fecha   |

### Panel lateral (durante el juego)

El panel derecho muestra en tiempo real:

- Nombre del jugador
- Puntaje con color dinámico (verde → amarillo → rojo según nivel)
- Barra de progreso de disparos restantes
- Leyenda de colores de celda
- Top 3 del ranking en vivo

### Animaciones

| Evento   | Animación                                                          |
|----------|--------------------------------------------------------------------|
| Agua     | Splash de 20 partículas azules + 2 ondas de expansión concéntricas |
| Impacto  | Explosión de 28 partículas naranja/rojo/amarillo + onda de fuego   |
| Hundido  | Doble explosión de alta intensidad + 2 ondas simultáneas           |

### Fin de partida

- **Victoria:** mensaje motivacional según puntaje (3 niveles) + ranking actualizado
- **Derrota:** mensaje expresivo según desempeño + botón **"👁 Ver ubicación de barcos"** que revela en el tablero la posición de los barcos restantes con colores por tipo
- Tres botones disponibles: **Jugar de nuevo**, **Menú principal** y **Salir del juego**

### Diseño visual

Estilo limpio y moderno con paleta clara y minimalista:

- Fondo gris claro con tarjetas blancas con sombra suave
- Celdas con `border-radius`, estados diferenciados por color
- Tipografía Segoe UI en jerarquía de tamaños
- Referencia visual: Linear / Jira (UI profesional y sin ornamentos)

---

## 🗄️ Base de datos — SQLite

El juego utiliza **SQLite** a través del módulo estándar `sqlite3` (sin dependencias externas) para persistir el ranking y el historial de partidas entre sesiones.

### Archivo de base de datos

La base de datos se crea automáticamente como `batalla_naval.db` en la raíz del proyecto la primera vez que se ejecuta el juego. No requiere ninguna configuración previa.

### Esquema relacional

```sql
CREATE TABLE jugadores (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT    NOT NULL UNIQUE
);

CREATE TABLE partidas (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    jugador_id      INTEGER NOT NULL,
    puntaje         INTEGER NOT NULL,
    disparos_usados INTEGER NOT NULL,
    resultado       TEXT    NOT NULL,   -- 'GANADO' | 'PERDIDO' | 'RENDIDO'
    fecha           TEXT    DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
);
```

La tabla `jugadores` y la tabla `partidas` están relacionadas mediante una **clave foránea** (`FOREIGN KEY`), lo que permite asociar múltiples partidas a un mismo jugador sin repetir su nombre.

### Operaciones principales

| Función               | Descripción                                                          |
|-----------------------|----------------------------------------------------------------------|
| `inicializar_db()`    | Crea las tablas si no existen. Se llama al iniciar la aplicación.    |
| `guardar_partida()`   | Registra el resultado de cada partida (jugador, puntaje, disparos, resultado). |
| `get_top10()`         | Retorna los 10 mejores jugadores con su **mayor puntaje histórico**, agrupando por jugador. |
| `get_historial()`     | Retorna las últimas 20 partidas ordenadas por fecha descendente.     |

### Consulta de ranking

El ranking no simplemente lista las últimas partidas: agrupa por jugador y selecciona su **mejor puntaje**, de modo que cada jugador aparece una sola vez.

```sql
SELECT j.nombre, MAX(p.puntaje) AS puntaje, COUNT(p.id) AS partidas_jugadas
FROM partidas p
JOIN jugadores j ON j.id = p.jugador_id
GROUP BY j.id
ORDER BY puntaje DESC
LIMIT 10
```

### Acceso al historial

#### Versión consola
El menú principal incluye la opción **"Ver Historial"** que muestra en tabla las últimas 20 partidas con jugador, puntaje, disparos usados, resultado y fecha.

#### Versión Pygame
Desde el menú principal, el botón **📋 Historial** abre una pantalla dedicada con la misma información en formato visual, con filas alternadas y colores por resultado (✓ verde / ✗ rojo / ~ amarillo).

---

## 🧱 Descripción de módulos

### `dominio/jugadores.py`
Entidad básica con `nombre` y `puntaje` encapsulados mediante **properties** de Python (equivalente a getters/setters de Java).

### `dominio/tipo_barco.py`
Implementado como **Enum** porque representa un conjunto cerrado y fijo de constantes con atributos asociados (`tamanio`, `simbolo`). Garantiza seguridad de tipo, evita instancias no válidas y facilita el mantenimiento.

### `dominio/tablero.py`
**Clase central del juego.** Contiene:
- Colocación aleatoria de barcos con detección de superposición (`while` + `all()`)
- Sistema de disparos: agua (`O`), impacto (`X`), hundido (`#`)
- Copia de seguridad del tablero original para mostrar la solución al final
- Métodos de visualización (usados por la versión consola; la versión Pygame accede directamente a la matriz `vista_jugador` y `copia_original`)

### `utilidades/db.py`
Capa de acceso a datos. Gestiona la conexión a SQLite, la creación del esquema y todas las operaciones de lectura y escritura. Usa `sqlite3.Row` para acceder a los resultados por nombre de columna. El resto del proyecto importa únicamente las funciones públicas (`inicializar_db`, `guardar_partida`, `get_top10`, `get_historial`), sin conocer los detalles de la conexión.

### `utilidades/ranking.py`
Delega la persistencia a `db.py`. Mantiene la misma interfaz pública (`jugadores`, `mostrar_top10`) para no modificar el código existente. La propiedad `jugadores` retorna objetos `Jugadores` construidos desde los resultados de `get_top10()`, compatible con la versión Pygame que los dibuja directamente.

### `utilidades/utilidades.py`
Clase no instanciable con métodos de clase. Convierte coordenadas tipo `"A5"` al par `[fila, columna]` (base 0), validando rango y formato.

### `batalla_naval.py`
Entry point de la versión consola con:
- Menú interactivo `while` con opciones Jugar / Ranking / Historial / Salir
- `EstadoJuego` como Enum interno (`GANADO`, `PERDIDO_SIN_DISPAROS`, `RENDIDO`)
- Llamada a `guardar_partida()` al finalizar cada partida
- Feedback dinámico según el resultado de cada disparo
- Mensajes motivacionales según el puntaje final

### `batallaNaval_pygame.py`
Entry point de la versión gráfica. Implementa la clase `BatallaNavalApp` con:
- Máquina de estados (`MENU` → `NOMBRE` → `JUEGO` → `RESULTADO` / `RANKING` / `HISTORIAL`)
- Llamada a `guardar_partida()` al finalizar cada partida (victoria o derrota)
- Sistema de partículas propio (`Particula`, `Onda`) para las animaciones
- Componente `Boton` reutilizable con soporte de hover
- Loop de juego con Pygame a 60 FPS, separando `_handle_events`, `_update` y `_draw`

---

## 🐍 Conceptos de Python aplicados

| Concepto Java original       | Equivalente Python                                      |
|------------------------------|---------------------------------------------------------|
| `private` + getters/setters  | Atributos `__` + `@property`                           |
| `enum` con constructor       | `Enum` con `__init__` de múltiples valores             |
| Clase de utilidad estática   | Clase con `__new__` bloqueado + `@classmethod`         |
| `switch` / `case`            | `match/case` (Python 3.10+) o `dict`                   |
| `System.out.println`         | `print()`                                               |
| `Scanner`                    | `input()`                                               |
| `ArrayList`                  | `list`                                                  |
| `Random`                     | `random.randint()` / `random.choice()`                 |
| `System.arraycopy`           | `copy.deepcopy()`                                       |
| GUI (Swing / JavaFX)         | `pygame` — superficie, eventos, loop de render a 60 FPS |
| Base de datos (JDBC)         | `sqlite3` — módulo estándar, sin dependencias externas  |

---

## 👨‍💻 Autores

**GRUPO: QWERTY 123**  
**INTEGRANTES: ANDRÉS, Tomás Miguel; CONTRERAS, Omar Gustavo; ADARO, Fernando; ROMERO, Paul.**

Proyecto Integrador: Batalla Naval  
Tercer Semestre - Programación III - Tecnicatura Universitaria en Programación - UTN FR San Rafael

---

## 📄 Licencia

Proyecto educativo de uso libre.