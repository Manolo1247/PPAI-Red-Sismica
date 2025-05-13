import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import UsuarioModel from "./usuarioModel.js";

class SesionModel extends Model {}

SesionModel.init({
    usuarioNombre: { type: DataTypes.STRING, primaryKey: true },
    fechaInicio: { type: DataTypes.DATE, primaryKey: true },
    fechaFin: { type: DataTypes.DATE, allowNull: true }
}, {
    sequelize,
    modelName: 'Sesion',
    tableName: 'sesiones',
    timestamps: false,
    underscored: true
});

SesionModel.belongsTo(UsuarioModel, {
    foreignKey: 'usuarioNombre', // Foreign key in SesionModel
    as: 'usuario' // Alias for the association
});

export default SesionModel;