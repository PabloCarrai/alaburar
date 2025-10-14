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
        #   Uso try por si falla algo
        try:
            #   Llamo a la apertura de la conexion
            conexion = self.abrir()
            #   Genero un cursos de la conexion
            mycursor = conexion.cursor()
            #   Hago la consulta a la db(en realidad la sql que voy a usar)
            sql = "insert into usuarios(nombre,email,contrasena) values(?,?,?)"
            #   Ahora si, corro la sentencia sql y uso los datos sobre la consulta
            mycursor.execute(sql, datos)
            #   Hago los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarUsuarios(self):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            sql = "select nombre from usuarios"
            mycursor.execute(sql)
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()

    def correoExiste(self, dato):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            mycursor.execute("select count(*) from usuarios where email=?", (dato,))
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()

    def listarPrioridades(self):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            sql = "select nombre from prioridades_tarea"
            mycursor.execute(sql)
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()

    def obtenerIdporNombreAsignadoa(self, datos):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            mycursor.execute("select id from usuarios where nombre=?", (datos,))
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()

    def obtenerIdPorNombrePrioridad(self, datos):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            mycursor.execute(
                "select id from prioridades_tarea where nombre=?", (datos,)
            )
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()

    def ingresarTareaNueva(self, datos):
        #   Uso try por si falla algo
        try:
            #   Llamo a la apertura de la conexion
            conexion = self.abrir()
            #   Genero un cursos de la conexion
            mycursor = conexion.cursor()

            sql = "insert into tareas(titulo,descripcion,fecha_vencimiento,id_creador,id_asignado,id_estado,id_prioridad) values(?,?,?,?,?,?,?)"
            #   Ahora si, corro la sentencia sql y uso los datos sobre la consulta
            mycursor.execute(sql, datos)
            #   Hago los cambios
            conexion.commit()
        finally:
            #   Cierro la conexion
            conexion.close()

    def listarEstados(self):
        #   Uso try por si falla algo
        try:
            conexion = self.abrir()
            mycursor = conexion.cursor()
            sql = "select nombre from estados_tarea"
            mycursor.execute(sql)
            info = mycursor.fetchall()
            return info
        finally:
            conexion.close()
