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

class AltaGuardiaMovilParamedico(ConexionConBase):
    def fill_Bases_sql(self):
        consulta = "SELECT mov_int_id , mov_txt_movil, mov_txt_patente FROM Moviles"
        return self.ejecutar_consulta(consulta)

    def movil_datos(self, base):
        consulta = "SELECT mov_int_id ,mov_txt_movil , mov_txt_patente FROM Moviles WHERE mov_int_id = ?"
        return self.ejecutar_consulta(consulta, base)

    def alta_movil(self, movil, patente):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Moviles] ([mov_txt_movil], [mov_txt_patente]) VALUES (?, ?)"
        self.ejecutar_consulta(consulta, movil, patente)

    def borrar_movil(self,movil):
        consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Moviles] WHERE mov_txt_movil = (?)"
        self.ejecutar_consulta(consulta, movil)

    def fill_paramedicos_sql(self):
        consulta = "SELECT par_int_id , par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos"
        return self.ejecutar_consulta(consulta)

    def paramedicos_datos(self, legajo):
        consulta = "SELECT par_int_id , par_int_legajo, par_txt_nombre, par_txt_apellido, par_fch_vencimientolicencia FROM Paramedicos WHERE par_int_id = (?)"
        return self.ejecutar_consulta(consulta, legajo)

    def alta_paramedico(self, legajo,nombre,apellido,fechavencimiento):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Paramedicos] ([par_int_legajo],[par_txt_nombre],[par_txt_apellido],[par_fch_vencimientolicencia]) VALUES (?, ?, ?, ?)"
        self.ejecutar_consulta(consulta, legajo,nombre,apellido,fechavencimiento)

    def borrar_paramedico(self,movil):
        consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Paramedicos] WHERE par_int_legajo = (?)"
        self.ejecutar_consulta(consulta, movil)

    def fill_table_guard_adg(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , par_txt_apellido , par_txt_nombre , grd_fyh_inicio , grd_fyh_fin
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)

    def alta_guardia_movil(self,idmovil,idparamedico,fyh_inicio,fyh_fin):
        consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Guardias] ([grd_int_idmovil],[grd_int_idparamedico],[grd_fyh_inicio],[grd_fyh_fin],[grd_txt_estado]) VALUES (?, ?, ?, ? , ?)"
        self.ejecutar_consulta(consulta, idmovil,idparamedico,fyh_inicio,fyh_fin,"incompleta")

class AltaGuardiasMedicos(ConexionConBase):

    def fill_table_guard_idm(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , CONCAT(par_txt_apellido , ' ',par_txt_nombre) , grd_fyh_inicio , grd_fyh_fin , CONCAT(med_txt_nombre, ' ', med_txt_apellido)
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                LEFT JOIN Medicos on grd_int_idmedico = med_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)
    
    def fill_table_enfermero_idm(self):
        consulta = """SELECT med_int_id , med_txt_nombre , med_txt_apellido , med_int_matricula
                FROM Medicos
                """
        return self.ejecutar_consulta(consulta)
    
    def fill_table_medicos_idm_search(self,valor):
        consulta = """SELECT med_int_id , med_txt_nombre , med_txt_apellido , med_int_matricula
                FROM Medicos
                WHERE med_txt_apellido LIKE ?
                """
        valor = ('%'+valor+'%')
        return self.ejecutar_consulta(consulta,valor)
        
    def to_assign_medico(self,id_medico , id_guardia):
        consulta = "UPDATE Guardias SET grd_int_idmedico = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_medico,id_guardia)

    def alta_medico(self, nombre,apellido,matricula):
            consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Medicos] ([med_txt_nombre],[med_txt_apellido],[med_int_matricula]) VALUES (?, ?, ?)"
            self.ejecutar_consulta(consulta, nombre,apellido,matricula)

    def borrar_medico(self,id_medico):
            consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Medicos] WHERE med_int_id = (?)"
            self.ejecutar_consulta(consulta, id_medico)

class AltaGuardiasEnfermero(ConexionConBase):

    def fill_table_guard_ide(self):
        consulta = """SELECT grd_int_id , mov_txt_movil , CONCAT(par_txt_apellido , ' ',par_txt_nombre) , grd_fyh_inicio , grd_fyh_fin , CONCAT(med_txt_nombre, ' ', med_txt_apellido) , CONCAT(enf_txt_nombre, ' ', enf_txt_apellido)
                FROM Guardias 
                JOIN Paramedicos on grd_int_idparamedico = par_int_id
                JOIN Moviles on grd_int_idmovil = mov_int_id
                LEFT JOIN Medicos on grd_int_idmedico = med_int_id
                LEFT JOIN Enfermeros on grd_int_idenfermero = enf_int_id
                WHERE grd_txt_estado = 'incompleta' OR grd_txt_estado = 'completa'"""
        return self.ejecutar_consulta(consulta)
    
    def fill_table_enfermero_ide(self):
        consulta = """SELECT enf_int_id , enf_txt_nombre , enf_txt_apellido , enf_int_matricula
                FROM Enfermeros
                """
        return self.ejecutar_consulta(consulta)
    
    def fill_table_enfermero_idm_search(self,valor):
        consulta = """SELECT enf_int_id , enf_txt_nombre , enf_txt_apellido , enf_int_matricula
                FROM Enfermeros
                WHERE enf_txt_apellido LIKE ?
                """
        valor = ('%'+valor+'%')
        return self.ejecutar_consulta(consulta,valor)
        
    def to_assign_enfermero(self,id_medico , id_guardia):
        consulta = "UPDATE Guardias SET grd_int_idmedico = ? WHERE grd_int_id = ?"
        self.ejecutar_consulta(consulta,id_medico,id_guardia)

    def alta_enfermero(self, nombre,apellido,matricula):
            consulta = "INSERT INTO [GuardiasMedicas].[dbo].[Medicos] ([med_txt_nombre],[med_txt_apellido],[med_int_matricula]) VALUES (?, ?, ?)"
            self.ejecutar_consulta(consulta, nombre,apellido,matricula)

    def borrar_enfermero(self,id_medico):
            consulta = "DELETE FROM [GuardiasMedicas].[dbo].[Medicos] WHERE med_int_id = (?)"
            self.ejecutar_consulta(consulta, id_medico)