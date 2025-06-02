from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.estacionSismologicaModel import EstacionSismologicaModel
from persistencia.empleadoModel import EmpleadoModel
from persistencia.estadoModel import EstadoModel


# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class OrdenDeInspeccionModel(Model):
    numero = AutoField()  # INTEGER PRIMARY KEY AUTOINCREMENT
    estacion = ForeignKeyField(
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

    @classmethod
    def findAll(cls):
        from entidades.ordenDeInspeccion import OrdenDeInspeccion
        from entidades.empleado import Empleado
        from entidades.rol import Rol
        from entidades.estado import Estado
        from entidades.estacionSismologica import EstacionSismologica


        rowOrdenes = cls.select()

        ordenes = []
        for rowOrden in rowOrdenes:
            rowEstacion = rowOrden.estacion
            rowEmpleado = rowOrden.empleado
            rowEstado = rowOrden.estado

            ordenes.append(
                OrdenDeInspeccion(
                    rowOrden.numero,
                    rowOrden.fecha_hora_inicio,
                    rowOrden.fecha_hora_finalizacion,
                    rowOrden.fecha_hora_cierre,
                    rowOrden.observacion_cierre,
                    EstacionSismologica(
                        rowEstacion.codigo_estacion,
                        rowEstacion.nombre,
                        rowEstacion.latitud,
                        rowEstacion.longitud,
                        rowEstacion.fecha_solicitud_certificacion,
                        rowEstacion.documento_certificacion,
                        rowEstacion.numero_certificacion,
                    ),
                    Empleado(
                        rowEmpleado.nombre,
                        rowEmpleado.apellido,
                        rowEmpleado.mail,
                        rowEmpleado.telefono,
                        Rol(
                            rowEmpleado.rol.nombre,
                            rowEmpleado.rol.descripcion,
                        ),
                    ),
                    Estado(rowEstado.ambito, rowEstado.nombre),
                )
            )

        return ordenes

    @classmethod
    def updateFromEntity(cls, orden):
        from entidades.ordenDeInspeccion import OrdenDeInspeccion
        if not isinstance(orden, OrdenDeInspeccion):
            raise TypeError("El parámetro debe ser una instancia de OrdenDeInspeccion")

        
        # Buscar la orden en la BD
        row = cls.get_or_none(cls.numero == orden.numero)
        if not row:
            raise ValueError(f"No existe una orden con número {orden.numero}")

        # Actualizar los campos
        row.fecha_hora_inicio = orden.fechaHoraInicio
        row.fecha_hora_finalizacion = orden.fechaHoraFinalizacion
        row.fecha_hora_cierre = orden.fechaHoraCierre
        row.observacion_cierre = orden.observacion_cierre

        # Actualizar datos relacionados
        if orden.empleado:
            row.nombre_empleado = orden.empleado.nombre
            row.apellido_empleado = orden.empleado.apellido
            row.mail_empleado = orden.empleado.mail
        if orden.estado:
            row.ambito = orden.estado.ambito
            row.nombre = orden.estado.nombre
        if orden.estacion:
            row.estacion = orden.estacion.codigo

        row.save()