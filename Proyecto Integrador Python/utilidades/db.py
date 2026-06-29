"""
Módulo: db.py
Descripción: Capa de acceso a datos SQLite para Batalla Naval.
             Gestiona la conexión, creación de tablas y operaciones de
             persistencia para jugadores, partidas y ranking.
"""

import sqlite3
import os
from pathlib import Path


# Ruta del archivo de base de datos (en el directorio raíz del proyecto)
DB_PATH = Path(__file__).parent.parent / "batalla_naval.db"


def _get_connection() -> sqlite3.Connection:
    """Abre y retorna una conexión a la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar_db():
    """
    Crea las tablas si no existen.
    Debe llamarse una vez al iniciar la aplicación.
    """
    with _get_connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS jugadores (
                id     INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT    NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS partidas (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                jugador_id      INTEGER NOT NULL,
                puntaje         INTEGER NOT NULL,
                disparos_usados INTEGER NOT NULL,
                resultado       TEXT    NOT NULL,
                fecha           TEXT    DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (jugador_id) REFERENCES jugadores(id)
            );
        """)


def guardar_partida(nombre: str, puntaje: int, disparos_usados: int, resultado: str):
    """
    Registra una partida completa en la base de datos.

    Inserta o reutiliza el jugador según su nombre, luego inserta
    la partida vinculada a ese jugador.

    Args:
        nombre:          Nombre del jugador.
        puntaje:         Puntaje obtenido en la partida.
        disparos_usados: Cantidad de disparos realizados.
        resultado:       'GANADO', 'PERDIDO' o 'RENDIDO'.
    """
    nombre = nombre.strip() or "Jugador"

    with _get_connection() as conn:
        # Insertar jugador si no existe; ignorar si ya está (UNIQUE)
        conn.execute(
            "INSERT OR IGNORE INTO jugadores (nombre) VALUES (?)",
            (nombre,)
        )
        jugador = conn.execute(
            "SELECT id FROM jugadores WHERE nombre = ?",
            (nombre,)
        ).fetchone()

        conn.execute(
            """
            INSERT INTO partidas (jugador_id, puntaje, disparos_usados, resultado)
            VALUES (?, ?, ?, ?)
            """,
            (jugador["id"], puntaje, disparos_usados, resultado)
        )


def get_top10() -> list[dict]:
    """
    Retorna el Top 10 de jugadores con su mejor puntaje histórico.

    Agrupa por jugador y toma el puntaje máximo de todas sus partidas.

    Returns:
        Lista de dicts con claves: nombre, puntaje, partidas_jugadas.
    """
    with _get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                j.nombre,
                MAX(p.puntaje)    AS puntaje,
                COUNT(p.id)       AS partidas_jugadas
            FROM partidas p
            JOIN jugadores j ON j.id = p.jugador_id
            GROUP BY j.id
            ORDER BY puntaje DESC
            LIMIT 10
            """
        ).fetchall()

    return [dict(row) for row in rows]


def get_historial(limite: int = 20) -> list[dict]:
    """
    Retorna las últimas partidas jugadas ordenadas por fecha descendente.

    Args:
        limite: Cantidad máxima de registros a retornar (default 20).

    Returns:
        Lista de dicts con claves: nombre, puntaje, disparos_usados,
        resultado, fecha.
    """
    with _get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                j.nombre,
                p.puntaje,
                p.disparos_usados,
                p.resultado,
                p.fecha
            FROM partidas p
            JOIN jugadores j ON j.id = p.jugador_id
            ORDER BY p.fecha DESC
            LIMIT ?
            """,
            (limite,)
        ).fetchall()

    return [dict(row) for row in rows]