"""
Módulo: utilidades.py
Descripción: Clase de utilidad con métodos estáticos para operaciones comunes del juego.
             Facilita la conversión y validación de coordenadas (ej: "A5" → [fila, col]).
"""


class Utilidades:
    """
    Clase de utilidad estática. No se puede instanciar.
    Provee métodos auxiliares reutilizables en todo el proyecto.
    """

    # Mapeo de letras de columna a índice (tablero 8x8: A-H)
    _LETRA_A_COLUMNA: dict[str, int] = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3,
        'E': 4, 'F': 5, 'G': 6, 'H': 7,
    }

    def __new__(cls, *args, **kwargs):
        raise TypeError("Clase de utilidad: no se puede instanciar.")

    @classmethod
    def letra_a_columna(cls, letra: str) -> int:
        """
        Convierte una letra de columna (A-H) a su índice numérico (0-7).

        Returns:
            Índice de columna o -1 si la letra no es válida.
        """
        return cls._LETRA_A_COLUMNA.get(letra.upper(), -1)

    @classmethod
    def parsear_coordenada(cls, coordenada: str) -> list[int] | None:
        """
        Convierte una cadena de coordenada (ej: "A5", "h3") a [fila, columna].

        Args:
            coordenada: Cadena tipo "A5", "b2", etc.

        Returns:
            Lista [fila, columna] (base 0) o None si la coordenada es inválida.
        """
        if not coordenada or len(coordenada) < 2:
            return None

        coordenada = coordenada.strip().upper()
        letra   = coordenada[0]
        num_str = coordenada[1:].strip()

        if not num_str.isdigit():
            return None

        columna = cls.letra_a_columna(letra)
        fila    = int(num_str) - 1  # El jugador ve 1-8; internamente es 0-7

        if columna < 0 or columna > 7 or fila < 0 or fila > 7:
            return None

        return [fila, columna]