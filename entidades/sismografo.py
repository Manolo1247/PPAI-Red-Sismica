from entidades.estado import Estado
from entidades.estacionSismologica import EstacionSismologica
from entidades.cambioEstado import CambioEstado
from typing import List

class Sismografo:
    def __init__(self, identificador, numeroSerie, fechaAdquisicion, estadoActual: Estado, estacionSismologica: EstacionSismologica, cambiosEstado: List[CambioEstado]):
        self.identificador = identificador
        self.numeroSerie = numeroSerie
        self.fechaAdquisicion = fechaAdquisicion
        self.estadoActual = estadoActual
        self.estacionSismologica = estacionSismologica
        self.cambiosEstado = cambiosEstado

    def esTuEstacion(self, estacion):
        return estacion == self.estacionSismologica
    
    def getId(self):
        return self.identificador

    def setEstadoActual(self, estado):
        self.estadoActual = estado

    def fueraDeServicio(self, estadoFueraServicio, fechaHoraFin, empleado, motivos, comentarios):
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esActual():
                cambioEstado.setFechaHoraFin(fechaHoraFin)
                break
        
        # Setear el estado actual del sismografo
        self.setEstadoActual(estadoFueraServicio)
        
        # Nuevo:CambioEstado
        cambioEstado = CambioEstado(fechaHoraFin, None, empleado, estadoFueraServicio, [], motivos=motivos, comentarios=comentarios)
        self.cambiosEstado.append(cambioEstado)

    def habilitar(self, estadoEnLinea, fechaHoraFin, empleado):       
        for cambioEstado in self.cambiosEstado:
            if cambioEstado.esActual():
                cambioEstado.setFechaHoraFin(fechaHoraFin)
                break

        # Setear el estado actual del sismografo
        self.setEstadoActual(estadoEnLinea)

        # Nuevo:CambioEstado
        cambioEstado = CambioEstado(fechaHoraFin, None, empleado, estadoEnLinea, [])
        self.cambiosEstado.append(cambioEstado)