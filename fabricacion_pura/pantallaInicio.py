import customtkinter as ctk
import sys
from fabricacion_pura.pantallaOrdenDeCierre import PantallaOrdenDeCierre

class PantallaInicio(ctk.CTkFrame):
    def __init__(self, parent, controller, sesion):
        super().__init__(parent)
        self.controller = controller
    
        # Encabezado estilo Bootstrap
        headerFrame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)  # Azul de Bootstrap
        headerFrame.pack(fill="x", padx=10)  # Padding para los bordes
        headerLabel = ctk.CTkLabel(
            headerFrame,
            text="Menú Principal",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        headerLabel.pack(pady=20)

        # Cuerpo estilo "card" con fondo claro
        self.mainFrame = ctk.CTkFrame(self, fg_color="#f8f9fa", corner_radius=12)  # Color de fondo claro
        self.mainFrame.pack(fill="both", expand=True, padx=80, pady=30)

        # Estilo base para botones
        botonEstilo = {
            "width": 250,
            "height": 50,
            "font": ("Arial", 16),
        }

        # Botones centrados con estilo de Bootstrap
        registrarBtn = ctk.CTkButton(
            self.mainFrame,
            text="Registrar Diagramación de Inspección de ES",
            **botonEstilo,
            fg_color="#0d6efd",  # Azul Bootstrap
            hover_color="#0b5ed7",  # Hover más oscuro
            corner_radius=8,
            #command=lambda: controller.showFrame(PantallaRegistrarInspeccion)
        )
        registrarBtn.pack(pady=20)

        cerrarOrdenBtn = ctk.CTkButton(
            self.mainFrame,
            text="Cerrar Orden de Inspección",
            **botonEstilo,
            fg_color="#0d6efd",  # Azul Bootstrap
            hover_color="#0b5ed7",  # Hover más oscuro
            corner_radius=8,
            command=lambda: controller.showFrame(PantallaOrdenDeCierre)
        )
        cerrarOrdenBtn.pack(pady=20)

        closeButton = ctk.CTkButton(
            self.mainFrame,
            text="Cerrar",
            **botonEstilo,
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            corner_radius=8,
            command=sys.exit
        )
        closeButton.pack(pady=30)

        # Añadir bordes sutiles en el cuerpo y el encabezado, para un efecto de separación
        self.mainFrame.configure(border_color="#dcdcdc", border_width=1)  # Borde de separación