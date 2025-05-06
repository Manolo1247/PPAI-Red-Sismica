import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import RolModel from "./rolModel.js";
import UsuarioModel from "./usuarioModel.js";

class EmpleadoModel extends Model {}

EmpleadoModel.init({
    id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    nombre: { type: DataTypes.STRING, allowNull: false },
    apellido: { type: DataTypes.STRING, allowNull: false },
    email: { type: DataTypes.STRING, allowNull: false, unique: true },
    telefono: { type: DataTypes.STRING, allowNull: false },
    idRol: { type: DataTypes.INTEGER, allowNull: false }
},{
    sequelize,
    modelName: "Empleado",
    tableName: "Empleados",
    timestamps: false,
    underscored: true
})

EmpleadoModel.belongsTo(RolModel, {
    foreignKey: "idRol", // Foreign key in EmpleadoModel
    as: "rol", // Alias for the association
});

EmpleadoModel.hasOne(UsuarioModel, {
    foreignKey: "empleadoId", // Foreign key in UsuarioModel 
    as: "usuario" // Alias for the association
  });

export default EmpleadoModel;