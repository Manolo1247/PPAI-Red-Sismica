from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.empleadoModel import EmpleadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class UsuarioModel(Model):
    nombre = CharField(primary_key=True)
    contraseña = CharField()
    nombre_empleado = CharField()
    apellido_empleado = CharField()
    mail_empleado = CharField()

    class Meta:
        database = db
        table_name = "Usuario"

    @property
    def empleado(self):
        return EmpleadoModel.get_or_none(
            (EmpleadoModel.nombre == self.nombre_empleado)
            & (EmpleadoModel.apellido == self.apellido_empleado)
            & (EmpleadoModel.mail == self.mail_empleado)
        )
