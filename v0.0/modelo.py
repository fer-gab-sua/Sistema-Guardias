import sqlite3
from classes.cls_guardia import Guardia


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

    def mod_actualizar_grilla(self,var_fecha_inicio,var_fecha_fin):
        """Consulta en la base de datos las guardias en un lapso de tiempo:
        si var_fecha_inicio es vacio, trae todo lo que esta en la base
        si var_fecha_fin es vacio, trae todo desde el var_fecha_inicio


        Args:
            var_fecha_inicio (str): Fecha en formato ##/##/#### de inicio del filtro
            var_fecha_fin (str): Fecha en formato ##/##/#### de din del filtro

        Returns:
            list: retorno de datos
        """    
        global estado_select
        fecha_desde  = var_fecha_inicio.get()
        fecha_hasta = var_fecha_fin.get()
        print(fecha_desde,fecha_hasta)
        if fecha_desde == '' and fecha_hasta == '':
            sql = """SELECT id, movil_guardia, medico_guardia, Paramedico_guardia, enfermero_guardia, fecha_ini_guardia, fecha_fin_guardia , observaciones_guardia FROM guardias"""
            self.cursor.execute(sql)
            estado_select = "con_filtro"
        elif fecha_desde != '' and fecha_hasta =='':
            data = (fecha_desde,)
            sql = """SELECT id, movil_guardia, medico_guardia, Paramedico_guardia, enfermero_guardia, fecha_ini_guardia, fecha_fin_guardia , observaciones_guardia FROM guardias WHERE fecha_ini_guardia >= ?
                """
            self.cursor.execute(sql,data)
        elif fecha_desde != '' and fecha_hasta != '' and fecha_desde != fecha_hasta:
            data = (fecha_desde, fecha_hasta)
            sql = """SELECT id, movil_guardia, medico_guardia, Paramedico_guardia, enfermero_guardia, fecha_ini_guardia, fecha_fin_guardia , observaciones_guardia FROM guardias WHERE fecha_ini_guardia >= ? and fecha_ini_guardia <= ?
                """
            self.cursor.execute(sql,data)
            estado_select = "con_filtro"
        elif fecha_desde == '' and fecha_hasta != '':
            data = (fecha_hasta,)
            sql = """SELECT id, movil_guardia, medico_guardia, Paramedico_guardia, enfermero_guardia, fecha_ini_guardia, fecha_fin_guardia , observaciones_guardia FROM guardias WHERE  fecha_ini_guardia =< ?
                """
            self.cursor.execute(sql,data)
            estado_select = "con_filtro"
        elif fecha_desde != '' and fecha_desde == fecha_hasta:
            data = (fecha_desde,)
            sql = """SELECT id, movil_guardia, medico_guardia, Paramedico_guardia, enfermero_guardia, fecha_ini_guardia, fecha_fin_guardia , observaciones_guardia FROM guardias WHERE fecha_ini_guardia = ?
                """
            self.cursor.execute(sql,data)
        datos = self.cursor.fetchall()
        #cursor.close()
        return datos

    def mod_nuevo_ingreso(self,guardia):
        sql = """INSERT INTO guardias(movil_guardia,
                medico_guardia,
                Paramedico_guardia,
                enfermero_guardia,
                fecha_ini_guardia,
                fecha_fin_guardia,
                observaciones_guardia) 
                VALUES (? ,? ,? ,? ,? ,? ,?)"""
        data = (guardia.movil_guardia,
                guardia.medico_guardia,
                guardia.paramedico_guardia,
                guardia.enfermero_guardia,
                guardia.fyh_inicio_guardia,
                guardia.fyh_fin_guardia,
                guardia.observaciones_guardia,)
        self.cursor.execute(sql,data)
        self.conexion.commit()
        mensaje = f'El ingreso de la guardia fue realizado con exito!'
        return mensaje

    def mod_modifica_ingreso(self,id_guardia,guardia):#id_guardia,movil_guardia,medico,paramedico,enfermero,fyh_inicio,fyh_fin,observaciones):
        """modifica una guardia en la base de datos

        Args:
            var_movil_guardia (obj): objeto de tkinter
            var_medico (obj): objeto de tkinter
            var_paramedico (obj): objeto de tkinter
            var_enfermero (obj): objeto de tkinter
            var_fyh_inicio (obj): objeto de tkinter
            var_fyh_fin (obj): objeto de tkinter
            var_observaciones (obj): objeto de tkinter

        Returns:
            str: retorna mensaje de confirmacion

        """
        id_guardia = int(id_guardia)
        data = (guardia.movil_guardia,
                guardia.medico_guardia,
                guardia.paramedico_guardia,
                guardia.enfermero_guardia,
                guardia.fyh_inicio_guardia,
                guardia.fyh_fin_guardia,
                guardia.observaciones_guardia,
                id_guardia,)
        sql = """UPDATE guardias SET 
                movil_guardia = ?,
                medico_guardia = ?,
                Paramedico_guardia = ?,
                enfermero_guardia = ?,
                fecha_ini_guardia = ?,
                fecha_fin_guardia = ?,
                observaciones_guardia = ? 
                WHERE id = ?"""
        mensaje = f'La modificacion de la guardia fue realizada con exito!{id_guardia}'
        self.cursor.execute(sql,data)
        self.conexion.commit()
        return mensaje

    def mod_borrar_registro(self,iddb):
        """Borra un registro en la base de datos

        Args:
            iddb (int): Id de la guardia a eliminar

        Returns:
            str: retorna mensaje de confirmacion
        """    
        data = (iddb,)
        sql = "DELETE FROM guardias WHERE id = ?"
        self.cursor.execute(sql,data)
        self.conexion.commit()
        return f"el id {iddb} fue eliminado exitosamente"