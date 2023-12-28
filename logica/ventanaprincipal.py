from PyQt5 import QtWidgets, uic 
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit,QPushButton ,QMessageBox , QDateEdit 
from PyQt5.QtCore import QDate , QDateTime

from modelo.Conect import ConsultasSql , AltaGuardiaMovilParamedico, AltaGuardiasMedicos , AltaGuardiasEnfermero


class Ui_VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_VentanaPrincipal, self).__init__()
        self.consultasql = ConsultasSql()
        self.sqlaltaguardia_paramedico = AltaGuardiaMovilParamedico()
        self.sqlaltaguardia_medicos = AltaGuardiasMedicos()
        self.sqlaltaguardia_enfermero = AltaGuardiasEnfermero()
        uic.loadUi('vista/pantalla.ui', self)
        self.setWindowTitle("Pantalla de guadias")
        #logica de usuarios:
        self.permisos(self.user_init.text())
        # Conecta eventos y métodos aquí
        self.actionAlta_de_Guardias.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(1))
        self.actionMedicos.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(2))
        self.actionCabina.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(3))
        self.actionEnfermeros.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(4))
        self.actionHistorial.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(5))
        #primera pantalla 1 - ALTA DE GUARDIA - BASES

        # Crear el modelo de ítems para la base
        self.model_moviles = QStandardItemModel()
        self.fill_adg_tblv_1()
        # Asignar el modelo a la QTableView
        self.adg_tblv_1.setModel(self.model_moviles)
        self.adg_tblv_1.resizeColumnsToContents()
        #conecto el dobleclick de moviles a la funcion
        self.adg_tblv_1.doubleClicked.connect(self.select_movil)
        #conecto el add y del de la base de moviles
        self.adg_btn_addbase.clicked.connect(lambda:self.addbase())
        self.adg_btn_delbase.clicked.connect(lambda:self.delbase())

        #conecto todo lo referido a la primera pantalla 1 - ALTA DE GUARDIA - PARAMEDICOS
        self.model_paramedicos = QStandardItemModel()
        self.fill_adg_tblv_2()
        self.adg_tblv_2.setModel(self.model_paramedicos)
        self.adg_tblv_2.doubleClicked.connect(self.select_paramedico)
        self.adg_tblv_2.resizeColumnsToContents()
        #conecto el add y del de la base de paramedicos
        self.adg_btn_addparamedico.clicked.connect(lambda:self.addparamedico())
        self.adg_btn_delparamedico.clicked.connect(lambda:self.delparamedico())

        #conecto todo lo referido a la primera pantalla 1 - ALTA DE GUARDIA - FECHAS
        self.adg_cal_1.selectionChanged.connect(self.select_fecha)
        self.adg_btn_addguardia.clicked.connect(lambda:self.alta_guardia_movil())

        #llenado de guardias en ALTA DE GUARDIAS - Grilla general
        self.model_guardias_moviles = QStandardItemModel()
        self.fill_adg_tblv_3()
        self.adg_tblv_3.setModel(self.model_guardias_moviles)
        self.adg_tblv_3.resizeColumnsToContents()

        #Segunda pantalla 2 - INGRSO MEDICO - 
        self.model_medicos_guardias = QStandardItemModel()
        self.fill_idm_tlbv_1()
        self.idm_tblv_1.setModel(self.model_medicos_guardias)
        self.idm_tblv_1.resizeColumnsToContents()
        self.idm_tblv_1.doubleClicked.connect(self.select_idm_tblv_1)
        
        #Segunda pantalla 2 - BASE DE MEDICOS - 
        self.model_medicos_base = QStandardItemModel()
        self.fill_idm_tlbv_2()
        self.idm_tblv_2.setModel(self.model_medicos_base)
        self.idm_tblv_2.resizeColumnsToContents()
        self.idm_tblv_2.doubleClicked.connect(self.select_idm_tblv_2)
        self.idm_txt_apellidomed.textChanged.connect(self.search_medico)

        #Segunda pantalla 2 - asignarmedico
        self.idm_btn_add_medico.clicked.connect(self.asignar_medico)
        self.idm_btn_addaltamedico.clicked.connect(lambda:self.alta_medicos())
        self.idm_btn_delaltamedico.clicked.connect(self.delmedico)

        #Segunda pantalla 3 - INGRSO Enfermero - 
        self.model_enfermero_guardias = QStandardItemModel()
        self.fill_ide_tlbv_1()
        self.ide_tlbv_1.setModel(self.model_enfermero_guardias)
        self.ide_tlbv_1.resizeColumnsToContents()
        self.ide_tlbv_1.doubleClicked.connect(self.select_ide_tblv_1)
        
        #Segunda pantalla 2 - BASE DE MEDICOS - 
        self.model_enfermero_base = QStandardItemModel()
        self.fill_ide_tlbv_2()
        self.ide_tlbv_2.setModel(self.model_enfermero_base)
        self.ide_tlbv_2.resizeColumnsToContents()
        self.ide_tlbv_2.doubleClicked.connect(self.select_ide_tblv_2)
        self.ide_txt_apellidosearch.textChanged.connect(self.search_enfermero)

        #Segunda pantalla 2 - asignarmedico
        #self.ide_btn_add_medico.clicked.connect(self.asignar_enfermero)
        #self.ide_btn_addaltamedico.clicked.connect(lambda:self.alta_enfermero())
        #self.ide_btn_delaltamedico.clicked.connect(self.delenfermero)
    """######### FUNCIONES GENERALES#####################"""
    def permisos(self,usuario):
        if usuario == "Admin":
            self.actionAlta_de_Guardias.setEnabled(True)
            self.actionMedicos.setEnabled(True)
            self.actionCabina.setEnabled(True)
            self.actionEnfermeros.setEnabled(True)
            self.actionHistorial.setEnabled(True)
        else:
            datos = self.consultasql.trae_permisos(usuario)
            print(datos)
            for permiso in datos:
                print(permiso[1])
                if int(permiso[1]) == 1:
                    print("permiso 1")
                    self.actionAlta_de_Guardias.setEnabled(True)
                elif int(permiso[1]) == 2:
                    print("permiso 2")
                    self.actionMedicos.setEnabled(True)
                elif int(permiso[1]) == 3:
                    print("permiso 3")
                    self.actionCabina.setEnabled(True)
                elif int(permiso[1]) == 4:
                    print("permiso 4")
                    self.actionEnfermeros.setEnabled(True)
                elif int(permiso[1]) == 5:
                    print("permiso 5")
                    self.actionHistorial.setEnabled(True)

    def fill_table(self,base_datos,modelo,header_labels):
        if base_datos:
            modelo.clear()

            for tupla in base_datos:
                fila = tupla
                row_items = [QStandardItem(str(dato)) for dato in fila]
                modelo.appendRow(row_items)
                modelo.setHorizontalHeaderLabels(header_labels)
        else:
            print("base d datos vacia")


    """########## ALTA DE GUARDIAS ####################### BASE"""
    def fill_adg_tblv_1(self,):
        bases_datos = self.sqlaltaguardia_paramedico.fill_Bases_sql()
        # Configuración del QTableView
        header_labels_base = ['Id' , 'Base', 'Patente']
        self.fill_table(bases_datos,self.model_moviles,header_labels_base)
        self.adg_tblv_1.resizeColumnsToContents()

    def select_movil(self):
        indice_seleccionado = self.adg_tblv_1.currentIndex()
        base = self.model_moviles.item(indice_seleccionado.row(), 0).text()
        print(base)

        movil_datos = self.sqlaltaguardia_paramedico.movil_datos(base)
        print(movil_datos)
        if movil_datos:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.adg_let_patente.setText(str(movil_datos[0][2]))
            titulo_base = (f"Movil: {movil_datos[0][1]}")
            self.adg_tlbox_1.setItemText(0,titulo_base)
            self.adg_let_base.setText(str(movil_datos[0][1]))
            self.adg_txt_movil.setText(str(movil_datos[0][1]))
            self.adg_int_idmovil.setText(str(movil_datos[0][0]))
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.adg_let_patente.setText("")
            self.adg_tlbox_1.setItemText(0,"")

    def addbase(self,):
        subventanamov = SubVentanaAddMovil()
        subventanamov.exec_()
        # Después de que se cierra la subventana, actualiza la tabla
        self.fill_adg_tblv_1()

    def delbase(self):
        # Obtener el índice de la fila seleccionada
        indice_seleccionado = self.adg_tblv_1.currentIndex()
        # Verificar si hay una selección válida
        if indice_seleccionado.isValid():
            # Obtener el valor de la primera columna (patente) en la fila seleccionada
            base = self.model_moviles.item(indice_seleccionado.row(), 1).text()
            print(base)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"¿Estás seguro de eliminar el registro con movil {base}?")
            msg.setWindowTitle("Confirmación de eliminación")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
            respuesta = msg.exec_()
            # Procesar la respuesta
            if respuesta == QMessageBox.Yes:
                # Si el usuario hizo clic en "Sí", eliminar el registro
                self.sqlaltaguardia_paramedico.borrar_movil(base)
            else:
                # Si el usuario hizo clic en "No" o cerró la ventana, no hacer nada
                print("Eliminación cancelada.")
            self.fill_adg_tblv_1()
        else:
            print("No hay una fila seleccionada")
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una fila antes de intentar borrar.',
                                QMessageBox.Ok)

    """########## ALTA DE GUARDIAS ####################### PARAMEDICO"""

    def fill_adg_tblv_2(self,):
        bases_datos = self.sqlaltaguardia_paramedico.fill_paramedicos_sql()
        # Configuración del QTableView
        header_labels_paramedico = ['Id','Legajo', 'Nombre' , 'Apellido' , 'Licencia Venc.']  
        self.fill_table(bases_datos,self.model_paramedicos,header_labels_paramedico)
        self.adg_tblv_2.resizeColumnsToContents()

    def select_paramedico(self):
        indice_seleccionado = self.adg_tblv_2.currentIndex()
        id_paramedico = self.model_paramedicos.item(indice_seleccionado.row(), 0).text()
        paramedico = self.sqlaltaguardia_paramedico.paramedicos_datos(id_paramedico)
        id_paramedico = int(paramedico[0][0])
        print(id_paramedico, "ESTE ES EL DATO")
        legajo = paramedico[0][1]
        nombre_apellido = paramedico[0][2] + " " + paramedico[0][3]
        fecha = paramedico[0][4]
        
        if paramedico:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.adg_let_legajoparamedico.setText(str(legajo))
            titulo_paramedico = (f"Paramedico: {nombre_apellido}")
            self.adg_let_nombreyapellido.setText(nombre_apellido)
            self.adg_date_licenciaparamedico.setDate(fecha)
            self.adg_tlbox_1.setItemText(1,titulo_paramedico)
            self.adg_txt_paramedico.setText(nombre_apellido)
            self.adg_int_idparamedico.setText(str(id_paramedico))
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.adg_let_legajoparamedico.setText("")
            self.adg_let_nombreyapellido.setText("")
            self.adg_date_licenciaparamedico.setDate("")
            self.adg_tlbox_1.setItemText(1,"Paramedico")

    def addparamedico(self):
        subventanapara = SubVentanaAddParamedico()
        subventanapara.exec_()
        # Después de que se cierra la subventana, actualiza la tabla
        self.fill_adg_tblv_2()

    def delparamedico(self):
        # Obtener el índice de la fila seleccionada
        indice_seleccionado = self.adg_tblv_2.currentIndex()
        # Verificar si hay una selección válida
        if indice_seleccionado.isValid():
            # Obtener el valor de la primera columna (patente) en la fila seleccionada
            paramedico = self.model_paramedicos.item(indice_seleccionado.row(), 1).text()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"¿Estás seguro de eliminar el registro con el legajo {paramedico}?")
            msg.setWindowTitle("Confirmación de eliminación")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
            respuesta = msg.exec_()
            # Procesar la respuesta
            if respuesta == QMessageBox.Yes:
                # Si el usuario hizo clic en "Sí", eliminar el registro
                print(paramedico)
                self.sqlaltaguardia_paramedico.borrar_paramedico(int(paramedico))
            else:
                # Si el usuario hizo clic en "No" o cerró la ventana, no hacer nada
                print("Eliminación cancelada.")
            self.fill_adg_tblv_2()
        else:
            print("No hay una fila seleccionada")
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una fila antes de intentar borrar.',
                                QMessageBox.Ok)

    """########## ALTA DE GUARDIAS ####################### FECHAS """

    def select_fecha(self):
        fecha_seleccionada = self.adg_cal_1.selectedDate()
        # Establecer el valor del QDate
        self.adg_fech_inicio.setDate(fecha_seleccionada)
        self.adg_fech_fin.setDate(fecha_seleccionada)
    
    def alta_guardia_movil(self):
        idmovil = self.adg_int_idmovil.text()
        idparamedico = self.adg_int_idparamedico.text()
        fecha_inicio = self.adg_fech_inicio.date()
        hora_inicio = self.adg_hor_inicio.time()
        fecha_fin = self.adg_fech_fin.date()
        hora_fin = self.adg_hor_fin.time()

        fyh_inicio = QDateTime(fecha_inicio,hora_inicio).toString("yyyy-MM-dd hh:mm:ss")
        fyh_fin = QDateTime(fecha_fin,hora_fin).toString("yyyy-MM-dd hh:mm:ss")
        
        self.sqlaltaguardia_paramedico.alta_guardia_movil(idmovil,idparamedico,fyh_inicio,fyh_fin)
        self.fill_adg_tblv_3()
        
    def fill_adg_tblv_3(self):
        bases_datos = self.sqlaltaguardia_paramedico.fill_table_guard_adg()
        # Configuración del QTableView
        header_labels_alta_guardia = ['Id','Base', 'Apellido P.' , 'Nombre P.', 'Fecha Inicio' , 'Fecha Fin']  
        self.fill_table(bases_datos,self.model_guardias_moviles,header_labels_alta_guardia)
        self.adg_tblv_3.resizeColumnsToContents()

    """########## ALTA DE GUARDIAS ####################### MEDICOS """
    def fill_idm_tlbv_2(self):
        bases_datos = self.sqlaltaguardia_medicos.fill_table_guard_idm()
        # Configuración del QTableView
        header_labels_alta_medicos = ['Id','Nombre', 'Apellido' , 'Matricula']  
        self.fill_table(bases_datos,self.model_medicos_base,header_labels_alta_medicos)
        self.idm_tblv_2.resizeColumnsToContents()

    def search_medico(self):
        if self.idm_txt_apellidomed:
            valor = self.idm_txt_apellidomed.text()
            bases_datos = self.sqlaltaguardia_medicos.fill_table_medicos_idm_search(valor)
            # Configuración del QTableView
            header_labels_alta_medicos = ['Id','Nombre', 'Apellido' , 'Matricula']  
            self.fill_table(bases_datos,self.model_medicos_base,header_labels_alta_medicos)
            self.idm_tblv_2.resizeColumnsToContents()
        else: 
            self.fill_idm_tlbv_2()

    def select_idm_tblv_2(self):
        indice_seleccionado = self.idm_tblv_2.currentIndex()
        id_medico = self.model_medicos_base.item(indice_seleccionado.row(), 0).text()
        medico_nombre = self.model_medicos_base.item(indice_seleccionado.row(), 1).text()
        medico_apellido = self.model_medicos_base.item(indice_seleccionado.row(), 2).text()
        
        if id_medico:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.idm_int_idmedico_ingreso.setText(str(id_medico))
            medico = (medico_nombre + " " + medico_apellido)
            self.idm_txt_medico_ingreso.setText(str(medico))
            self.idm_tlbox_1.setItemText(0,str("Medico: "+medico))

        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.idm_tlbox_1.setItemText(0,str("Medico: "))

    def fill_idm_tlbv_1(self):
        bases_datos = self.sqlaltaguardia_medicos.fill_table_guard_idm()
        # Configuración del QTableView
        header_labels_alta_guardia = ['Id','Base', 'Paramedico', 'Fecha Inicio' , 'Fecha Fin', 'Medico']  
        self.fill_table(bases_datos,self.model_medicos_guardias,header_labels_alta_guardia)
        self.idm_tblv_1.resizeColumnsToContents()

    def select_idm_tblv_1(self):
        indice_seleccionado = self.idm_tblv_1.currentIndex()
        id_guardia = self.model_medicos_guardias.item(indice_seleccionado.row(), 0).text()
        base = self.model_medicos_guardias.item(indice_seleccionado.row(), 1).text()
        paramedico = self.model_medicos_guardias.item(indice_seleccionado.row(), 2).text()
        fecha_ini = self.model_medicos_guardias.item(indice_seleccionado.row(), 3).text()
        fecha_fin = self.model_medicos_guardias.item(indice_seleccionado.row(), 4).text()
                
        if id_guardia:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.idm_int_idguardia.setText(str(id_guardia))
            self.idm_txt_base.setText(str(base))
            self.idm_txt_paramedico.setText(str(paramedico))
            self.idm_txt_enfermero.setText(str(""))
            fecha_hora_ini = QDateTime.fromString(fecha_ini, "yyyy-MM-dd hh:mm:ss")
            self.idm_fyh_inicio.setDateTime(fecha_hora_ini)
            fecha_hora_fin = QDateTime.fromString(fecha_fin, "yyyy-MM-dd hh:mm:ss")
            self.idm_fyh_fin.setDateTime(fecha_hora_fin)
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            pass

    def asignar_medico(self):
        id_medico = self.idm_int_idmedico_ingreso.text()
        id_guardia = self.idm_int_idguardia.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(f"¿Estás seguro de asignar el medico{id_medico}, con el id_guardia {id_guardia}?")
        msg.setWindowTitle("Confirmación de eliminación")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
        respuesta = msg.exec_()
        # Procesar la respuesta
        if respuesta == QMessageBox.Yes:
            if self.idm_int_idmedico_ingreso.text():
                self.sqlaltaguardia_medicos.to_assign_medico(id_medico,id_guardia)
                self.fill_idm_tlbv_1()

    def alta_medicos(self):
        subventanapara = SubVentanaAddMedico()
        subventanapara.exec_()
        # Después de que se cierra la subventana, actualiza la tabla
        self.fill_idm_tlbv_2()

    def delmedico(self):
        # Obtener el índice de la fila seleccionada
        indice_seleccionado = self.idm_tblv_2.currentIndex()
        # Verificar si hay una selección válida
        if indice_seleccionado.isValid():
            # Obtener el valor de la primera columna (patente) en la fila seleccionada
            medico = self.model_medicos_base.item(indice_seleccionado.row(), 0).text()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"¿Estás seguro de eliminar el registro con el id {medico}?")
            msg.setWindowTitle("Confirmación de eliminación")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
            respuesta = msg.exec_()
            # Procesar la respuesta
            if respuesta == QMessageBox.Yes:
                # Si el usuario hizo clic en "Sí", eliminar el registro
                print(medico)
                self.sqlaltaguardia_medico.borrar_paramedico(int(medico))
            else:
                # Si el usuario hizo clic en "No" o cerró la ventana, no hacer nada
                print("Eliminación cancelada.")
            self.fill_adg_tblv_2()
        else:
            print("No hay una fila seleccionada")
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una fila antes de intentar borrar.',
                                QMessageBox.Ok)

    """########## ALTA DE GUARDIAS ####################### ENFERMERO """

    def fill_ide_tlbv_1(self):
        bases_datos = self.sqlaltaguardia_enfermero.fill_table_guard_ide()
        # Configuración del QTableView
        header_labels_alta_guardiaenfermero = ['Id','Base', 'Paramedico', 'Fecha Inicio' , 'Fecha Fin', 'Medico','Enfermero']  
        self.fill_table(bases_datos,self.model_enfermero_guardias,header_labels_alta_guardiaenfermero)
        self.ide_tlbv_1.resizeColumnsToContents()

    def fill_ide_tlbv_2(self):
        bases_datos = self.sqlaltaguardia_enfermero.fill_table_enfermero_ide()
        print(bases_datos)
        # Configuración del QTableView
        header_labels_alta_enfermero = ['Id','Nombre', 'Apellido' , 'Matricula']  
        self.fill_table(bases_datos,self.model_enfermero_base,header_labels_alta_enfermero)
        self.idm_tblv_2.resizeColumnsToContents()
    
    def search_enfermero(self):
        if self.ide_txt_apellidosearch:
            valor = self.ide_txt_apellidosearch.text()
            bases_datos = self.sqlaltaguardia_enfermero.fill_table_enfermero_idm_search(valor)
            # Configuración del QTableView
            header_labels_alta_enfermero = ['Id','Nombre', 'Apellido' , 'Matricula']  
            self.fill_table(bases_datos,self.model_enfermero_base,header_labels_alta_enfermero)
            self.idm_tblv_2.resizeColumnsToContents()
        else: 
            self.fill_ide_tlbv_2()

    def select_ide_tblv_2(self):
        indice_seleccionado = self.ide_tlbv_2.currentIndex()
        id_enfermero = self.model_enfermero_base.item(indice_seleccionado.row(), 0).text()
        enfermero_nombre = self.model_enfermero_base.item(indice_seleccionado.row(), 1).text()
        enfermero_apellido = self.model_enfermero_base.item(indice_seleccionado.row(), 2).text()
  
        if id_enfermero:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.ide_int_idenfermero_ingreso.setText(str(id_enfermero))
            enfermero = (enfermero_nombre + " " + enfermero_apellido)
            self.ide_txt_enfermero_ingreso.setText(str(enfermero))
            self.ide_tlbox_1.setItemText(0,str("Enfermero "+enfermero))

        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.ide_tlbox_1.setItemText(0,str("Enfermero: "))



    def select_ide_tblv_1(self):
        indice_seleccionado = self.ide_tlbv_1.currentIndex()
        id_guardia = self.model_enfermero_guardias.item(indice_seleccionado.row(), 0).text()
        base = self.model_enfermero_guardias.item(indice_seleccionado.row(), 1).text()
        paramedico = self.model_enfermero_guardias.item(indice_seleccionado.row(), 2).text()
        fecha_ini = self.model_enfermero_guardias.item(indice_seleccionado.row(), 3).text()
        fecha_fin = self.model_enfermero_guardias.item(indice_seleccionado.row(), 4).text()
                
        if id_guardia:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.ide_int_idguardia.setText(str(id_guardia))
            self.ide_txt_base.setText(str(base))
            self.ide_txt_paramedico.setText(str(paramedico))
            self.ide_txt_enfermero.setText(str(""))
            fecha_hora_ini = QDateTime.fromString(fecha_ini, "yyyy-MM-dd hh:mm:ss")
            self.ide_fyh_inicio.setDateTime(fecha_hora_ini)
            fecha_hora_fin = QDateTime.fromString(fecha_fin, "yyyy-MM-dd hh:mm:ss")
            self.ide_fyh_fin.setDateTime(fecha_hora_fin)
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            pass
    """      
    def asignar_medico(self):
        id_medico = self.idm_int_idmedico_ingreso.text()
        id_guardia = self.idm_int_idguardia.text()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText(f"¿Estás seguro de asignar el medico{id_medico}, con el id_guardia {id_guardia}?")
        msg.setWindowTitle("Confirmación de eliminación")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
        respuesta = msg.exec_()
        # Procesar la respuesta
        if respuesta == QMessageBox.Yes:
            if self.idm_int_idmedico_ingreso.text():
                self.sqlaltaguardia_medicos.to_assign_medico(id_medico,id_guardia)
                self.fill_idm_tlbv_1()

    def alta_medicos(self):
        subventanapara = SubVentanaAddMedico()
        subventanapara.exec_()
        # Después de que se cierra la subventana, actualiza la tabla
        self.fill_idm_tlbv_2()

    def delmedico(self):
        # Obtener el índice de la fila seleccionada
        indice_seleccionado = self.idm_tblv_2.currentIndex()
        # Verificar si hay una selección válida
        if indice_seleccionado.isValid():
            # Obtener el valor de la primera columna (patente) en la fila seleccionada
            medico = self.model_medicos_base.item(indice_seleccionado.row(), 0).text()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText(f"¿Estás seguro de eliminar el registro con el id {medico}?")
            msg.setWindowTitle("Confirmación de eliminación")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            # Mostrar el cuadro de mensaje y obtener la respuesta del usuario
            respuesta = msg.exec_()
            # Procesar la respuesta
            if respuesta == QMessageBox.Yes:
                # Si el usuario hizo clic en "Sí", eliminar el registro
                print(medico)
                self.sqlaltaguardia_medico.borrar_paramedico(int(medico))
            else:
                # Si el usuario hizo clic en "No" o cerró la ventana, no hacer nada
                print("Eliminación cancelada.")
            self.fill_adg_tblv_2()
        else:
            print("No hay una fila seleccionada")
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una fila antes de intentar borrar.',
                                QMessageBox.Ok)


    """
#asd
    """########## GUARDIAS CABINA ####################### """
    """########## GUARDIAS HISTORIAL ####################### """

class SubVentanaAddMovil(QDialog):
    def __init__(self):
        super(SubVentanaAddMovil, self).__init__()

        # Crear widgets para la subventana
        self.label_movil = QLabel("Movil:")
        self.lineEdit_movil = QLineEdit(self)
        self.label_patente = QLabel("Patente:")
        self.lineEdit_patente = QLineEdit(self)
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.clicked.connect(self.guardar_movil)

        # Crear el diseño de la subventana
        layout = QVBoxLayout()
        layout.addWidget(self.label_movil)
        layout.addWidget(self.lineEdit_movil)
        layout.addWidget(self.label_patente)
        layout.addWidget(self.lineEdit_patente)
        layout.addWidget(self.btnAceptar)

        # Configurar el diseño en la subventana
        self.setLayout(layout)

    def guardar_movil(self):
        movil = self.lineEdit_movil.text()
        patente = self.lineEdit_patente.text()
        print(movil,patente)
        sql = AltaGuardiaMovilParamedico()
        sql.alta_movil(movil, patente)
        self.accept()

class SubVentanaAddParamedico(QDialog):
    def __init__(self):
        super(SubVentanaAddParamedico, self).__init__()

        # Crear widgets para la subventana
        self.label_legajo = QLabel("Legajo:")
        self.lineEdit_legajo = QLineEdit(self)

        self.label_nombre = QLabel("Nombre:")
        self.lineEdit_nombre = QLineEdit(self)

        self.label_apellido = QLabel("Apellido:")
        self.lineEdit_apellido = QLineEdit(self)

        self.label_fechavencimiento = QLabel("Fecha de Vencimiento:")
        self.dateEdit_fechavencimiento = QDateEdit(self)
        self.dateEdit_fechavencimiento.setDate(QDate.currentDate())  # Establecer la fecha actual como valor predeterminado
        self.dateEdit_fechavencimiento.setDisplayFormat("yyyy-MM-dd")  # Formato de visualización de la fecha

        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.clicked.connect(self.guardar_paramedico)

        # Crear el diseño de la subventana
        layout = QVBoxLayout()
        layout.addWidget(self.label_legajo)
        layout.addWidget(self.lineEdit_legajo)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.lineEdit_nombre)
        layout.addWidget(self.label_apellido)
        layout.addWidget(self.lineEdit_apellido)
        layout.addWidget(self.label_fechavencimiento)
        layout.addWidget(self.dateEdit_fechavencimiento)
        layout.addWidget(self.btnAceptar)

        # Configurar el diseño en la subventana
        self.setLayout(layout)

    def guardar_paramedico(self):
        legajo = self.lineEdit_legajo.text()
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        fechavencimiento = self.dateEdit_fechavencimiento.date().toString("yyyy-MM-dd")

        sql = AltaGuardiaMovilParamedico()
        sql.alta_paramedico(legajo, nombre, apellido, fechavencimiento)
        self.accept()

class SubVentanaAddMedico(QDialog):
    def __init__(self):
        super(SubVentanaAddMedico, self).__init__()

        # Crear widgets para la subventana
        self.label_nombre = QLabel("Nombre:")
        self.lineEdit_nombre = QLineEdit(self)

        self.label_apellido = QLabel("Apellido:")
        self.lineEdit_apellido = QLineEdit(self)

        self.label_matricula= QLabel("Matricula:")
        self.lineEdit_matricula = QLineEdit(self)

        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.clicked.connect(self.guardar_medico)

        # Crear el diseño de la subventana
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.lineEdit_nombre)
        layout.addWidget(self.label_apellido)
        layout.addWidget(self.lineEdit_apellido)
        layout.addWidget(self.label_matricula)
        layout.addWidget(self.lineEdit_matricula)
        layout.addWidget(self.btnAceptar)

        # Configurar el diseño en la subventana
        self.setLayout(layout)

    def guardar_medico(self):
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        matricula = self.lineEdit_matricula.text()

        sql = AltaGuardiasMedicos()
        sql.alta_medico(nombre, apellido, matricula)
        self.accept()