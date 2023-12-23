from PyQt5 import QtWidgets, uic
from logica.ventanaprincipal import Ui_VentanaPrincipal
from modelo.Conect import ConsultasSql


class Ui_LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_LoginForm, self).__init__()
        self.ventana_principal = Ui_VentanaPrincipal()  # Instancia única de la ventana principal
        uic.loadUi('vista/login.ui', self)
        self.pushButton.clicked.connect(self.validar_credenciales)
        self.consultasql = ConsultasSql()

    def validar_credenciales(self):
        self.abrir_ventana_principal()
        """
        if self.consultasql.validar_usuarios(self.user.text(),self.passw.text()) == True:
            self.abrir_ventana_principal()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Credenciales incorrectas', QtWidgets.QMessageBox.Ok)
        """
    def abrir_ventana_principal(self):
        self.hide()  # Oculta la ventana de login

        self.ventana_principal.show()  # Muestra la única instancia de la ventana principal

        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    login_form = Ui_LoginForm()
    login_form.show()

    app.exec_()