from .estado import Estado
from .empleado import Empleado
from .estacionSismologica import EstacionSismologica

class OrdenDeInspeccion:
    def __init__(self, numero, fechaHoraInicio, fechaHoraFinalizacion, fechaHoraCierre, observacion_cierre, estacion: EstacionSismologica, empleado: Empleado, estado: Estado):
        self.numero = numero
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFinalizacion = fechaHoraFinalizacion
        self.fechaHoraCierre = fechaHoraCierre
        self.observacion_cierre = observacion_cierre
        self.estacion = estacion
        self.empleado = empleado
        self.estado = estado

    def esDeEmpleado(self, empleado: Empleado):
        return self.empleado == empleado
    
    def estaRealizada(self):
        return self.estado.estaRealizada()
    
    def getNroOrden(self):
        return self.numero
    
    def getFechaFinalizacion(self):
        return self.fechaHoraFinalizacion
    
    def getNombreEstacion(self):
        return self.estacion.getNombre()
    
    def getSismografo(self):
        return self.estacion.getIdSismografo()