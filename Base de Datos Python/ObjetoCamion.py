from ObjetoAbstracto import vehiculo
import sqlite3

class camion(vehiculo):
    def __init__(self, id, nombre, tAlmacenaje, placas, marca):
        self.id = id
        self.nombre = nombre
        self.tAlmacenaje = tAlmacenaje
        self.placas = placas
        self.marca = marca

    def insertarCamiones(self):
        # Cambiando la conexión a SQLite3
        connection = sqlite3.connect('refaccionaria.db')  # Nombre de la base de datos SQLite
        cursor = connection.cursor()
        sql_insert = "INSERT INTO Camion (Nombre, Totalmacenaje, Placas, Marca) VALUES (?, ?, ?, ?)"
        values = (self.nombre, self.tAlmacenaje, self.placas, self.marca)
        cursor.execute(sql_insert, values)
        connection.commit()

        # Cerrar la conexión
        cursor.close()
        connection.close()

    @classmethod
    def devolverCamiones(cls):
        # Cambiando la conexión a SQLite3
        connection = sqlite3.connect('refaccionaria.db')  # Nombre de la base de datos SQLite
        cursor = connection.cursor()
        query = "SELECT * FROM Camion"
        cursor.execute(query)
        camiones = cursor.fetchall()

        # Crear instancias de camion con los datos obtenidos
        camiones_instancias = [cls(*camion_datos) for camion_datos in camiones]
        return camiones_instancias

    @classmethod
    def DevolverUnCamion(cls, nombre_solicitado):
        # Cambiando la conexión a SQLite3
        connection = sqlite3.connect('refaccionaria.db')  # Nombre de la base de datos SQLite
        cursor = connection.cursor()
        query = "SELECT * FROM Camion WHERE Nombre = ?"
        cursor.execute(query, (nombre_solicitado,))
        camionsito = cursor.fetchone()

        if camionsito:
            return cls(*camionsito)
        else:
            print("No se encontró el camion solicitado")
          