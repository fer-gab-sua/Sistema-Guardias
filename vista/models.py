import sqlite3

class MiBaseDeDatos:
    def __init__(self, nombre_base_de_datos = "guardias.db"):
        self.nombre_base_de_datos = nombre_base_de_datos
        self.conexion = sqlite3.connect(self.nombre_base_de_datos)
        self.cursor = None
        self.conectar()
        self.crear_tablas()
        self.desconectar()

    def conectar(self):
        try:
            self.conexion.isolation_level = None  # Desactiva el autocommit
            self.cursor = self.conexion.cursor()
            print("---> Conexión abierta")
        except sqlite3.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def crear_tablas(self):
        if self.cursor:
            try:
                #CREO TABLA - GUARDIAS
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS guardias (
                                    gua_int_guardia INTEGER PRIMARY KEY AUTOINCREMENT,
                                    gua_int_idmovil INTEGER,
                                    movil_guardia TEXT,
                                    medico_guardia TEXT,
                                    paramedico_guardia TEXT,
                                    enfermero_guardia TEXT,
                                    fecha_ini_guardia DATE,
                                    fecha_fin_guardia DATE,
                                    observaciones_guardia TEXT,
                                    estado_guardia TEXT
                                    )
                                    """)
                #CREO TABLA  -  MOVILES
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS moviles (
                                    mov_int_idmovil INTEGER PRIMARY KEY AUTOINCREMENT,
                                    mov_des_descripcion TEXT,
                                    mov_des_patente TEXT,
                                    mov_fch_vencimiento DATE,
                                    mov_txt_observaciones TEXT,
                                    instante DATE,
                                    usuario TEXT
                                    )
                                    """)
                #CREO TABLA  -  PARAMEDICOS
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS paramedicos(
                                    par_int_idparamedico INTEGER PRIMARY KEY AUTOINCREMENT,
                                    par_int_legajo INTEGER,
                                    par_des_nombre TEXT,
                                    par_des_apellido TEXT,
                                    par_des_matricula TEXT,
                                    instante DATE,
                                    usuario TEXT
                                    )
                                    """)
                #CREO TABLA  -  ENFERMERO
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS enfermero(
                                    enf_int_idenfermero INTEGER PRIMARY KEY AUTOINCREMENT,
                                    enf_int_legajo INTEGER,
                                    enf_des_nombre TEXT,
                                    enf_des_apellido TEXT,
                                    enf_des_matricula TEXT,
                                    instante DATE,
                                    usuario TEXT
                                    )
                                    """)
                #CREO TABLA  -  MEDICOS
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS medicos(
                                    med_int_idmedico INTEGER PRIMARY KEY AUTOINCREMENT,
                                    med_int_legajo INTEGER,
                                    med_des_nombre TEXT,
                                    med_des_apellido TEXT,
                                    med_des_matricula TEXT,
                                    instante DATE,
                                    usuario TEXT
                                    )
                                    """)
                self.conexion.commit()
                print("---> Bases validadas/creadas")
            except sqlite3.Error as error:
                print(f"Error en la actualización de datos: {error}")
                self.conexion.rollback()

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            print("---> Conexión cerrada")


class Guardia():
    def __init__(self,gua_int_idmovil, gua_fyh_inicial,gua_fyh_final) -> None:
        self.gua_int_guardia = None
        self.gua_int_idmovil = gua_int_idmovil
        self.gua_int_idparamedico = None
        self.gua_int_idenfermero = None
        self.gua_int_idmedico = None
        self.gua_fyh_inicial = gua_fyh_inicial
        self.gua_fyh_final = gua_fyh_final
        self.gua_txt_observaciones = None
    
    def cargo_dotacion_paramedico(self,id_paramedico):
        self.gua_int_idparamedico = id_paramedico

    def cargo_dotacion_enfermero(self,id_enfermero):
        self.gua_int_idenfermero = id_enfermero

    def cargo_dotacion_medico(self,id_medico):
        self.gua_int_idmedico = id_medico

    def cargo_observacaciones(self,observacion):
        self.gua_txt_observaciones = observacion

    def cambio_estado(self,estado):
        pass






