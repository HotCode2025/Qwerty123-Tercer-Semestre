"""
Módulo: ranking.py
Descripción: Gestiona el ranking de jugadores delegando la persistencia a SQLite.
             Mantiene la misma interfaz pública que la versión en memoria para
             no romper el código existente en batalla_naval.py y batallaNaval_pygame.py.
"""

from dominio.jugadores import Jugadores
from utilidades.db import get_top10


class Ranking:
    """
    Ranking de jugadores respaldado por SQLite.

    La inserción de nuevas partidas se realiza directamente a través de
    utilidades.db.guardar_partida(); esta clase solo se ocupa de la consulta
    y visualización del Top 10.
    """

    def agregar_jugador(self, nuevo: Jugadores):
        """
        Compatibilidad con la interfaz anterior.

        En la nueva arquitectura la persistencia se hace desde batalla_naval.py
        y batallaNaval_pygame.py via db.guardar_partida(), por lo que este
        método ya no necesita hacer nada. Se conserva para no romper llamadas
        existentes durante la transición.
        """
        pass  # La escritura la hace db.guardar_partida() en el flujo de partida

    @property
    def jugadores(self) -> list[Jugadores]:
        """
        Retorna la lista del Top 10 como objetos Jugadores.
        Usado por la versión Pygame para dibujar el ranking en pantalla.
        """
        filas = get_top10()
        return [Jugadores(f["nombre"], f["puntaje"]) for f in filas]

    def mostrar_top10(self):
        """Muestra los 10 mejores jugadores en consola (versión texto)."""
        filas = get_top10()

        print()
        print("=" * 42)
        print("       TOP 10 MEJORES JUGADORES")
        print("=" * 42)
        print()
        print("Pos.   Jugador               Puntaje   Partidas")
        print("-----  --------------------  -------   --------")

        if not filas:
            print("  (Sin registros aún)")
        else:
            for i, f in enumerate(filas):
                if f["puntaje"] <= 0:
                    break
                pos    = f" {i + 1:>2}."
                nombre = (
                    f["nombre"][:17] + "..."
                    if len(f["nombre"]) > 17
                    else f["nombre"].ljust(20)
                )
                print(
                    f"{pos}    {nombre}  {f['puntaje']:>5} pts"
                    f"   {f['partidas_jugadas']:>2} partida(s)"
                )

        print()
        print("=" * 42)
        print()