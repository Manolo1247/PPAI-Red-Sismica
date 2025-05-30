import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from entidades.estado import Estado
from entidades.empleado import Empleado
from entidades.estacionSismologica import EstacionSismologica

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
    
    def setEstado(self, estado):
        self.estado = estado

    def setFechaHoraCierre(self, fechaHoraCierre):
        self.fechaHoraCierre = fechaHoraCierre

    def setObservacionCierre(self, observacion):
        self.observacion_cierre = observacion

    def cerrar(self, fechaHora, estadoCerrada, observacion):
        self.setEstado(estadoCerrada)
        self.setFechaHoraCierre(fechaHora)
        self.setObservacionCierre(observacion)

        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql1 = (
                'UPDATE OrdenDeInspeccion '
                'SET fecha_hora_cierre = ?, ambito = ?, nombre = ?, observacion_cierre = ? '
                'WHERE numero = ?'
            )
            cursor.execute(sql1, (self.fechaHoraCierre, estadoCerrada.ambito, estadoCerrada.nombre, observacion, self.numero))
            con.commit()

    def fueraDeServicio(self, estadoFueraServicio, motivos, comentarios):
        self.estacion.fueraDeServicio(estadoFueraServicio, self.fechaHoraCierre, self.empleado, motivos, comentarios)

    def habilitarSismografo(self, estadoEnLinea):
        self.estacion.habilitarSismografo(estadoEnLinea, self.fechaHoraCierre, self.empleado)