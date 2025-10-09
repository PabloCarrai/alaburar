from tkinter import *
from tkinter import ttk
import gestordb
from tkinter import messagebox as ms


class acceso:
    def __init__(self):
        self.usuarioSesion = ""
        self.claveSesion = ""

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
            self.labelframe, textvariable=self.datoEntradaClaveUsuario, show="*"
        )
        self.entradaClaveUsuario.grid(column=1, row=1, padx=10, pady=10)
        self.botonIngresar = Button(
            self.labelframe, text="Ingresar", command=self.ingresar
        )
        self.botonIngresar.grid(column=0, row=2, padx=5, pady=5)

        self.botonRegistrar = Button(
            self.labelframe, text="Registrarse", command=self.registrarUsuario
        )
        self.botonRegistrar.grid(column=1, row=2, padx=5, pady=5)

        self.ventana.mainloop()

    def ingresar(self):
        """Aca hay que hacer bien el metodo, esto por ahora es prueba"""
        nombre = self.datoEntradaNombreUsuario.get()
        self.usuarioSesion = nombre
        clave = self.datoEntradaClaveUsuario.get()
        self.claveSesion = clave
        print(nombre, clave)
        conexion = gestordb.gestordb()
        resultado = conexion.consultarUsuario((nombre,))
        for e in resultado:
            print(e)

    def registrarUsuario(self):
        self.ventanaRegistrarUsuario = Toplevel(self.ventana)
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
        self.datoEntradaRegistroUsuarioMail = StringVar()
        self.entradaRegistroUsuarioMail = Entry(
            self.labelframeRegistroUsuario,
            textvariable=self.datoEntradaRegistroUsuarioMail,
        )
        self.entradaRegistroUsuarioMail.grid(column=1, row=1, padx=10, pady=10)

        self.etiquetaRegistroUsuarioClave = Label(
            self.labelframeRegistroUsuario, text="Clave"
        )
        self.etiquetaRegistroUsuarioClave.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaRegistroUsuarioClave = StringVar()
        self.entradaRegistroUsuarioClave = Entry(
            self.labelframeRegistroUsuario,
            textvariable=self.datoEntradaRegistroUsuarioClave,
        )
        self.entradaRegistroUsuarioClave.grid(column=1, row=2, padx=10, pady=10)

        self.etiquetaRegistroUsuarioClaveReingreso = Label(
            self.labelframeRegistroUsuario, text="Clave"
        )
        self.etiquetaRegistroUsuarioClaveReingreso.grid(
            column=0, row=3, padx=10, pady=10
        )

        self.datoEntradaRegistroUsuarioClave1 = StringVar()
        self.entradaRegistroUsuarioClave1 = Entry(
            self.labelframeRegistroUsuario,
            textvariable=self.datoEntradaRegistroUsuarioClave1,
        )
        self.entradaRegistroUsuarioClave1.grid(column=1, row=3, padx=10, pady=10)

        self.botonRegistroUsuarioRegistrar = Button(
            self.labelframeRegistroUsuario,
            text="Registrar",
            command=self.insertarUsuariodb,
        )
        self.botonRegistroUsuarioRegistrar.grid(column=1, row=4, padx=10, pady=10)

    def insertarUsuariodb(self):
        nombre = self.datoEntradaRegistroUsuarioNombre.get()
        correo = self.datoEntradaRegistroUsuarioMail.get()
        clave = self.datoEntradaRegistroUsuarioClave.get()
        conexion = gestordb.gestordb()
        datos = (nombre, correo, clave)
        conexion.insertarUsuario(datos)
        self.entradaRegistroUsuarioNombre.delete(0, END)
        self.entradaRegistroUsuarioMail.delete(0, END)
        self.entradaRegistroUsuarioClave.delete(0, END)
        self.entradaRegistroUsuarioClave1.delete(0, END)
        ms.showinfo("Registro de usuario Exitoso", "Vamos carajo")


acceso = acceso()
