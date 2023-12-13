from PyQt5 import QtWidgets
import sys

# Importa la clase Ui_MainWindow del módulo donde la has definido
from vista import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec_())