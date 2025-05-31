from peewee import *
from RUTAS.rutas import ARCHIVO_BD

# Conexión a la base de datos SQLite
db = SqliteDatabase(ARCHIVO_BD)


class RolModel(Model):
    nombre = CharField(primary_key=True)
    descripcion = CharField(null=True)

    class Meta:
        database = db
        table_name = "Rol"

    @classmethod
    def findAll(cls):
        from entidades.rol import Rol
        
        rowRoles = cls.select()

        roles = []
        for rowRol in rowRoles:
            roles.append(Rol(rowRol.nombre, rowRol.descripcion))

        return roles
