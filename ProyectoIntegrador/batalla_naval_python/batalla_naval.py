"""
Módulo: batalla_naval.py
Descripción: Punto de entrada del juego Batalla Naval.
             Controla el menú principal, el flujo de partida y el resultado final.
"""


# ------------------------------------------------------------------ #
#  Estado de finalización de partida                                  #
# ------------------------------------------------------------------ #

class EstadoJuego(Enum):
    GANADO              = auto()
    PERDIDO_SIN_DISPAROS = auto()
    RENDIDO             = auto()


# ------------------------------------------------------------------ #
#  Constantes de partida                                              #
# ------------------------------------------------------------------ #

DISPAROS_TOTALES  = 25
PUNTAJE_INICIAL   = 125
PENALIZACION_AGUA = 5


# ------------------------------------------------------------------ #
#  Instancias globales de sesión                                      #
# ------------------------------------------------------------------ #

ranking = Ranking()


# ------------------------------------------------------------------ #
#  Helpers de entrada                                                 #
# ------------------------------------------------------------------ #

def leer_entero(prompt: str = "") -> int:
    """Lee un entero desde la consola; retorna -1 si la entrada no es válida."""
    try:
        return int(input(prompt).strip())
    except (ValueError, EOFError):
        return -1


def leer_texto(prompt: str = "") -> str:
    """Lee una línea de texto desde la consola."""
    try:
        return input(prompt).strip()
    except EOFError:
        return ""


# ------------------------------------------------------------------ #
#  Menú principal                                                     #
# ------------------------------------------------------------------ #

def mostrar_menu():
    print("\n" + "=" * 42)
    print("         BATALLA NAVAL  -  MENÚ")
    print("=" * 42)
    print("  1.  Jugar")
    print("  2.  Ver Ranking")
    print("  3.  Ver Historial")
    print("  4.  Salir")
    print("=" * 42)


# ------------------------------------------------------------------ #
#  Lógica de partida                                                  #
# ------------------------------------------------------------------ #

def jugar():
    nombre = leer_texto("Ingrese su nombre: ")
    if not nombre:
        nombre = "Jugador"

    puntaje           = PUNTAJE_INICIAL
    disparos_restantes = DISPAROS_TOTALES
    disparos_validos   = 0

    tablero = Tablero()
    tablero.colocar_barcos()

    estado = EstadoJuego.PERDIDO_SIN_DISPAROS

    # ── Bucle de juego ─────────────────────────────────────────────
    while not tablero.juego_finalizado() and disparos_restantes > 0:
        print()
        tablero.mostrar_vista_jugador()
        print(f"\n  Disparos restantes : {disparos_restantes}")
        print(f"  Puntaje actual     : {puntaje}")

        puede_rendirse = disparos_validos > 0 and disparos_validos % 5 == 0

        if puede_rendirse:
            prompt = "\nIngrese coordenada (ej: A5) o 'salir' para rendirse: "
        else:
            prompt = "\nIngrese coordenada (ej: A5): "

        entrada = leer_texto(prompt)

        # Opción de rendirse (solo disponible tras múltiplos de 5 disparos válidos)
        if puede_rendirse and entrada.lower() in ("salir", "rendirse", "q"):
            print(f"\n  Te has rendido tras {disparos_validos} disparos válidos.")
            estado = EstadoJuego.RENDIDO
            break

        # Validar formato de coordenada
        coords = Utilidades.parsear_coordenada(entrada)
        if coords is None:
            print("\n  Formato incorrecto. Usá letra y número (ej: A5).")
            if puede_rendirse:
                print("  Tip: podés escribir 'salir' ahora para rendirte.")
            continue

        fila, columna = coords

        # Ejecutar disparo
        if not tablero.disparar(fila, columna):
            print("\n  Ya disparaste ahí o la coordenada es inválida.")
            continue

        # Disparo válido: actualizar contadores
        disparos_validos   += 1
        disparos_restantes -= 1

        # Evaluar resultado del disparo
        celda = tablero.vista_jugador[fila][columna]
        if celda == Tablero.AGUA:
            puntaje -= PENALIZACION_AGUA
            print(f"\n  ¡Agua! (-{PENALIZACION_AGUA} puntos)")
        elif celda in (Tablero.IMPACTO, Tablero.HUNDIDO):
            print("\n  ¡Impacto!")
            if celda == Tablero.HUNDIDO:
                print("  ¡¡Barco hundido!!")

        # Feedback cada 5 disparos válidos
        if disparos_validos % 5 == 0:
            print(f"  Has completado {disparos_validos} disparos válidos.")

    # ── Determinar estado final ────────────────────────────────────
    if tablero.juego_finalizado():
        estado = EstadoJuego.GANADO
    elif estado != EstadoJuego.RENDIDO:
        estado = EstadoJuego.PERDIDO_SIN_DISPAROS

    disparos_usados = DISPAROS_TOTALES - disparos_restantes

    # ── Mostrar resultado ──────────────────────────────────────────
    mostrar_resultado_final(tablero, puntaje, disparos_restantes, estado)

    # ── Persistir en base de datos ─────────────────────────────────
    guardar_partida(nombre, puntaje, disparos_usados, estado.name)


def mostrar_resultado_final(
    tablero: Tablero,
    puntaje: int,
    disparos_restantes: int,
    estado: EstadoJuego,
):
    """Muestra el resultado de la partida según cómo terminó el juego."""
    print()
    print("=" * 52)
    print("                JUEGO FINALIZADO")
    print("=" * 52)

    if estado == EstadoJuego.GANADO:
        titulo = "¡MAESTRO!" if puntaje >= 100 else "¡CAMPEÓN!"
        print(f"\n  ¡FELICITACIONES, {titulo}")
        print("  ¡Hundiste todos los barcos enemigos!")
        print("\n  Tu desempeño:")
        tablero.mostrar_vista_jugador()

    elif estado == EstadoJuego.PERDIDO_SIN_DISPAROS:
        print("\n  ¡PERDISTE! Te quedaste sin disparos.")
        print("  No lograste hundir todos los barcos.")
        print("\n  Solución:")
        tablero.mostrar_tablero_original()
        print("  Tus disparos:")
        tablero.mostrar_vista_jugador()

    elif estado == EstadoJuego.RENDIDO:
        print("\n  JUEGO INTERRUMPIDO")
        print("  Decidiste rendirte antes de terminar.")
        resp = leer_texto("\n¿Querés ver dónde estaban los barcos? (s/n): ")
        if not resp or resp.lower() in ("s", "si", "sí"):
            tablero.mostrar_tablero_original()
        print("  Tus disparos:")
        tablero.mostrar_vista_jugador()

    disparos_usados = DISPAROS_TOTALES - disparos_restantes
    print(f"\n  Puntaje final      : {puntaje} puntos")
    print(f"  Disparos utilizados: {disparos_usados} de {DISPAROS_TOTALES}")

    if estado == EstadoJuego.GANADO:
        print("  ¡Sos un estratega nato!")
    elif puntaje > 50:
        print("  ¡Buen intento! Con un poco más de suerte, ¡la próxima es tuya!")
    else:
        print("  Consejo: ¡los barcos no se mueven! Estudiá patrones para ser más efectivo.")

    print("=" * 52 + "\n")


def mostrar_historial():
    """Muestra las últimas 20 partidas jugadas desde la base de datos."""
    from utilidades.db import get_historial

    filas = get_historial(20)

    print()
    print("=" * 68)
    print("                  HISTORIAL DE PARTIDAS")
    print("=" * 68)
    print()
    print(f"{'Jugador':<20}  {'Puntaje':>7}  {'Disparos':>8}  {'Resultado':<10}  Fecha")
    print("-" * 68)

    if not filas:
        print("  (Sin partidas registradas aún)")
    else:
        iconos = {"GANADO": "✓", "PERDIDO": "✗", "RENDIDO": "~"}
        for f in filas:
            icono  = iconos.get(f["resultado"], "?")
            nombre = f["nombre"][:18]
            fecha  = f["fecha"][:16]  # "YYYY-MM-DD HH:MM"
            print(
                f"  {nombre:<18}  {f['puntaje']:>7}  "
                f"{f['disparos_usados']:>8}  "
                f"{icono} {f['resultado']:<9}  {fecha}"
            )

    print()
    print("=" * 68)
    print()


# ------------------------------------------------------------------ #
#  Entry point                                                        #
# ------------------------------------------------------------------ #

def main():
    inicializar_db()  # Crea las tablas si no existen

    opcion = 0
    while opcion != 4:
        mostrar_menu()
        opcion = leer_entero("  Seleccione una opción: ")
        if opcion == 1:
            jugar()
        elif opcion == 2:
            ranking.mostrar_top10()
        elif opcion == 3:
            mostrar_historial()
        elif opcion == 4:
            print("\n  Gracias por jugar. ¡Hasta la próxima!\n")
        else:
            print("\n  Opción inválida. Intentá nuevamente.")


if __name__ == "__main__":
    main()