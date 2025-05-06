import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import EstacionSismologicaModel from "./estacionSismologicaModel.js";

class SismografoModel extends Model {}

SismografoModel.init({
    nroSerie: { type: DataTypes.STRING, primaryKey: true },
    identificadorSismografo: { type: DataTypes.STRING, allowNull: false },
    fechaAdquisicion: { type: DataTypes.DATE, allowNull: false },
    // cambiosEstado: { type: DataTypes.JSON, allowNull: true },
    codigoEstacion: { type: DataTypes.INTEGER }
}, {
    sequelize,
    modelName: "Sismografo",
    tableName: "Sismografos",
    timestamps: false,
    underscored: true
})

SismografoModel.belongsTo(EstacionSismologicaModel, {
    foreignKey: "codigoEstacion",   // Foreign key in SismografoModel
    as: "estacion"  // Alias for the association
})



export default SismografoModel;