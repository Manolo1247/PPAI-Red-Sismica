from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.estacionSismologicaModel import EstacionSismologicaModel
from persistencia.estadoModel import EstadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)

class SismografoModel(Model):
    identificador = CharField(primary_key=True)
    fecha_adquisicion = DateTimeField(null=True)
    numero_serie = CharField(null=True)
    estacion = ForeignKeyField(
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

    @classmethod
    def findAll(cls):
        from persistencia.cambioEstadoModel import CambioEstadoModel

        from entidades.sismografo import Sismografo
        from entidades.estado import Estado
        from entidades.estacionSismologica import EstacionSismologica
        
        rowSismografos = cls.select()
        sismografos = []
        
        for rowSismografo in rowSismografos:
            # buscar cambios de estado
            cambiosEstado = CambioEstadoModel.findBySismografo(rowSismografo.identificador)
            # buscar estado actual
            rowEstado = rowSismografo.estado_actual
            # buscar estacion
            rowEstacion = rowSismografo.estacion

            sismografos.append(
                Sismografo(
                    rowSismografo.identificador,
                    rowSismografo.numero_serie,
                    rowSismografo.fecha_adquisicion,
                    Estado( rowEstado.ambito, rowEstado.nombre ),
                    EstacionSismologica(
                        rowEstacion.codigo_estacion,
                        rowEstacion.nombre,
                        rowEstacion.latitud,
                        rowEstacion.longitud,
                        rowEstacion.fecha_solicitud_certificacion,
                        rowEstacion.documento_certificacion,
                        rowEstacion.numero_certificacion
                    ),
                    cambiosEstado
                )
            )

        return sismografos