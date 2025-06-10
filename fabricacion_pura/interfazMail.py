import customtkinter as ctk

class InterfazMail(ctk.CTkToplevel):
    def __init__(self, master, mails, asunto, mensaje):
        super().__init__(master)
        self.title("Correo")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#fff")

        self.transient(master)
        self.grab_set()

        self.mails = mails
        self.asunto = asunto
        self.mensaje = mensaje

        # Cabecera roja tipo Gmail
        header = ctk.CTkFrame(self, fg_color="#d93025", height=40)
        header.pack(fill="x", side="top")
        ctk.CTkLabel(header, text="Correo Enviado", font=("Arial", 18, "bold"), text_color="white", bg_color="#d93025").pack(side="left", padx=15, pady=5)

        # Cuerpo del mail (usa fill y expand para ocupar todo)
        body = ctk.CTkFrame(self, fg_color="#fff")
        body.pack(fill="both", expand=True, padx=40, pady=20)

        # Destinatarios estilo Gmail (chips)
        ctk.CTkLabel(body, text="Para", font=("Arial", 14, "bold"), text_color="#5f6368").grid(row=0, column=0, sticky="ne", pady=(5, 2))
        chips_frame = ctk.CTkFrame(body, fg_color="#fff")
        chips_frame.grid(row=0, column=1, sticky="w", pady=(5, 2), padx=(5,0))

        MAX_CHIPS_POR_FILA = 6  # Más chips por fila para ventana grande

        if isinstance(self.mails, list):
            for idx, mail in enumerate(self.mails):
                fila = idx // MAX_CHIPS_POR_FILA
                columna = idx % MAX_CHIPS_POR_FILA
                chip = ctk.CTkLabel(
                    chips_frame,
                    text=mail,
                    font=("Arial", 13),
                    text_color="#202124",
                    fg_color="#e0e0e0",
                    corner_radius=18,
                    padx=12,
                    pady=3
                )
                chip.grid(row=fila, column=columna, padx=4, pady=4, sticky="w")
        else:
            chip = ctk.CTkLabel(
                chips_frame,
                text=str(self.mails),
                font=("Arial", 13),
                text_color="#202124",
                fg_color="#e0e0e0",
                corner_radius=18,
                padx=12,
                pady=3
            )
            chip.grid(row=0, column=0, padx=4, pady=4, sticky="w")

        # Asunto
        ctk.CTkLabel(body, text="Asunto", font=("Arial", 14, "bold"), text_color="#5f6368").grid(row=1, column=0, sticky="ne", pady=(15, 2))
        ctk.CTkLabel(body, text=self.asunto, font=("Arial", 13), text_color="#202124", anchor="w").grid(row=1, column=1, sticky="ew", pady=(15, 2), padx=(5,0))

        # Mensaje
        ctk.CTkLabel(
            body,
            text="Mensaje",
            font=("Arial", 14, "bold"),
            text_color="#5f6368"
        ).grid(row=2, column=0, sticky="w", pady=(15, 2), padx=(5, 0))

        mensaje_box = ctk.CTkTextbox(body, width=600, height=300)
        mensaje_box.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(5, 2), padx=(5, 0))
        mensaje_box.insert("1.0", self.mensaje)
        mensaje_box.configure(state="disabled")

        # Ajusta el rowconfigure para la nueva fila del mensaje
        body.grid_rowconfigure(4, weight=1)
        body.grid_columnconfigure(1, weight=1)

        # Botón cerrar abajo a la derecha
        cerrar_frame = ctk.CTkFrame(body, fg_color="#fff")
        cerrar_frame.grid(row=5, column=1, sticky="se", pady=(20, 0))
        ctk.CTkButton(
            cerrar_frame,
            text="Cerrar",
            fg_color="#dc3545",
            hover_color="#c82333",
            font=("Arial", 13, "bold"),
            width=120,
            command=self.destroy
        ).pack(side="right", padx=10, pady=10)
               
        self.enviarMail()

    def enviarMail(self):
        # Implementacion de la logica para enviar el mail
        print(f"\n\nDestinatario/s: {self.mails}")
        print(f"Asunto: {self.asunto}")
        print(f"Mensaje: \n{self.mensaje}")