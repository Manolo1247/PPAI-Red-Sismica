class Estado:
    def __init__(self, ambito, nombre):
        self.ambito = ambito
        self.nombre = nombre

    def estaRealizada(self):
        return self.nombre == "Completamente Realizada"