from ObjetoCamion import camion
import sqlite3

class Servicio:
    def __init__(self,id, nombre, tAlmacenaje, placas, marca):
        self.id = id
        self.nombre = nombre
        self.tAlmacenaje = tAlmacenaje
        self.placas = placas
        self.marca = marca

        conn = sqlite3.connect('refaccionaria.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Camion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre TEXT,
                Totalmacenaje TEXT,
                Placas TEXT,
                Marca TEXT
            )
        ''')

        conn.commit()
        conn.close()

    def SolicitarInserccion(self):
        camionInsertado = camion(id=None,nombre=self.nombre, tAlmacenaje=self.tAlmacenaje, placas=self.placas, marca=self.marca)
        camionInsertado.insertarCamiones()

    def SolicitarBusqueda(self):
        camionesSolicitados = camion.devolverCamiones()
        return camionesSolicitados

    def SolicitarBusquedaIndividual(self, nombre):
        camionBuscado = camion.DevolverUnCamion(nombre_solicitado=nombre)
        return camionBuscado
    