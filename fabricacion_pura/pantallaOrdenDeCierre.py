import customtkinter as ctk
import sys
from fabricacion_pura.gestor import GestorOrdenDeCierre

class PantallaOrdenDeCierre(ctk.CTkFrame):
    def __init__(self, parent, controller, sesion):
        super().__init__(parent)
        self.controller = controller
        
        self.sesion = sesion
        
        self.headerText = None
        self.datosOrdenes = []
        self.observacion = None
        self.motivos = []
        self.motivosSeleccionados = []

    @property
    def header(self):
        # Encabezado estilo Bootstrap
        frame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        frame.pack(fill="x", padx=10)

        label = ctk.CTkLabel(
            frame,
            text=self.headerText,
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        label.pack(pady=20)

    @property
    def ordenesGrilla(self):
        tableFrame = ctk.CTkFrame(self)
        tableFrame.pack(fill="both", expand=True, pady=(20, 0))

        if not self.datosOrdenes:
            sin_ordenes_label = ctk.CTkLabel(
                tableFrame,
                text="No se encontraron órdenes \ncompletamente realizadas",
                font=("Arial", 36, "bold"),
                text_color="red"
            )
            sin_ordenes_label.pack(expand=True, pady=60)
        else:
            # Encabezados
            columnas = ["Número de Orden", "Fecha de Finalizacion", "Nombre Estación", "Identificador Sismografo"]
            for col_idx, col in enumerate(columnas):
                label = ctk.CTkLabel(tableFrame, text=col, font=("Arial", 14, "bold"))
                label.grid(row=0, column=col_idx, padx=10, pady=10)

            for i, orden in enumerate(self.datosOrdenes):
                ctk.CTkLabel(tableFrame, text=orden.get("numero", "")).grid(row=i+1, column=0, padx=10, pady=5)
                ctk.CTkLabel(tableFrame, text=orden.get("fechaFinalizacion", "")).grid(row=i+1, column=1, padx=10, pady=5)
                ctk.CTkLabel(tableFrame, text=orden.get("nombreEstacion", "")).grid(row=i+1, column=2, padx=10, pady=5)
                ctk.CTkLabel(tableFrame, text=orden.get("sismografo", "")).grid(row=i+1, column=3, padx=10, pady=5)
                selectButton = ctk.CTkButton(
                    tableFrame,
                    text="Seleccionar",
                    command=lambda ordenSeleccionada=orden["orden"]: self.seleccionarOI(ordenSeleccionada)
                )
                selectButton.grid(row=i+1, column=4, padx=10, pady=5)

    @property
    def botonCancelar(self):
        # Botón para cancelar CU
        cancelar_btn = ctk.CTkButton(
            self,
            text="Cancelar",
            fg_color="#dc3545",  # Rojo Bootstrap
            hover_color="#c82333",  # Hover más oscuro
            command=self.cerrar,
            width=200,
            height=55,
            font=("Arial", 18, "bold")
        )
        cancelar_btn.pack(pady=10)

    @property
    def cuadroObservacion(self):
        observacion_entry = ctk.CTkTextbox(self, width=400, height=100)
        observacion_entry.pack(pady=10)

        mensaje_error = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 14, "bold"))
        mensaje_error.pack(pady=5)

        def guardar_observacion():
            self.observacion = observacion_entry.get("1.0", "end").strip()
            if not self.observacion:
                mensaje_error.configure(text="Debe ingresar una observación.")
                return
            mensaje_error.configure(text="")
            self.tomarObservacion()

        botones_frame = ctk.CTkFrame(self, fg_color="transparent")
        botones_frame.pack(pady=20)

        guardar_btn = ctk.CTkButton(
            botones_frame,
            text="Guardar",
            command=guardar_observacion,
            width=200,  
            height=55,  
            font=("Arial", 18, "bold"),
            fg_color="#198754",
            hover_color="#157347"  
        )
        guardar_btn.pack(side="left", padx=10)

        volver_btn = ctk.CTkButton(
            botones_frame,
            text="Volver",
            command=lambda: self.mostrarOI(self.datosOrdenes),
            width=200,  
            height=55,  
            font=("Arial", 18, "bold"),
            fg_color="#6c757d",      
            hover_color="#5a6268"
        )
        volver_btn.pack(side="left", padx=10)

    @property
    def frameDeEspera(self):
        pass

    @property
    def motivosGrilla(self):
        # Frame contenedor horizontal
        tablaFrame = ctk.CTkFrame(self)
        tablaFrame.pack(fill="both", expand=True, pady=(20, 0))

        # Crear encabezados de tabla
        columnas = ["Descripción", "Seleccionar", "Anular Selección"]
        for col_idx, col in enumerate(columnas):
            label = ctk.CTkLabel(tablaFrame, text=col, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col_idx, padx=10, pady=10)

        # Llenar la tabla con motivos No seleccionados
        #   Tienen un botón Seleccionar
        for i, motivo_dict in enumerate(self.motivos):
            descripcion = motivo_dict.get("descripcion")
            # motivo_obj = motivo_dict.get("motivo")
            ctk.CTkLabel(tablaFrame, text=descripcion).grid(row=i+1, column=0, padx=10, pady=5)
            selectButton = ctk.CTkButton(
                tablaFrame,
                text="Seleccionar",
                command=lambda m=motivo_dict: self.tomarMFS(m)
            )
            selectButton.grid(row=i+1, column=1, padx=10, pady=5)

        # Lenar la tabla con motivos Seleccionados
        #   Tienen un botón Borrar
        for i, motivo_dict in enumerate(self.motivosSeleccionados):
            i += len(self.motivos)
            descripcion = motivo_dict.get("descripcion")
            # motivo_obj = motivo_dict.get("motivo")
            ctk.CTkLabel(tablaFrame, text=descripcion).grid(row=i+1, column=0, padx=10, pady=5)
            selectButton = ctk.CTkButton(
                tablaFrame,
                text="Anular Selección",
                command=lambda m=motivo_dict: self.anularSeleccionMFS(m),
                fg_color="#dc3545",
                hover_color="#c82333",
            )
            selectButton.grid(row=i+1, column=2, padx=10, pady=5)





    def habilitarVentana(self):
        self.tkraise()
        self.gestor = GestorOrdenDeCierre(self.sesion, self)

    def mostrarOI(self, ordenes):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        self.headerText = "Órdenes de Inspección"
        self.header

        # tabla 
        self.datosOrdenes = ordenes
        self.ordenesGrilla

        # Botón para cancelar CU
        self.botonCancelar

    def seleccionarOI(self, orden):
        self.gestor.tomarOrden(orden)

    def pedirObservacion(self):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        self.headerText = "Ingrese la observación de cierre"
        self.header

        # Input para la Observación de cierre
        self.cuadroObservacion

        # Botón para cancelar CU
        self.botonCancelar

    def tomarObservacion(self):
        self.gestor.tomarObservacion(self.observacion)

    def pedirSituacionSismografo(self, estadoEnLinea, estadoFueraDeServicio):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        self.headerText = "Situación del Sismógrafo"
        self.header

        # Frame para los estados y botones
        estados_frame = ctk.CTkFrame(self, fg_color="transparent")
        estados_frame.pack(pady=40)

        # Estado En Línea
        en_linea_label = ctk.CTkLabel(
            estados_frame,
            text=estadoEnLinea,
            font=("Arial", 20, "bold"),
            text_color="#198754"
        )
        en_linea_label.grid(row=0, column=0, padx=40, pady=10)
        en_linea_btn = ctk.CTkButton(
            estados_frame,
            text="Seleccionar",
            command=self.seleccionarEnLinea,
            width=180,
            height=45,
            font=("Arial", 16, "bold")
        )
        en_linea_btn.grid(row=1, column=0, padx=40, pady=10)

        # Estado Fuera de Servicio
        fs_label = ctk.CTkLabel(
            estados_frame,
            text=estadoFueraDeServicio,
            font=("Arial", 20, "bold"),
            text_color="#dc3545"
        )
        fs_label.grid(row=0, column=1, padx=40, pady=10)
        fs_btn = ctk.CTkButton(
            estados_frame,
            text="Seleccionar",
            command=self.seleccionarFS,
            width=180,
            height=45,
            font=("Arial", 16, "bold")
        )
        fs_btn.grid(row=1, column=1, padx=40, pady=10)

        # Botón para cancelar CU
        self.botonCancelar

    def seleccionarFS(self):
        self.gestor.seleccionarFS()

    def seleccionarEnLinea(self):
        self.gestor.seleccionarEnLinea()

    def mostrarMFS(self, motivos=None):
        if motivos:
            self.motivos = motivos
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        self.headerText = "Motivos de Cierre"
        self.header

        # Tabla
        self.motivosGrilla

        # Botón para cancelar CU
        self.botonCancelar

    def tomarMFS(self, motivo):
        # Limpia la pantalla y muestra campo para comentario del motivo seleccionado
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        self.header

        label = ctk.CTkLabel(
            self,
            text=f"Ingrese un comentario",
            font=("Arial", 30, "bold"),
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
            
            self.tomarComentario(motivo, comentario)

        # Frame para los botones
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
        self.botonCancelar

    def tomarComentario(self, motivo, comentario):
        self.motivos.remove(motivo)
        self.motivosSeleccionados.append(motivo)
        
        self.gestor.tomarMotivoYComentario(motivo.get("motivo"), comentario)

    def anularSeleccionMFS(self, motivo):
        self.motivosSeleccionados.remove(motivo)
        self.motivos.append(motivo)

        self.gestor.anularSeleccionMFS(motivo.get("motivo"))

    def pedirConfirmacion(self):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado
        # self.headerText = "Motivos de Cierre"
        self.header

        # Tabla
        self.motivosGrilla

        # Frame para los botones
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
            command=self.confirmar
        )
        confirmar_btn.pack(side="left", padx=10)

        # Botón para cancelar CU
        self.botonCancelar

    def confirmar(self):
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
        self.gestor.confirmar()

    def cerrar(self):
        from fabricacion_pura.pantallaInicio import PantallaInicio
        self.controller.showFrame(PantallaInicio)

