from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.estacionSismologicaModel import EstacionSismologicaModel
from persistencia.empleadoModel import EmpleadoModel
from persistencia.estadoModel import EstadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class OrdenDeInspeccionModel(Model):
    numero = AutoField()  # INTEGER PRIMARY KEY AUTOINCREMENT
    codigo_estacion = ForeignKeyField(
        EstacionSismologicaModel,
        backref="ordenes_inspeccion",
        column_name="codigo_estacion",
        null=True,
    )
    fecha_hora_inicio = DateTimeField(null=True)
    fecha_hora_finalizacion = DateTimeField(null=True)
    fecha_hora_cierre = DateTimeField(null=True)
    observacion_cierre = TextField(null=True)
    nombre_empleado = CharField(null=True)
    apellido_empleado = CharField(null=True)
    mail_empleado = CharField(null=True)
    ambito = CharField(null=True)
    nombre = CharField(null=True)

    class Meta:
        database = db
        table_name = "OrdenDeInspeccion"

    @property
    def empleado(self):
        return EmpleadoModel.get_or_none(
            (EmpleadoModel.nombre == self.nombre_empleado)
            & (EmpleadoModel.apellido == self.apellido_empleado)
            & (EmpleadoModel.mail == self.mail_empleado)
        )

    @property
    def estado(self):
        return EstadoModel.get_or_none(
            (EstadoModel.ambito == self.ambito) & (EstadoModel.nombre == self.nombre)
        )
