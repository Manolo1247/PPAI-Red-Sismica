import RolModel from "../models/rolModel.js";

async function seedRoles() {
    const roles = [
        { nombre: "Administrador de Red", descripcion: "Administra la red sismológica" },
        { nombre: "Encargado de Instalaciones", descripcion: "Gestiona la instalación de equipos" },
        { nombre: "Analista en Sismos", descripcion: "Analiza eventos sísmicos" },
        { nombre: "Responsable de Inspecciones", descripcion: "Supervisa inspecciones de estaciones" }
    ];
    for (const rol of roles) {
        await RolModel.findOrCreate({ where: { nombre: rol.nombre }, defaults: rol });
    }
    console.log("Roles iniciales insertados correctamente.");
}

seedRoles().then(() => process.exit()).catch(e => { console.error(e); process.exit(1); });
