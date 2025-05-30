from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from sismografoModel import SismografoModel
from empleadoModel import EmpleadoModel
from estadoModel import EstadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class CambioEstadoModel(Model):
    fecha_hora_inicio = DateTimeField()
    ambito = CharField()
    nombre = CharField()
    identificador_sismografo = ForeignKeyField(
        SismografoModel,
        backref="cambios_estado",
        column_name="identificador_sismografo",
    )
    fecha_hora_fin = DateTimeField(null=True)
    nombre_empleado = CharField()
    apellido_empleado = CharField()
    mail_empleado = CharField()

    class Meta:
        database = db
        table_name = "CambioDeEstado"
        primary_key = CompositeKey(
            "fecha_hora_inicio", "ambito", "nombre", "identificador_sismografo"
        )

    @property
    def estado(self):
        return EstadoModel.get_or_none(
            (EstadoModel.ambito == self.ambito) & (EstadoModel.nombre == self.nombre)
        )

    @property
    def empleado(self):
        return EmpleadoModel.get_or_none(
            (EmpleadoModel.nombre == self.nombre_empleado)
            & (EmpleadoModel.apellido == self.apellido_empleado)
            & (EmpleadoModel.mail == self.mail_empleado)
        )
