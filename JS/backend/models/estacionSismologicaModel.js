import { DataTypes, Model } from "sequelize";
import sequelize from "../data/db.js";
import SismografoModel from "./sismografoModel.js";

class EstacionSismologicaModel extends Model {}

EstacionSismologicaModel.init({
    codigo: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
    nombre: { type: DataTypes.STRING, allowNull: false },
    latitud: { type: DataTypes.FLOAT, allowNull: false },
    longitud: { type: DataTypes.FLOAT, allowNull: false },
    fechaSolicitudCertificacion: { type: DataTypes.DATE },
    docCertificacion: { type: DataTypes.STRING },
    nroCertificacionAdquisicion: { type: DataTypes.STRING },
}, {
    sequelize,
    modelName: "EstacionSismologica",
    tableName: "EstacionesSismologicas",
    timestamps: false,
    underscored: true
})

EstacionSismologicaModel.hasOne(SismografoModel, {
    foreignKey: "codigoEstacion",   // Foreign key in SismografoModel
    as: "sismografo"    // Alias for the association
})



export default EstacionSismologicaModel;