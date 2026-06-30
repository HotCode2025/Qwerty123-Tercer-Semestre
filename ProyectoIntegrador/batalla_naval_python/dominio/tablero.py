"""
Módulo: tablero.py
Descripción: Clase principal del juego. Gestiona el tablero 8x8, la colocación
             aleatoria de barcos, el sistema de disparos y la visualización.
"""

import random
import copy
from .tipo_barco import TipoBarco


class Tablero:
    """
    Clase central del juego Batalla Naval.

    Atributos privados:
        __FILAS / __COLUMNAS : Dimensiones fijas del tablero (8x8).
        __barcos             : Matriz interna con IDs de barcos (0 = agua).
        __vista_jugador      : Matriz visible para el jugador ('?' sin disparar).
        __copia_original     : Snapshot del tablero para mostrar la solución al final.
    """

    FILAS = 8
    COLUMNAS = 8

    # Símbolos de celda
    AGUA = "O"  # disparo al agua
    IMPACTO = "X"  # parte de barco golpeada
    HUNDIDO = "#"  # barco completamente hundido
    SIN_DISP = "?"  # celda no disparada
    SIM_AGUA = "~"  # agua en tablero original

    def __init__(self):
        self.__barcos = [[0] * self.COLUMNAS for _ in range(self.FILAS)]
        self.__vista_jugador = [
            [self.SIN_DISP] * self.COLUMNAS for _ in range(self.FILAS)
        ]
        self.__copia_original = [[0] * self.COLUMNAS for _ in range(self.FILAS)]

    # ------------------------------------------------------------------ #
    #  Colocación de barcos                                               #
    # ------------------------------------------------------------------ #

    def colocar_barcos(self):
        """Coloca todos los tipos de barco de forma aleatoria y guarda una copia."""
        self.__colocar_barco(TipoBarco.SUBMARINO)
        self.__colocar_barco(TipoBarco.CRUCERO)
        self.__colocar_barco(TipoBarco.DESTRUCTOR)
        self.__copiar_barcos()

    def __colocar_barco(self, tipo: TipoBarco):
        """
        Coloca un barco del tipo dado en una posición aleatoria válida.
        El bucle while repite intentos aleatorios hasta encontrar una posición libre.
        """
        tamanio = tipo.tamanio
        id_barco = tipo.to_id()
        colocado = False

        while not colocado:
            fila = random.randint(0, self.FILAS - 1)
            columna = random.randint(0, self.COLUMNAS - 1)
            horizontal = random.choice([True, False])

            if horizontal and columna + tamanio <= self.COLUMNAS:
                # Verificar que todas las celdas necesarias estén libres
                if all(self.__barcos[fila][columna + j] == 0 for j in range(tamanio)):
                    for j in range(tamanio):
                        self.__barcos[fila][columna + j] = id_barco
                    colocado = True

            elif not horizontal and fila + tamanio <= self.FILAS:
                if all(self.__barcos[fila + i][columna] == 0 for i in range(tamanio)):
                    for i in range(tamanio):
                        self.__barcos[fila + i][columna] = id_barco
                    colocado = True

    def __copiar_barcos(self):
        """Crea una copia profunda del estado actual de los barcos como snapshot."""
        self.__copia_original = copy.deepcopy(self.__barcos)

    # ------------------------------------------------------------------ #
    #  Sistema de disparos                                                #
    # ------------------------------------------------------------------ #