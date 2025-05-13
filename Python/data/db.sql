-- Tabla: Rol
CREATE TABLE IF NOT EXISTS Rol (
    nombre TEXT PRIMARY KEY,
    descripcion TEXT
);

-- Tabla: Empleado
CREATE TABLE IF NOT EXISTS Empleado (
    nombre TEXT,
    apellido TEXT,
    mail TEXT,
    telefono TEXT,
    rol TEXT,
    PRIMARY KEY (nombre, apellido, mail),
	FOREIGN KEY (rol) REFERENCES Rol(nombre)
);

-- Tabla: Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    nombre TEXT PRIMARY KEY,
    contraseña TEXT,
    nombre_empleado TEXT,
    apellido_empleado TEXT,
    mail_empleado TEXT,
    FOREIGN KEY (nombre_empleado, apellido_empleado, mail_empleado) REFERENCES Empleado(nombre, apellido, mail)
);

-- Tabla: Sesion
CREATE TABLE IF NOT EXISTS Sesion (
    nombre_usuario TEXT,
    fecha_hora_inicio DATETIME,
    fecha_hora_fin DATETIME,
    PRIMARY KEY (nombre_usuario, fecha_hora_inicio),
    FOREIGN KEY (nombre_usuario) REFERENCES Usuario(nombre)
);

-- Tabla: Estado
CREATE TABLE IF NOT EXISTS Estado (
    ambito TEXT,
    nombre TEXT,
    PRIMARY KEY (ambito, nombre)
);

-- Tabla: MotivoTipo
CREATE TABLE IF NOT EXISTS MotivoTipo (
    descripcion TEXT PRIMARY KEY
);

-- Tabla: MotivoFueraServicio
CREATE TABLE IF NOT EXISTS MotivoFueraServicio (
    fecha_hora_inicio DATETIME,
    ambito TEXT,
    nombre TEXT,
    motivo_tipo TEXT,
    comentario TEXT,
    PRIMARY KEY (fecha_hora_inicio, ambito, nombre, motivo_tipo),
    FOREIGN KEY (fecha_hora_inicio, ambito, nombre) REFERENCES CambioDeEstado(fecha_hora_inicio, ambito, nombre),
    FOREIGN KEY (motivo_tipo) REFERENCES MotivoTipo(descripcion)
);

-- Tabla: EstacionSismologica
CREATE TABLE IF NOT EXISTS EstacionSismologica (
    codigo_estacion TEXT PRIMARY KEY,
    nombre TEXT,
    latitud REAL,
    longitud REAL,
    fecha_solicitud_certificacion DATETIME,
    documento_certificacion TEXT,
    numero_certificacion TEXT
);

-- Tabla: Sismografo
CREATE TABLE IF NOT EXISTS Sismografo (
    identificador TEXT PRIMARY KEY,
    fecha_adquisicion DATETIME,
    numero_serie TEXT,
    codigo_estacion TEXT,
    ambito_estado_actual TEXT,
    nombre_estado_actual TEXT,
    FOREIGN KEY (codigo_estacion) REFERENCES EstacionSismologica(codigo_estacion),
    FOREIGN KEY (ambito_estado_actual, nombre_estado_actual) REFERENCES Estado(ambito, nombre)
);

-- Tabla: CambioDeEstado
CREATE TABLE IF NOT EXISTS CambioDeEstado (
    fecha_hora_inicio DATETIME,
    ambito TEXT,
    nombre TEXT,
    fecha_hora_fin DATETIME,
    nombre_empleado TEXT,
    apellido_empleado TEXT,
    mail_empleado TEXT,
    identificador_sismografo TEXT,
    PRIMARY KEY (fecha_hora_inicio, ambito, nombre),
    FOREIGN KEY (ambito, nombre) REFERENCES Estado(ambito, nombre),
    FOREIGN KEY (identificador_sismografo) REFERENCES Sismografo(identificador),
    FOREIGN KEY (nombre_empleado, apellido_empleado, mail_empleado) REFERENCES Empleado(nombre, apellido, mail)
);

-- Tabla: OrdenDeInspeccion
CREATE TABLE IF NOT EXISTS OrdenDeInspeccion (
    numero INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_estacion TEXT,
    fecha_hora_inicio DATETIME,
    fecha_hora_finalizacion DATETIME,
    fecha_hora_cierre DATETIME,
    observacion_cierre TEXT,
    nombre_empleado TEXT,
    apellido_empleado TEXT,
    mail_empleado TEXT,
    ambito TEXT,
    nombre TEXT,
    FOREIGN KEY (codigo_estacion) REFERENCES EstacionSismologica(codigo_estacion),
    FOREIGN KEY (nombre_empleado, apellido_empleado, mail_empleado) REFERENCES Empleado(nombre, apellido, mail),
    FOREIGN KEY (ambito, nombre) REFERENCES Estado(ambito, nombre)
);
