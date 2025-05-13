import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import SesionModel from "./sesionModel.js";
import EmpleadoModel from "./empleadoModel.js";

class UsuarioModel extends Model {}

UsuarioModel.init({
    nombre: { type: DataTypes.STRING, primaryKey: true },
    contrasena: { type: DataTypes.STRING, allowNull: false },
    empleadoId: { type: DataTypes.INTEGER, allowNull: false }
}, {
    sequelize,
    modelName: "Usuario",
    tableName: "Usuarios",
    timestamps: false,
    underscored: true
})

UsuarioModel.hasMany(SesionModel, {
    foreignKey: "usuarioNombre", // Foreign key in SesionModel
    as: "sesiones" // Alias for the association
})

UsuarioModel.belongsTo(EmpleadoModel, {
    foreignKey: "empleadoId", // Foreign key in UsuarioModel
    as: "empleado" // Alias for the association
})

export default UsuarioModel;