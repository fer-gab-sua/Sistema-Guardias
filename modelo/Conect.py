import pyodbc

class ConexionConBase:
    def __init__(self):
        self.server = 'DESKTOP-PP1EQCP\SQLEXPRESS'
        self.database = 'GuardiasMedicas'
        self.username = 'sa'
        self.password = 'j12p60ma'
        self.conn = None

    def conectar(self):
        try:
            conn_str = (
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={self.server};'
                f'DATABASE={self.database};'
                f'UID={self.username};'
                f'PWD={self.password}'
            )
            self.conn = pyodbc.connect(conn_str)
            print("Conexión exitosa.")
        except pyodbc.Error as ex:
            print("Error en la conexión:", ex)

    def cerrar_conexion(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")
            
    def ejecutar_consulta(self, consulta, *params):
        try:
            self.conectar()
            cursor = self.conn.cursor()
            cursor.execute(consulta, params)

            # Verificar si la consulta es de tipo SELECT
            if "SELECT" in consulta.upper():
                resultado = cursor.fetchall()
                return resultado
            else:
                self.conn.commit()
                return None

        except pyodbc.Error as ex:
            print("Error al ejecutar la consulta:", ex)
            return None
        finally:
            self.cerrar_conexion()

class ConsultasSql(ConexionConBase):
    def validar_usuarios(self, usuario, contraseña):
        consulta = "SELECT Usuario, Pass FROM Usuarios WHERE Usuario = ?"
        resultado = self.ejecutar_consulta(consulta, usuario)
        if resultado and usuario == resultado[0][0] and contraseña == resultado[0][1]:
            return True
        return False

    def trae_permisos(self, usuario):
        consulta = """
            SELECT Usuarios.Usuario, Permisos.VentanaHabilitada
            FROM Permisos
            JOIN Usuarios ON Usuarios.Id = Permisos.idUsuario
            WHERE Usuarios.Usuario = ?;
        """
        return self.ejecutar_consulta(consulta, usuario)






class ConsultasCabina(ConexionConBase):
    def fill_table_guard_cab(self,ini="2000-12-26 23:59:59.000",fin="2223-12-26 23:59:59.000"):
        consulta = """SELECT grd_int_id ,
                            mov_txt_movil ,
                            CONCAT(par_txt_apellido , ' ',par_txt_nombre) ,
                            CONCAT(enf_txt_nombre, ' ', enf_txt_apellido) ,   
                            CONCAT(med_txt_nombre, ' ', med_txt_apellido) , 
                            grd_fyh_inicio , 
                            grd_fyh_fin , 
                            grd_txt_observaciones, 
                            grd_txt_estado
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                LEFT JOIN Medicos on grd_int_idmedico = med_int_id
                LEFT JOIN Enfermeros on grd_int_idenfermero = enf_int_id
                WHERE grd_fyh_inicio >= ? AND grd_fyh_fin <= ?"""
        
        return self.ejecutar_consulta(consulta,ini,fin)

