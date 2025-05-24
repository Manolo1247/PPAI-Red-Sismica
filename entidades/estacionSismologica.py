import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from entidades.sismografo import Sismografo
from entidades.estado import Estado
from entidades.cambioEstado import CambioEstado
from entidades.empleado import Empleado
from entidades.rol import Rol
from entidades.motivoFueraServicio import MotivoFueraServicio
from entidades.motivoTipo import MotivoTipo

class EstacionSismologica:
    def __init__(self, codigo, nombre, latitud, longitud, fechaSolicitudCertificacion, documentoCertificacion, numeroCertificacion):
        self.codigo = codigo
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self.documentoCertificacion = documentoCertificacion
        self.numeroCertificacion = numeroCertificacion

    def getNombre(self):
        return self.nombre
    
    def getIdSismografo(self):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql1 = (
                'SELECT S.identificador, S.numero_serie, S.fecha_adquisicion '
                'FROM Sismografo S '
                'WHERE S.codigo_estacion = ?'
            )
            cursor.execute(sql1, (self.codigo,))
            row = cursor.fetchone()

        sismografo = Sismografo(row[0], row[1], row[2], None, None, None)
        return sismografo.getId()

    def fueraDeServicio(self, estadoFueraServicio, fechaHoraFin, empleado, motivosSeleccionados, comentarios):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = (
                'SELECT S.identificador, S.numero_serie, S.fecha_adquisicion, S.ambito_estado_actual, S.nombre_estado_actual '
                'FROM Sismografo S WHERE codigo_estacion = ?'
            )
            cursor.execute(sql, (self.codigo,))
            rowSismografo = cursor.fetchone()
            sql = (
                'SELECT C.fecha_hora_inicio, C.fecha_hora_fin, C.ambito, C.nombre, '
                'E.nombre, E.apellido, E.mail, E.telefono, R.nombre, R.descripcion '
                'FROM CambioDeEstado C JOIN Empleado E ON C.nombre_empleado = E.nombre AND C.apellido_empleado = E.apellido AND C.mail_empleado = E.mail '
                'JOIN Rol R ON E.rol = R.nombre '
                'WHERE C.identificador_sismografo = ?'
            )
            cursor.execute(sql, (rowSismografo[0],))
            rowCambioEstado = cursor.fetchall()

        estadoSismografo = Estado(rowSismografo[3], rowSismografo[4])
        cambiosEstado = []
        for cambio in rowCambioEstado:
            rol = Rol(cambio[8], cambio[9])
            empleado = Empleado(cambio[4], cambio[5], cambio[6], cambio[7], rol)
            estadoCE = Estado(cambio[2], cambio[3])
            # Si el estado es fuera de servicio, se obtienen los motivos
            motivos = []
            if estadoCE.esFueraDeServicio():
                sql = (
                    'SELECT M.motivo_tipo, M.comentario '
                    'FROM MotivoFueraServicio M '
                    'WHERE M.fecha_hora_inicio = ? AND M.ambito = ? AND M.nombre = ? AND M.id_sismografo = ?'
                )
                cursor.execute(sql, (cambio[0], cambio[2], cambio[3], rowSismografo[0]))
                rowMotivos = cursor.fetchall()
                
                for motivo in rowMotivos:
                    motivoTipo = MotivoTipo(motivo[0])
                    MFS = MotivoFueraServicio(motivoTipo, motivo[1])
                    motivos.append(MFS)

            cambiosEstado.append(CambioEstado(cambio[0], cambio[1], empleado, estadoCE, motivos))
        
        sismografo = Sismografo(rowSismografo[0], rowSismografo[1], rowSismografo[2], estadoSismografo, self, cambiosEstado)

        sismografo.fueraDeServicio(estadoFueraServicio, fechaHoraFin, empleado, motivosSeleccionados, comentarios)

    def habilitarSismografo(self, estadoEnLinea, fechaHoraFin, empleado):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = (
                'SELECT S.identificador, S.numero_serie, S.fecha_adquisicion, S.ambito_estado_actual, S.nombre_estado_actual '
                'FROM Sismografo S WHERE codigo_estacion = ?'
            )
            cursor.execute(sql, (self.codigo,))
            rowSismografo = cursor.fetchone()
            sql = (
                'SELECT C.fecha_hora_inicio, C.fecha_hora_fin, C.ambito, C.nombre, '
                'E.nombre, E.apellido, E.mail, E.telefono, R.nombre, R.descripcion '
                'FROM CambioDeEstado C JOIN Empleado E ON C.nombre_empleado = E.nombre AND C.apellido_empleado = E.apellido AND C.mail_empleado = E.mail '
                'JOIN Rol R ON E.rol = R.nombre '
                'WHERE C.identificador_sismografo = ?'
            )
            cursor.execute(sql, (rowSismografo[0],))
            rowCambioEstado = cursor.fetchall()

        estadoSismografo = Estado(rowSismografo[3], rowSismografo[4])
        cambiosEstado = []
        for cambio in rowCambioEstado:
            rol = Rol(cambio[8], cambio[9])
            empleado = Empleado(cambio[4], cambio[5], cambio[6], cambio[7], rol)
            estadoCE = Estado(cambio[2], cambio[3])
            # Si el estado es fuera de servicio, se obtienen los motivos
            motivos = []
            if estadoCE.esFueraDeServicio():
                sql = (
                    'SELECT M.motivo_tipo, M.comentario '
                    'FROM MotivoFueraServicio M '
                    'WHERE M.fecha_hora_inicio = ? AND M.ambito = ? AND M.nombre = ? AND M.id_sismografo = ?'
                )
                cursor.execute(sql, (cambio[0], cambio[2], cambio[3], rowSismografo[0]))
                rowMotivos = cursor.fetchall()
                
                for motivo in rowMotivos:
                    motivoTipo = MotivoTipo(motivo[0])
                    MFS = MotivoFueraServicio(motivoTipo, motivo[1])
                    motivos.append(MFS)

            cambiosEstado.append(CambioEstado(cambio[0], cambio[1], empleado, estadoCE, motivos))
        
        sismografo = Sismografo(rowSismografo[0], rowSismografo[1], rowSismografo[2], estadoSismografo, self, cambiosEstado)

        sismografo.habilitar(estadoEnLinea, fechaHoraFin, empleado)