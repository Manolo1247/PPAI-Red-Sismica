from fabricacion_pura.gestor import GestorOrdenDeCierre
from entidades.sesion import Sesion
from entidades.usuario import Usuario
from entidades.empleado import Empleado
from entidades.rol import Rol
from entidades.ordenDeInspeccion import OrdenDeInspeccion
from entidades.estacionSismologica import EstacionSismologica
from entidades.estado import Estado

import sqlite3
from RUTAS.rutas import ARCHIVO_BD
from datetime import datetime



fechaHoraActual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
numero = 1

con = sqlite3.connect(ARCHIVO_BD)
try:
    cursor = con.cursor()
    sql1 = (
        'UPDATE OrdenDeInspeccion '
        'SET fecha_hora_cierre = ?'
        'WHERE numero = ?'
    )
    cursor.execute(sql1, (fechaHoraActual, numero))
    con.commit()
finally:
    con.close()

print(fechaHoraActual)