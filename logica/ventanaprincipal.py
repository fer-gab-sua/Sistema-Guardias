from PyQt5 import QtWidgets, uic 
from PyQt5.QtGui import QStandardItemModel, QStandardItem


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
        self.adg_comb_basecurrentIndexChanged.connect(self.metodo_seleccion)



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
        print(f"Elemento seleccionado: {selected_text}")
