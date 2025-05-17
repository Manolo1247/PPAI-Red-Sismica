from .empleado import Empleado

class Usuario():
    def __init__(self, nombre, contraseña, empleado: Empleado):
        self.nombre = nombre
        self.contraseña = contraseña
        self.empleado = empleado

    def getEmpleado(self):
        return self.empleado
