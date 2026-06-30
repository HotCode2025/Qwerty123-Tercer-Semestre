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
