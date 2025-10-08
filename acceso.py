from tkinter import *
from tkinter import ttk


class acceso:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Bienvenido a AlAburaR")
        self.labelframe = LabelFrame(self.ventana, text="Credenciales")
        self.labelframe.grid(column=0, row=0, padx=10, pady=10)
        self.etiquetaNombreUsuario = Label(self.labelframe, text="Usuario")
        self.etiquetaNombreUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.datoEntradaNombreUsuario = StringVar()
        self.entradaNombreUsuario = Entry(
            self.labelframe, textvariable=self.datoEntradaNombreUsuario
        )
        self.entradaNombreUsuario.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaClaveUsuario = Label(self.labelframe, text="Clave")
        self.etiquetaClaveUsuario.grid(column=0, row=1, padx=10, pady=10)

        self.datoEntradaClaveUsuario = StringVar()
        self.entradaClaveUsuario = Entry(
            self.labelframe, textvariable=self.datoEntradaClaveUsuario
        )
        self.entradaClaveUsuario.grid(column=1, row=1, padx=10, pady=10)
        self.botonIngresar = Button(self.labelframe, text="Ingresar")
        self.botonIngresar.grid(column=0, row=2, padx=5, pady=5)

        self.botonRegistrar = Button(
            self.labelframe, text="Registrarse", command=self.registrarUsuario
        )
        self.botonRegistrar.grid(column=1, row=2, padx=5, pady=5)

        self.ventana.mainloop()

    def registrarUsuario(self):
        self.ventanaRegistrarUsuario = Toplevel()
        self.ventanaRegistrarUsuario.title("Ventana de Registro de Usuario")
        self.ventanaRegistrarUsuario.geometry("300x250")

        self.labelframeRegistroUsuario = LabelFrame(
            self.ventanaRegistrarUsuario, text="Registro de Usuario"
        )
        self.labelframeRegistroUsuario.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaRegistroUsuarioNombre = Label(
            self.labelframeRegistroUsuario, text="Nombre"
        )
        self.etiquetaRegistroUsuarioNombre.grid(column=0, row=0, padx=10, pady=10)

        self.datoEntradaRegistroUsuarioNombre = StringVar()
        self.entradaRegistroUsuarioNombre = Entry(
            self.labelframeRegistroUsuario,
            textvariable=self.datoEntradaRegistroUsuarioNombre,
        )
        self.entradaRegistroUsuarioNombre.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaRegistroUsuarioMail = Label(
            self.labelframeRegistroUsuario, text="Correo"
        )
        self.etiquetaRegistroUsuarioMail.grid(column=0, row=1, padx=10, pady=10)
        self.datoEntradaRegistroUsuarioMail=StringVar()
        self.entradaRegistroUsuarioMail=Entry(self.labelframeRegistroUsuario,textvariable=self.datoEntradaRegistroUsuarioMail)
        self.entradaRegistroUsuarioMail.grid(column=1,row=1, padx=10, pady=10)

        self.etiquetaRegistroUsuarioClave=Label(self.labelframeRegistroUsuario,text="Clave")
        self.etiquetaRegistroUsuarioClave.grid(column=0,row=2, padx=10, pady=10)

        self.datoEntradaRegistroUsuarioClave=StringVar()
        self.entradaRegistroUsuarioClave=Entry(self.labelframeRegistroUsuario,textvariable=self.datoEntradaRegistroUsuarioClave)
        self.entradaRegistroUsuarioClave.grid(column=1,row=2, padx=10, pady=10)

        self.etiquetaRegistroUsuarioClaveReingreso=Label(self.labelframeRegistroUsuario,text="Clave")
        self.etiquetaRegistroUsuarioClaveReingreso.grid(column=0,row=3, padx=10, pady=10)

        self.datoEntradaRegistroUsuarioClave1=StringVar()
        self.entradaRegistroUsuarioClave1=Entry(self.labelframeRegistroUsuario,textvariable=self.datoEntradaRegistroUsuarioClave1)
        self.entradaRegistroUsuarioClave1.grid(column=1,row=3, padx=10, pady=10)

        self.botonRegistroUsuarioRegistrar=Button(self.labelframeRegistroUsuario,text="Registrar")
        self.botonRegistroUsuarioRegistrar.grid(column=1,row=4, padx=10, pady=10)


acceso = acceso()
