from .estado import Estado
from .motivoFueraServicio import MotivoFueraServicio
from .empleado import Empleado
from typing import List

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, empleado: Empleado, estado: Estado, motivoFueraServicio: List[MotivoFueraServicio]):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.empleado = empleado
        self.estado = estado
        self.motivoFueraServicio = motivoFueraServicio
