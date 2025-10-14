from tkinter import *
from tkinter import ttk
import conexion
from tkinter import messagebox as ms
from tkcalendar import DateEntry
import sqlite3


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
        #   Genero la tupla a partir de los valores ingresados
        datos = (
            self.datoEntradaCorreoPantallaLogin.get(),
            self.datoEntradaClavePantallaLogin.get(),
        )
        #   Hago la consulta a la db
        resultados = self.conexion.consultarUsuario(datos)
        #   Si devuelve 1 es porque existe alguien con esas credenciales
        if len(resultados) != 0:
            #   Limpio los entry de correo y clave.
            self.entradaCorreoPantallaLogin.delete(0, END)
            self.entradaClavePantallaLogin.delete(0, END)
            #   Aca tendria que llamar al metodo de la ventana principal de la aplicacion
            #   Guardo datos de sesion
            for i in resultados:
                #   Id usuario que se logueo
                self.idUsuarioLogueado = i[0]
                #   Nombre
                self.nombreUsuarioLogueado = i[1]
                #   Correo
                self.correoUsuarioLogueado = i[2]
            #   Acceso a la pantalla principal para usuario logueados
            self.pantallaUsuarioLogueado()
        else:
            ms.showerror(
                "Problemas", "No tengo a ningun usuario registrado con esos datos"
            )
            #   Limpio los entry de correo y clave.
            self.entradaCorreoPantallaLogin.delete(0, END)
            self.entradaClavePantallaLogin.delete(0, END)

    def registrarUsuario(self):
        #   Guardo el contenido de las entradas en variables
        nombre = self.datoEntradaNombrePantallaRegistroUsuario.get()
        correo = self.datoEntradaCorreoPantallaRegistroUsuario.get()
        clave = self.datoEntradaClavePantallaRegistroUsuario.get()
        clave1 = self.datoEntradaClave1PantallaRegistroUsuario.get()
        #   Genero una tupla para el insert a la tabla usuario
        datos = (nombre, correo, clave)

        #   Chequeo que no haya alguna entrada vacia
        if len(nombre) == 0 or len(correo) == 0 or len(clave) == 0 or len(clave1) == 0:
            print("Esta vacio")
            ms.showwarning("Error", "Hay campos vacios o mal cargados")
        else:
            #   Tengo que chequer antes que nada que el correo no exista.
            correoexiste = self.conexion.correoExiste(correo)
            #   Si correoexiste devuelve 1 es porque el correo existe. Y muestra un error
            if correoexiste[0][0] == 1:
                # Si el correo existe en la db muestro el error y limpio el campo para que ingrese uno nuevo
                ms.showwarning("Error", "El correo existe.")
                self.entradaCorreoPantallaRegistroUsuario.delete(0, END)
            else:
                #   Chequeo que ambas claves coincidan
                if clave != clave1:
                    ms.showwarning("Error", "Ingresastes dos claves diferentes")
                else:
                    #   Si valida las condiciones anteriores inserto el registro y vacio los entry
                    self.conexion.registrarUsuario(datos)
                    self.entradaNombrePantallaRegistroUsuario.delete(0, END)
                    self.entradaCorreoPantallaRegistroUsuario.delete(0, END)
                    self.entradaClavePantallaRegistroUsuario.delete(0, END)
                    self.entradaClave1PantallaRegistroUsuario.delete(0, END)
                    ms.showinfo("Vamos", "Nuevo Usuario")

    def pantallaUsuarioLogueado(self):
        #   Por ahora solo los muestro para onda ver si hay o no usuario
        print(
            self.idUsuarioLogueado,
            self.nombreUsuarioLogueado,
            self.correoUsuarioLogueado,
        )
        self.ventanaPantallaPrincipalUsuarioLogueado = Toplevel()

        #   Arrancamos con el notebook
        self.notebookPantallaPrincipalUsuarioLogueado = ttk.Notebook(
            self.ventanaPantallaPrincipalUsuarioLogueado
        )
        self.notebookPantallaPrincipalUsuarioLogueado.grid(padx=10, pady=10)
        #   Aca defino los frame para cada seccion(este es para datos de sesion)
        self.frame1 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        #   Defino el labelframe para datos de session
        self.labelframeDatosDeSesion = LabelFrame(self.frame1, text="Datos de Session")
        self.labelframeDatosDeSesion.grid(column=0, row=0, padx=10, pady=10)

        #   Agrego una etiqueta id Usuario
        self.etiquetaidUsuarioLogueadoLabelFrameDatosDeSesion = Label(
            self.labelframeDatosDeSesion, text="Id:"
        )
        self.etiquetaidUsuarioLogueadoLabelFrameDatosDeSesion.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Etiqueta con el dato del id del usuario logueado
        self.datoetiquetaidUsuarioLogueadoLabelFrameDatoDeSesion = Label(
            self.labelframeDatosDeSesion, text=self.idUsuarioLogueado
        )
        self.datoetiquetaidUsuarioLogueadoLabelFrameDatoDeSesion.grid(
            column=1, row=0, padx=10, pady=10
        )

        #   Aca va la etiqueda del nombre
        self.etiquetaNombreUsuarioLogueadoLabelFrameDatoDeSesion = Label(
            self.labelframeDatosDeSesion, text="Nombre:"
        )
        self.etiquetaNombreUsuarioLogueadoLabelFrameDatoDeSesion.grid(
            column=0, row=2, padx=10, pady=10
        )

        #   Aca va la etiqueta con el dato nombre
        self.datoNombreUsuarioLogueadoLabelFrameDatoDeSesion = Label(
            self.labelframeDatosDeSesion, text=self.nombreUsuarioLogueado
        )
        self.datoNombreUsuarioLogueadoLabelFrameDatoDeSesion.grid(
            column=1, row=2, padx=10, pady=10
        )

        #   Aca va la etiqueta correo
        self.etiquetaCorreoUsuarioLogueadoLabelFrameDatoDeSesion = Label(
            self.labelframeDatosDeSesion, text="Correo"
        )
        self.etiquetaCorreoUsuarioLogueadoLabelFrameDatoDeSesion.grid(
            column=0, row=3, padx=10, pady=10
        )

        #   Aca va el dato de la etiqueta Correo
        self.datoCorreoUsuarioLogueadoLabelFrameDatoDeSesion = Label(
            self.labelframeDatosDeSesion, text=self.correoUsuarioLogueado
        )
        self.datoCorreoUsuarioLogueadoLabelFrameDatoDeSesion.grid(
            column=1, row=3, padx=10, pady=10
        )

        #   Aca defino los frame para cada seccion(Este es para cargar la tarea)
        self.frame2 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)

        #   Este es el labelframe para esta seccion(Carga de tarea)
        self.labelframeCargaDeTareas = LabelFrame(self.frame2, text="Carga de Tareas")
        self.labelframeCargaDeTareas.grid(column=0, row=0, padx=10, pady=10)

        #   Etiqueta Titulo de la seccion Carga de Tarea
        self.etiquetaTituloTareaLabelFrameCargaDeTareas = Label(
            self.labelframeCargaDeTareas, text="Titulo"
        )
        self.etiquetaTituloTareaLabelFrameCargaDeTareas.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   El stringvar del titulo de la tarea
        self.datoEntradaTituloTareaLabelFrameCargaDeTareas = StringVar()
        self.entradaTituloTareaLabelFrameCargaDeTareas = Entry(
            self.labelframeCargaDeTareas,
            textvariable=self.datoEntradaTituloTareaLabelFrameCargaDeTareas,
        )
        self.entradaTituloTareaLabelFrameCargaDeTareas.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Etiqueta Descripcion de la tarea
        self.etiquetaDescripcionTareaLabelFrameCargaDeTareas = Label(
            self.labelframeCargaDeTareas, text="Descripcion"
        )
        self.etiquetaDescripcionTareaLabelFrameCargaDeTareas.grid(
            column=0, row=2, padx=10, pady=10
        )
        #   Texto de la descripcion de la tarea
        self.textoDescripcionTareaLabelFrameCargaDeTareas = Text(
            self.labelframeCargaDeTareas, height=5, width=20
        )
        self.textoDescripcionTareaLabelFrameCargaDeTareas.grid(
            column=1, row=2, padx=10, pady=10
        )
        #   Etiqueta del combobox Vencimiento(Fecha de vencimiento de la tarea)
        self.etiquetaCalendarioTareaLabelFrameCargaDeTareas = Label(
            self.labelframeCargaDeTareas, text="Vencimiento"
        )
        self.etiquetaCalendarioTareaLabelFrameCargaDeTareas.grid(
            column=0, row=3, padx=10, pady=10
        )
        #   Calendario para cargar la fecha del vencimiento de la tarea
        self.calendarioTareaLabelFrameCargaDeTareas = DateEntry(
            self.labelframeCargaDeTareas
        )
        self.calendarioTareaLabelFrameCargaDeTareas.grid(
            column=1, row=3, padx=10, pady=10
        )
        #   Etiqueta Asignado a
        self.etiquetaAsignadoALabelFrameCargaDeTareas = Label(
            self.labelframeCargaDeTareas, text="Asignado a"
        )
        self.etiquetaAsignadoALabelFrameCargaDeTareas.grid(
            column=0, row=4, padx=10, pady=10
        )
        #   Stringvar del combobox Vencimiento
        self.datoComboBoxAsignadoA = StringVar()
        #   Aca guardo la lista de los usuarios existentes para mostrarlo en el combobox asignado a
        nombresCombobox = self.conexion.listarUsuarios()
        #   El combobox que se arma con el listado de las personas a quienes se le puede asignar tarea
        self.comboboxAsignadoALabelFrameCargaDeTareas = ttk.Combobox(
            self.labelframeCargaDeTareas,
            state="readonly",
            values=nombresCombobox,
            textvariable=self.datoComboBoxAsignadoA,
        )
        self.comboboxAsignadoALabelFrameCargaDeTareas.grid(
            column=1, row=4, padx=10, pady=10
        )
        #   Etiqueta de la prioridad de la tarea
        self.etiquetaPrioridadLabelFrameCargaDeTareas = Label(
            self.labelframeCargaDeTareas, text="Prioridad"
        )
        self.etiquetaPrioridadLabelFrameCargaDeTareas.grid(
            column=0, row=5, padx=10, pady=10
        )
        #   Stringvar para el combobox de Prioridades
        self.datoComboBoxPrioridadLabelFrameCargaDeTarea = StringVar()
        #   Aca tomo los nombres de las prioridades para mostrar en el combobox
        prioridadComboBox = self.conexion.listarPrioridades()
        #   Armo el combobox de prioridades
        self.comboboxPrioridadALabelFrameCargaDeTareas = ttk.Combobox(
            self.labelframeCargaDeTareas,
            state="readonly",
            values=prioridadComboBox,
            textvariable=self.datoComboBoxPrioridadLabelFrameCargaDeTarea,
        )
        self.comboboxPrioridadALabelFrameCargaDeTareas.grid(
            column=1, row=5, padx=10, pady=10
        )
        #   Boton Crear tarea
        self.botonCrearTareaLabelFrameCargaDeTareas = Button(
            self.labelframeCargaDeTareas, text="Crear Tarea", command=self.crearTarea
        )
        self.botonCrearTareaLabelFrameCargaDeTareas.grid(
            column=1, row=6, padx=10, pady=10
        )

        #   Frame del listado de tareas
        self.frame3 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)

        self.labelframeListadoDeTareas = LabelFrame(
            self.frame3, text="Listado de Tareas"
        )
        self.labelframeListadoDeTareas.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaNombreDeTareaLabelFrameListadoDeTareas = Label(
            self.labelframeListadoDeTareas, text="Nombre"
        )
        self.etiquetaNombreDeTareaLabelFrameListadoDeTareas.grid(
            column=0, row=0, padx=10, pady=10
        )

        self.frame4 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        self.frame5 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        self.frame6 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)

        #   Agrego los frames al notebook
        self.notebookPantallaPrincipalUsuarioLogueado.add(
            self.frame1, text="Datos De Sesion"
        )
        self.notebookPantallaPrincipalUsuarioLogueado.add(
            self.frame2, text="Carga De Tareas"
        )
        self.notebookPantallaPrincipalUsuarioLogueado.add(
            self.frame3, text="Listado de Tareas"
        )
        self.notebookPantallaPrincipalUsuarioLogueado.add(self.frame4, text="tab4")
        self.notebookPantallaPrincipalUsuarioLogueado.add(self.frame5, text="tab5")
        self.notebookPantallaPrincipalUsuarioLogueado.add(self.frame6, text="tab6")

    def crearTarea(self):

        idAsinadoA = self.conexion.obtenerIdporNombreAsignadoa(
            self.datoComboBoxAsignadoA.get()
        )
        #   Esto es el id del usuario AsignadoA
        idAsinadoAValor = idAsinadoA[0][0]
        #   Esto es el id de la prioridad de la tarea
        idPrioridadTarea = self.conexion.obtenerIdPorNombrePrioridad(
            self.datoComboBoxPrioridadLabelFrameCargaDeTarea.get()
        )
        idPrioridadTareaValor = idPrioridadTarea[0][0]
        """
        Aca por el momento tengo, 
        titulo, descripcion,vencimiento,idcreadir,asignadoA,estadotarea,Prioridad
        """
        datos = (
            self.datoEntradaTituloTareaLabelFrameCargaDeTareas.get(),
            self.textoDescripcionTareaLabelFrameCargaDeTareas.get("1.0", END),
            self.calendarioTareaLabelFrameCargaDeTareas.get_date(),
            self.idUsuarioLogueado,
            idAsinadoAValor,
            1,
            idPrioridadTareaValor,
        )
        self.conexion.ingresarTareaNueva(datos)
        ms.showinfo("vamos", "Registro de tarea nueva creada")
        self.entradaTituloTareaLabelFrameCargaDeTareas.delete(0, END)
        self.textoDescripcionTareaLabelFrameCargaDeTareas.delete("1.0", END)
        self.comboboxAsignadoALabelFrameCargaDeTareas.set("")
        self.comboboxPrioridadALabelFrameCargaDeTareas.set("")


aplicacion = acceso()
