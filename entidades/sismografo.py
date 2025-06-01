import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from entidades.estado import Estado
from entidades.estacionSismologica import EstacionSismologica
from entidades.cambioEstado import CambioEstado

class Sismografo:
    def __init__(self, identificador, numeroSerie, fechaAdquisicion, estadoActual: Estado, estacionSismologica: EstacionSismologica, cambiosEstado: CambioEstado):
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
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = (
                'UPDATE Sismografo '
                'SET ambito_estado_actual = ?, nombre_estado_actual = ? '
                'WHERE identificador = ?'
            )
            cursor.execute(sql, (self.estadoActual.ambito, self.estadoActual.nombre, self.identificador))
            con.commit()

    def fueraDeServicio(self, estadoFueraServicio, fechaHoraFin, empleado, motivos, comentarios):
        for CE in self.cambiosEstado:
            if CE.esActual():
                CE.setFechaHoraFin(fechaHoraFin, self.identificador)    # Actual:CambioEstado
                break
        # Setear el estado actual del sismografo
        self.setEstadoActual(estadoFueraServicio)
        
        # Nuevo:CambioEstado
        cambioEstado = CambioEstado(fechaHoraFin, None, empleado, estadoFueraServicio, [], motivos=motivos, comentarios=comentarios)
        self.cambiosEstado.append(cambioEstado)

        # Guardar 
        cambioEstado.guardar(self.identificador)

    def habilitar(self, estadoEnLinea, fechaHoraFin, empleado):
        for CE in self.cambiosEstado:
            if CE.esActual():
                CE.setFechaHoraFin(fechaHoraFin, self.identificador)    # Actual:CambioEstado
                break
        # Setear el estado actual del sismografo
        self.setEstadoActual(estadoEnLinea)

        # Nuevo:CambioEstado
        cambioEstado = CambioEstado(fechaHoraFin, None, empleado, estadoEnLinea, [])
        self.cambiosEstado.append(cambioEstado)
        
        # Guardar 
        cambioEstado.guardar(self.identificador)