import UsuarioModel from "../models/usuarioModel.js";
import EmpleadoModel from "../models/empleadoModel.js";

async function seedUsuarios() {
    // Asegúrate de que existan empleados con estos IDs antes de correr este seeder
    const usuarios = [
        { nombre: "admin", contrasena: "admin123", empleadoId: 1 },
        { nombre: "instalador", contrasena: "instalador123", empleadoId: 2 },
        { nombre: "analista", contrasena: "analista123", empleadoId: 3 },
        { nombre: "inspector", contrasena: "inspector123", empleadoId: 4 }
    ];
    for (const usuario of usuarios) {
        await UsuarioModel.findOrCreate({ where: { nombre: usuario.nombre }, defaults: usuario });
    }
    console.log("Usuarios iniciales insertados correctamente.");
}

seedUsuarios().then(() => process.exit()).catch(e => { console.error(e); process.exit(1); });
