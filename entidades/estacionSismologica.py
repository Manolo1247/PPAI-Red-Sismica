class EstacionSismologica:
    def __init__(self, codigo, nombre, latitud, longitud, fechaSolicitudCertificacion, documentoCertificacion, numeroCertificacion):
        self.codigo = codigo
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.fechaSolicitudCertificacion = fechaSolicitudCertificacion
        self.documentoCertificacion = documentoCertificacion
        self.numeroCertificacion = numeroCertificacion

    def __eq__(self, other):
        if not isinstance(other, EstacionSismologica):
            return False
        return (
            self.codigo == other.codigo
        )

    def getNombre(self):
        return self.nombre
    