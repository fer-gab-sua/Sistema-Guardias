from modelo import Guardia
from tkinter import messagebox
import re
from datetime import datetime

class Validador():
    @staticmethod
    def validar_fecha(fecha_str):
        """VALIDADOR DE FORMATO DE FECHA dd-mm-aaaa

        Args:
            fecha_str (str): fecha a validar por formato

        Returns:
            str: True / False
        """        
        try:
            # Intenta parsear la fecha utilizando el formato especificado
            datetime.strptime(fecha_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False
        
    @staticmethod
    def validar_hora(hora):
        """VALIDADOR DE FORMATO DE HORA 00:00

        Args:
            hora (str): Hora a validad

        Returns:
            str: True / False
        """        
        patron_hora = r'^[0-2][0-9]:[0-5][0-9]$'
        return re.match(patron_hora, hora) is not None
    
    def validacion(self,ventana):
        """VALIDADOR DEL FORMULARIO COMPLETO, CON TODOS SUS CAMPOS

        Args:
            ventana (obj): objeto ventana donde obtiene todas las variables

        Returns:
            str: True / False
        """            
        val_movil_guardia = r'^[a-zA-Z0-9]+$'
        #valido el campo movil
        if re.match(val_movil_guardia, ventana.var_movil_guardia.get()) is None:
            mensaje = "El campo Movil no puede conterner caracteres especiales o estar vacio"
            messagebox.showerror("Error de formato", mensaje)
        #valido las fechas
        # Valida las fechas
        fecha = ventana.var_hora_inicio.get()
        self.validar_fecha(fecha)
        if not self.validar_fecha(ventana.var_fecha_inicio.get()) or not self.validar_fecha(ventana.var_fecha_fin.get()):
            mensaje = "La fecha no es válida. El formato debe ser dd-mm-aaaa"
            messagebox.showerror("Error de formato", mensaje)
            return False

        #Valida las horas
        if not self.validar_hora(ventana.var_hora_inicio.get()) or not self.validar_hora(ventana.var_hora_fin.get()):
            mensaje = "La hora no es válida. El formato debe ser hh:mm"
            messagebox.showerror("Error de formato", mensaje)

            return False
        print("---> Validacion de campos pasada con exito <---")
        return True


class Controlador():
    def __init__(self,base_sql) -> None:
        """CONTROLADOR, ENCARGADO EN INTERACTUAR ENTRE LA VISTA Y EL MODELO

        Args:
            base_sql (obj): Objeto de Base de datos
        """        
        self.base_sql = base_sql
        
    def actualizar_grilla(self,ventana):
        """Busca en el modelo y actualiza la grilla

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """            

        datos = self.base_sql.mod_actualizar_grilla(ventana.var_fecha_ini_filtro,ventana.var_fecha_fin_filtro)

        for item in ventana.tree.get_children():
            ventana.tree.delete(item)
        for row in datos:
            ventana.tree.insert("", "end", text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        print("---> Tree actualizado correctamente <---")
        
    def nuevo(self,ventana):
        """METODO PARA PREPARAR LA VENTANA PARA EL INGRESO DE DATOS

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """        
        #elijo la vista que deseo mostrar:
        ventana.modo_pantalla("mod_ingreso")
        #aplico logica para enviar los datos al modelo
        ventana.estado_programa = "nuevo_reg"

    def guardar(self,ventana):
        """FUNCION QUE LLAMA A VALIDAR Y SI ESTA CORRECTO GUARDA EN LA BASE DE DATOS DEPENDIENDO DE LA VARIABLE ESTADO_PROGRAMA = "nuevo_reg" / "modifica_reg"

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """        
        validador = Validador()
        resultado = validador.validacion(ventana)
        if resultado == False:
            return
        if ventana.estado_programa == "nuevo_reg":
            fyh_inicio_guardia = ventana.var_fecha_inicio.get() + " " + ventana.var_hora_inicio.get()
            fyh_fin_guardia = ventana.var_fecha_fin.get() + " " + ventana.var_hora_fin.get()
            movil_guardia = ventana.var_movil_guardia.get()
            medico_guardia = ventana.var_medico.get()
            paramedico_guardia = ventana.var_paramedico.get()
            enfermero_guardia = ventana.var_enfermero.get()
            observaciones_guardia = ventana.var_observaciones.get()
            estado_guardia = "pendiente"
            guardia = Guardia(movil_guardia,medico_guardia,paramedico_guardia,
                enfermero_guardia,fyh_inicio_guardia,fyh_fin_guardia,observaciones_guardia,
                estado_guardia)
            print(self.base_sql.mod_nuevo_ingreso(guardia))
        elif ventana.estado_programa == "modifica_reg":
            fyh_inicio_guardia = ventana.var_fecha_inicio.get() + " " + ventana.var_hora_inicio.get()
            fyh_fin_guardia = ventana.var_fecha_fin.get() + " " + ventana.var_hora_fin.get()
            id_guardia = ventana.var_id_guardia.get()
            movil_guardia = ventana.var_movil_guardia.get()
            medico_guardia = ventana.var_medico.get()
            paramedico_guardia = ventana.var_paramedico.get()
            enfermero_guardia = ventana.var_enfermero.get()
            observaciones_guardia = ventana.var_observaciones.get()
            guardia = Guardia(movil_guardia,medico_guardia,paramedico_guardia,
                enfermero_guardia,fyh_inicio_guardia,fyh_fin_guardia,observaciones_guardia,
                estado_guardia = "")
            print(self.base_sql.mod_modifica_ingreso(id_guardia,guardia))
        ventana.modo_pantalla("mod_ini")#LLAMO AL ESTADO DE LA PANTALLA INICIAL
        ventana.estado_programa = "a_espera"#CAMBIO EL ESTADO DEL PROGRAMA
        self.actualizar_grilla(ventana)

    def modificar(self,ventana):
        """PREPARA LA PANTALLA  Y EL PROGRAMA PARA MODIFICAR UNA GUARDIA 

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """        
        #elijo la vista que deseo mostrar:
        ventana.estado_programa = "modifica_reg"
        ventana.modo_pantalla("mod_modificacion")

    def borrar(self, ventana):
        """OBTIENE EL NUMERO DE REGISTRO Y LO ENVIA AL MODELO PARA SER ELIMINADO

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """        
        #aplico logica para enviar los datos al modelo
        ventana.estado_programa
        item = ventana.tree.focus()
        iddb = int(ventana.tree.item(item, "text"))
        mensaje = f"Estas seguro de eliminar el registro {iddb}:"
        resultado = messagebox.askyesno("Confirmación", mensaje )
        if resultado == True:
            mensaje = self.base_sql.mod_borrar_registro(iddb)
            print(mensaje)
        #elijo la vista que deseo mostrar:
        ventana.modo_pantalla("mod_ini")
        self.actualizar_grilla(ventana)
        ventana.estado_programa="a_espera"

    def cancelar(self,ventana):
        """CANCELA LA OPERACION

        Args:
            ventana (obj): objeto ventana donde obtiene todos los objetos de la vista
        """        
        #elijo la vista que deseo mostrar:
        ventana.modo_pantalla("mod_ini")
        #aplico logica para enviar los datos al modelo
        ventana.estado_programa = "a_espera"