from decouple import config
import mysql.connector


class gestordb:
    def abrirconexion(self):
        try:
            mydb = mysql.connector.connect(
                host=config("MYSQL_HOST"),
                user=config("MYSQL_USER"),
                password=config("MYSQL_PASSWORD"),
                port=config("MYSQL_PORT"),
                database=config("MYSQL_DATABASE"),
            )
            return mydb
        except mysql.connector.Error as error:
            print(error)

    def consultarUsuario(self, datos):
        conexion = self.abrirconexion()
        mycursor = conexion.cursor()
        sql = "select * from usuarios where nombre=%s"
        mycursor.execute(sql, datos)
        return mycursor
        conexion.close()

    def insertarUsuario(self, datos):
        conexion = self.abrirconexion()
        mycursor = conexion.cursor()
        sql = "insert into usuarios(nombre,email,contrasena) values(%s,%s,%s)"
        mycursor.execute(sql, datos)
        conexion.commit()
        conexion.close()

    def consultarId(self, datos):
        conexion = self.abrirconexion()
        mycursor = conexion.cursor()
        sql = "select nombre from usuarios where nombre=%s"
        mycursor.execute(sql, datos)
        return mycursor
        conexion.close()
