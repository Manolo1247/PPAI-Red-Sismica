class Estado:
    def __init__(self, ambito, nombre):
        self.ambito = ambito
        self.nombre = nombre
    
    def estaRealizada(self):
        return self.nombre == "Completamente Realizada"
    
    def esAmbitoSismografo(self):
        return self.ambito == "Sismografo"
    
    def esFueraDeServicio(self):
        return self.nombre == "Fuera de Servicio"
    
    def esEnLinea(self):
        return self.nombre == "En Linea"
    
    def esAmbitoOI(self):
        return self.ambito == "Orden de Inspeccion"
    
    def esCerrada(self):
        return self.nombre == "Cerrada"