import sqlite3
from RUTAS.rutas import ARCHIVO_BD

con = sqlite3.connect(ARCHIVO_BD)
cursor = con.cursor()
sql = (
            'SELECT O.numero, O.fecha_hora_inicio, O.fecha_hora_finalizacion, O.fecha_hora_cierre, O.observacion_cierre, O.ambito, O.nombre, '
            'E.nombre, E.apellido, E.mail, E.telefono, R.nombre, R.descripcion, '
            'ES.codigo_estacion, ES.nombre, ES.latitud, ES.longitud, ES.fecha_solicitud_certificacion, ES.documento_certificacion, ES.numero_certificacion '
            'FROM OrdenDeInspeccion O '
            'JOIN Empleado E ON O.nombre_empleado = E.nombre AND O.apellido_empleado = E.apellido AND O.mail_empleado = E.mail '
            'JOIN Rol R ON E.rol = R.nombre '
            'JOIN EstacionSismologica ES ON O.codigo_estacion = ES.codigo_estacion '
        )
cursor.execute(sql)
filas = cursor.fetchall()
if filas:
    fila = filas[0]
    for col_idx, valor in enumerate(fila):
        print(f'{col_idx}: {valor}')
con.close()