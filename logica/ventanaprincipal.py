from PyQt5 import QtWidgets, uic 
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit,QPushButton

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
        #conecto todo lo referido a la primera pantalla 1 - ALTA DE GUARDIA
        
        # Configuración del QTableView
        header_labels = ['Base', 'Patente']
        
        # Crear el modelo de ítems
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(header_labels)

        self.fill_adg_tblv_1()
        # Asignar el modelo a la QTableView
        self.adg_tblv_1.setModel(self.model)
        #lleno el combo box
        self.fill_adg_comb_base()
        self.adg_comb_base.currentIndexChanged.connect(self.select_adg_comb_base)

        #conecto el add y del de la base de moviles
        self.adg_btn_addbase.clicked.connect(lambda:self.addbase())
        self.adg_btn_delbase.clicked.connect(lambda:self.delbase())



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

    """########## TODO ALTA DE GUARDIAS #######################"""
    def fill_adg_tblv_1(self,):
        bases_datos = self.sqlaltaguardia.fill_Bases_sql()

        for tupla in bases_datos:
            fila = tupla 
            
            row_items = [QStandardItem(str(dato)) for dato in fila]
            self.model.appendRow(row_items)

    def fill_adg_comb_base(self):
        bases_datos = self.sqlaltaguardia.fill_Bases_sql()

        for item in bases_datos:
            self.adg_comb_base.addItem(item[0])

    def select_adg_comb_base(self):
        selected_text = self.adg_comb_base.currentText()
        patente = self.sqlaltaguardia.patente(selected_text)
        self.adg_let_patente.setText(str(patente[0][0]))

    def addbase(self,):
        subventanamov = SubVentanaMovil()
        subventanamov.exec_()


    def delbase(self):
        pass
    
    
    
class SubVentanaMovil(QDialog):
    def __init__(self):
        super(SubVentanaMovil, self).__init__()

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
