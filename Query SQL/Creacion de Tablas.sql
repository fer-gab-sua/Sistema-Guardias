-- Comprobar si la base de datos existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'GuardiasMedicas')
BEGIN
    CREATE DATABASE GuardiasMedicas;
END;

-- Usar la base de datos
USE GuardiasMedicas;

-- Comprobar si la tabla existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Usuarios')
BEGIN
    -- Crear la tabla 
    CREATE TABLE Usuarios (
        ID INT PRIMARY KEY,
        Usuario NVARCHAR(30),
		Pass NVARCHAR(20),
    );
END;

-- Comprobar si la tabla existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Permisos')
BEGIN
    -- Crear la tabla 
    CREATE TABLE Permisos (
        ID INT PRIMARY KEY,
		IdUsuario INT,
        VentanaHabilitada NVARCHAR(30),
		
    );
END;


