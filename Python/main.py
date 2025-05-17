import customtkinter as ctk
from pantallas import PantallaInicio, PantallaOrdenDeCierre

from entidades.sesion import Sesion
from entidades.usuario import Usuario
from entidades.empleado import Empleado
from entidades.rol import Rol

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Pantalla(ctk.CTk):
    def __init__(self, sesion, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inicio")
        self.geometry("800x600")

        # Contenedor principal con fondo blanco
        container = ctk.CTkFrame(self, fg_color="white")
        container.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Diccionario de todos los frames
        self.frames = {}

        # Crear e inicializar cada frame
        for F in (PantallaInicio, PantallaOrdenDeCierre):
            frame = F(container, self, sesion)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=ctk.NSEW)

        # Mostrar la pantalla principal inicialmente
        self.showFrame(PantallaInicio)

    def showFrame(self, container):
        frame = self.frames[container]
        if hasattr(frame, 'habilitarVentana'):
            frame.habilitarVentana()
        frame.tkraise()


if __name__ == "__main__":
    sesion = Sesion(
        Usuario(
            "anam",
            "insp321",
            Empleado(
                "Ana",
                "Martínez",
                "ana.martinez@mail.com",
                "4444444444",
                Rol("Responsable de Inspeccion", "Coordina y realiza inspecciones de estaciones y equipos.")
            )
        )
    )
    app = Pantalla(sesion)
    app.mainloop()