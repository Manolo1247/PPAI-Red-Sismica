from entidades.estado import Estado
from entidades.motivoFueraServicio import MotivoFueraServicio
from entidades.motivoTipo import MotivoTipo
from entidades.empleado import Empleado

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, empleado: Empleado, estado: Estado, motivoFueraServicio, motivos=[], comentarios=[]):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.empleado = empleado
        self.estado = estado
        self.motivosFueraServicio = motivoFueraServicio

        if self.estado.esFueraDeServicio() and len(self.motivosFueraServicio) == 0:
            self.crearMotivos(motivos, comentarios)

    def esActual(self):
        return self.fechaHoraFin is None
    
    def setFechaHoraFin(self, fechaHoraFin):
        self.fechaHoraFin = fechaHoraFin

    def crearMotivos(self, motivos, comentarios):              
        n = len(motivos)
        for i in range(n):
            motivo = motivos[i]
            comentario = comentarios[i]
            motivoFueraServicio = MotivoFueraServicio(comentario, MotivoTipo(motivo))
            
            self.motivosFueraServicio.append(motivoFueraServicio)