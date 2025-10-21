import sqlite3


class conexion:
    def abrir(self):
        try:
            mydb = sqlite3.connect("gestor_proyecto.db")
            return mydb
        except:
            print("Error al conectar a la db SQlite3")

    # def crear_tablas(self):
    #     try:
    #         conexion = self.abrir()
    #         mycursor = conexion.cursor()
    #         sql = "CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(100) NOT NULL,email VARCHAR(100) NOT NULL UNIQUE,contrasena VARCHAR(255) NOT NULL,fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
    #         mycursor.execute(sql)
    #         sql = "CREATE TABLE estados_tarea (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL UNIQUE)"
    #         mycursor.execute(sql)
    #         sql = "INSERT INTO estados_tarea (nombre) VALUES ('Pendiente'),('En Progreso'),('Completada'),('Cancelada')"
    #         mycursor.execute(sql)
    #         sql = "CREATE TABLE prioridades_tarea (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL UNIQUE)"
    #         mycursor.execute(sql)
    #         sql = "INSERT INTO prioridades_tarea (nombre) VALUES ('Baja'),('Media'),('Alta')"
    #         mycursor.execute(sql)
    #         sql = "CREATE TABLE tareas (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255) NOT NULL, descripcion TEXT, fecha_vencimiento DATE, fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, id_creador INT NOT NULL, id_asignado INT, id_estado INT NOT NULL, id_prioridad INT NOT NULL, FOREIGN KEY (id_creador) REFERENCES usuarios(id), FOREIGN KEY (id_asignado) REFERENCES usuarios(id), FOREIGN KEY (id_estado) REFERENCES estados_tarea(id),FOREIGN KEY (id_prioridad) REFERENCES prioridades_tarea(id))"
    #         mycursor.execute(sql)
    #         sql = "CREATE TABLE comentarios (id INT AUTO_INCREMENT PRIMARY KEY, id_tarea INT NOT NULL, id_usuario INT NOT NULL, comentario TEXT NOT NULL, fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (id_tarea) REFERENCES tareas(id), FOREIGN KEY (id_usuario) REFERENCES usuarios(id))"
    #         mycursor.execute(sql)
    #         conexion.commit()
    #     except sqlite3.OperationalError as er:
    #         print(f"{er}")
    #     finally:
    #         conexion.close()

    def consultarUsuario(self, datos):
        #   Uso try por si falla algo
        try:
            #   Llamo a la apertura de la conexion
            conexion = self.abrir()
            #   Genero un cursos de la conexion
            mycursor = conexion.cursor()
            #   Hago la consulta a la db(en realidad la sql que voy a usar)
            sql = "select * from usuarios where email=? and contrasena=?"
            #   Ahora si, corro la sentencia sql y uso los datos sobre la consulta
            mycursor.execute(sql, datos)
            #   Guardo los resultados en info
            info = mycursor.fetchall()
            #   devuelvo info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def registrarUsuario(self, datos):
        #   Registro un usuario en sistema
        try:
            #   Llamo a la apertura de la conexion
            conexion = self.abrir()
            #   Genero un cursos de la conexion
            mycursor = conexion.cursor()
            #   Hago el insert de los datos nombre,email y contrasena
            sql = "insert into usuarios(nombre,email,contrasena) values(?,?,?)"
            #   Ahora si, corro la sentencia sql y uso los datos sobre la consulta
            mycursor.execute(sql, datos)
            #   Hago los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarUsuarios(self):
        #   Consulta para traerme el listado de los usuarios existentes
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   genero el cursor
            mycursor = conexion.cursor()
            #   Elijo todos los nombres existentes en la tabla usuarios
            sql = "select nombre from usuarios"
            mycursor.execute(sql)
            #   Corro la consulta
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def correoExiste(self, dato):
        #   El campo email es unico. Con esto chequeo si existe un correo o no registrado
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero un cursor
            mycursor = conexion.cursor()
            #   Cuento cuantos email como los que me traigo existen en la db(no puede existir un correo repetido)
            mycursor.execute("select count(*) from usuarios where email=?", (dato,))
            #   Devuelvo el resultado
            info = mycursor.fetchall()
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerIdporNombreAsignadoa(self, datos):
        #   Busco el id del usuario por su nombre
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero un cursor
            mycursor = conexion.cursor()
            #   Hago la busqueda de los id en usuarios segun su nombre
            mycursor.execute("select id from usuarios where nombre=?", (datos,))
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerIdPorNombrePrioridad(self, datos):
        #   obtengo el id de la prioridad de la tarea en base a su nombre
        try:
            #   abro la conexion
            conexion = self.abrir()
            #   Genero un cursor
            mycursor = conexion.cursor()
            #   Busco los id segun el nombre de la prioridad
            mycursor.execute(
                "select id from prioridades_tarea where nombre=?", (datos,)
            )
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerIdporNombreEstado(self, datos):
        #   Obtengo el id de la tarea en base a su estado
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero un cursor
            mycursor = conexion.cursor()
            #   Traigo los id de estados_tarea en base a su nombre
            mycursor.execute("select id from estados_tarea where nombre=?", (datos,))
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def ingresarTareaNueva(self, datos):
        #   Creo la tarea en la db
        try:
            #   Llamo a la apertura de la conexion
            conexion = self.abrir()
            #   Genero un cursos de la conexion
            mycursor = conexion.cursor()
            #   El insert registra una tarea nueva
            sql = "insert into tareas(titulo,descripcion,fecha_vencimiento,id_creador,id_asignado,id_estado,id_prioridad) values(?,?,?,?,?,?,?)"
            #   Ahora si, corro la sentencia sql y uso los datos sobre la consulta
            mycursor.execute(sql, datos)
            #   Hago los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarEstados(self):
        #   Me traigo los nombres de las tareas segun su estado
        try:
            #   Genero la conexion
            conexion = self.abrir()
            #   El cursor
            mycursor = conexion.cursor()
            #   La consulta
            sql = "select nombre from estados_tarea"
            mycursor.execute(sql)
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarPrioridad(self):
        #   Me traigo los nombres de las prioridades
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero un cursor
            mycursor = conexion.cursor()
            #   Traigo los nombres de las prioridades_tarea
            sql = "select nombre from prioridades_tarea"
            mycursor.execute(sql)
            info = mycursor.fetchall()
            #   Regreso la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarTareasSegunDatos(self, datos):
        #   Aca uso el id_estado el id_prioridad y id_asignado para buscar las tareas(id,titulo)
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Hago la consulta
            sql = "select id,titulo from tareas where id_estado=? and id_prioridad=? and id_asignado=?"
            mycursor.execute(sql, datos)
            info = mycursor.fetchall()
            #   Retorno la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def buscarTareaendb(self, datos):
        #   Traigo la tarea en base al id de la misma
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Hago la consulta
            sql = "select * from tareas where id=?"
            mycursor.execute(sql, datos)
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerNombreAsignadoaporid(self, dato):
        #   Traigo el nombre del usuario en base a su id en usuarios
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco los nombres en base al id
            mycursor.execute("select nombre from usuarios where id=?", (dato,))
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerNombresEstados(self):
        #   Traigo nombre de los estados
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco los nombres en base al id
            mycursor.execute("select nombre from estados_tarea")
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerNombreEstadoPorId(self, dato):
        #   Traigo el nombre del usuario en base a su id en usuarios
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco los nombres en base al id
            mycursor.execute("select nombre from estados_tarea where id=?", (dato,))
            info = mycursor.fetchall()
            #   Devuelvo la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def actualizarTarea(self, datos):
        #   Traigo el nombre del usuario en base a su id en usuarios
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco los nombres en base al id
            mycursor.execute("update tareas set titulo=?, descripcion=?,fecha_vencimiento=?,id_creador=?,id_asignado=?,id_estado=? where id=?", datos)
            #   Ejecuto los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()

    def obtenerTareaPorId(self,datos):
        #   Traigo el nombre del usuario en base a su id en usuarios
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco Tarea por id
            mycursor.execute("select t.titulo,t.descripcion,u.nombre from tareas t left join usuarios u on t.id_asignado=u.id where t.id=?", datos)
            info = mycursor.fetchall()
            #   Retorno la info
            return info
        finally:
            #   Cierro la conexion
            conexion.close()

    def eliminarTareaPorId(self,datos):
        #   Traigo el nombre del usuario en base a su id en usuarios
        try:
            #   Abro la conexion
            conexion = self.abrir()
            #   Genero el cursor
            mycursor = conexion.cursor()
            #   Busco los nombres en base al id
            mycursor.execute("delete from tareas where id=?", datos)
            #   Ejecuto los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()
        pass