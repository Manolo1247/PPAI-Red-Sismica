import customtkinter as ctk
import sys
from fabricacion_pura.gestor import GestorOrdenDeCierre

class PantallaOrdenDeCierre(ctk.CTkFrame):
    def __init__(self, parent, controller, sesion):
        super().__init__(parent)
        self.controller = controller
        
        self.sesion = sesion
        self.motivosGrilla = []

    def habilitarVentana(self):
        self.gestor = GestorOrdenDeCierre(self.sesion, self)

    def mostrarOI(self, ordenes):
        # Limpia la pantalla
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

        # Cuerpo de la tabla (más abajo con pady extra)
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True, pady=(20, 0))  # <-- agrega espacio arriba

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

        # Botón para cancelar CU
        cancelar_btn = ctk.CTkButton(
            self,
            text="Cancelar",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.cancelar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(pady=10)

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

        # Frame para los botones en línea
        botones_frame = ctk.CTkFrame(self, fg_color="transparent")
        botones_frame.pack(pady=20)

        guardar_btn = ctk.CTkButton(
            botones_frame,
            text="Guardar",
            command=guardar_observacion,
            width=200,  
            height=55,  
            font=("Arial", 18, "bold")  
        )
        guardar_btn.pack(side="left", padx=10)

        cancelar_btn = ctk.CTkButton(
            botones_frame,
            text="Cancelar",
            fg_color="#dc3545",
            hover_color="#c82333",
            command=self.cancelar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(side="left", padx=10)

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

        # Cuerpo de la tabla (más abajo con pady extra)
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True, pady=(20, 0))  # <-- agrega espacio arriba

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

        # Botón para cancelar CU
        cancelar_btn = ctk.CTkButton(
            self,
            text="Cancelar",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.cancelar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(pady=10)

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

        # Frame para los botones en línea
        botones_frame = ctk.CTkFrame(self, fg_color="transparent")
        botones_frame.pack(pady=20)
        
        guardar_btn = ctk.CTkButton(
            botones_frame,
            text="Guardar Comentario",
            command=guardarComentario,
            width=200,  
            height=55,  
            font=("Arial", 18, "bold")  
        )
        guardar_btn.pack(side="left", padx=10)

        # Botón para cancelar CU
        cancelar_btn = ctk.CTkButton(
            botones_frame,
            text="Cancelar",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.cancelar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(side="left", padx=10)

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

        # Cuerpo de la tabla (más abajo con pady extra)
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True, pady=(20, 0))  # <-- agrega espacio arriba

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

        # Frame para los botones en línea
        botones_frame = ctk.CTkFrame(self, fg_color="transparent")
        botones_frame.pack(pady=20)

        # Botón de confirmación
        confirmar_btn = ctk.CTkButton(
            botones_frame,
            text="Confirmar",
            font=("Arial", 18, "bold"),
            fg_color="#198754",
            hover_color="#157347",
            width=200,
            height=50,
            command=confirmar_y_mostrar_espera
        )
        confirmar_btn.pack(side="left", padx=10)

        # Botón para cancelar CU
        cancelar_btn = ctk.CTkButton(
            botones_frame,
            text="Cancelar",
            fg_color="#dc3545",
            hover_color="#c82333",
            command=self.cancelar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(side="left", padx=10)

    def cancelar(self):
        from fabricacion_pura.pantallaInicio import PantallaInicio
        self.gestor.finCU(cancelar=True)
        self.controller.showFrame(PantallaInicio)



