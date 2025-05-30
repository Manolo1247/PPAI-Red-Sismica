from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.rolModel import RolModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class EmpleadoModel(Model):
    nombre = CharField()
    apellido = CharField()
    mail = CharField()
    telefono = CharField(null=True)
    rol = ForeignKeyField(RolModel, backref="empleados", column_name="rol")

    class Meta:
        database = db
        table_name = "Empleado"
        primary_key = CompositeKey("nombre", "apellido", "mail")
