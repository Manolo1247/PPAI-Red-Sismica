import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import EmpleadoModel from "./empleadoModel.js";

class RolModel extends Model {}

RolModel.init({
    id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    nombre: { type: DataTypes.STRING, allowNull: false },
    descripcion: { type: DataTypes.STRING, allowNull: false }
} ,{
    sequelize,
    modelName: "Rol",
    tableName: "Roles",
    timestamps: false,
    underscored: true,
})

RolModel.hasMany(EmpleadoModel, {
    foreignKey: "idRol", // Foreign key in EmpleadoModel
    as: "empleados", // Alias for the association
})

export default RolModel;