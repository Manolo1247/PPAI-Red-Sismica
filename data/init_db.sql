-- Script para inicializar la base de datos

-- Insertar roles con descripciones
INSERT INTO Rol (nombre, descripcion) VALUES ('Administrador de Red', 'Gestiona la red y la infraestructura tecnológica de la red sísmica.');
INSERT INTO Rol (nombre, descripcion) VALUES ('Encargado de Instalaciones', 'Supervisa y ejecuta la instalación y mantenimiento de equipos.');
INSERT INTO Rol (nombre, descripcion) VALUES ('Analista en Sismos', 'Analiza los datos sísmicos y genera reportes técnicos.');
INSERT INTO Rol (nombre, descripcion) VALUES ('Responsable de Inspecciones', 'Coordina y realiza inspecciones de estaciones y equipos.');
INSERT INTO Rol (nombre, descripcion) VALUES ('Responsable de Reparacion', 'Gestiona y coordina las reparaciones de equipos y estaciones.');

-- Insertar estados para Orden de Inspeccion
INSERT INTO Estado (ambito, nombre) VALUES ('Orden de Inspeccion', 'Pendiente de Realizacion');
INSERT INTO Estado (ambito, nombre) VALUES ('Orden de Inspeccion', 'Parcialmente Realizada');
INSERT INTO Estado (ambito, nombre) VALUES ('Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO Estado (ambito, nombre) VALUES ('Orden de Inspeccion', 'Cerrada');

-- Insertar estados para Sismografo
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Disponible');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Pendiente Cerfificacion');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Habilitado para Construccion');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Incluido en Plan Construccion');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'En Instalacion');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Reclamado');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'En Linea');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Inhabilitado');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'Fuera de Servicio');
INSERT INTO Estado (ambito, nombre) VALUES ('Sismografo', 'De Baja');

-- Insertar motivos tipo
INSERT INTO MotivoTipo (descripcion) VALUES ('Avería por vibración');
INSERT INTO MotivoTipo (descripcion) VALUES ('Desgaste de componente');
INSERT INTO MotivoTipo (descripcion) VALUES ('Fallo en el sistema de registro');
INSERT INTO MotivoTipo (descripcion) VALUES ('Vandalismo');
INSERT INTO MotivoTipo (descripcion) VALUES ('Fallo en fuente de alimentación');

-- Insertar empleados, uno para cada rol
INSERT INTO Empleado (nombre, apellido, mail, telefono, rol) VALUES ('Juan', 'Pérez', 'juan.perez@mail.com', '1111111111', 'Administrador de Red');
INSERT INTO Empleado (nombre, apellido, mail, telefono, rol) VALUES ('María', 'Gómez', 'maria.gomez@mail.com', '2222222222', 'Encargado de Instalaciones');
INSERT INTO Empleado (nombre, apellido, mail, telefono, rol) VALUES ('Carlos', 'López', 'carlos.lopez@mail.com', '3333333333', 'Analista en Sismos');
INSERT INTO Empleado (nombre, apellido, mail, telefono, rol) VALUES ('Ana', 'Martínez', 'ana.martinez@mail.com', '4444444444', 'Responsable de Inspecciones');


-- Insertar usuarios uno para cada empleado
INSERT INTO Usuario (nombre, contraseña, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('juanp', 'admin123', 'Juan', 'Pérez', 'juan.perez@mail.com');
INSERT INTO Usuario (nombre, contraseña, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('mariag', 'instal456', 'María', 'Gómez', 'maria.gomez@mail.com');
INSERT INTO Usuario (nombre, contraseña, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('carlosl', 'sismo789', 'Carlos', 'López', 'carlos.lopez@mail.com');
INSERT INTO Usuario (nombre, contraseña, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('anam', 'insp321', 'Ana', 'Martínez', 'ana.martinez@mail.com');

-- Insertar 10 estaciones sismológicas de ejemplo
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST001', 'Estación Norte', -31.4201, -64.1888, '2023-01-10', 'doc1.pdf', 'CERT001');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST002', 'Estación Sur', -32.8908, -68.8272, '2023-01-15', 'doc2.pdf', 'CERT002');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST003', 'Estación Este', -34.6037, -58.3816, '2023-01-20', 'doc3.pdf', 'CERT003');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST004', 'Estación Oeste', -38.4161, -63.6167, '2023-01-25', 'doc4.pdf', 'CERT004');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST005', 'Estación Central', -31.5375, -68.5364, '2023-02-01', 'doc5.pdf', 'CERT005');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST006', 'Estación Delta', -27.4606, -58.9839, '2023-02-05', 'doc6.pdf', 'CERT006');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST007', 'Estación Sierra', -24.7821, -65.4232, '2023-02-10', 'doc7.pdf', 'CERT007');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST008', 'Estación Pampa', -36.6200, -64.2900, '2023-02-15', 'doc8.pdf', 'CERT008');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST009', 'Estación Andina', -33.0472, -71.6127, '2023-02-20', 'doc9.pdf', 'CERT009');
INSERT INTO EstacionSismologica (codigo_estacion, nombre, latitud, longitud, fecha_solicitud_certificacion, documento_certificacion, numero_certificacion) VALUES ('EST010', 'Estación Patagonia', -42.7692, -65.0385, '2023-02-25', 'doc10.pdf', 'CERT010');

-- Insertar 10 sismografos de ejemplo, todos en estado Inhabilitado y asociados a estaciones
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO001', '2022-01-10', 'SN-1001', 'EST001', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO002', '2022-02-15', 'SN-1002', 'EST002', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO003', '2022-03-20', 'SN-1003', 'EST003', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO004', '2022-04-25', 'SN-1004', 'EST004', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO005', '2022-05-30', 'SN-1005', 'EST005', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO006', '2022-06-10', 'SN-1006', 'EST006', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO007', '2022-07-15', 'SN-1007', 'EST007', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO008', '2022-08-20', 'SN-1008', 'EST008', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO009', '2022-09-25', 'SN-1009', 'EST009', 'Sismografo', 'Inhabilitado');
INSERT INTO Sismografo (identificador, fecha_adquisicion, numero_serie, codigo_estacion, ambito_estado_actual, nombre_estado_actual) VALUES ('SISMO010', '2022-10-30', 'SN-1010', 'EST010', 'Sismografo', 'Inhabilitado');

-- Insertar 10 órdenes de inspección: 9 finalizadas y 1 pendiente de realización, todas asignadas a Ana Martínez
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST001', '2024-01-10 08:00:00', '2024-01-10 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST002', '2024-01-11 08:00:00', '2024-01-11 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST003', '2024-01-12 08:00:00', '2024-01-12 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST004', '2024-01-13 08:00:00', '2024-01-13 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST005', '2024-01-14 08:00:00', '2024-01-14 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST006', '2024-01-15 08:00:00', '2024-01-15 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST007', '2024-01-16 08:00:00', '2024-01-16 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST008', '2024-01-17 08:00:00', '2024-01-17 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST009', '2024-01-18 08:00:00', '2024-01-18 12:00:00', NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Completamente Realizada');
INSERT INTO OrdenDeInspeccion (codigo_estacion, fecha_hora_inicio, fecha_hora_finalizacion, fecha_hora_cierre, observacion_cierre, nombre_empleado, apellido_empleado, mail_empleado, ambito, nombre) VALUES ('EST010', '2024-01-19 08:00:00', NULL, NULL, NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com', 'Orden de Inspeccion', 'Pendiente de Realizacion');

-- Insertar cambios de estado para los 10 sismógrafos
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO001', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO001', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO001', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO001', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO001', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO002', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO002', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO002', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO002', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO002', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO003', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO003', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO003', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO003', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO003', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO004', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO004', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO004', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO004', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO004', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO005', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO005', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO005', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO005', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO005', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO006', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO006', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO006', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO006', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO006', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO007', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO007', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO007', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO007', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO007', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO008', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO008', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO008', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO008', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO008', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO009', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO009', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO009', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO009', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO009', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-01 08:00:00', 'Sismografo', 'Disponible', 'SISMO010', '2024-01-02 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-02 08:00:00', 'Sismografo', 'Incluido en Plan Construccion', 'SISMO010', '2024-01-03 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-03 08:00:00', 'Sismografo', 'En Instalacion', 'SISMO010', '2024-01-04 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-04 08:00:00', 'Sismografo', 'En Linea', 'SISMO010', '2024-01-05 08:00:00', 'Ana', 'Martínez', 'ana.martinez@mail.com');
INSERT INTO CambioDeEstado (fecha_hora_inicio, ambito, nombre, identificador_sismografo, fecha_hora_fin, nombre_empleado, apellido_empleado, mail_empleado) VALUES ('2024-01-05 08:00:00', 'Sismografo', 'Inhabilitado', 'SISMO010', NULL, 'Ana', 'Martínez', 'ana.martinez@mail.com');

