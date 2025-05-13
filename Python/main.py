import customtkinter as ctk
from pantallas import PantallaInicio, PantallaOrdenDeCierre

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Pantalla(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Inicio")
        self.geometry("600x400")

        # Contenedor principal con fondo blanco
        container = ctk.CTkFrame(self, fg_color="white")
        container.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        # Diccionario de todos los frames
        self.frames = {}

        # Crear e inicializar cada frame
        for F in (PantallaInicio, PantallaOrdenDeCierre):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=ctk.NSEW)

        # Mostrar la pantalla principal inicialmente
        self.show_frame(PantallaInicio)

    def show_frame(self, container):
        frame = self.frames[container]
        if hasattr(frame, 'habilitar_ventana'):
            frame.habilitar_ventana()
        frame.tkraise()


if __name__ == "__main__":
    app = Pantalla()
    app.mainloop()