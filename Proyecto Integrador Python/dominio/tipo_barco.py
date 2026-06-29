"""
Módulo: tipo_barco.py
Descripción: Define los tipos de barcos disponibles en el juego mediante un Enum.
             Cada barco tiene un tamaño y un símbolo visual asociado.
"""

from enum import Enum


class TipoBarco(Enum):
    """
    Enumeración de tipos de barcos con sus atributos de tamaño y símbolo.

    Uso de Enum: Representa un conjunto cerrado y fijo de constantes con comportamiento
    asociado, garantizando seguridad de tipo y evitando instancias no válidas.
    """
    SUBMARINO  = (1, 'S')
    DESTRUCTOR = (2, 'D')
    CRUCERO    = (3, 'C')

    def __init__(self, tamanio: int, simbolo: str):
        self.tamanio = tamanio
        self.simbolo = simbolo

    @staticmethod
    def from_id(id_barco: int) -> "TipoBarco":
        """Retorna el TipoBarco correspondiente a un ID numérico."""
        mapa = {1: TipoBarco.SUBMARINO, 2: TipoBarco.DESTRUCTOR, 3: TipoBarco.CRUCERO}
        if id_barco not in mapa:
            raise ValueError(f"ID de barco no válido: {id_barco}")
        return mapa[id_barco]

    def to_id(self) -> int:
        """Retorna el ID numérico del tipo de barco."""
        mapa = {TipoBarco.SUBMARINO: 1, TipoBarco.DESTRUCTOR: 2, TipoBarco.CRUCERO: 3}
        return mapa[self]