from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de QTableView")
        self.setGeometry(100, 100, 600, 400)

        # Crear un modelo de datos
        modelo = QStandardItemModel(self)

        # Agregar encabezados a las columnas
        modelo.setHorizontalHeaderLabels(['Nombre', 'Edad', 'Ciudad'])

        # Agregar datos al modelo
        datos = [
            ['Juan', 25, 'Ciudad A'],
            ['María', 30, 'Ciudad B'],
            ['Pedro', 22, 'Ciudad C'],
        ]

        for fila, datos_fila in enumerate(datos):
            for columna, valor in enumerate(datos_fila):
                item = QStandardItem(str(valor))
                modelo.setItem(fila, columna, item)

        # Crear un QTableView y establecer el modelo
        tabla = QTableView(self)
        tabla.setModel(modelo)

        # Crear un layout y agregar el QTableView
        layout = QVBoxLayout()
        layout.addWidget(tabla)

        # Crear un widget contenedor para el layout
        contenedor = QWidget()
        contenedor.setLayout(layout)

        # Establecer el widget contenedor como el widget central
        self.setCentralWidget(contenedor)

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    ventana.show()
    app.exec_()