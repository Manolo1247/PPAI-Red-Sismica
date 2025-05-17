import customtkinter as ctk
import sys
from gestor import GestorOrdenDeCierre

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
            #command=lambda: print("Diagramación")
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


class PantallaOrdenDeCierre(ctk.CTkFrame):
    def __init__(self, parent, controller, sesion):
        super().__init__(parent)
        self.controller = controller

        self.sesion = sesion

    def habilitarVentana(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.gestor = GestorOrdenDeCierre(self.sesion, self)

    def mostrarOI(self, ordenes):
        # Encabezado estilo Bootstrap
        headerFrame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        headerFrame.pack(fill="x", padx=10)
        headerLabel = ctk.CTkLabel(
            headerFrame,
            text="Órdenes de Inspección",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        headerLabel.pack(pady=20)

        # Cuerpo de la tabla
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True)

        # Crear encabezados de tabla
        columnas = ["Número de Orden", "Fecha de Finalizacion", "Nombre Estación", "Identificador Sismografo"]
        for col_idx, col in enumerate(columnas):
            label = ctk.CTkLabel(tableFrame, text=col, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col_idx, padx=10, pady=10)

        # Llenar la tabla con datos
        for i, orden in enumerate(ordenes):
            ctk.CTkLabel(tableFrame, text=orden.get("numero", "")).grid(row=i+1, column=0, padx=10, pady=5)
            ctk.CTkLabel(tableFrame, text=orden.get("fechaFinalizacion", "")).grid(row=i+1, column=1, padx=10, pady=5)
            ctk.CTkLabel(tableFrame, text=orden.get("nombreEstacion", "")).grid(row=i+1, column=2, padx=10, pady=5)
            ctk.CTkLabel(tableFrame, text=orden.get("sismografo", "")).grid(row=i+1, column=3, padx=10, pady=5)
            # Botón para seleccionar esta orden
            selectButton = ctk.CTkButton(
                tableFrame,
                text="Seleccionar",
                command=lambda o=orden: self.seleccionarOI(o)
            )
            selectButton.grid(row=i+1, column=4, padx=10, pady=5)

    def seleccionarOI(self, orden):
        self.gestor.tomarOrden(orden)

    def pedirObservacion(self):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado estilo Bootstrap
        headerFrame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        headerFrame.pack(fill="x", padx=10)
        headerLabel = ctk.CTkLabel(
            headerFrame,
            text="Ingrese la observación de cierre:",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        headerLabel.pack(pady=20)

        observacion_entry = ctk.CTkTextbox(self, width=400, height=100)
        observacion_entry.pack(pady=10)

        def guardar_observacion():
            observacion = observacion_entry.get("1.0", "end").strip()
            self.gestor.tomarObservacion(observacion)
            # Puedes mostrar un mensaje de éxito o volver a otra pantalla

        guardar_btn = ctk.CTkButton(self, text="Guardar", command=guardar_observacion)
        guardar_btn.pack(pady=20)