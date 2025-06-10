from datetime import datetime
import os
# Capa de persistencia
from persistencia.ordenDeInspeccionModel import OrdenDeInspeccionModel
from persistencia.sismografoModel import SismografoModel
from persistencia.estadoModel import EstadoModel
from persistencia.motivoTipoModel import MotivoTipoModel
from persistencia.empleadoModel import EmpleadoModel


from fabricacion_pura.interfazMail import InterfazMail
from fabricacion_pura.pantallaCCRS import PantallaCCRS


class GestorOrdenDeCierre():
    def __init__(self, sesion, pantalla):
        self.sesion = sesion
        self.pantalla = pantalla
        self.empleado = None
        self.ordenesDeInspeccion = OrdenDeInspeccionModel.findAll()
        self.sismografos = SismografoModel.findAll()
        self.ordenSeleccionada = None
        self.observacion = None
        self.estados = EstadoModel.findAll()
        self.estadoFueraDeServicio = None
        self.estadoEnLinea = None
        self.motivosTipo = MotivoTipoModel.findAll()
        self.motivosSeleccionados = []
        self.comentarios = []
        self.estadoCerrada = None
        self.fechaHoraActual = None
        self.empleados = EmpleadoModel.findAll()
        self.mailsResponsableReparaciones = []
        self.sismografoSeleccionado = None

        self.buscarEmpleadoRI()

    def buscarEmpleadoRI(self):
        self.empleado = self.sesion.getEmpleado()
        self.buscarOrdenDeInspeccion()

    def buscarOrdenDeInspeccion(self):
        datosOrdenesDeInspeccion = []
        for orden in self.ordenesDeInspeccion:
            # Filtrar las ordenes de inspección que son del empleado y están realizadas
            if orden.esDeEmpleado(self.empleado) and orden.estaRealizada():
                for s in self.sismografos:
                    estacion = orden.getEstacion()
                    if s.esTuEstacion(estacion):
                        sismografo = s
                        break
                
                datos = {
                    "numero": orden.getNroOrden(),
                    "fechaFinalizacion": orden.getFechaFinalizacion(),
                    "nombreEstacion": orden.getNombreEstacion(),
                    "sismografo": sismografo.getId(),
                    "orden": orden
                }
                datosOrdenesDeInspeccion.append(datos)

        self.ordenarOI(datosOrdenesDeInspeccion)

    def ordenarOI(self, ordenes):
        # Ordenar las ordenes de inspección por fecha de finalización (de más vieja a más nueva)
        ordenes.sort(key=lambda x: x["fechaFinalizacion"])
        self.pantalla.mostrarOI(ordenes=ordenes)

    def tomarOrden(self, orden):
        self.ordenSeleccionada = orden
        self.pantalla.pedirObservacion()

    def tomarObservacion(self, observacion):
        self.observacion = observacion
        self.buscarEstadoFS()

    def buscarEstadoFS(self):
        for estado in self.estados:
            if estado.esAmbitoSismografo() and estado.esFueraDeServicio():
                self.estadoFueraDeServicio = estado
                break

        self.buscarEstadoEnLinea()
    
    def buscarEstadoEnLinea(self):
        for estado in self.estados:
            if estado.esAmbitoSismografo() and estado.esEnLinea():
                self.estadoEnLinea = estado
                break
        
        self.pantalla.pedirSituacionSismografo(estadoEnLinea=self.estadoEnLinea.nombre, estadoFueraDeServicio=self.estadoFueraDeServicio.nombre)

    def buscarEstadoCerrada(self, EnLinea=True):
        for estado in self.estados:
            if estado.esAmbitoOI() and estado.esCerrada():
                self.estadoCerrada = estado
                break

        self.obtenerSismografo(EnLinea)

    def seleccionarEnLinea(self):
        self.buscarEstadoCerrada()

    def seleccionarFS(self):
        self.buscarMFS()

    def buscarMFS(self):
        motivos = []
        for motivo in self.motivosTipo:
            if motivo in self.motivosSeleccionados:
                continue
    
            datos = {
                "descripcion": motivo.getDescripcion(),
                "motivo": motivo
            }
            motivos.append(datos)

        if len(self.motivosSeleccionados) == 0:
            self.pantalla.mostrarMFS(motivos=motivos)
        else:
            self.pantalla.pedirConfirmacion()

    def tomarMotivoYComentario(self, motivo, comentario):
        self.motivosSeleccionados.append(motivo)
        self.comentarios.append(comentario)

        self.pantalla.pedirConfirmacion()

    def anularSeleccionMFS(self, motivo):
        self.motivosSeleccionados.remove(motivo)
        
        if len(self.motivosSeleccionados) == 0:
            self.pantalla.mostrarMFS()
        else:
            self.pantalla.pedirConfirmacion()

    def confirmar(self):
        self.buscarEstadoCerrada(EnLinea=False)

    def obtenerSismografo(self, EnLinea):
        estacion = self.ordenSeleccionada.getEstacion()
        for sismografo in self.sismografos:
            if sismografo.esTuEstacion(estacion):
                self.sismografoSeleccionado = sismografo
                break
        
        self.getFechaHoraActual(EnLinea)

    def getFechaHoraActual(self, EnLinea=True):
        self.fechaHoraActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.ordenSeleccionada.cerrar(self.fechaHoraActual, self.estadoCerrada, self.observacion)
        
        if EnLinea:
            self.sismografoSeleccionado.habilitar(self.estadoEnLinea, self.fechaHoraActual, self.empleado)
            self.finCU()
        else:
            self.sismografoSeleccionado.fueraDeServicio(self.estadoFueraDeServicio, self.fechaHoraActual, self.empleado, self.motivosSeleccionados, self.comentarios)
            self.getMailResponsableReparaciones()

    def getMailResponsableReparaciones(self):
        for empleado in self.empleados:
            if empleado.esResponsableReparacion():
                mail = empleado.getMail()
                self.mailsResponsableReparaciones.append(mail)

        self.enviarNotificacionMail()

    def enviarNotificacionMail(self):
        idSismografo = self.sismografoSeleccionado.getId()
        asunto = f"Orden de Inspeccion Cerrada"
        mensaje = f"La orden de inspección para el sismógrafo {idSismografo} ha sido cerrada.\n" \
                    f"El sismografo ahora se encuentra {self.estadoFueraDeServicio.nombre}\n" \
                    f"Fecha y hora de cierre: {self.fechaHoraActual}\n" \
                    f"Motivos:\n"
        
        for i in range(len(self.motivosSeleccionados)):
            motivo = self.motivosSeleccionados[i]
            comentario = self.comentarios[i]
            mensaje += f"\t{motivo.getDescripcion()} || Comentario: {comentario}\n"

        popUp = InterfazMail(self.pantalla, self.mailsResponsableReparaciones, asunto, mensaje)
        popUp.grab_set()
        popUp.wait_window()

        self.publicarMonitores()

    def publicarMonitores(self):
        idSismografo = self.sismografoSeleccionado.getId()
        popUp = PantallaCCRS(self.pantalla, idSismografo)
        popUp.grab_set()
        popUp.wait_window()

        self.finCU()

    def finCU(self):
        # lógica para persistir los cambios
        OrdenDeInspeccionModel.updateFromEntity(self.ordenSeleccionada)
        SismografoModel.updateFromEntity(self.sismografoSeleccionado)

        self.pantalla.cerrar()