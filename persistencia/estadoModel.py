from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)

class EstadoModel(Model):
    ambito = CharField()
    nombre = CharField()

    class Meta:
        database = db
        table_name = "Estado"
        primary_key = CompositeKey("ambito", "nombre")

    @classmethod
    def findAll(cls):
        from entidades.estado import Estado
        
        rowEstados = cls.select()

        estados = []
        for rowEstado in rowEstados:
            estados.append(Estado(rowEstado.ambito, rowEstado.nombre))

        return estados
