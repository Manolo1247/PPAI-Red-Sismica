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
        self.motivosGrilla = []

    def habilitarVentana(self):
        self.gestor = GestorOrdenDeCierre(self.sesion, self)
    
    def mostrarOI(self, ordenes):
        # Limpiar la pantalla antes de cargar nuevos widgets para el correcto funcionamiento del botón volver
        for widget in self.winfo_children():
            widget.destroy()
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
                command=lambda ordenSeleccionada=orden["orden"]: self.seleccionarOI(ordenSeleccionada)
            )
            selectButton.grid(row=i+1, column=4, padx=10, pady=5)

            volver_btn = ctk.CTkButton(
            self,
            text="Volver",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.volverInicio,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        volver_btn.pack(pady=10)

    def volverInicio(self):
        self.controller.showFrame(PantallaInicio)

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

        mensaje_error = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14, "bold"))
        mensaje_error.pack(pady=5)

        def guardar_observacion():
            observacion = observacion_entry.get("1.0", "end").strip()
            if not observacion:
                mensaje_error.configure(text="Debe ingresar una observación.")
                return
            mensaje_error.configure(text="")
            self.tomarObservacion(observacion)
            # Puedes mostrar un mensaje de éxito o volver a otra pantalla

        guardar_btn = ctk.CTkButton(
            self,
            text="Guardar",
            command=guardar_observacion,
            width=200,  
            height=55,  
            font=("Arial", 18, "bold")  
        )
        guardar_btn.pack(pady=20)

        volver_btn = ctk.CTkButton(
            self,
            text="Volver",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.volver,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        volver_btn.pack(pady=10)

    def volver(self):
        self.controller.showFrame(PantallaOrdenDeCierre)


    def tomarObservacion(self, observacion):
        self.gestor.tomarObservacion(observacion)

    def mostrarMFS(self, motivos):
        self.motivosGrilla = motivos
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado estilo Bootstrap
        headerFrame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        headerFrame.pack(fill="x", padx=10)
        headerLabel = ctk.CTkLabel(
            headerFrame,
            text="Motivos de Cierre",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        headerLabel.pack(pady=20)

        # Cuerpo de la tabla
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True)

        # Crear encabezados de tabla
        columnas = ["Descripción", "Seleccionar"]
        for col_idx, col in enumerate(columnas):
            label = ctk.CTkLabel(tableFrame, text=col, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col_idx, padx=10, pady=10)

        # Llenar la tabla con datos, cada motivo tiene un botón "Seleccionar"
        for i, motivo in enumerate(motivos):
            ctk.CTkLabel(tableFrame, text=getattr(motivo, "getDescripcion", lambda: str(motivo))()).grid(row=i+1, column=0, padx=10, pady=5)
            selectButton = ctk.CTkButton(
                tableFrame,
                text="Seleccionar",
                command=lambda m=motivo: self.tomarMFS(m)
            )
            selectButton.grid(row=i+1, column=1, padx=10, pady=5)

    def tomarMFS(self, motivo):
        # Limpia la pantalla y muestra campo para comentario del motivo seleccionado
        for widget in self.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(
            self,
            text=f"Ingrese un comentario para: {getattr(motivo, 'getDescripcion', lambda: str(motivo))()}",
            font=("Arial", 18, "bold"),
            text_color="#0d6efd"
        )
        label.pack(pady=20)

        comentario_entry = ctk.CTkTextbox(self, width=400, height=100)
        comentario_entry.pack(pady=10)

        mensaje_error = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14, "bold"))
        mensaje_error.pack(pady=5)

        def guardarComentario():
            comentario = comentario_entry.get("1.0", "end").strip()
            if not comentario:
                mensaje_error.configure(text="Debe ingresar un comentario.")
                return
            mensaje_error.configure(text="")
            # Elimina el motivo de la grilla antes de pasar al gestor
            self.motivosGrilla.remove(motivo)
            self.tomarComentario(motivo, comentario)

        guardar_btn = ctk.CTkButton(
            self,
            text="Guardar Comentario",
            command=guardarComentario,
            width=200,  
            height=55,  
            font=("Arial", 18, "bold")  
        )
        guardar_btn.pack(pady=20)

    def tomarComentario(self, motivo, comentario):
        self.gestor.tomarMotivoYComentario(motivo, comentario)

    def pedirConfirmacion(self):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado estilo Bootstrap
        headerFrame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        headerFrame.pack(fill="x", padx=10)
        headerLabel = ctk.CTkLabel(
            headerFrame,
            text="Motivos de Cierre",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        headerLabel.pack(pady=20)

        # Cuerpo de la tabla
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True)

        # Crear encabezados de tabla
        columnas = ["Descripción", "Seleccionar"]
        for col_idx, col in enumerate(columnas):
            label = ctk.CTkLabel(tableFrame, text=col, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col_idx, padx=10, pady=10)

        # Llenar la tabla con datos, cada motivo tiene un botón "Seleccionar"
        for i, motivo in enumerate(self.motivosGrilla):
            ctk.CTkLabel(tableFrame, text=getattr(motivo, "getDescripcion", lambda: str(motivo))()).grid(row=i+1, column=0, padx=10, pady=5)
            selectButton = ctk.CTkButton(
                tableFrame,
                text="Seleccionar",
                command=lambda m=motivo: self.tomarMFS(m)
            )
            selectButton.grid(row=i+1, column=1, padx=10, pady=5)

        # Botón de confirmación
        def confirmar_y_mostrar_espera():
            # Limpiar widgets
            for widget in self.winfo_children():
                widget.destroy()
            # Mostrar mensaje de espera
            espera_frame = ctk.CTkFrame(self)
            espera_frame.pack(expand=True)
            engranaje_label = ctk.CTkLabel(
                espera_frame,
                text="🔄",
                font=("Arial", 48)
            )
            engranaje_label.pack(pady=10)
            mensaje_label = ctk.CTkLabel(
                espera_frame,
                text="Por favor, espere...",
                font=("Arial", 20, "bold")
            )
            mensaje_label.pack(pady=10)
            # Llamar a la lógica real después de actualizar la UI
            self.after(100, self.gestor.confirmar)

        confirmar_btn = ctk.CTkButton(
                self,
                text="Confirmar",
                font=("Arial", 18, "bold"),
                fg_color="#198754",  # Verde Bootstrap
                hover_color="#157347",  # Verde más oscuro al pasar el mouse
                width=200,
                height=50,
                command=confirmar_y_mostrar_espera
            )
        confirmar_btn.pack(pady=30)



