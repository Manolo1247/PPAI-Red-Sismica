from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class EstacionSismologicaModel(Model):
    codigo_estacion = CharField(primary_key=True)
    nombre = CharField()
    latitud = FloatField()
    longitud = FloatField()
    fecha_solicitud_certificacion = DateTimeField(null=True)
    documento_certificacion = CharField(null=True)
    numero_certificacion = CharField(null=True)

    class Meta:
        database = db
        table_name = "EstacionSismologica"
