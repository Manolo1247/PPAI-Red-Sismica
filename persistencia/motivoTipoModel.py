from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)

class MotivoTipoModel(Model):
    descripcion = CharField(primary_key=True)

    class Meta:
        database = db
        table_name = "MotivoTipo"

    @classmethod
    def findAll(cls):
        from entidades.motivoTipo import MotivoTipo
        
        rowMTs = cls.select()

        motivos = []
        for rowMT in rowMTs:
            motivos.append(MotivoTipo(rowMT.descripcion))

        return motivos
