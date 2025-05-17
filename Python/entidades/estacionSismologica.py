import sqlite3
from RUTAS.rutas import ARCHIVO_BD

#from .sismografo import Sismografo
class EstacionSismologica:
    def __init__(self, codigo, nombre, latitud, longitud, fechaSolicitudCertificacion, documentoCertificacion, numeroCertificacion):
        self.codigo = codigo
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self.documentoCertificacion = documentoCertificacion
        self.numeroCertificacion = numeroCertificacion

    def getNombre(self):
        return self.nombre
    
    def getIdSismografo(self):
        con = sqlite3.connect(ARCHIVO_BD)
        cursor = con.cursor()
        sql = "SELECT identificador FROM Sismografo WHERE codigo_estacion = ?"
        cursor.execute(sql, (self.codigo,))
        row = cursor.fetchone()
        con.close()
        return row[0] 