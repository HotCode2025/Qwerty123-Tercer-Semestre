"""
Módulo: jugadores.py
Descripción: Representa a un jugador del juego con su nombre y puntaje.
"""


class Jugadores:
    """Entidad que modela un jugador con nombre y puntaje encapsulados."""

    def __init__(self, nombre: str, puntaje: int):
        self.__nombre  = nombre
        self.__puntaje = puntaje

    # --- Getters y Setters ---

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        self.__nombre = valor

    @property
    def puntaje(self) -> int:
        return self.__puntaje

    @puntaje.setter
    def puntaje(self, valor: int):
        self.__puntaje = valor

    def __repr__(self) -> str:
        return f"Jugadores(nombre='{self.__nombre}', puntaje={self.__puntaje})"
