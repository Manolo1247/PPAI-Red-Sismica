import EmpleadoModel from "../models/empleadoModel.js";

async function seedEmpleados() {
    const empleados = [
        { nombre: "Juan", apellido: "Pérez", email: "juan.perez@example.com", telefono: "123456789", idRol: 1 },
        { nombre: "Ana", apellido: "García", email: "ana.garcia@example.com", telefono: "987654321", idRol: 2 },
        { nombre: "Carlos", apellido: "López", email: "carlos.lopez@example.com", telefono: "555555555", idRol: 3 },
        { nombre: "María", apellido: "Fernández", email: "maria.fernandez@example.com", telefono: "444444444", idRol: 4 }
    ];
    for (const empleado of empleados) {
        await EmpleadoModel.findOrCreate({ where: { email: empleado.email }, defaults: empleado });
    }
    console.log("Empleados iniciales insertados correctamente.");
}

seedEmpleados().then(() => process.exit()).catch(e => { console.error(e); process.exit(1); });
