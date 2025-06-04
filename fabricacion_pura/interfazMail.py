import customtkinter as ctk

class InterfazMail(ctk.CTkToplevel):
    def __init__(self, master, mails, asunto, mensaje):
        super().__init__(master)
        self.title("Correo")
        self.geometry("500x380")
        self.resizable(False, False)
        self.configure(bg="#fff")

        self.transient(master)
        self.grab_set()

        # Cabecera roja tipo Gmail
        header = ctk.CTkFrame(self, fg_color="#d93025", height=40)
        header.pack(fill="x", side="top")
        ctk.CTkLabel(header, text="Correo Enviado", font=("Arial", 18, "bold"), text_color="white", bg_color="#d93025").pack(side="left", padx=15, pady=5)

        # Cuerpo del mail
        body = ctk.CTkFrame(self, fg_color="#fff")
        body.pack(fill="both", expand=True, padx=20, pady=10)

        # Destinatarios estilo Gmail (chips)
        ctk.CTkLabel(body, text="Para", font=("Arial", 12, "bold"), text_color="#5f6368").grid(row=0, column=0, sticky="nw", pady=(5, 2))
        chips_frame = ctk.CTkFrame(body, fg_color="#fff")
        chips_frame.grid(row=0, column=1, sticky="w", pady=(5, 2), padx=(5,0))

        MAX_CHIPS_POR_FILA = 2  

        if isinstance(mails, list):
            for idx, mail in enumerate(mails):
                fila = idx // MAX_CHIPS_POR_FILA
                columna = idx % MAX_CHIPS_POR_FILA
                chip = ctk.CTkLabel(
                    chips_frame,
                    text=mail,
                    font=("Arial", 12),
                    text_color="#202124",
                    fg_color="#e0e0e0",
                    corner_radius=18,
                    padx=8,
                    pady=1
                )
                chip.grid(row=fila, column=columna, padx=2, pady=2, sticky="w")
        else:
            chip = ctk.CTkLabel(
                chips_frame,
                text=str(mails),
                font=("Arial", 12),
                text_color="#202124",
                fg_color="#e0e0e0",
                corner_radius=18,
                padx=8,
                pady=1
            )
            chip.grid(row=0, column=0, padx=2, pady=2, sticky="w")

        # Asunto
        ctk.CTkLabel(body, text="Asunto", font=("Arial", 12, "bold"), text_color="#5f6368").grid(row=1, column=0, sticky="w", pady=(5, 2))
        ctk.CTkLabel(body, text=asunto, font=("Arial", 12), text_color="#202124").grid(row=1, column=1, sticky="w", pady=(5, 2), padx=(5,0))

        # Mensaje
        ctk.CTkLabel(body, text="Mensaje", font=("Arial", 12, "bold"), text_color="#5f6368").grid(row=2, column=0, sticky="nw", pady=(5, 2))
        mensaje_box = ctk.CTkTextbox(body, width=340, height=120)
        mensaje_box.grid(row=2, column=1, sticky="w", pady=(5, 2), padx=(5,0))
        mensaje_box.insert("1.0", mensaje)
        mensaje_box.configure(state="disabled")

        # Botón enviar (simulado) y cerrar
        botones = ctk.CTkFrame(body, fg_color="#fff")
        botones.grid(row=3, column=1, sticky="e", pady=(20, 0))

        ctk.CTkButton(botones, text="Cerrar", fg_color="#dc3545", hover_color="#c82333", font=("Arial", 12, "bold"), width=90, command=self.destroy).pack(side="left")

        # Ajustar columnas para mejor visual
        body.grid_columnconfigure(0, minsize=70)
        body.grid_columnconfigure(1, weight=1)

    @staticmethod
    def enviarMail(mail, asunto, mensaje):
        # Implementacion de la logica para enviar el mail
        print(f"\n\nDestinatario: {mail}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: \n{mensaje}")