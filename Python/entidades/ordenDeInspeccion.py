from .estado import Estado
from .empleado import Empleado
from .estacionSismologica import EstacionSismologica

class OrdenDeInspeccion:
    def __init__(self, numero, fechaHoraInicio, fechaHoraFinalizacion, fechaHoraCierre, estacion: EstacionSismologica, empleado: Empleado, estado: Estado):
        self.numero = numero
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFinalizacion = fechaHoraFinalizacion
        self.fechaHoraCierre = fechaHoraCierre
        self.estacion = estacion
        self.empleado = empleado
        self.estado = estado
