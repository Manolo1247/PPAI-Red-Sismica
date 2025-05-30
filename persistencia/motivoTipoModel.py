from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class MotivoTipoModel(Model):
    descripcion = CharField(primary_key=True)

    class Meta:
        database = db
        table_name = "MotivoTipo"
