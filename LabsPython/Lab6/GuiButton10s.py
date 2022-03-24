from tkinter import Tk, Label, Button
import pyfirmata
from pyfirmata import Arduino
import time

board = Arduino("\\.\COM4")
ps = 0

class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Python 3.10 - Arduino")

        self.etiqueta = Label(master, text="Pulse el boton para encender el led.")
        self.etiqueta.pack()

        self.botonEncender = Button(master, text="Encender Led", command=self.encender)
        self.botonEncender.pack()

        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()

    def encender(self):
        global ps
        ps = ps + 1
        if ps == 2:
            print("Encendiendo led...")
            board.digital[8].write(1)
            time.sleep(10)
            print("Apagando led...")
            board.digital[8].write(0)
            ps = 0


root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()