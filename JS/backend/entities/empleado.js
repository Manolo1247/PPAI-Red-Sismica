class Empleado {
    constructor(nombre, apellido, telefono, mail, rol) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.telefono = telefono;
        this.mail = mail;
        this.rol = rol;
    }
    obtenerMail() {     // método de ejemplo
        return this.mail;
    }
}