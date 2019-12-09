#Introduccion a la programacion de GUI (Grophical User Interface)
#Hasta ahora hemos escrito algunos programas que se ejecutan en una linea de comando. Sin embargo un usuario promedio espera, interactuar de forma grafica con la computadora
#En python existe un modulo que se llama "tKinter" que provee una serie de librerias estandar para el manjeo de graficos en la computadora. Este modulo permite generar graficos en cualquier tipo de plataforma
# y utiliza el manejo de clases y objetos utulizando una forma de programacion llamada "PROGRAMACION ORIENTADA A EVENTOS", en el que un evento se activa cuando el usuario hace algo, por ejemplo 
# Cuando se da un clik en un boton  o cuando se preciona una cierta tecla estas aplicaciones siempre deven de escuchar los eventos y responder en el caso de que ocurra un evento 
#tkinter libreria Tk (ventana)
#label (etiqueta)
#button(botonoes)
# a master no se le puede cambiar el nombre, siempre va llevar el master cada que tengamos que hacer una interfaz grafica
#master (ventana)
#pack (agrupando a como se vallan creando)
#tk(tambien reacciona a android, etc, wiiled)





from tkinter import Tk, Label, Button

class MiPrimeraGUI:
    def __init__(self, master):
        self.master = master
#cambiando el nombre de la ventana
        master.title("Una GUI sencilla")

        self.etiqueta = Label(master, text="Mi primera GUI")
        self.etiqueta.pack()

        self.boton_saludo = Button(master, text="Saludo", command=self.saludar)
        self.boton_saludo.pack()

        self.boton_cerrar = Button(master, text="Cerrar", command=master.quit)
        self.boton_cerrar.pack()
    def saludar(self):
        print("Saludos!")

root = Tk()
mi_gui = MiPrimeraGUI(root)
root.mainloop()