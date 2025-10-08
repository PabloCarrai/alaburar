from tkinter import *
from tkinter import ttk


class acceso:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Bienvenido a AlAburaR")
        self.labelframe = LabelFrame(self.ventana, text="Credenciales")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)
        self.etiquetaNombreUsuario = Label(self.labelframe, text="Nombre de Usuario")
        self.etiquetaNombreUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.datoEntradaNombreUsuario = StringVar()
        self.entradaNombreUsuario = Entry(
            self.labelframe, textvariable=self.datoEntradaNombreUsuario
        )
        self.entradaNombreUsuario.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaClaveUsuario = Label(self.labelframe, text="Clave")
        self.etiquetaClaveUsuario.grid(column=0, row=1, padx=10, pady=10)

        self.ventana.mainloop()


acceso = acceso()
