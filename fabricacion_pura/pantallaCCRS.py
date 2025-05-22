class PantallaCCRS:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.estado = "apagada"
        self.brightness = 0

    def encender(self):
        self.estado = "encendida"
        print(f"La pantalla {self.nombre} está {self.estado}.")

    def apagar(self):
        self.estado = "apagada"
        print(f"La pantalla {self.nombre} está {self.estado}.")