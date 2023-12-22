from PyQt5 import QtWidgets, uic

class Ui_VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_VentanaPrincipal, self).__init__()
        uic.loadUi('vista/pantalla.ui', self)
        self.setWindowTitle("Pantalla de guadias")  # Cambia el título de la ventana si es necesario
        self.label.setText("hola como estas?")
        # Conecta eventos y métodos aquí
        self.actionAlta_de_Guardias.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(0))
        self.actionMedicos.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(1))
        self.actionCabina.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(2))
        self.actionEnfermeros.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(3))
        self.actionHistorial.triggered.connect(lambda: self.StackedWidget_stwid_1.setCurrentIndex(3))