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

class AltaGuardia(ConexionConBase):
    def fill_Bases_sql(self):
        consulta = "SELECT mov_txt_movil, mov_txt_patente FROM Moviles"
        return self.ejecutar_consulta(consulta)

    def patente(self, base):
        consulta = "SELECT mov_txt_patente FROM Moviles WHERE mov_txt_movil = ?"
        return self.ejecutar_consulta(consulta, base)

    def alta_movil(self, movil, patente):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Moviles] ([mov_txt_movil], [mov_txt_patente]) VALUES (?, ?)"
        self.ejecutar_consulta(consulta, movil, patente)

    def borrar_movil(self,movil):
        consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Moviles] WHERE mov_txt_movil = (?)"
        self.ejecutar_consulta(consulta, movil)

    def fill_paramedicos_sql(self):
        consulta = "SELECT par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos"
        return self.ejecutar_consulta(consulta)

    def paramedicos_datos(self, legajo):
        consulta = "SELECT par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos WHERE par_int_legajo = (?)"
        return self.ejecutar_consulta(consulta, legajo)

