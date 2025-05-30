from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


# Modelo: Estado
class EstadoModel(Model):
    ambito = CharField()
    nombre = CharField()

    class Meta:
        database = db
        table_name = "Estado"
        primary_key = CompositeKey("ambito", "nombre")
