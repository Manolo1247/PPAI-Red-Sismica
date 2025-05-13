from datetime import datetime
from .usuario import Usuario

class Sesion():
    def __init__(self, usuario: Usuario, fecha_hora_inicio = datetime.now(), fecha_hora_fin = None):
        self.usuario = usuario
        self.fecha_hora_inicio = fecha_hora_inicio
        self.fecha_hora_fin = fecha_hora_fin

    def getUsuario(self):
        return self.usuario.getEmpleado()