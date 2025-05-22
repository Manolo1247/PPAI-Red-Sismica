class Estado:
    def __init__(self, ambito, nombre):
        self.ambito = ambito
        self.nombre = nombre

    def getNombre(self):
        return self.nombre
    
    def estaRealizada(self):
        return self.nombre == "Completamente Realizada"
    
    def esAmbitoSismografo(self):
        return self.ambito == "Sismografo"
    
    def esFueraDeServicio(self):
        return self.nombre == "Fuera de Servicio"
    
    def esAmbitoOI(self):
        return self.ambito == "Orden de Inspeccion"
    
    def esCerrada(self):
        return self.nombre == "Cerrada"