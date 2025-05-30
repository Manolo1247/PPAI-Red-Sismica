from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from estacionSismologicaModel import EstacionSismologicaModel
from estadoModel import EstadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class SismografoModel(Model):
    identificador = CharField(primary_key=True)
    fecha_adquisicion = DateTimeField(null=True)
    numero_serie = CharField(null=True)
    codigo_estacion = ForeignKeyField(
        EstacionSismologicaModel, backref="sismografos", column_name="codigo_estacion"
    )
    ambito_estado_actual = CharField()
    nombre_estado_actual = CharField()

    class Meta:
        database = db
        table_name = "Sismografo"

    @property
    def estado_actual(self):
        return EstadoModel.get_or_none(
            (EstadoModel.ambito == self.ambito_estado_actual)
            & (EstadoModel.nombre == self.nombre_estado_actual)
        )
