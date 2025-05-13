import customtkinter as ctk
import sys

class PantallaInicio(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Encabezado estilo Bootstrap
        header_frame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)  # Azul de Bootstrap
        header_frame.pack(fill="x", padx=10)  # Padding para los bordes
        header_label = ctk.CTkLabel(
            header_frame,
            text="Menú Principal",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        header_label.pack(pady=20)

        # Cuerpo estilo "card" con fondo claro
        self.main_frame = ctk.CTkFrame(self, fg_color="#f8f9fa", corner_radius=12)  # Color de fondo claro
        self.main_frame.pack(fill="both", expand=True, padx=80, pady=30)

        # Estilo base para botones
        boton_estilo = {
            "width": 250,
            "height": 50,
            "font": ("Arial", 16),
        }

        # Botones centrados con estilo de Bootstrap
        import_button = ctk.CTkButton(
            self.main_frame,
            text="Registrar Diagramación de Inspección de ES",
            **boton_estilo,
            fg_color="#0d6efd",  # Azul Bootstrap
            hover_color="#0b5ed7",  # Hover más oscuro
            corner_radius=8,
            #command=lambda: print("Diagramación")
        )
        import_button.pack(pady=20)

        view_button = ctk.CTkButton(
            self.main_frame,
            text="Cerrar Orden de Inspección",
            **boton_estilo,
            fg_color="#0d6efd",  # Azul Bootstrap
            hover_color="#0b5ed7",  # Hover más oscuro
            corner_radius=8,
            command=lambda: controller.show_frame(PantallaOrdenDeCierre)
        )
        view_button.pack(pady=20)

        close_button = ctk.CTkButton(
            self.main_frame,
            text="Cerrar",
            **boton_estilo,
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            corner_radius=8,
            command=sys.exit
        )
        close_button.pack(pady=30)

        # Añadir bordes sutiles en el cuerpo y el encabezado, para un efecto de separación
        self.main_frame.configure(border_color="#dcdcdc", border_width=1)  # Borde de separación


class PantallaOrdenDeCierre(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Pantalla Orden de Cierre", font=("Arial", 20))
        label.pack(pady=20)

