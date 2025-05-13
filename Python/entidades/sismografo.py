from .estado import Estado
from .estacionSismologica import EstacionSismologica
from .cambioEstado import CambioEstado
from typing import List


class Sismografo:
    def __init__(self, identificador, numeroSerie, fechaAdquisicion, estadoActual: Estado, estacionSismologica: EstacionSismologica, cambioEstado: List[CambioEstado]):
        self.identificador = identificador
        self.numeroSerie = numeroSerie
        self.fechaAdquisicion = fechaAdquisicion
        self.estadoActual = estadoActual
        self.estacionSismologica = estacionSismologica
        self.cambioEstado = cambioEstado


