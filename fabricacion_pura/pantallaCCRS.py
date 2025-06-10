import customtkinter as ctk

class PantallaCCRS(ctk.CTkToplevel):
    def __init__(self, master, sismografo):
        super().__init__(master)
        self.title("Pantalla CCRS")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#fff")
        self.configure(border_color="#dcdcdc", border_width=1)


        self.sismografo=sismografo

        self.publicar()

    @property
    def header(self):
        # Encabezado estilo Bootstrap
        frame = ctk.CTkFrame(self, fg_color="#0d6efd", height=80)
        frame.grid(row=0, column=0, columnspan=2, sticky="ew")  # sticky="ew" para expandir en X
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(
            frame,
            text="Pantalla CCRS",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        label.pack(pady=20)

    @property
    def funciones(self):
        frame = ctk.CTkFrame(self, fg_color="#f1f3f4")
        frame.grid(row=1, column=0, padx=10, pady=20)

        # Estilo base para botones
        botonEstilo = {
            "width": 250,
            "height": 50,
            "font": ("Arial", 16),
        }

        # Botones centrados con estilo de Bootstrap
        funcion1 = ctk.CTkButton(
            frame,
            text="Función 1",
            **botonEstilo,
            fg_color="#0d6efd",  
            hover_color="#0b5ed7",  
            corner_radius=8,
        )
        funcion1.pack(pady=20)

        funcion2 = ctk.CTkButton(
            frame,
            text="Función 2",
            **botonEstilo,
            fg_color="#0d6efd",  
            hover_color="#0b5ed7",  
            corner_radius=8,
        )
        funcion2.pack(pady=20)

        closeButton = ctk.CTkButton(
            frame,
            text="Cerrar",
            **botonEstilo,
            fg_color="#dc3545",
            hover_color="#c82333",
            corner_radius=8,
            command=self.destroy
        )
        closeButton.pack(pady=30)

    @property
    def frameDeNotificacion(self):
        frame = ctk.CTkFrame(self,fg_color="#f1f3f4")
        frame.grid(row=1,column=1,padx=10)

        # Label de título
        titulo = ctk.CTkLabel(
            frame,
            text="Notificaciones",
            font=("Arial", 18, "bold"),
            text_color="#0d6efd"
        )
        titulo.pack(pady=(10, 20))

        # Cuadro de notificación
        notif_frame = ctk.CTkFrame(frame, fg_color="#fff3cd", border_color="#ffeeba", border_width=2, corner_radius=10)
        notif_frame.pack(fill="x", padx=10, pady=5)

        notif_label = ctk.CTkLabel(
            notif_frame,
            text=f"Nuevo sismógrafo fuera de servicio: {self.sismografo}",
            font=("Arial", 14, "bold"),
            text_color="#856404"
        )
        notif_label.pack(padx=10, pady=10)


    def publicar(self):
        # Limpia la pantalla
        for widget in self.winfo_children():
            widget.destroy()

        # Encabezado 
        self.header

        # Frame de funciones
        self.funciones
        # Frame de Notificaciones
        self.frameDeNotificacion




