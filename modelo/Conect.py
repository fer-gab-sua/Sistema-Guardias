import pyodbc

class ConexionConBase:
    def __init__(self) -> None:
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



class ConsultasSql(ConexionConBase):
    def validar_usuarios(self,usuario,contraseña):
        try:
            self.conectar()
            cursor = self.conn.cursor()
            consulta = "Select Usuario,Pass from Usuarios"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            if usuario == resultado[0][0] and contraseña == resultado[0][1]:
                return True
            else:
                return False
            
        except pyodbc.Error as ex:
            print("Error al ejecutar la consulta:", ex)
            return None
        finally:
            self.cerrar_conexion()

# Ejemplo de uso de la clase
if __name__ == "__main__":
    consultasql = ConsultasSql()
    resultado = consultasql.validar_usuarios("Admin","Admin")
    print(resultado)
