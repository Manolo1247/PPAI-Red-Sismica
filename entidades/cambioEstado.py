import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from entidades.estado import Estado
from entidades.motivoFueraServicio import MotivoFueraServicio
from entidades.motivoTipo import MotivoTipo
from entidades.empleado import Empleado

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, empleado, estado, motivoFueraServicio, motivos=[], comentarios=[]):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.empleado = empleado
        self.estado = estado
        self.motivosFueraServicio = motivoFueraServicio

        if self.estado.esFueraDeServicio() and len(self.motivosFueraServicio) == 0:
            self.crearMotivos(motivos, comentarios)

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

    def crearMotivos(self, motivos, comentarios):              
        n = len(motivos)
        for i in range(n):
            motivo = motivos[i]
            comentario = comentarios[i]
            motivoFueraServicio = MotivoFueraServicio(comentario, MotivoTipo(motivo))
            
            self.motivosFueraServicio.append(motivoFueraServicio)

    def guardar(self, idSismografo):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql_CE = (
                'INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, nombre_empleado, apellido_empleado, mail_empleado) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)'
            )
            cursor.execute(sql_CE, (self.fechaHoraInicio, self.estado.ambito, self.estado.nombre, idSismografo, self.empleado.nombre, self.empleado.apellido, self.empleado.mail))
            con.commit()

            for motivoFueraServicio in self.motivosFueraServicio:
                sql_MFS = (
                'INSERT INTO MotivoFueraServicio (fecha_hora_inicio, ambito, nombre, motivo_tipo, comentario, id_sismografo) '
                'VALUES (?, ?, ?, ?, ?, ?)'
                )
                cursor.execute(sql_MFS, (self.fechaHoraInicio, self.estado.ambito, self.estado.nombre, motivoFueraServicio.motivoTipo.descripcion, motivoFueraServicio.comentario, idSismografo))
            con.commit()