CREATE TABLE retencion (
    ID_retencion SERIAL PRIMARY KEY,
    Ingresos_laborales DECIMAL(10,2) NOT NULL,
    Otros_ingresos DECIMAL(10,2) NOT NULL,
    Retenciones DECIMAL(10,2) NOT NULL,
    Seguridad_social DECIMAL(10,2) NOT NULL,
    Aportes_pension DECIMAL(10,2) NOT NULL,
    Gastos_creditos_hipotecarios DECIMAL(10,2) NOT NULL,
    Donaciones DECIMAL(10,2) NOT NULL,
    Gastos_educacion DECIMAL(10,2) NOT NULL,
    ID_Usuario INT NOT NULL,
    FOREIGN KEY (ID_Usuario) REFERENCES usuarios(ID_Usuario)
);
