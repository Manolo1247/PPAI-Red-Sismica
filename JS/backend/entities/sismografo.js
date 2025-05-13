class Sismografo {
    // no se contempló la clase Modelo
    constructor (nroSerie, identificadorSismografo, fechaAdquisicion, cambiosEstado=[], estacion) {
        this.nroSerie = nroSerie; 
        this.identificadorSismografo = identificadorSismografo; 
        this.fechaAdquisicion = fechaAdquisicion; 
        this.cambiosEstado = cambiosEstado; 
        this.estacion = estacion; 
    }
}