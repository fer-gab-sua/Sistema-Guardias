from tkinter import Tk
from vista import Ventana 
from modelo import BaseDeDatos 
from controlador import Controlador

if __name__ == "__main__":
    base_sql = BaseDeDatos() 
    pantalla = Tk()
    controlador = Controlador(base_sql) #instancio Controlador
    ventana = Ventana(pantalla,controlador)
    pantalla.mainloop()
