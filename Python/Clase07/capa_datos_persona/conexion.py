import psycopg2 as bd
from logger_base import log
import sys


class Conexion:
    DATABASE = "persona_db"
    USERNAME = "postgres"
    PASSWORD = "admin"
    DB_PORT = "5432"
    HOST = "127.0.0.1"

    conexion = None
    cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.conexion is None:
            try:
                cls.conexion = bd.connect(
                    host=cls.HOST,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                )

                log.debug(f"Conexión exitosa: {cls.conexion}")

            except Exception as e:
                log.error(f"Ocurrió un error al conectar a la base de datos: {e}")
                sys.exit()

        return cls.conexion

    @classmethod
    def obtenerCursor(cls):
        if cls.cursor is None:
            try:
                cls.cursor = cls.obtenerConexion().cursor()

                log.debug(f"Se abrió correctamente el cursor: {cls.cursor}")

            except Exception as e:
                log.error(f"Ocurrió un error al abrir el cursor: {e}")
                sys.exit()

        return cls.cursor

    @classmethod
    def cerrar(cls):
        try:
            if cls.cursor is not None:
                cls.cursor.close()
                log.debug("Se cerró correctamente el cursor")
                cls.cursor = None

            if cls.conexion is not None:
                cls.conexion.close()
                log.debug("Se cerró correctamente la conexión")
                cls.conexion = None

        except Exception as e:
            log.error(f"Ocurrió un error al cerrar la conexión: {e}")
            sys.exit()


if __name__ == "__main__":
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()
