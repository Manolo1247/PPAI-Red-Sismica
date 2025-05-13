from pantallas import PantallaOrdenDeCierre
from .entidades.sesion import Sesion



class GestorOrdenDeCierre():
    def __init__(self, sesion):
        self.sesion = sesion
        self.empleado = None
        

    def cerrarOrden(self):
        # Método de creacion en el diagrama de secuencia
        pass
    
    def buscarEmpleadoRI(self):
        self.empleado = self.sesion.getUsuario()
        self.buscarOrdenDeInspeccion()

    def buscarOrdenDeInspeccion(self):
        pass