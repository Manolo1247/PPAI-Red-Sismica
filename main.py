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
        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.current_frame = None
        self.sesion = sesion

        # Mostrar la pantalla principal inicialmente
        self.showFrame(PantallaInicio)

    def showFrame(self, frame_class):
        # Destruir el frame actual si existe
        if self.current_frame is not None:
            self.current_frame.destroy()
        # Crear una nueva instancia del frame
        frame = frame_class(self.container, self, self.sesion)
        frame.grid(row=0, column=0, sticky=ctk.NSEW)
        self.current_frame = frame
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