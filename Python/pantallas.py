import customtkinter as ctk

class PantallaOrdenDeCierre(ctk.CTkFrame):
    def __init__(self, master, gestor):
        super().__init__(master)
        self.gestor = gestor
        self.pack(fill="both", expand=True)

    def mostrarMFS(self, motivos):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        self.motivos_restantes = motivos  # Guarda motivos restantes

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

        # Llenar la tabla con datos
        for i, motivo in enumerate(motivos):
            ctk.CTkLabel(tableFrame, text=motivo.getDescripcion()).grid(row=i+1, column=0, padx=10, pady=5)
            selectButton = ctk.CTkButton(
                tableFrame,
                text="Seleccionar",
                command=lambda m=motivo: self.tomarMotivo(m)
            )
            selectButton.grid(row=i+1, column=1, padx=10, pady=5)

        # Si ya no quedan motivos, mostrar botón de confirmación
        if not motivos:
            confirmar_btn = ctk.CTkButton(
                self,
                text="Confirmar",
                font=("Arial", 18, "bold"),
                fg_color="#198754",  # Verde Bootstrap
                hover_color="#157347",  # Verde más oscuro al pasar el mouse
                width=200,
                height=50,
                command=self.gestor.confirmar
            )
            confirmar_btn.pack(pady=30)

    def tomarMotivo(self, motivo):
        # Limpia la pantalla y muestra campo para comentario
        for widget in self.winfo_children():
            widget.destroy()

        label = ctk.CTkLabel(self, text=f"Comentario para: {motivo.getDescripcion()}", font=("Arial", 18, "bold"), text_color="#0d6efd")
        label.pack(pady=20)

        comentario_entry = ctk.CTkTextbox(self, width=400, height=100)
        comentario_entry.pack(pady=10)

        def guardar_comentario():
            comentario = comentario_entry.get("1.0", "end").strip()
            self.tomarComentario(motivo, comentario)

        guardar_btn = ctk.CTkButton(
            self,
            text="Guardar",
            font=("Arial", 18, "bold"),
            fg_color="#0d6efd",
            hover_color="#0b5ed7",
            width=200,
            height=50,
            command=guardar_comentario
        )
        guardar_btn.pack(pady=20)

    def tomarComentario(self, motivo, comentario):
        # Arma el diccionario y llama al gestor
        motivo_dict = {"motivo": motivo, "comentario": comentario}
        self.gestor.tomarMotivoYComentario(motivo_dict)

    def pedirConfirmacion(self):
        # Muestra la tabla de motivos restantes y botón de confirmación si no quedan más
        motivos_restantes = [m for m in self.motivos_restantes if m not in [d["motivo"] for d in self.gestor.motivosSeleccionados]]
        self.mostrarMFS(motivos_restantes)