import customtkinter as ctk

class PantallaCCRS(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("")
        self.geometry("400x100")
        self.resizable(False, False)
        self.configure(fg_color="#f1f3f4")  # Fondo gris claro para todo el popup

        # Centrar el popup en la pantalla principal
        self.update_idletasks()
        x = master.winfo_x() + (master.winfo_width() // 2) - 200
        y = master.winfo_y() + (master.winfo_height() // 2) - 50
        self.geometry(f"+{x}+{y}")

        self.publicar()

    def publicar(self):
        # Frame de notificación tipo push estilo moderno gris
        notif_frame = ctk.CTkFrame(
            self,
            fg_color="#e0e0e0",           # Fondo gris claro moderno
            border_color="#bdbdbd",       # Borde gris más oscuro
            border_width=2,
            corner_radius=12
        )
        notif_frame.pack(fill="both", expand=True, padx=10, pady=10)

        notif_label = ctk.CTkLabel(
            notif_frame,
            text="Nuevo sismógrafo Fuera de Servicio",
            font=("Arial", 15, "bold"),
            text_color="#424242"          # Texto gris oscuro
        )
        notif_label.pack(expand=True, padx=18, pady=18)