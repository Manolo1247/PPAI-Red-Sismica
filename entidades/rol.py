class Rol():
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def esResponsableReparacion(self):
        return self.nombre == "Responsable de Reparación"