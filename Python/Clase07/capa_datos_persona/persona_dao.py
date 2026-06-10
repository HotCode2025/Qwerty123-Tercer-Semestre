from conexion import Conexion
from persona import Persona


class PersonaDao:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)"
    _ACTUALIZAR = (
        "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    )
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        print("Seleccionando personas...")

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(
                        registro[0], registro[1], registro[2], registro[3]
                    )
                    personas.append(persona)

        print(f"Insertando: {persona}")

    @classmethod
    def actualizar(cls, persona):
        print(f"Actualizando: {persona}")

    @classmethod
    def eliminar(cls, persona):
        print(f"Eliminando: {persona}")
