import tkinter as tk
from Servicios import Servicio
from tkinter import ttk

#Configuraciones de la ventana prinsipal
ventana = tk.Tk()
ventana.title("Servicio de camiones")
ventana.attributes("-fullscreen", True)

#Funciones llamadas desde antes para evitar conflictos de referencias

def crearInstancia():
    nombre = entradaNombre.get()
    tAlmacenamineto = entradaTAlmacenaje.get()
    placa = entradaPlaca.get()
    marca = entradaMarca.get()
    nuevoCamion = Servicio(None,nombre, tAlmacenamineto, placa, marca)
    nuevoCamion.SolicitarInserccion()
    etiquetaDeSalida.config(text = f"Has insertado a: {nuevoCamion.nombre}")
    TraerATodosLosDatos()
    
def TraerATodosLosDatos():
    camionesRecolectados = Servicio(None, None, None,None,None)
    camiones_obtenidos = camionesRecolectados.SolicitarBusqueda()
    
    tableView.delete(*tableView.get_children())

    for camion_obtenido in camiones_obtenidos:
        tableView.insert("", "end", values=(camion_obtenido.id, camion_obtenido.nombre, camion_obtenido.tAlmacenaje, camion_obtenido.placas, camion_obtenido.marca))
def TraerUnSoloDato():
    nombreCamion = entradaDeBusqueda.get()
    camionRecolectado = Servicio(None,None,None,None,None)
    camionObtenido = camionRecolectado.SolicitarBusquedaIndividual(nombreCamion)
    tableView.delete(*tableView.get_children())
    tableView.insert("", "end", values=(camionObtenido.id, camionObtenido.nombre, camionObtenido.tAlmacenaje, camionObtenido.placas, camionObtenido.marca))
def CerrarPrograma():
    ventana.destroy()
    
#La etiqueta de instrucciónes

etiquetaBinevenida = tk.Label(ventana, text="Hola bienvenido al servicio de camiones", font="Monserrath 20 bold")
etiquetaBinevenida.place(x=50, y=50)

etiquetaNombre = tk.Label(ventana, text="Nombre", font= "Arial 14 bold")
etiquetaNombre.place(x=50, y=150)

etiquetaEdad = tk.Label(ventana, text="Total de almacenamiento ", font= "Arial 14 bold")
etiquetaEdad.place(x=50, y=250)

etiquetaPlacas = tk.Label(ventana, text="Placas", font="Arial 14 bold")
etiquetaPlacas.place(x=50, y=350)

etiquetaMarca = tk.Label(ventana, text="Marca", font="Arial 14 bold")
etiquetaMarca.place(x=50, y=450)

etiquetaBuscar = tk.Label(ventana, text="Busca con el nombre", font="Monserrath 14 bold")
etiquetaBuscar.place(x=1100, y=150)

#Entradas de información

entradaNombre = tk.Entry(ventana)
entradaNombre.place(x=50, y=200)

entradaTAlmacenaje = tk.Entry(ventana)
entradaTAlmacenaje.place(x=50, y=300)

entradaPlaca = tk.Entry(ventana)
entradaPlaca.place(x=50, y=400)

entradaMarca = tk.Entry(ventana)
entradaMarca.place(x=50, y=500)

entradaDeBusqueda = tk.Entry(ventana)
entradaDeBusqueda.place(x=1100, y=200)

#Boton de crear instancia de una persona

botonCrearInstacia = tk.Button(ventana, text="Crear usuario", command=crearInstancia)
botonCrearInstacia.place(x=50, y=600)

botonTraerTodolosDatos = tk.Button(ventana, text="Mostrar todos los datos", command=TraerATodosLosDatos)
botonTraerTodolosDatos.place(x=400, y=700)

botonCerrarPrograma = tk.Button(ventana, text="Salir del programa", command=CerrarPrograma)
botonCerrarPrograma.place(x=900, y=700)

botonTraerUnDato = tk.Button(ventana, text="Buscar registro",command=TraerUnSoloDato)
botonTraerUnDato.place(x=1100, y=250)

#Mostrar el nuevo usuario credo :)

etiquetaDeSalida = tk.Label(ventana, font="Monserrath 14 bold")
etiquetaDeSalida.place(x=50, y=700)

#Creacion de la tablas vista
columnas = ("Id","Nombre", "Total Almacenamiento", "Placas", "Marca")
tableView = ttk.Treeview(ventana, columns=columnas, show="headings")
# Configurar las columnas
for col in columnas:
    tableView.heading(col, text=col)
    tableView.column(col, anchor="center", width=150)

# Ubicar el Treeview
tableView.place(x=300, y=150)

ventana.mainloop()