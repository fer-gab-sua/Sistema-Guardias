-- Comprobar si la base de datos existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM sys.databases WHERE name = 'GuardiasMedicas')
BEGIN
    CREATE DATABASE GuardiasMedicas;
END;

-- Usar la base de datos
USE GuardiasMedicas;


-----------------------------------------------------------------------------------------------------------------------
-- Comprobar si la tabla existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Usuarios')
BEGIN
    -- Crear la tabla 
    CREATE TABLE Usuarios (
        ID INT IDENTITY(1,1) PRIMARY KEY,
        Usuario NVARCHAR(30),
		Pass NVARCHAR(20),
    );
END;

-----------------------------------------------------------------------------------------------------------------------
-- Comprobar si la tabla existe y, si no, crearla
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Permisos')
BEGIN
    -- Crear la tabla 
    CREATE TABLE Permisos (
        ID INT IDENTITY(1,1) PRIMARY KEY,
		IdUsuario INT,
        VentanaHabilitada NVARCHAR(30),
		
    );
END;
-----------------------------------------------------------------------------------------------------------------------

IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Guardias')
BEGIN
	--Creo la tabla principal
	CREATE TABLE Guardias (
	grd_int_id INT IDENTITY(1,1) PRIMARY KEY,
	grd_int_idmovil INT,
	grd_int_idparamedico INT,
	grd_int_idmedico INT,
	grd_int_idenfermero INT,
	grd_fyh_inicio DATETIME,
	grd_fyh_fin DATETIME,
	grd_int_duracionguardiahs INT,
	grd_txt_observaciones NVARCHAR(120),
	grd_txt_estado NVARCHAR(20)
	);
END;
-----------------------------------------------------------------------------------------------------------------------
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Moviles')
BEGIN
	--Creo la tabla principal
	CREATE TABLE Moviles(
	mov_int_id INT IDENTITY(1,1) PRIMARY KEY,
	mov_txt_movil NVARCHAR(10),
	mov_txt_patente NVARCHAR(10)
	);
END;

-----------------------------------------------------------------------------------------------------------------------

IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Paramedicos')
BEGIN
	--Creo la tabla principal
	CREATE TABLE Paramedicos (
	par_int_id INT IDENTITY(1,1) PRIMARY KEY,
	par_int_legajo INT,
	par_txt_nombre NVARCHAR(30),
	par_txt_apellido NVARCHAR(30),
	par_fch_vencimientolicencia DATE
	);
END;

-----------------------------------------------------------------------------------------------------------------------
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Medicos')
BEGIN
	--Creo la tabla principal
	CREATE TABLE Medicos (
	med_int_id INT IDENTITY(1,1) PRIMARY KEY,
	med_txt_nombre NVARCHAR(30),
	med_txt_apellido NVARCHAR(30),
	med_int_matricula INT,
	);
END;

-----------------------------------------------------------------------------------------------------------------------
IF NOT EXISTS (SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Enfermeros')
BEGIN
	--Creo la tabla principal
	CREATE TABLE Enfermeros(
	enf_int_id INT IDENTITY(1,1) PRIMARY KEY,
	enf_txt_nombre NVARCHAR(30),
	enf_txt_apellido NVARCHAR(30),
	enf_int_matricula INT,
	);
END;

