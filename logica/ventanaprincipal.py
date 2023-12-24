from PyQt5 import QtWidgets, uic 
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit,QPushButton ,QMessageBox

from modelo.Conect import ConsultasSql , AltaGuardia


class Ui_VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_VentanaPrincipal, self).__init__()
        self.consultasql = ConsultasSql()
        self.sqlaltaguardia = AltaGuardia()
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
        #conecto todo lo referido a la primera pantalla 1 - ALTA DE GUARDIA - BASES
        
        # Crear el modelo de ítems para la base
        self.model_moviles = QStandardItemModel()
        self.fill_adg_tblv_1()
        # Asignar el modelo a la QTableView
        self.adg_tblv_1.setModel(self.model_moviles)
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
        #conecto el add y del de la base de paramedicos
        self.adg_btn_addparamedico.clicked.connect(lambda:self.addparamedico())
        self.adg_btn_delparamedico.clicked.connect(lambda:self.delparamedico())


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

    """########## TODO ALTA DE GUARDIAS ####################### BASE"""
    def fill_adg_tblv_1(self,):
        bases_datos = self.sqlaltaguardia.fill_Bases_sql()
        self.model_moviles.clear()
        # Configuración del QTableView
        header_labels = ['Base', 'Patente']
        self.model_moviles.setHorizontalHeaderLabels(header_labels)

        for tupla in bases_datos:
            fila = tupla 
            
            row_items = [QStandardItem(str(dato)) for dato in fila]
            self.model_moviles.appendRow(row_items)

    def select_movil(self):
        indice_seleccionado = self.adg_tblv_1.currentIndex()
        base = self.model_moviles.item(indice_seleccionado.row(), 0).text()
        print(base)

        patente = self.sqlaltaguardia.patente(base)

        if patente:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.adg_let_patente.setText(str(patente[0][0]))
            titulo_base = (f"Movil: {base}")
            self.adg_tlbox_1.setItemText(0,titulo_base)
            self.adg_let_base.setText(str(base))
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.adg_let_patente.setText("")
            self.adg_tlbox_1.setItemText(0,"")

    def addbase(self,):
        subventanamov = SubVentanaAddMovil()
        subventanamov.exec_()
        # Después de que se cierra la subventana, actualiza el combo box y la tabla
        self.fill_adg_comb_base()
        self.fill_adg_tblv_1()

    def delbase(self):
        # Obtener el índice de la fila seleccionada
        indice_seleccionado = self.adg_tblv_1.currentIndex()
        # Verificar si hay una selección válida
        if indice_seleccionado.isValid():
            # Obtener el valor de la primera columna (patente) en la fila seleccionada
            base = self.model_moviles.item(indice_seleccionado.row(), 0).text()
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
                self.sqlaltaguardia.borrar_movil(base)
            else:
                # Si el usuario hizo clic en "No" o cerró la ventana, no hacer nada
                print("Eliminación cancelada.")
            self.fill_adg_comb_base()
            self.fill_adg_tblv_1()
        else:
            print("No hay una fila seleccionada")
            QMessageBox.warning(self, 'Advertencia', 'Por favor, selecciona una fila antes de intentar borrar.',
                                QMessageBox.Ok)

    """########## TODO ALTA DE GUARDIAS ####################### PARAMEDICO"""

    def fill_adg_tblv_2(self,):
        
        # Asignar el modelo a la QTableView
        self.adg_tblv_2.setModel(self.model_paramedicos)

        bases_datos = self.sqlaltaguardia.fill_paramedicos_sql()
        # Configuración del QTableView
        header_labels_paramedicos = ['Legajo', 'Nombre' , 'Apellido' , 'Licencia Venc.'] 
        # Crear el modelo de ítems
        self.model_paramedicos.setHorizontalHeaderLabels(header_labels_paramedicos)

        for tupla in bases_datos:
            fila = tupla 
            
            row_items = [QStandardItem(str(dato)) for dato in fila]
            self.model_paramedicos.appendRow(row_items)

    def select_paramedico(self):
        indice_seleccionado = self.adg_tblv_2.currentIndex()
        legajo = self.model_paramedicos.item(indice_seleccionado.row(), 0).text()
        print(legajo)
        paramedico = self.sqlaltaguardia.paramedicos_datos(legajo)
        legajo = paramedico[0][0]
        nombre_apellido = paramedico[0][1] + " " + paramedico[0][2]
        fecha = paramedico[0][3]
        
        if paramedico:
            # Asegúrate de que la lista patente no esté vacía antes de acceder al índice
            self.adg_let_legajoparamedico.setText(str(legajo))
            titulo_paramedico = (f"Paramedico: {nombre_apellido}")
            self.adg_let_nombreyapellido.setText(nombre_apellido)
            self.adg_date_licenciaparamedico.setDate(fecha)
            self.adg_tlbox_1.setItemText(1,titulo_paramedico)
        else:
            # Si patente está vacío, establece el texto en blanco o maneja la situación según tu lógica
            self.adg_let_legajoparamedico.setText("")
            self.adg_let_nombreyapellido.setText("")
            self.adg_date_licenciaparamedico.setDate("")
            self.adg_tlbox_1.setItemText(1,"Paramedico")

    def addparamedico(self):
        pass

    def delparamedico(self):
        pass



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
        sql = AltaGuardia()
        sql.alta_movil(movil, patente)
        self.accept()

