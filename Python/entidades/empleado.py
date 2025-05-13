from .rol import Rol

class Empleado():
    def __init__(self, nombre, apellido, mail, telefono, rol: Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        self.rol = rol

    def getMail(self):
        return self.mail
    
    def esResponsableReparacion(self):
        return self.rol.esResponsableReparacion()