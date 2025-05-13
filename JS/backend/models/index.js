import UsuarioModel from "./usuarioModel.js";
import SesionModel from "./sesionModel.js";
import EmpleadoModel from "./empleadoModel.js";
import RolModel from "./rolModel.js";
import EstacionSismologicaModel from "./estacionSismologicaModel.js";
import SismografoModel from "./sismografoModel.js";

// Usuario tiene muchas sesiones
UsuarioModel.hasMany(SesionModel, {
    foreignKey: "usuarioNombre",
    as: "sesiones"
});
// Sesion pertenece a un usuario
SesionModel.belongsTo(UsuarioModel, {
    foreignKey: "usuarioNombre",
    as: "usuario"
});

// Usuario pertenece a un empleado
UsuarioModel.belongsTo(EmpleadoModel, {
    foreignKey: "empleadoId",
    as: "empleado"
});
// Empleado tiene un usuario
EmpleadoModel.hasOne(UsuarioModel, {
    foreignKey: "empleadoId",
    as: "usuario"
});

// Empleado tiene un rol
EmpleadoModel.belongsTo(RolModel, {
    foreignKey: "idRol",
    as: "rol"
});
// Rol tiene muchos empleados
RolModel.hasMany(EmpleadoModel, {
    foreignKey: "idRol",
    as: "empleados"
});

// EstacionSismologica tiene muchos sismografos
EstacionSismologicaModel.hasMany(SismografoModel, {
    foreignKey: "estacionId",
    as: "sismografos"
});
// Sismografo pertenece a una estacion
SismografoModel.belongsTo(EstacionSismologicaModel, {
    foreignKey: "estacionId",
    as: "estacion"
});

export {
    UsuarioModel,
    SesionModel,
    EmpleadoModel,
    RolModel,
    EstacionSismologicaModel,
    SismografoModel
};
