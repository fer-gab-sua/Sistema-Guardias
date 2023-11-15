import sqlite3


class Connect():
    def __init__(self,nombre_base_datos = "base.db") -> None:
        try:
                
            self.connection = sqlite3.connect(nombre_base_datos)
            self.cursor = self.connection.cursor()
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
                )""")
            
        except:sqlite3.Error as error:
    print(f"Error en la actualización de datos: {error}")
    # Regresar a un estado anterior (hacer rollback)
    con.rollback()



class BaseDeDatos():
    def __init__(self,nombre_base_datos = "guardias2023.db") -> None:
        self.conexion = sqlite3.connect(nombre_base_datos)
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS guardias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movil_guardia TEXT,
            medico_guardia TEXT,
            paramedico_guardia TEXT,
            enfermero_guardia TEXT,
            fecha_ini_guardia DATE,
            fecha_fin_guardia DATE,
            observaciones_guardia TEXT,
            estado_guardia TEXT
            )""")
        self.conexion.commit()