import tkinter as tk
from tkinter import simpledialog

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")

        self.boton_abrir = tk.Button(master, text="Abrir Ventana Emergente", command=self.abrir_ventana_emergente)
        self.boton_abrir.pack(pady=20)

    def abrir_ventana_emergente(self):
        # Configurar el mensaje y las opciones del ComboBox
        mensaje = "Selecciona una opción:"
        opciones = ["Opción 1", "Opción 2", "Opción 3"]

        # Mostrar la ventana emergente con un ComboBox
        seleccion = simpledialog.askstring("Mensaje", mensaje, parent=self.master, initialvalue=opciones[0])

        if seleccion:
            print("Opción seleccionada:", seleccion)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app_principal = VentanaPrincipal(ventana_principal)
    ventana_principal.mainloop()