from tkinter import *
from tkinter import ttk
import conexion
from tkinter import messagebox as ms
from tkinter import scrolledtext as sc
from tkcalendar import DateEntry
from datetime import datetime


class acceso:
    def __init__(self):
        self.ventana = Tk()
        self.erroresDeIntentoDeAcceso = 0

        # Objeto con la conexion
        self.conexion = conexion.conexion()
        self.ventana.title("Bienvenido a Alaburar")
        self.ventana.geometry("310x250")
        # #   Ponerle el icono
        icono = PhotoImage(file="/home/ed/alaburar/icono-app.png")
        self.ventana.iconphoto(True, icono)

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
        self.botonIngresarPantallaLogin.grid(column=0, row=5, padx=10, pady=10)
        self.botonRegistrarUsuarioPantallaLogin = Button(
            self.labelFramePantallaLogin,
            text="Registrarse",
            command=self.pantallaRegistroUsuario,
        )
        self.botonRegistrarUsuarioPantallaLogin.grid(column=1, row=5, padx=10, pady=10)

        self.datacheckbuttonForMostrarOcultarClave = IntVar()
        self.checkbuttonForMostrarOcultarClave = Checkbutton(
            self.labelFramePantallaLogin,
            text="Mostrar/Ocutar clave",
            variable=self.datacheckbuttonForMostrarOcultarClave,
            onvalue=1,
            offvalue=0,
            command=self.mostrarClave,
        )
        self.checkbuttonForMostrarOcultarClave.grid(column=1, row=4, padx=10, pady=10)

        self.ventana.mainloop()

    def mostrarClave(self):
        if self.datacheckbuttonForMostrarOcultarClave.get() == 1:
            self.entradaClavePantallaLogin.config(show="")
        else:
            if self.datacheckbuttonForMostrarOcultarClave.get() == 0:
                self.entradaClavePantallaLogin.config(show="*")

    def pantallaRegistroUsuario(self):
        #   Levantamos una pantalla para el login
        self.ventanaRegistroUsuario = Toplevel()
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
            show="*",
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
            show="*",
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

            #   Acceso a admin
            if self.idUsuarioLogueado == 12:
                self.pantallaUsuarioAdmin()
            else:
                #   Acceso a la pantalla principal para usuario logueados
                self.pantallaUsuarioLogueado()
        else:
            ms.showerror(
                "Problemas", "No tengo a ningun usuario registrado con esos datos"
            )
            #   Limpio los entry de correo y clave.
            self.entradaCorreoPantallaLogin.delete(0, END)
            self.entradaClavePantallaLogin.delete(0, END)
            self.erroresDeIntentoDeAcceso = self.erroresDeIntentoDeAcceso + 1
            if self.erroresDeIntentoDeAcceso > 2:
                self.ventana.destroy()

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
        #   Esta seria la ventana principal del usuario una vez pasado el login
        self.ventanaPantallaPrincipalUsuarioLogueado = Toplevel()
        #   Arrancamos con el notebook
        self.notebookPantallaPrincipalUsuarioLogueado = ttk.Notebook(
            self.ventanaPantallaPrincipalUsuarioLogueado
        )
        #   El notebook es para todas las pantallas
        self.notebookPantallaPrincipalUsuarioLogueado.grid(padx=10, pady=10)
        #   Aca defino los frame para cada seccion(este es para datos de sesion)
        self.frame1 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        #   Defino el labelframe para datos de sesion
        self.labelframeDatosDeSesion = LabelFrame(self.frame1, text="Datos de Sesion")
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
        #   Este frame lo usamos en la seccion carga de tarea
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
            self.labelframeCargaDeTareas, date_pattern="yyyy-mm-dd"
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
        prioridadComboBox = self.conexion.listarPrioridad()
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
        #   Este es el label frame del listado de tareas
        self.labelframeListadoDeTareas = LabelFrame(
            self.frame3, text="Listado de Tareas"
        )
        self.labelframeListadoDeTareas.grid(column=0, row=0, padx=10, pady=10)
        #   Aca vamos con la etiqueta Estado del label frame listado de tareas
        self.etiquetaEstadosDeTareaLabelFrameListadoDeTareas = Label(
            self.labelframeListadoDeTareas, text="Estado:"
        )
        self.etiquetaEstadosDeTareaLabelFrameListadoDeTareas.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Stringvar para el combobox de Estados
        self.datoComboBoxEstadosLabelFrameListadoDeTareas = StringVar()
        #   Aca tomo los nombres de las Estados para mostrar en el combobox
        estadosComboBox = self.conexion.listarEstados()
        #   Armo el combobox de prioridades
        self.comboboxPrioridadALabelFrameListadoDeTareas = ttk.Combobox(
            self.labelframeListadoDeTareas,
            state="readonly",
            values=estadosComboBox,
            textvariable=self.datoComboBoxEstadosLabelFrameListadoDeTareas,
        )
        self.comboboxPrioridadALabelFrameListadoDeTareas.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Etiqueta Prioridad LabelFrame Listado de tareas
        self.etiquetaPrioridadDeTareaLabelFrameListadoDeTareas = Label(
            self.labelframeListadoDeTareas, text="Prioridad:"
        )
        self.etiquetaPrioridadDeTareaLabelFrameListadoDeTareas.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Stringvar para el combobox de Prioridad
        self.datoComboBoxPrioridadLabelFrameListadoDeTareas = StringVar()
        #   Aca tomo los nombres de las Prioridad para mostrar en el combobox
        prioridadComboBox = (
            self.conexion.listarPrioridad()
        )  #   Tengo que generar el metodo y cambiarlo aca
        #   Armo el combobox de prioridades
        self.comboboxPrioridadALabelFrameListadoDeTareas = ttk.Combobox(
            self.labelframeListadoDeTareas,
            state="readonly",
            values=prioridadComboBox,
            textvariable=self.datoComboBoxPrioridadLabelFrameListadoDeTareas,
        )
        self.comboboxPrioridadALabelFrameListadoDeTareas.grid(
            column=1, row=1, padx=10, pady=10
        )
        #   Etiqueta Asignado a listado de tareas
        self.etiquetaAsignadoADeTareaLabelFrameListadoDeTareas = Label(
            self.labelframeListadoDeTareas, text="Asignado a:"
        )
        self.etiquetaAsignadoADeTareaLabelFrameListadoDeTareas.grid(
            column=0, row=2, padx=10, pady=10
        )
        #   Stringvar para el combobox de AsignadoA
        self.datoComboBoxAsignadoALabelFrameListadoDeTareas = StringVar()
        #   Aca tomo los nombres de las AsignadoA para mostrar en el combobox
        asignadoAComboBox = (
            self.conexion.listarUsuarios()
        )  #   Tengo que generar el metodo y cambiarlo aca
        #   Armo el combobox de prioridades
        self.comboboxPrioridadALabelFrameListadoDeTareas = ttk.Combobox(
            self.labelframeListadoDeTareas,
            state="readonly",
            values=asignadoAComboBox,
            textvariable=self.datoComboBoxAsignadoALabelFrameListadoDeTareas,
        )
        self.comboboxPrioridadALabelFrameListadoDeTareas.grid(
            column=1, row=2, padx=10, pady=10
        )
        #   Boton de Consulta de tareas
        self.botonConsultarLabelFrameListadoDeTarea = Button(
            self.labelframeListadoDeTareas,
            text="Consultar",
            command=self.consultarTareaDb,
        )
        self.botonConsultarLabelFrameListadoDeTarea.grid(
            column=1, row=3, padx=10, pady=10
        )
        #   Aca va lo del labelframeResultado
        self.labelframeListadoDeTareasResultado = LabelFrame(
            self.frame3, text="Resultado"
        )
        self.labelframeListadoDeTareasResultado.grid(column=0, row=1, padx=10, pady=10)
        #   Etiqueta Tareas
        self.etiquetaLabelFrameListadoDeTareasResultado = Label(
            self.labelframeListadoDeTareasResultado, text="Tareas"
        )
        self.etiquetaLabelFrameListadoDeTareasResultado.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Scrooledtext para listar las tareas
        self.scrooledtextLabelFrameListadoDeTareasResultado = sc.ScrolledText(
            self.labelframeListadoDeTareasResultado, width=40, height=10
        )
        self.scrooledtextLabelFrameListadoDeTareasResultado.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   frame4 es para Edicion de Tareas
        self.frame4 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        #   Labelframe de Edicion de tareas
        self.labelFrameEdicionDeTareas = LabelFrame(
            self.frame4, text="Edicion de Tareas"
        )
        self.labelFrameEdicionDeTareas.grid(column=0, row=0, padx=10, pady=10)
        #   Etiqueta codigo para edicion de tareas
        self.etiquetaCodigoTareaLabelFrameEdicionDeTareas = Label(
            self.labelFrameEdicionDeTareas, text="Codigo"
        )
        self.etiquetaCodigoTareaLabelFrameEdicionDeTareas.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Stringvar del entry de codigo para edicion de tareas
        self.datoEntradaCodigoLabelFrameEdicionDeTareas = StringVar()
        #   Entry de codigo
        self.entradaCodigoLabelFrameEdicionDeTareas = Entry(
            self.labelFrameEdicionDeTareas,
            textvariable=self.datoEntradaCodigoLabelFrameEdicionDeTareas,
        )
        self.entradaCodigoLabelFrameEdicionDeTareas.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Botom consulta
        self.botonEditarTareaLabelFrameEdicionDeTareas = Button(
            self.labelFrameEdicionDeTareas, text="Consultar", command=self.buscarTarea
        )
        self.botonEditarTareaLabelFrameEdicionDeTareas.grid(
            column=1, row=1, padx=10, pady=10
        )
        #   Labelframe datos a modificar
        self.labelFrameEdicionDeTareasDatosExistentes = LabelFrame(
            self.frame4, text="Datos a Modificar"
        )
        self.labelFrameEdicionDeTareasDatosExistentes.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Etiqueta titulo
        self.etiquetaTitulolabelFrameEdicionDeTareasDatosExistentes = Label(
            self.labelFrameEdicionDeTareasDatosExistentes, text="Titulo"
        )
        self.etiquetaTitulolabelFrameEdicionDeTareasDatosExistentes.grid(
            column=0, row=0, padx=10, pady=10
        )
        #   Stringvar titulo
        self.datoEntradaTitulolabelFrameEdicionDeTareasDatosExistente = StringVar()
        self.entradaTitulolabelFrameEdicionDeTareasDatosExistente = Entry(
            self.labelFrameEdicionDeTareasDatosExistentes,
            textvariable=self.datoEntradaTitulolabelFrameEdicionDeTareasDatosExistente,
        )
        self.entradaTitulolabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=0, padx=10, pady=10
        )
        #   Etiqueta Descripcion
        self.etiquetaComentariolabelFrameEdicionDeTareasDatosExistente = Label(
            self.labelFrameEdicionDeTareasDatosExistentes, text="Descripcion"
        )
        self.etiquetaComentariolabelFrameEdicionDeTareasDatosExistente.grid(
            column=0, row=1, padx=10, pady=10
        )
        #   Stringvar Descripcion
        self.datoEntradaDescripcionlabelFrameEdicionDeTareasDatosExistente = StringVar()
        self.entradaDescripcionlabelFrameEdicionDeTareasDatosExistente = Entry(
            self.labelFrameEdicionDeTareasDatosExistentes,
            textvariable=self.datoEntradaDescripcionlabelFrameEdicionDeTareasDatosExistente,
        )
        self.entradaDescripcionlabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=1, padx=10, pady=10
        )
        #   Etiqueta Vencimiento
        self.etiquetaVencimientolabelFrameEdicionDeTareasDatosExistente = Label(
            self.labelFrameEdicionDeTareasDatosExistentes, text="Vencimiento"
        )
        self.etiquetaVencimientolabelFrameEdicionDeTareasDatosExistente.grid(
            column=0, row=2, padx=10, pady=10
        )
        #   Calendario para cargar la fecha del vencimiento de la tarea
        self.calendarioVencimientolabelFrameEdicionDeTareasDatosExistente = DateEntry(
            self.labelFrameEdicionDeTareasDatosExistentes, date_pattern="yyyy-mm-dd"
        )
        self.calendarioVencimientolabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=2, padx=10, pady=10
        )
        #   Etiqueta Asignado a
        self.etiquetaAsignadoAlabelFrameEdicionDeTareasDatosExistente = Label(
            self.labelFrameEdicionDeTareasDatosExistentes, text="Asignado a"
        )
        self.etiquetaAsignadoAlabelFrameEdicionDeTareasDatosExistente.grid(
            column=0, row=3, padx=10, pady=10
        )
        #   Combobox Asignado a
        datoscombobox = self.conexion.listarUsuarios()
        self.datoComboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente = StringVar()
        self.comboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente = ttk.Combobox(
            self.labelFrameEdicionDeTareasDatosExistentes,
            textvariable=self.datoComboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente,
            values=datoscombobox,
        )
        self.comboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=3, padx=10, pady=10
        )
        #   Etiqueta Prioridad
        self.etiquetaPrioridadDeTarealabelFrameEdicionDeTareasDatosExistente = Label(
            self.labelFrameEdicionDeTareasDatosExistentes, text="Estado"
        )
        self.etiquetaPrioridadDeTarealabelFrameEdicionDeTareasDatosExistente.grid(
            column=0, row=4, padx=10, pady=10
        )

        #   Parte del combobox Prioridades
        datoscomboboxEstados = self.conexion.obtenerNombresEstados()
        self.datoComboboxEstadoslabelFrameEdicionDeTareasDatosExistente = StringVar()
        self.comboboxEstadoslabelFrameEdicionDeTareasDatosExistente = ttk.Combobox(
            self.labelFrameEdicionDeTareasDatosExistentes,
            textvariable=self.datoComboboxEstadoslabelFrameEdicionDeTareasDatosExistente,
            values=datoscomboboxEstados,
        )
        self.comboboxEstadoslabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=4, padx=10, pady=10
        )

        self.botonActualizarTarealabelFrameEdicionDeTareasDatosExistente = Button(
            self.labelFrameEdicionDeTareasDatosExistentes,
            text="Actualizar",
            command=self.actualizarTarea,
        )
        self.botonActualizarTarealabelFrameEdicionDeTareasDatosExistente.grid(
            column=1, row=5, padx=10, pady=10
        )

        #   Arranco el tab Eliminar la tarea

        #   frame5 es para Eliminar de Tareas
        self.frame5 = ttk.Frame(self.notebookPantallaPrincipalUsuarioLogueado)
        #   Labelframe de Eliminar de tareas
        self.labelFrameEliminarTareas = LabelFrame(self.frame5, text="Eliminar Tarea")
        self.labelFrameEliminarTareas.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaCodigolabelFrameEliminarTareas = Label(
            self.labelFrameEliminarTareas, text="Codigo"
        )
        self.etiquetaCodigolabelFrameEliminarTareas.grid(
            column=0, row=0, padx=10, pady=10
        )

        #   Stringvar de Codigo en Eliminar Tarea
        self.datoEntradaCodigolabelFrameEliminarTareas = StringVar()
        #   Entry de Codigo eliminar tarea
        self.entradaCodigolabelFrameEliminarTareas = Entry(
            self.labelFrameEliminarTareas,
            textvariable=self.datoEntradaCodigolabelFrameEliminarTareas,
        )
        self.entradaCodigolabelFrameEliminarTareas.grid(
            column=1, row=0, padx=10, pady=10
        )

        #   Boton consultar codigo tareas
        self.botonConsultarCodigolabelFrameEliminarTareas = Button(
            self.labelFrameEliminarTareas,
            text="Consultar",
            command=self.consultarTareaPorId,
        )

        self.botonConsultarCodigolabelFrameEliminarTareas.grid(
            column=1, row=1, padx=10, pady=10
        )

        #   Labelframe de Eliminar de tareas
        self.labelFrameEliminarTareasListadoTareas = LabelFrame(
            self.frame5, text="Tarea"
        )
        self.labelFrameEliminarTareasListadoTareas.grid(
            column=1, row=0, padx=10, pady=10
        )

        self.etiquetaTituloTarealabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text="Titulo:"
        )
        self.etiquetaTituloTarealabelFrameEliminarTareasListadoTareas.grid(
            column=0, row=0, padx=10, pady=10
        )

        self.datoEtiquetaTituloTarealabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text=""
        )
        self.datoEtiquetaTituloTarealabelFrameEliminarTareasListadoTareas.grid(
            column=1, row=0, padx=10, pady=10
        )

        self.etiquetaDescripcionTarealabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text="Descripcion"
        )
        self.etiquetaDescripcionTarealabelFrameEliminarTareasListadoTareas.grid(
            column=0, row=1, padx=10, pady=10
        )

        self.datoEtiquetaDescripcionTarealabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text=""
        )
        self.datoEtiquetaDescripcionTarealabelFrameEliminarTareasListadoTareas.grid(
            column=1, row=1, padx=10, pady=10
        )

        self.etiquetaAsignadoAlabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text="Asignado A"
        )
        self.etiquetaAsignadoAlabelFrameEliminarTareasListadoTareas.grid(
            column=0, row=2, padx=10, pady=10
        )

        self.datoEtiquetaAsignadoAlabelFrameEliminarTareasListadoTareas = Label(
            self.labelFrameEliminarTareasListadoTareas, text=""
        )
        self.datoEtiquetaAsignadoAlabelFrameEliminarTareasListadoTareas.grid(
            column=1, row=2, padx=10, pady=10
        )

        self.botonEliminarTarealabelFrameEliminarTareasListadoTareas = Button(
            self.labelFrameEliminarTareasListadoTareas,
            text="Eliminar",
            command=self.eliminarTareas,
        )
        self.botonEliminarTarealabelFrameEliminarTareasListadoTareas.grid(
            column=1, row=3, padx=10, pady=10
        )

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
        self.notebookPantallaPrincipalUsuarioLogueado.add(
            self.frame4, text="Edicion de Tarea"
        )
        self.notebookPantallaPrincipalUsuarioLogueado.add(
            self.frame5, text="Eliminar Tarea"
        )

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

    def consultarTareaDb(self):
        if (
            (not self.datoComboBoxEstadosLabelFrameListadoDeTareas.get())
            or (not self.datoComboBoxPrioridadLabelFrameListadoDeTareas.get())
            or (not self.datoComboBoxAsignadoALabelFrameListadoDeTareas.get())
        ):
            ms.showinfo("Error", "No se ha elegido ninguna opcion en los desplegables")
        else:
            #   Obtengo los id de cada elemento elegido en los combobox(los tres)
            datos = (
                self.conexion.obtenerIdporNombreEstado(
                    self.datoComboBoxEstadosLabelFrameListadoDeTareas.get()
                )[0][0],
                self.conexion.obtenerIdPorNombrePrioridad(
                    self.datoComboBoxPrioridadLabelFrameListadoDeTareas.get()
                )[0][0],
                self.conexion.obtenerIdporNombreAsignadoa(
                    self.datoComboBoxAsignadoALabelFrameListadoDeTareas.get()
                )[0][0],
            )
            #   Tengo que traerme el id,titulo de las tareas segun datos
            #   select id,titulo from tareas where id_estado=? and id_prioridad=? and id_asignado=?
            resultado = self.conexion.listarTareasSegunDatos(datos)
        if len(resultado) == 0:
            ms.showinfo("Error", "No tenemos tareas segun esas condiciones")
        else:
            self.scrooledtextLabelFrameListadoDeTareasResultado.delete("1.0", END)
            for tupla in resultado:
                linea_resultado = f"ID: {tupla[0]} Titulo: {tupla[1]}\n"
                self.scrooledtextLabelFrameListadoDeTareasResultado.insert(
                    END, linea_resultado
                )

    def buscarTarea(self):
        dato = (self.datoEntradaCodigoLabelFrameEdicionDeTareas.get(),)
        consulta = self.conexion.buscarTareaendb(dato)
        if len(consulta) == 0:
            ms.showinfo("Error", "No existe tarea con ese id")
            self.entradaCodigoLabelFrameEdicionDeTareas.delete(0, END)
        else:
            self.entradaTitulolabelFrameEdicionDeTareasDatosExistente.delete(0, END)
            self.entradaDescripcionlabelFrameEdicionDeTareasDatosExistente.delete(
                0, END
            )
            self.comboboxEstadoslabelFrameEdicionDeTareasDatosExistente.set("")
            titulo = consulta[0][1]
            descripcion = consulta[0][2]
            #   Cadena de la fecha original año mes dia
            cadena_fecha_original = consulta[0][3]
            #   Formato original
            formato_original = "%Y-%m-%d"
            #   Tranformo el string a una fecha con formato
            objeto_fecha = datetime.strptime(cadena_fecha_original, formato_original)
            #   Hago la conversion
            cadena_Fecha_formateada = objeto_fecha.strftime(formato_original)
            #   Esto va a guardar consultando el id de la tarea a quien se le asigno la misma(el nombre)
            asignadoA = self.conexion.obtenerNombreAsignadoaporid(consulta[0][6])
            #   Aca hago el set de el nombre del asignado a por id
            self.comboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente.set(asignadoA)
            #   Pongo los datos de la tarea
            #   Primero titulo
            self.entradaTitulolabelFrameEdicionDeTareasDatosExistente.insert(0, titulo)
            #   Descripcion
            self.entradaDescripcionlabelFrameEdicionDeTareasDatosExistente.insert(
                0, descripcion.rstrip("\n")
            )
            #   Seteo la cadena al date_entry
            self.calendarioVencimientolabelFrameEdicionDeTareasDatosExistente.set_date(
                cadena_Fecha_formateada
            )
            nombreEstadoTareaPorId = self.conexion.obtenerNombreEstadoPorId(
                consulta[0][7]
            )
            #   Aca tengo que setear el nombre del estado de la tarea en base a su id
            self.comboboxEstadoslabelFrameEdicionDeTareasDatosExistente.set(
                nombreEstadoTareaPorId
            )

    def actualizarTarea(self):
        idAsignadoA = self.conexion.obtenerIdporNombreAsignadoa(
            self.datoComboboxAsignadoAlabelFrameEdicionDeTareasDatosExistente.get()
        )
        idEstado = self.conexion.obtenerIdporNombreEstado(
            self.datoComboboxEstadoslabelFrameEdicionDeTareasDatosExistente.get()
        )
        datos = (
            self.datoEntradaTitulolabelFrameEdicionDeTareasDatosExistente.get(),
            self.datoEntradaDescripcionlabelFrameEdicionDeTareasDatosExistente.get(),
            self.calendarioVencimientolabelFrameEdicionDeTareasDatosExistente.get(),
            self.idUsuarioLogueado,
            idAsignadoA[0][0],
            idEstado[0][0],
            self.datoEntradaCodigoLabelFrameEdicionDeTareas.get(),
        )
        self.conexion.actualizarTarea(datos)
        ms.showinfo("Hecho", "Tarea modificada")

    def consultarTareaPorId(self):
        resultado = self.conexion.obtenerTareaPorId(
            (self.datoEntradaCodigolabelFrameEliminarTareas.get(),)
        )
        if len(resultado) > 0:
            titulo = resultado[0][0]
            descripcion = resultado[0][1]
            asignadoa = resultado[0][2]
            self.datoEtiquetaTituloTarealabelFrameEliminarTareasListadoTareas.config(
                text=titulo
            )
            self.datoEtiquetaDescripcionTarealabelFrameEliminarTareasListadoTareas.config(
                text=descripcion
            )
            self.datoEtiquetaAsignadoAlabelFrameEliminarTareasListadoTareas.config(
                text=asignadoa
            )
            self.botonEliminarTarealabelFrameEliminarTareasListadoTareas.config(
                state="normal"
            )

        else:
            ms.showerror("Error", "No existe tarea con ese id")
            self.entradaCodigolabelFrameEliminarTareas.delete(0, END)
            self.botonEliminarTarealabelFrameEliminarTareasListadoTareas.config(
                state="disabled"
            )

    def eliminarTareas(self):
        self.conexion.eliminarTareaPorId(
            (self.datoEntradaCodigolabelFrameEliminarTareas.get(),)
        )
        ms.showinfo("Hecho", "Tarea eliminada")

    def pantallaUsuarioAdmin(self):
        self.ventanaPantallaAdmin = Toplevel()
        self.labelframeUsuarioAdmin = LabelFrame(
            self.ventanaPantallaAdmin, text="ABM-Usuarios"
        )
        self.labelframeUsuarioAdmin.grid(column=0, row=0, padx=10, pady=10)
        self.botonAltaUsuariolabelframeUsuarioAdmin = Button(
            self.labelframeUsuarioAdmin,
            text="Alta Usuario",
            command=self.pantallaRegistroUsuario,
        )
        self.botonAltaUsuariolabelframeUsuarioAdmin.grid(
            column=0, row=0, padx=10, pady=10
        )
        self.botonBajaUsuariolabelframeUsuarioAdmin = Button(
            self.labelframeUsuarioAdmin, text="Baja Usuario", command=self.bajaUsuario
        )
        self.botonBajaUsuariolabelframeUsuarioAdmin.grid(
            column=1, row=0, padx=10, pady=10
        )

        self.botonListadoUsuariolabelframeUsuarioAdmin = Button(
            self.labelframeUsuarioAdmin,
            text="Listado Usuario",
            command=self.listar_Usuario,
        )
        self.botonListadoUsuariolabelframeUsuarioAdmin.grid(
            column=0, row=1, padx=10, pady=10
        )

        self.botonModificacionUsuariolabelframeUsuarioAdmin = Button(
            self.labelframeUsuarioAdmin, text="Mod. Usuario"
        )
        self.botonModificacionUsuariolabelframeUsuarioAdmin.grid(
            column=1, row=1, padx=10, pady=10
        )

    def editar_Usuario(self):
        pass

    def listar_Usuario(self):
        self.ventanaListadoUsuarios = Toplevel()
        self.labelframeListadoUsuarios = LabelFrame(
            self.ventanaListadoUsuarios, text="Listado de Usuarios"
        )
        self.labelframeListadoUsuarios.grid(column=0, row=0, padx=10, pady=10)
        self.botonListarlabelframeListadoUsuarios = Button(
            self.labelframeListadoUsuarios,
            text="Listado de Usuario",
            command=self.insertarDatosListarUsuarios,
        )
        self.botonListarlabelframeListadoUsuarios.grid(
            column=0, row=0, padx=10, pady=10
        )
        self.treeviewlabelframeListadoUsuarios = ttk.Treeview(
            self.labelframeListadoUsuarios,
            columns=("Id", "Nombre", "Correo"),
            show="headings",
        )
        self.treeviewlabelframeListadoUsuarios.grid(column=0, row=1, padx=10, pady=10)
        self.treeviewlabelframeListadoUsuarios.heading("Id", text="Id")
        self.treeviewlabelframeListadoUsuarios.heading("Nombre", text="Nombre")
        self.treeviewlabelframeListadoUsuarios.heading("Correo", text="Correo")

    def modificar_Usuario(self):
        pass

    def insertarDatosListarUsuarios(self):
        resultados = self.conexion.mostrarListaUsuario()
        for items in self.treeviewlabelframeListadoUsuarios.get_children():
            self.treeviewlabelframeListadoUsuarios.delete(items)
        for id, nombre, email in resultados:
            self.treeviewlabelframeListadoUsuarios.insert(
                "", "end", values=f"{id} {nombre} {email}"
            )

    def bajaUsuario(self):
        self.ventanaBajaUsuario = Toplevel()
        self.labelframeBajaUsuario = LabelFrame(
            self.ventanaBajaUsuario, text="Listar usuarios"
        )
        self.labelframeBajaUsuario.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaCodigoUsuariolabelframeBajaUsuario = Label(
            self.labelframeBajaUsuario, text="Codigo"
        )
        self.etiquetaCodigoUsuariolabelframeBajaUsuario.grid(
            column=0, row=0, padx=10, pady=10
        )

        self.datoEntradaCodigoUsuariolabelframeBajaUsuario = StringVar()
        self.entradaCodigoUsuariolabelframeBajaUsuario = Entry(
            self.labelframeBajaUsuario,
            textvariable=self.datoEntradaCodigoUsuariolabelframeBajaUsuario,
        )
        self.entradaCodigoUsuariolabelframeBajaUsuario.grid(
            column=1, row=0, padx=10, pady=10
        )

        self.botonBuscarUsuarioCodigolabelframeBajaUsuario = Button(
            self.labelframeBajaUsuario,
            text="Buscar Usuario",
            command=self.buscarUsuarioPorCodigo,
        )
        self.botonBuscarUsuarioCodigolabelframeBajaUsuario.grid(
            column=1, row=1, padx=10, pady=10
        )

        #   nombre,correo,clave
        self.etiquetaNombrelabelframeBajaUsuario = Label(
            self.labelframeBajaUsuario, text="Nombre"
        )
        self.etiquetaNombrelabelframeBajaUsuario.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaNombrelabelframeBajaUsuario = StringVar()
        self.entradaNombrelabelframeBajaUsuario = Entry(
            self.labelframeBajaUsuario,
            textvariable=self.datoEntradaNombrelabelframeBajaUsuario,
        )
        self.entradaNombrelabelframeBajaUsuario.grid(column=1, row=2, padx=10, pady=10)

        self.etiquetaCorreolabelframeBajaUsuario = Label(
            self.labelframeBajaUsuario, text="Correo"
        )
        self.etiquetaCorreolabelframeBajaUsuario.grid(column=0, row=3, padx=10, pady=10)

        self.datoEntradaCorreolabelframeBajaUsuario = StringVar()
        self.entradaCorreolabelframeBajaUsuario = Entry(
            self.labelframeBajaUsuario,
            textvariable=self.datoEntradaCorreolabelframeBajaUsuario,
        )
        self.entradaCorreolabelframeBajaUsuario.grid(column=1, row=3, padx=10, pady=10)

        self.etiquetaClavelabelframeBajaUsuario = Label(
            self.labelframeBajaUsuario, text="Clave"
        )
        self.etiquetaClavelabelframeBajaUsuario.grid(column=0, row=4, padx=10, pady=10)

        self.datoEntradaClavelabelframeBajaUsuario = StringVar()
        self.entradaClavelabelframeBajaUsuario = Entry(
            self.labelframeBajaUsuario,
            textvariable=self.datoEntradaClavelabelframeBajaUsuario,
        )
        self.entradaClavelabelframeBajaUsuario.grid(column=1, row=4, padx=10, pady=10)
        self.botonEliminarUsuariolabelframeBajaUsuario = Button(
            self.labelframeBajaUsuario,
            text="Eliminar Usuario",
            command=self.eliminarUsuarioPorID,
        )
        self.botonEliminarUsuariolabelframeBajaUsuario.grid(
            column=1, row=5, padx=10, pady=10
        )

    def buscarUsuarioPorCodigo(self):
        "nombre,correo,clave"
        codigo = self.datoEntradaCodigoUsuariolabelframeBajaUsuario.get()
        resultado = self.conexion.mostrarDatosActualesUsuario((codigo,))
        if len(resultado) == 0:
            ms.showinfo(
                "Error", "No tenemos usuario con ese id. Busquelo en lista usuarios"
            )
        else:
            for nombre, correo, clave in resultado:
                self.entradaNombrelabelframeBajaUsuario.delete(0, END)
                self.entradaNombrelabelframeBajaUsuario.insert(0, nombre)
                self.entradaCorreolabelframeBajaUsuario.delete(0, END)
                self.entradaCorreolabelframeBajaUsuario.insert(0, correo)
                self.entradaClavelabelframeBajaUsuario.delete(0, END)
                self.entradaClavelabelframeBajaUsuario.insert(0, clave)

    def eliminarUsuarioPorID(self):
        if len(self.datoEntradaCodigoUsuariolabelframeBajaUsuario.get()) == 0:
            ms.showinfo("Error", "Revise el dato del codigo del usuario")
        else:
            self.conexion.eliminarUsuarioPorId(
                (self.datoEntradaCodigoUsuariolabelframeBajaUsuario.get(),)
            )
            ms.showinfo("Adios", "Eliminamos dicho usuario")
            self.entradaNombrelabelframeBajaUsuario.delete(0, END)
            self.entradaCorreolabelframeBajaUsuario.delete(0, END)
            self.entradaClavelabelframeBajaUsuario.delete(0, END)


aplicacion = acceso()
