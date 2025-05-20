import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from .estado import Estado
from .motivoFueraServicio import MotivoFueraServicio
from .motivoTipo import MotivoTipo
from .empleado import Empleado

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, empleado, estado, motivoFueraServicio, motivos=[], comentarios=[], idSismografo=None):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.empleado = empleado
        self.estado = estado
        self.motivoFueraServicio = motivoFueraServicio

        if self.estado.esFueraDeServicio() and len(self.motivoFueraServicio) == 0:
            self.crearMotivos(motivos, comentarios, idSismografo)

    def esActual(self):
        return self.fechaHoraFin is None
    
    def setFechaHoraFin(self, fechaHoraFin, idSismografo):
        self.fechaHoraFin = fechaHoraFin

        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql1 = (
                'UPDATE CambioDeEstado '
                'SET fecha_hora_fin = ? '
                'WHERE identificador_sismografo = ? AND fecha_hora_inicio = ? AND ambito = ? AND nombre = ?'
            )
            cursor.execute(sql1, (self.fechaHoraFin, idSismografo, self.fechaHoraInicio, self.estado.ambito, self.estado.nombre))
            con.commit()

    def crearMotivos(self, motivos, comentarios, idSismografo):      
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            # Guardar Cambio de Estado
            sql_CE = (
                'INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, nombre_empleado, apellido_empleado, mail_empleado) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)'
            )
            cursor.execute(sql_CE, (self.fechaHoraInicio, self.estado.ambito, self.estado.nombre, idSismografo, self.empleado.nombre, self.empleado.apellido, self.empleado.mail))
            con.commit()

            # Guardar Motivos Fuera de Servicio
            n = len(motivos)
            for i in range(n):
                motivo = motivos[i]
                comentario = comentarios[i]
                motivoFueraServicio = MotivoFueraServicio(comentario, MotivoTipo(motivo))
                self.motivoFueraServicio.append(motivoFueraServicio)

                sql_MFS = (
                'INSERT INTO MotivoFueraServicio (fecha_hora_inicio, ambito, nombre, motivo_tipo, comentario, id_sismografo) '
                'VALUES (?, ?, ?, ?, ?, ?)'
                )
                cursor.execute(sql_MFS, (self.fechaHoraInicio, self.estado.ambito, self.estado.nombre, motivoFueraServicio.motivoTipo.descripcion, motivoFueraServicio.comentario, idSismografo))
            con.commit()