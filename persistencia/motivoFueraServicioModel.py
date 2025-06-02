from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.cambioEstadoModel import CambioEstadoModel
from persistencia.motivoTipoModel import MotivoTipoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)

class MotivoFueraServicioModel(Model):
    fecha_hora_inicio = DateTimeField()
    ambito = CharField()
    nombre = CharField()
    id_sismografo = CharField()
    motivo_tipo = ForeignKeyField(
        MotivoTipoModel, backref="motivos_fuera_servicio", column_name="motivo_tipo"
    )
    comentario = TextField(null=True)

    class Meta:
        database = db
        table_name = "MotivoFueraServicio"
        primary_key = CompositeKey(
            "fecha_hora_inicio", "ambito", "nombre", "motivo_tipo"
        )

    @property
    def cambio_de_estado(self):
        return CambioEstadoModel.get_or_none(
            (CambioEstadoModel.fecha_hora_inicio == self.fecha_hora_inicio)
            & (CambioEstadoModel.ambito == self.ambito)
            & (CambioEstadoModel.nombre == self.nombre)
            & (CambioEstadoModel.identificador_sismografo == self.id_sismografo)
        )

    @classmethod
    def findByCambioEstado(cls, inicio, ambito, nombre):
        from entidades.motivoFueraServicio import MotivoFueraServicio
        from entidades.motivoTipo import MotivoTipo

        rowMotivosFS = cls.select().where(
            (cls.fecha_hora_inicio == inicio) & (cls.nombre == nombre) & (cls.ambito == ambito)
        )

        motivos = []
        for rowMotivoFS in rowMotivosFS:
            rowTipo = rowMotivoFS.motivo_tipo
            motivos.append(
                MotivoFueraServicio(
                    rowMotivoFS.comentario,
                    MotivoTipo(rowTipo.descripcion)
                )
            )

        return motivos
    
    @classmethod
    def createFromEntity(cls, motivoFS, fecha_hora_inicio, ambito, nombre, id_sismografo):
        from entidades.motivoFueraServicio import MotivoFueraServicio
        if not isinstance(motivoFS, MotivoFueraServicio):
            raise TypeError("El parámetro debe ser una instancia de MotivoFueraServicio")

        # Buscar el MotivoTipoModel correspondiente
        motivo_tipo_row = MotivoTipoModel.get_or_none(MotivoTipoModel.descripcion == motivoFS.motivoTipo.descripcion)
        if not motivo_tipo_row:
            raise ValueError(f"No existe un MotivoTipo con descripción '{motivoFS.motivoTipo.descripcion}'")

        # Crear el registro usando la instancia de MotivoTipoModel
        cls.create(
            fecha_hora_inicio=fecha_hora_inicio,
            ambito=ambito,
            nombre=nombre,
            id_sismografo=id_sismografo,
            motivo_tipo=motivo_tipo_row,
            comentario=motivoFS.comentario
        )