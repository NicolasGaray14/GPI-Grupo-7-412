import mysql.connector #pip install mysql-connector-python

class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión a MySQL establecida.")
        except mysql.connector.Error as err:
            print(f"Error al conectarse a MySQL: {err}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexión a MySQL cerrada.")

    def execute_query(self, query, values=None):
        if self.connection:
            cursor = self.connection.cursor()
            try:
                if values:
                    cursor.execute(query, values)
                else:
                    cursor.execute(query)
                self.connection.commit()
                print("Consulta ejecutada con éxito.")
            except mysql.connector.Error as err:
                print(f"Error al ejecutar la consulta: {err}")
            finally:
                cursor.close()
        else:
            print("No hay conexión a MySQL.")

# Ejemplo de uso
if __name__ == "__main__":
    connection = MySQLConnection(
        host="localhost",
        user="Gustavo",
        password="fldsmdfr",
        database="tu_base_de_datos"
    )

    connection.connect()
    
    # Crear un cursor para ejecutar comandos SQL
    cursor = connection.cursor()

    # Ejemplo de inserción de datos
    insert_query = "INSERT INTO mi_tabla (nombre, edad) VALUES (%s, %s)"
    valores = ("Juan", 30)
    cursor.execute(insert_query, valores)

    # Confirmar los cambios en la base de datos (importante para inserciones, actualizaciones o eliminaciones)
    connection.commit()

    # Ejemplo de selección de datos
    select_query = "SELECT * FROM mi_tabla"
    cursor.execute(select_query)
    resultados = cursor.fetchall()

    for resultado in resultados:
        print(resultado)

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()
        
    connection.disconnect()