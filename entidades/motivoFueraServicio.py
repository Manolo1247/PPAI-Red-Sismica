from entidades.motivoTipo import MotivoTipo

class MotivoFueraServicio:
    def __init__(self, comentario, motivoTipo: MotivoTipo):
        self.comentario = comentario
        self.motivoTipo = motivoTipo