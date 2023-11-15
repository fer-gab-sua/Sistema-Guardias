from tkinter import StringVar,BooleanVar,ttk,Button,W
from tkcalendar import Calendar

class Ventana():  #inicia en nuevo_reg
    def __init__(self, pantalla,controlador) -> None:
        self.controlador = controlador
        self.pantalla = pantalla
        global estado_programa
        pantalla.title("Ingreso de guardias")
        self.var_id_guardia = StringVar()
        self.var_movil_guardia = StringVar()
        self.var_fecha_inicio = StringVar()
        self.var_hora_inicio =StringVar()
        self.var_fecha_fin = StringVar()
        self.var_hora_fin =StringVar()
        self.var_medico = StringVar()
        self.var_paramedico= StringVar()
        self.var_enfermero= StringVar()
        self.var_observaciones= StringVar()
        checkbox_value= BooleanVar()
        self.var_fecha_ini_filtro = StringVar()
        self.var_fecha_fin_filtro = StringVar()
        dark_mode_var = BooleanVar()
        dark_mode_var.set(False)
        self.estado_programa = "a_espera"  #estados posibles: inicio , modifica , alta
        #inicio marco de pantalla
        estado_select = "sin_filtro"
        marco = ttk.Frame(self.pantalla)
        marco.grid()
        #validador = Validador()


        # titulo del form
        label_titulo = ttk.Label(marco, text="Sistema de alta de guardias", font=("Helvetica", 14))
        label_titulo.grid(row=0, column=2)

        # Creo un contenedor para el ingreso de datos
        ingreso_datos = ttk.Frame(marco)
        ingreso_datos.grid(row=1,column=0)

        #lleno el contenedor de ingreso de datos
        label_id_guardia = ttk.Label(ingreso_datos, text="Numero de guardia")
        label_id_guardia.grid(row=0,column=1)
        self.entry_id_guardia = ttk.Entry(ingreso_datos, textvariable=self.var_id_guardia, width=30, state="disabled")
        self.entry_id_guardia.grid(row=0,column=2)

        label_movil_guardia = ttk.Label(ingreso_datos, text="Movil")
        label_movil_guardia.grid(row=1,column=1)
        self.entry_movil_guardia = ttk.Entry(ingreso_datos, textvariable=self.var_movil_guardia, width=30,state="disabled")
        self.entry_movil_guardia.grid(row=1,column=2, padx=10, pady=10)

        label_paramedico = ttk.Label(ingreso_datos, text="Paramedico")
        label_paramedico.grid(row=2,column=1)
        self.entry_paramedico = ttk.Entry(ingreso_datos, textvariable=self.var_paramedico, width=30,state="disabled")
        self.entry_paramedico.grid(row=2,column=2, padx=10, pady=10)

        label_medico = ttk.Label(ingreso_datos, text="Medico")
        label_medico.grid(row=3,column=1)
        self.entry_medico = ttk.Entry(ingreso_datos, textvariable=self.var_medico, width=30,state="disabled")
        self.entry_medico.grid(row=3,column=2, padx=10, pady=10)

        label_enfermero = ttk.Label(ingreso_datos, text="Enfermero")
        label_enfermero.grid(row=4,column=1)
        self.entry_enfermero = ttk.Entry(ingreso_datos, textvariable=self.var_enfermero, width=30,state="disabled")
        self.entry_enfermero.grid(row=4,column=2, padx=10, pady=10)

        label_observaciones = ttk.Label(ingreso_datos, text="Observaciones")
        label_observaciones.grid(row=5,column=1)
        self.entry_observaciones = ttk.Entry(ingreso_datos, textvariable=self.var_observaciones, width=30,state="disabled")
        self.entry_observaciones.grid(row=5,column=2, padx=10, pady=10)

        # marco para el ingreso de la fecha y hora
        marco_ingreso_fyh_ini = ttk.Frame(marco, borderwidth=2, relief="ridge")
        marco_ingreso_fyh_ini.grid(row=1, column=1)

        label_titulo_ini = ttk.Label(marco_ingreso_fyh_ini, text="Inicio de Guardia:")
        label_titulo_ini.grid(row=0, column=1)
        label_fecha_ini = ttk.Label(marco_ingreso_fyh_ini, text="Fecha inicio:")
        label_fecha_ini.grid(row=2, column=1)
        self.entry_fecha_ini = ttk.Entry(marco_ingreso_fyh_ini, textvariable=self.var_fecha_inicio, width=30,state="disabled")
        self.entry_fecha_ini.grid(row=3, column=1)

        self.cal_fecha_ini = Calendar(marco_ingreso_fyh_ini, selectmode="day", date_pattern="dd-mm-yyyy",state="disabled")
        self.cal_fecha_ini.grid(row=1, column=1, padx=20, pady=20)
        self.cal_fecha_ini.bind("<<CalendarSelected>>", lambda event, entry=self.entry_fecha_ini: (entry.delete(0, 'end'), entry.insert(0, self.cal_fecha_ini.get_date()), self.cal_fecha_fin.selection_set(self.cal_fecha_ini.get_date())))



        label_hora_ini = ttk.Label(marco_ingreso_fyh_ini, text="Hora inicio:")
        label_hora_ini.grid(row=4, column=1)
        self.entry_hora_ini = ttk.Entry(marco_ingreso_fyh_ini, textvariable=self.var_hora_inicio, width=30,state="disabled")
        self.entry_hora_ini.grid(row=5, column=1, padx=10, pady=10)

        #marco para el ingreso de la fecha y hora de fin de guardia
        marco_ingreso_fyh_fin = ttk.Frame(marco, borderwidth=2, relief="ridge")
        marco_ingreso_fyh_fin.grid(row=1, column=2)

        label_titulo_fin = ttk.Label(marco_ingreso_fyh_fin, text="Fin de Guardia:")
        label_titulo_fin.grid(row=0, column=1)

        label_fecha_fin = ttk.Label(marco_ingreso_fyh_fin, text="Fecha Fin:")
        label_fecha_fin.grid(row=2, column=1)
        self.entry_fecha_fin = ttk.Entry(marco_ingreso_fyh_fin, textvariable=self.var_fecha_fin, width=30,state="disabled")
        self.entry_fecha_fin.grid(row=3, column=1)

        self.cal_fecha_fin = Calendar(marco_ingreso_fyh_fin, selectmode="day", date_pattern="dd-mm-yyyy",state="disabled")
        self.cal_fecha_fin.grid(row=1, column=1, padx=20, pady=20)
        self.cal_fecha_fin.bind("<<CalendarSelected>>", lambda event, entry=self.entry_fecha_fin: (entry.delete(0, 'end'), entry.insert(0, self.cal_fecha_fin.get_date())))



        label_hora_fin = ttk.Label(marco_ingreso_fyh_fin, text="Hora fin:")
        label_hora_fin.grid(row=4, column=1)
        self.entry_hora_fin = ttk.Entry(marco_ingreso_fyh_fin, textvariable=self.var_hora_fin, width=30,state="disabled")
        self.entry_hora_fin.grid(row=5, column=1, padx=10, pady=10)

        #inicio el marco para los botones

        marco_botones = ttk.Frame(marco, borderwidth=2, relief="ridge")
        marco_botones.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
        self.boton_nuevo = Button(marco_botones, text="Nuevo", command=lambda:controlador.nuevo(self))
        self.boton_nuevo.grid(row=0, column=0, padx=20, pady=20)
        self.boton_guardar = Button(marco_botones, text="Guardar", command=lambda:controlador.guardar(self))
        self.boton_guardar.grid(row=0, column=1, padx=20, pady=20)
        self.boton_modificar = Button(marco_botones, text="Modificar",command=lambda:controlador.modificar(self))
        self.boton_modificar.grid(row=0, column=2, padx=20, pady=20)
        self.boton_borrar = Button(marco_botones, text="Borrar",command=lambda:controlador.borrar(self))
        self.boton_borrar.grid(row=0, column=3, padx=20, pady=20)
        self.boton_cancelar = Button(marco_botones, text="Cancelar", command=lambda:controlador.cancelar(self))
        self.boton_cancelar.grid(row=0, column=4, padx=20, pady=20)

        #inicio el marco para la visualizacion de datos
        marco_datos = ttk.Frame(marco, borderwidth=2, relief="ridge")
        marco_datos.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

        self.tree = ttk.Treeview(marco_datos)
        self.tree["columns"] = ("col1", "col2", "col3","col4","col5","col6","col7")
        self.tree.column("#0", width=50, minwidth=50, anchor=W)
        self.tree.column("col1", width=150, minwidth=150, anchor=W)
        self.tree.column("col2", width=180, minwidth=180, anchor=W)
        self.tree.column("col3", width=110, minwidth=110, anchor=W)
        self.tree.column("col4", width=110, minwidth=110, anchor=W)
        self.tree.column("col5", width=110, minwidth=110, anchor=W)
        self.tree.column("col6", width=110, minwidth=110, anchor=W)
        self.tree.column("col7", width=110, minwidth=110, anchor=W)
        self.tree.grid(row=1,columnspan=6)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Movil")
        self.tree.heading("col2", text="Medico") 
        self.tree.heading("col3", text="Paramedico")   
        self.tree.heading("col4", text="Enfermero")   
        self.tree.heading("col5", text="Fecha de inicio")   
        self.tree.heading("col6", text="Fecha de fin")   
        self.tree.heading("col7", text="Observaciones")   
        self.tree.bind("<ButtonRelease-1>", self.cargar_datos_seleccionados)
        label_filtro = ttk.Label(marco_datos, text="Filtro fecha desde")
        label_filtro.grid(row=2,column=0)
        self.entry_fecha_ini_filtro = ttk.Entry(marco_datos, textvariable=self.var_fecha_ini_filtro, width=30)
        self.entry_fecha_ini_filtro.grid(row=2, column=1)

        label_filtro = ttk.Label(marco_datos, text="Filtro fecha hasta")
        label_filtro.grid(row=2,column=2)
        self.entry_fecha_fin_filtro = ttk.Entry(marco_datos, textvariable=self.var_fecha_fin_filtro, width=30)
        self.entry_fecha_fin_filtro.grid(row=2, column=3)

        boton_actualizar = Button(marco_datos, text="Actualizar grilla")#, command=lambda:actualizar_grilla())
        boton_actualizar.grid(row=2,column=4)    
        self.controlador.actualizar_grilla(self)
        #actualizar_grilla()
        self.modo_pantalla("mod_ini")

    def modo_pantalla(self,modo):
        """Se encarga de habilitar y deshabilitar botones, entry de la ventana, dependiendo el estado

        Args:
            modo (str): "mod_ini" / "mod_ingreso" / "mod_seleccionado"

        Returns:
            _str_: informa estado de vista aplicada
        """        
        print(modo)
        if modo == "mod_ini":
            #configuro los estados de botones
            self.boton_nuevo.config(state="normal")
            self.boton_guardar.config(state="disabled")
            self.boton_modificar.config(state="disabled")
            self.boton_borrar.config(state="disable")
            self.boton_cancelar.config(state="disabled")
            #configuro estados de los calendarios
            self.cal_fecha_ini.config(state="disabled")
            self.cal_fecha_fin.config(state="disabled")
            #configuro los estados de las entry
            self.entry_id_guardia.config(state="disabled")
            self.entry_movil_guardia.config(state="disabled")
            self.entry_paramedico.config(state="disabled")
            self.entry_medico.config(state="disabled")
            self.entry_enfermero.config(state="disabled")
            self.entry_fecha_ini.config(state="disabled")
            self.entry_hora_ini.config(state="disabled")
            self.entry_fecha_fin.config(state="disabled")
            self.entry_hora_fin.config(state="disabled")
            self.entry_observaciones.config(state="disabled")
            estado_programa = "inicio"
            print(self.var_fecha_fin.get())
            #actualizar_grilla()
            return "-->modo_ini iniciado<--"
        elif modo =="mod_ingreso":
            """Formatea el formulario preparandolo para el ingreso de una nueva entrada
            """
            #estado_programa = "inicio"
            # Limpiar las variables de los entry
            self.var_id_guardia.set("")
            self.var_movil_guardia.set("")
            self.var_medico.set("")
            self.var_paramedico.set("")
            self.var_enfermero.set("")
            self.var_fecha_inicio.set("")
            self.var_hora_inicio.set("")
            self.var_hora_fin.set("")
            self.var_fecha_fin.set("")
            self.var_observaciones.set("")
            # Habilitar los botones para el ingreso de datos  boton_nuevo.config(state="disabled")
            self.boton_nuevo.config(state="disabled")
            self.boton_guardar.config(state="normal")
            self.boton_modificar.config(state="disabled")
            self.boton_borrar.config(state="disable")
            self.boton_cancelar.config(state="normal")
            # Habilitar los entry para el ingreso de datos  boton_nuevo.config(state="disabled")
            self.entry_id_guardia.config(state="disabled")
            self.entry_movil_guardia.config(state="normal")
            self.entry_paramedico.config(state="normal")
            self.entry_medico.config(state="normal")
            self.entry_enfermero.config(state="normal")
            self.entry_fecha_ini.config(state="normal")
            self.entry_hora_ini.config(state="normal")
            self.entry_fecha_fin.config(state="normal")
            self.entry_hora_fin.config(state="normal")
            self.entry_observaciones.config(state="normal")
            #Habilito los dos calendarios para que puedan elegir fecha
            self.cal_fecha_ini.config(state="normal")
            self.cal_fecha_fin.config(state="normal")
            return "-->modo_ingreso iniciado<--"
        elif modo =="mod_modificacion":
            self.boton_nuevo.config(state="disabled")
            self.boton_guardar.config(state="normal")
            self.boton_modificar.config(state="disabled")
            self.boton_borrar.config(state="disable")
            self.boton_cancelar.config(state="normal")
            # Habilitar los entry para el ingreso de datos  boton_nuevo.config(state="disabled")
            self.entry_id_guardia.config(state="disabled")
            self.entry_movil_guardia.config(state="normal")
            self.entry_paramedico.config(state="normal")
            self.entry_medico.config(state="normal")
            self.entry_enfermero.config(state="normal")
            self.entry_fecha_ini.config(state="normal")
            self.entry_hora_ini.config(state="normal")
            self.entry_fecha_fin.config(state="normal")
            self.entry_hora_fin.config(state="normal")
            self.entry_observaciones.config(state="normal")
            #Habilito los dos calendarios para que puedan elegir fecha
            self.cal_fecha_ini.config(state="normal")
            self.cal_fecha_fin.config(state="normal")
            return "-->modo_modificacion iniciado<--"
        elif modo =="mod_seleccionado":
            #configuro los estados de botones
            self.boton_nuevo.config(state="normal")
            self.boton_guardar.config(state="disabled")
            self.boton_modificar.config(state="normal")
            self.boton_borrar.config(state="normal")
            self.boton_cancelar.config(state="disabled")
            #configuro estados de los calendarios
            self.cal_fecha_ini.config(state="disabled")
            self.cal_fecha_fin.config(state="disabled")
            #configuro los estados de las entry
            self.entry_id_guardia.config(state="disabled")
            self.entry_movil_guardia.config(state="disabled")
            self.entry_paramedico.config(state="disabled")
            self.entry_medico.config(state="disabled")
            self.entry_enfermero.config(state="disabled")
            self.entry_fecha_ini.config(state="disabled")
            self.entry_hora_ini.config(state="disabled")
            self.entry_fecha_fin.config(state="disabled")
            self.entry_hora_fin.config(state="disabled")
            self.entry_observaciones.config(state="disabled")
            self.estado_programa = "a_espera"
            print(self.var_fecha_fin.get())
            #actualizar_grilla()
            return "-->mod_ingreso iniciado<--"
        
        else:
            return "-->mod incorrecto<--"

    def cargar_datos_seleccionados(self,event):
        #voy cargando los todos del tree en los entry
        """CARGO TODOS LOS ENTRY CUANDO EL TREE (EVENT) ES SELECCIONADO
        """        
        if self.estado_programa == "a_espera": #como inicia ok
            self.modo_pantalla("mod_seleccionado")
        elif self.estado_programa == "nuevo_reg": #cuando vengo de Nuevo
            self.modo_pantalla("mod_ingreso")
        else:
            print("return")
            return
        item = self.tree.focus()
        if item:
            datos_registro = self.tree.item(item, "values")  # Obtener los valores del registro seleccionado
            if datos_registro:
                self.var_movil_guardia.set(datos_registro[0])
                self.var_medico.set(datos_registro[1])
                self.var_paramedico.set(datos_registro[2])
                self.var_enfermero.set(datos_registro[3])
                #divido la fecha y hora en dos registros
                divfyh = datos_registro[4]
                datos_fyh = divfyh.split(" ")
                self.var_fecha_inicio.set(datos_fyh[0])
                self.var_hora_inicio.set(datos_fyh[1])
                divfyh = datos_registro[5]
                datos_fyh = divfyh.split(" ")
                self.var_fecha_fin.set(datos_fyh[0])
                self.var_hora_fin.set(datos_fyh[1])
                #sigo con las observaciones
                self.var_observaciones.set(datos_registro[6])
                datos_registro = self.tree.item(item, "text")
                self.var_id_guardia.set(datos_registro)