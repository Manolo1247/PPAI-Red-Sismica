import sqlite3
from RUTAS.rutas import ARCHIVO_BD
from datetime import datetime

from entidades.sesion import Sesion
from entidades.rol import Rol
from entidades.empleado import Empleado
from entidades.ordenDeInspeccion import OrdenDeInspeccion
from entidades.estacionSismologica import EstacionSismologica
from entidades.estado import Estado
from entidades.motivoTipo import MotivoTipo

class GestorOrdenDeCierre():
    def __init__(self, sesion, pantalla):
        self.sesion = sesion
        self.pantalla = pantalla
        self.empleado = None
        self.ordenesDeInspeccion = []
        self.datosOrdenesDeInspeccion = []
        self.ordenSeleccionada = None
        self.observacion = None
        self.motivos = []
        self.motivosSeleccionados = []
        self.comentarios = []
        self.estadoFueraDeServicio = None
        self.estadoCerrada = None
        self.fechaHoraActual = None
        self.mailsResponsableReparaciones = []

        self.buscarEmpleadoRI()

    def buscarEmpleadoRI(self):
        self.empleado = self.sesion.getUsuario()
        self.buscarOrdenDeInspeccion()

    def buscarOrdenDeInspeccion(self):
        # Buscar las ordenes de inspección en la base de datos
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = (
                'SELECT O.numero, O.fecha_hora_inicio, O.fecha_hora_finalizacion, O.fecha_hora_cierre, O.observacion_cierre, O.ambito, O.nombre, '
                'E.nombre, E.apellido, E.mail, E.telefono, R.nombre, R.descripcion, '
                'ES.codigo_estacion, ES.nombre, ES.latitud, ES.longitud, ES.fecha_solicitud_certificacion, ES.documento_certificacion, ES.numero_certificacion '
                'FROM OrdenDeInspeccion O '
                'JOIN Empleado E ON O.nombre_empleado = E.nombre AND O.apellido_empleado = E.apellido AND O.mail_empleado = E.mail '
                'JOIN Rol R ON E.rol = R.nombre '
                'JOIN EstacionSismologica ES ON O.codigo_estacion = ES.codigo_estacion '
            )
            cursor.execute(sql)
            filas = cursor.fetchall()

        for fila in filas:
            rol = Rol(fila[11], fila[12])
            empleado = Empleado(fila[7], fila[8], fila[9], fila[10], rol)
            estacion = EstacionSismologica(fila[13], fila[14], fila[15], fila[16], fila[17], fila[18], fila[19])
            estado = Estado(fila[5], fila[6])
            orden = OrdenDeInspeccion(fila[0], fila[1], fila[2], fila[3], fila[4], estacion, empleado, estado)
            self.ordenesDeInspeccion.append(orden)
        
        for orden in self.ordenesDeInspeccion:
            # Filtrar las ordenes de inspección que son del empleado y están realizadas
            if orden.esDeEmpleado(self.empleado) and orden.estaRealizada():
                datos = {
                    "numero": orden.getNroOrden(),
                    "fechaFinalizacion": orden.getFechaFinalizacion(),
                    "nombreEstacion": orden.getNombreEstacion(),
                    "sismografo": orden.getSismografo(),  # solo el id
                    "orden": orden  # objeto completo
                }
                self.datosOrdenesDeInspeccion.append(datos)

        self.ordenarOI()

    def ordenarOI(self):
        # Ordenar las ordenes de inspección por fecha de finalización
        self.datosOrdenesDeInspeccion.sort(key=lambda x: x["fechaFinalizacion"], reverse=True)
        self.pantalla.mostrarOI(self.datosOrdenesDeInspeccion)

    def tomarOrden(self, orden):
        self.ordenSeleccionada = orden
        self.pantalla.pedirObservacion()

    def tomarObservacion(self, observacion):
        self.observacion = observacion
        self.buscarMFS()

    def buscarMFS(self):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = 'SELECT descripcion FROM MotivoTipo'
            cursor.execute(sql)
            filas = cursor.fetchall()

        for fila in filas:
            motivo = MotivoTipo(fila[0])
            self.motivos.append(motivo.getDescripcion())

        self.pantalla.mostrarMFS(self.motivos)

    def tomarMotivoYComentario(self, motivo, comentario):
        self.motivosSeleccionados.append(motivo)
        self.comentarios.append(comentario)

        self.pantalla.pedirConfirmacion()

    def confirmar(self):
        self.validarObservacionesYmotivos()

    def validarObservacionesYmotivos(self):

        self.buscarEstadoFSYCerrada()

    def buscarEstadoFSYCerrada(self):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = 'SELECT ambito, nombre FROM Estado'
            cursor.execute(sql)
            filas = cursor.fetchall()

        for fila in filas:
            estado = Estado(fila[0], fila[1])
            if estado.esAmbitoSismografo() and estado.esFueraDeServicio():
                self.estadoFueraDeServicio = estado
            if estado.esAmbitoOI() and estado.esCerrada():
                self.estadoCerrada = estado

        self.getFechaHoraActual()

    def getFechaHoraActual(self):
        self.fechaHoraActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.ordenSeleccionada.cerrar(self.fechaHoraActual, self.estadoCerrada, self.observacion)
        self.ordenSeleccionada.fueraDeServicio(self.estadoFueraDeServicio, self.motivosSeleccionados, self.comentarios)

        self.getMailResponsableReparaciones()

    def getMailResponsableReparaciones(self):
        with sqlite3.connect(ARCHIVO_BD) as con:
            cursor = con.cursor()
            sql = (
                'SELECT E.nombre, E.apellido, E.mail, E.telefono, R.nombre, R.descripcion '
                'FROM Empleado E JOIN Rol R ON E.rol = R.nombre '
            )
            cursor.execute(sql)
            filas = cursor.fetchall()

        for fila in filas:
            rol = Rol(fila[4], fila[5])
            empleado = Empleado(fila[0], fila[1], fila[2], fila[3], rol)
            if empleado.esResponsableReparacion():
                self.mailsResponsableReparaciones.append(empleado.getMail())

        self.enviarNotificacionMail()

    def enviarNotificacionMail(self):
        pass





    def finCU(self):
        del self