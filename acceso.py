from tkinter import *
from tkinter import ttk
import conexion
from tkinter import messagebox as ms


class acceso:
    def __init__(self):
        self.ventana = Tk()

        # Objeto con la conexion
        self.conexion = conexion.conexion()
        self.ventana.title("Bienvenido a Alaburar")
        self.ventana.geometry("300x200")
        #   Labelframe de la ventana de login
        self.labelFramePantallaLogin = LabelFrame(self.ventana, text="Datos de Acceso:")
        self.labelFramePantallaLogin.grid(column=0, row=0, padx=10, pady=10)
        #   Etiqueta de Correo para la pantalla de login
        self.etiquetaCorreoPantallaLogin = Label(
            self.labelFramePantallaLogin, text="Correo:"
        )
        self.etiquetaCorreoPantallaLogin.grid(column=0, row=0, padx=10, pady=10)
        #   Stringvar para la entrada del correo de la pantalla login
        self.datoEntradaCorreoPantallaLogin = StringVar()
        self.entradaCorreoPantallaLogin = Entry(
            self.labelFramePantallaLogin,
            textvariable=self.datoEntradaCorreoPantallaLogin,
        )
        self.entradaCorreoPantallaLogin.grid(column=1, row=0, padx=10, pady=10)

        #   Etiqueta Clave pantalla login
        self.etiquetaClavePantallaLogin = Label(
            self.labelFramePantallaLogin, text="Clave"
        )
        self.etiquetaClavePantallaLogin.grid(column=0, row=2, padx=10, pady=10)
        #   Stringvar para entrada de clave pantalla login
        self.datoEntradaClavePantallaLogin = StringVar()
        self.entradaClavePantallaLogin = Entry(
            self.labelFramePantallaLogin,
            textvariable=self.datoEntradaClavePantallaLogin,
            show="*",
        )
        self.entradaClavePantallaLogin.grid(column=1, row=2, padx=10, pady=10)
        self.botonIngresarPantallaLogin = Button(
            self.labelFramePantallaLogin, text="Ingresar", command=self.existeUsuario
        )
        #   Boton Ingresar Pantalla Login
        self.botonIngresarPantallaLogin.grid(column=0, row=3, padx=10, pady=10)
        self.botonRegistrarUsuarioPantallaLogin = Button(
            self.labelFramePantallaLogin,
            text="Registrarse",
            command=self.pantallaRegistroUsuario,
        )
        self.botonRegistrarUsuarioPantallaLogin.grid(column=1, row=3, padx=10, pady=10)

        self.ventana.mainloop()

    def pantallaRegistroUsuario(self):
        #   Levantamos una pantalla para el login
        self.ventanaRegistroUsuario = Toplevel(self.ventana)
        #   Seteamos un titulo
        self.ventanaRegistroUsuario.title("Registro de Usuario")
        #   Le agregamos un labelframe
        self.labelFramePantallaRegistroUsuario = LabelFrame(
            self.ventanaRegistroUsuario, text="Registro:"
        )
        #   Creamos el label nombre para la pantalla registro de usuario
        self.labelFramePantallaRegistroUsuario.grid(column=0, row=0, padx=10, pady=10)
        self.etiquetaNombrePantallaRegistroUsuario = Label(
            self.labelFramePantallaRegistroUsuario, text="Nombre"
        )
        self.etiquetaNombrePantallaRegistroUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Creamos un stringvar y una entrada para el nombre
        self.datoEntradaNombrePantallaRegistroUsuario = StringVar()
        self.entradaNombrePantallaRegistroUsuario = Entry(
            self.labelFramePantallaRegistroUsuario,
            textvariable=self.datoEntradaNombrePantallaRegistroUsuario,
        )
        self.entradaNombrePantallaRegistroUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Etiqueta para el correo en el registro de usuario
        self.etiquetaCorreoPantallaRegistroUsuario = Label(
            self.labelFramePantallaRegistroUsuario, text="Correo"
        )
        self.etiquetaCorreoPantallaRegistroUsuario.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Stringvar para entrada de correo en Registro Usuario
        self.datoEntradaCorreoPantallaRegistroUsuario = StringVar()
        self.entradaCorreoPantallaRegistroUsuario = Entry(
            self.labelFramePantallaRegistroUsuario,
            textvariable=self.datoEntradaCorreoPantallaRegistroUsuario,
        )
        self.entradaCorreoPantallaRegistroUsuario.grid(
            column=1, row=1, padx=10, pady=10
        )
        #   Primer etiqueta para la clave(Son dos)
        self.etiquetaClavePantallaRegistroUsuario = Label(
            self.labelFramePantallaRegistroUsuario, text="Clave"
        )
        self.etiquetaClavePantallaRegistroUsuario.grid(
            column=0, row=2, padx=10, pady=10
        )
        #   Stringvar para la entrada de la clave en pantalla registro usuario
        self.datoEntradaClavePantallaRegistroUsuario = StringVar()
        self.entradaClavePantallaRegistroUsuario = Entry(
            self.labelFramePantallaRegistroUsuario,
            textvariable=self.datoEntradaClavePantallaRegistroUsuario,
        )
        self.entradaClavePantallaRegistroUsuario.grid(column=1, row=2, padx=10, pady=10)
        self.etiquetaClave1PantallaRegistroUsuario = Label(
            self.labelFramePantallaRegistroUsuario, text="Clave"
        )
        self.etiquetaClave1PantallaRegistroUsuario.grid(
            column=0, row=3, padx=10, pady=10
        )

        self.datoEntradaClave1PantallaRegistroUsuario = StringVar()
        self.entradaClave1PantallaRegistroUsuario = Entry(
            self.labelFramePantallaRegistroUsuario,
            textvariable=self.datoEntradaClave1PantallaRegistroUsuario,
        )
        self.entradaClave1PantallaRegistroUsuario.grid(
            column=1, row=3, padx=10, pady=10
        )

        self.botonRegistrarPantallaRegistroUsuario = Button(
            self.labelFramePantallaRegistroUsuario,
            text="Registrarse",
            command=self.registrarUsuario,
        )
        self.botonRegistrarPantallaRegistroUsuario.grid(
            column=1, row=4, padx=10, pady=10
        )

    def existeUsuario(self):
        correo = self.datoEntradaCorreoPantallaLogin.get()
        clave = self.datoEntradaClavePantallaLogin.get()
        datos = (correo, clave)
        print(correo, clave)
        resultados = self.conexion.consultarUsuario(datos)
        print(len(resultados))

    def registrarUsuario(self):
        nombre = self.datoEntradaNombrePantallaRegistroUsuario.get()
        correo = self.datoEntradaCorreoPantallaRegistroUsuario.get()
        clave = self.datoEntradaClavePantallaRegistroUsuario.get()
        clave1 = self.datoEntradaClave1PantallaRegistroUsuario.get()
        datos = (nombre, correo, clave)
        if len(nombre) == 0 or len(correo) == 0 or len(clave) == 0 or len(clave1) == 0:
            print("Esta vacio")
            ms.showwarning("Error", "Hay campos vacios o mal cargados")
        else:
            if clave != clave1:
                ms.showwarning("Error", "Ingresastes dos claves diferentes")
            else:
                self.conexion.registrarUsuario(datos)
                ms.showinfo("Vamos", "Nuevo Usuario")


aplicacion = acceso()
