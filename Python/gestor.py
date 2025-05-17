import sqlite3
from RUTAS.rutas import ARCHIVO_BD

from entidades.sesion import Sesion
from entidades.rol import Rol
from entidades.empleado import Empleado
from entidades.ordenDeInspeccion import OrdenDeInspeccion
from entidades.estacionSismologica import EstacionSismologica
from entidades.estado import Estado

class GestorOrdenDeCierre():
    def __init__(self, sesion: Sesion, pantalla):
        self.sesion = sesion
        self.empleado = None
        self.pantalla = pantalla
        self.ordenesDeInspeccion = []
        self.datosOrdenesDeInspeccion = []
        self.ordenSeleccionada = None
        self.observacion = None

        self.buscarEmpleadoRI()

    def buscarEmpleadoRI(self):
        self.empleado = self.sesion.getUsuario()
        self.buscarOrdenDeInspeccion()

    def buscarOrdenDeInspeccion(self):
        # Buscar las ordenes de inspección en la base de datos
        con = sqlite3.connect(ARCHIVO_BD)
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
        con.close()

        # print("DEBUG - Total ordenes obtenidas:", len(self.ordenesDeInspeccion))
        for orden in self.ordenesDeInspeccion:
            # print("DEBUG - Orden:", orden.getNroOrden(), orden.getNombreEstacion(), orden.getFechaFinalizacion())
            # print("DEBUG - Estado:", orden.estado.nombre, "| Ámbito:", orden.estado.ambito)
            # print("DEBUG - esDeEmpleado:", orden.esDeEmpleado(self.empleado))
            # print("DEBUG - estaRealizada:", orden.estaRealizada())
            if orden.esDeEmpleado(self.empleado) and orden.estaRealizada():
                datos = {
                    "numero": orden.getNroOrden(),
                    "fechaFinalizacion": orden.getFechaFinalizacion(),
                    "nombreEstacion": orden.getNombreEstacion(),
                    "sismografo": orden.getSismografo()  # solo el id
                }
                self.datosOrdenesDeInspeccion.append(datos)
        # print("DEBUG - datosOrdenesDeInspeccion:", self.datosOrdenesDeInspeccion)

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
        pass