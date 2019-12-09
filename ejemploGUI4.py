#Entry: caja de texto
#primero se comienza por el eje "y" (row), despues por el eje "x" (column)

from tkinter import *

class MiPrimeraGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")

        self.label = Label(master, text="peso:")
        self.label.grid(row=0, column=0)


        self.caja_texto_peso = Entry(master)
        self.caja_texto_peso.grid(row=1, column=1)

    
         
        self.label = Label(master, text="altura:")
        self.label.grid(row=1, column=0)


        self.caja_texto_altura = Entry(master)
        self.caja_texto_altura.grid(row=0, column=1)
        self.boton_calcular = Button(master, text="Calcular", command=self.calcular)
        self.boton_calcular.grid(row=2, column=0)


        self.boton_cerrar = Button(master, text="CERRAR", command=master.quit)
        self.boton_cerrar.grid(row=2, column=1)

        self.texto_imc = StringVar()
        self.etiqueta_imc = Label(master, textvariable = self.texto_imc)
        self.etiqueta_imc.grid(row=3, column=1)

    def calcular(self):
        texto1 = self.caja_texto_peso.get()
        texto2 = self.caja_texto_altura.get()
        peso = float(texto1)
        altura = float(texto2)
        imc = peso / altura **2       
        if imc <16:
            self.texto_imc.set('Tienes delgadez severa')
        elif imc >=16 and imc <17:
            self.texto_imc.set('Tiene delgadez moderada')
        elif imc >=17 and imc <18.5:
            self.texto_imc.set('Delgadez leve')
        elif imc >18.5 and imc <25:
            self.texto_imc.set('Tiene un estado normal')
        elif imc >=25 and imc <30:
            self.texto_imc.set('Tiene preobesidad')
        elif imc >=30 and imc <35:
            self.texto_imc.set('Tiene obesidad leve')
        elif imc >=40:
            self.texto_imc.set('Tiene obesidad morbida')
        else:
            self.texto_imc.set('Opcion invalida')
           

root = Tk()
mi_gui = MiPrimeraGUI(root)
root.mainloop()