

from tkinter import Tk, Label, Button

class MiPrimeraGUI:
    def __init__(self, master):
        self.master = master
#cambiando el nombre de la ventana
        master.title("Te amo alejandro")

        self.etiqueta = Label(master, text="Mi primera GUI")
        self.etiqueta.pack()

        self.boton_saludo = Button(master, text="Saludo", command=self.saludar)
        self.boton_saludo.pack()

        self.boton_dias = Button(master, text="Buenos Dias", command=self.darBuenos)
        self.boton_dias.pack()

        self.boton_cerrar = Button(master, text="Cerrar", command=master.quit)
        self.boton_cerrar.pack()

    def saludar(self):
        print("Saludos!")

    def darBuenos(self):
        print("Buenos dias")

root = Tk()
mi_gui = MiPrimeraGUI(root)
root.mainloop()