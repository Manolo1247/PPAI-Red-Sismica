from peewee import *
from RUTAS.rutas import ARCHIVO_BD
from persistencia.sismografoModel import SismografoModel
from persistencia.empleadoModel import EmpleadoModel
from persistencia.estadoModel import EstadoModel

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)

class CambioEstadoModel(Model):
    fecha_hora_inicio = DateTimeField()
    ambito = CharField()
    nombre = CharField()
    sismografo = ForeignKeyField(
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
            "fecha_hora_inicio", "ambito", "nombre", "sismografo"
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

    @classmethod
    def findBySismografo(cls, sismo_id):
        from persistencia.motivoFueraServicioModel import MotivoFueraServicioModel

        from entidades.cambioEstado import CambioEstado
        from entidades.estado import Estado
        from entidades.motivoFueraServicio import MotivoFueraServicio
        from entidades.motivoTipo import MotivoTipo
        from entidades.empleado import Empleado
        from entidades.rol import Rol

        rowCambiosEstado = cls.select().where(cls.sismografo == sismo_id)
        cambios = []
        for rowCambioEstado in rowCambiosEstado:
            # Buscar motivos fuera de servicio asociados a este cambio de estado
            # si no tiene será un array vacío
            motivosFS = MotivoFueraServicioModel.findByCambioEstado(
                rowCambioEstado.fecha_hora_inicio,
                rowCambioEstado.ambito,
                rowCambioEstado.nombre
            )

            # Buscar el empleado y su rol
            rowEmpleado = rowCambioEstado.empleado
            rowRol = rowEmpleado.rol
            # Buscar el estado
            rowEstado = rowCambioEstado.estado

            cambios.append(
                CambioEstado(
                    rowCambioEstado.fecha_hora_inicio,
                    rowCambioEstado.fecha_hora_fin,
                    Empleado(
                        rowEmpleado.nombre,
                        rowEmpleado.apellido,
                        rowEmpleado.mail,
                        rowEmpleado.telefono,
                        Rol( rowRol.nombre, rowRol.descripcion ),
                    ),
                    Estado( rowEstado.ambito, rowEstado.nombre ),
                    motivosFS
                )
            )

        return cambios
    
    @classmethod
    def updateFromEntity(cls, cambioEstado, id_sismografo):
        from entidades.cambioEstado import CambioEstado
        if not isinstance(cambioEstado, CambioEstado):
            raise TypeError("El parámetro debe ser una instancia de CambioEstado")
        
        # Buscar el registro por clave compuesta
        row = cls.get_or_none(
            (cls.fecha_hora_inicio == cambioEstado.fechaHoraInicio) &
            (cls.ambito == cambioEstado.estado.ambito) &
            (cls.nombre == cambioEstado.estado.nombre) &
            (cls.sismografo == id_sismografo)
        )
        if not row:
            raise ValueError("No existe un CambioEstado con los datos proporcionados")

        # Actualizar los campos
        row.fecha_hora_fin = cambioEstado.fechaHoraFin
        if cambioEstado.empleado:
            row.nombre_empleado = cambioEstado.empleado.nombre
            row.apellido_empleado = cambioEstado.empleado.apellido
            row.mail_empleado = cambioEstado.empleado.mail
        if cambioEstado.estado:
            row.ambito = cambioEstado.estado.ambito
            row.nombre = cambioEstado.estado.nombre

        row.save()

    @classmethod
    def createFromEntity(cls, cambioEstado, id_sismografo):
        from entidades.cambioEstado import CambioEstado
        if not isinstance(cambioEstado, CambioEstado):
            raise TypeError("El parámetro debe ser una instancia de CambioEstado")
        
        # Crear el registro en la tabla CambioDeEstado
        cls.create(
            fecha_hora_inicio=cambioEstado.fechaHoraInicio,
            fecha_hora_fin=cambioEstado.fechaHoraFin,
            ambito=cambioEstado.estado.ambito,
            nombre=cambioEstado.estado.nombre,
            sismografo=id_sismografo,
            nombre_empleado=cambioEstado.empleado.nombre,
            apellido_empleado=cambioEstado.empleado.apellido,
            mail_empleado=cambioEstado.empleado.mail,
        )

        # Si hay motivos fuera de servicio, crearlos en la tabla correspondiente
        if hasattr(cambioEstado, "motivosFueraServicio") and cambioEstado.motivosFueraServicio:
            from persistencia.motivoFueraServicioModel import MotivoFueraServicioModel
            for motivo in cambioEstado.motivosFueraServicio:
                MotivoFueraServicioModel.createFromEntity(
                    motivo,
                    cambioEstado.fechaHoraInicio,
                    cambioEstado.estado.ambito,
                    cambioEstado.estado.nombre,
                    id_sismografo
                )