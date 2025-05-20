from .rol import Rol

class Empleado():
    def __init__(self, nombre, apellido, mail, telefono, rol: Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.telefono = telefono
        self.rol = rol

    def __eq__(self, other):
        if not isinstance(other, Empleado):
            return False
        return (
            self.nombre == other.nombre and
            self.apellido == other.apellido and
            self.mail == other.mail
        )
       
    def esResponsableReparacion(self):
        return self.rol.esResponsableReparacion()

    def getMail(self):
        return self.mail