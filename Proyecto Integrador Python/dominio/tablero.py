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

    def disparar(self, fila: int, columna: int) -> bool:
        """
        Ejecuta un disparo en la posición indicada.

        Returns:
            True  si el disparo fue válido (celda no disparada previamente).
            False si la coordenada es inválida o ya fue disparada.
        """
        if not (0 <= fila < self.FILAS and 0 <= columna < self.COLUMNAS):
            return False
        if self.__vista_jugador[fila][columna] != self.SIN_DISP:
            return False

        valor = self.__barcos[fila][columna]
        if valor == 0:
            self.__vista_jugador[fila][columna] = self.AGUA
        else:
            self.__vista_jugador[fila][columna] = self.IMPACTO
            # Marcar como hundido y limpiar en __barcos si el barco fue completamente destruido
            if self.__barco_hundido(valor):
                self.__marcar_hundido(valor)
                self.__limpiar_barco(valor)

        return True

    def __barco_hundido(self, tipo_id: int) -> bool:
        """Verifica si todas las celdas del barco han sido impactadas."""
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if (
                    self.__barcos[i][j] == tipo_id
                    and self.__vista_jugador[i][j] == self.SIN_DISP
                ):
                    return False
        return True

    def __marcar_hundido(self, tipo_id: int):
        """Cambia los símbolos de IMPACTO a HUNDIDO para el barco indicado."""
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if (
                    self.__barcos[i][j] == tipo_id
                    and self.__vista_jugador[i][j] == self.IMPACTO
                ):
                    self.__vista_jugador[i][j] = self.HUNDIDO

    def __limpiar_barco(self, tipo_id: int):
        """Pone a 0 las celdas del barco hundido en la matriz interna."""
        for i in range(self.FILAS):
            for j in range(self.COLUMNAS):
                if self.__barcos[i][j] == tipo_id:
                    self.__barcos[i][j] = 0

    def juego_finalizado(self) -> bool:
        """Retorna True si no quedan barcos sin hundir en el tablero."""
        return all(
            self.__barcos[i][j] == 0
            for i in range(self.FILAS)
            for j in range(self.COLUMNAS)
        )

    # ------------------------------------------------------------------ #
    #  Visualización                                                      #
    # ------------------------------------------------------------------ #

    def mostrar_vista_jugador(self):
        """Muestra el tablero con el estado de los disparos del jugador."""
        print("\n    A B C D E F G H")
        print("   " + "-" * 17)
        for i in range(self.FILAS):
            fila_str = " ".join(self.__vista_jugador[i])
            print(f"{i + 1:>2} | {fila_str}")

    def mostrar_tablero_original(self):
        """Muestra la ubicación real de todos los barcos (solución)."""
        simbolo_map = {1: "S", 2: "D", 3: "C"}
        print("\n=== UBICACIÓN DE LAS NAVES EN EL TABLERO ===")
        print("    A B C D E F G H")
        print("   " + "-" * 17)
        for i in range(self.FILAS):
            celdas = []
            for j in range(self.COLUMNAS):
                id_b = self.__copia_original[i][j]
                celdas.append(simbolo_map.get(id_b, self.SIM_AGUA))
            print(f"{i + 1:>2} | {' '.join(celdas)}")
        print()
        print(
            "S = Submarino (1)  |  D = Destructor (2)  |  C = Crucero (3)  |  ~ = Agua"
        )
        print()

    # ------------------------------------------------------------------ #
    #  Getters                                                            #
    # ------------------------------------------------------------------ #

    @property
    def vista_jugador(self) -> list[list[str]]:
        return self.__vista_jugador

    @property
    def copia_original(self) -> list[list[int]]:
        return self.__copia_original