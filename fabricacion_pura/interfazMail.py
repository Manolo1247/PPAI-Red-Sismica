class InterfazMail:
    @staticmethod
    def enviarMail(mail, asunto, mensaje):
        # Implementacion de la logica para enviar el mail
        print(f"\n\nDestinatario: {mail}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: \n{mensaje}")