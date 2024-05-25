import sqlite3 
import os

class BaseDatos:
    
    def __init__(self, nombreBaseDatos):
        self.nombreBaseDatos = nombreBaseDatos
    
    def crearBaseDatos(self):
        try:
            conn = sqlite3.connect(self.nombreBaseDatos) 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))
            
    def verificarBaseDatosExiste(self):
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False
    
    def crearTablas(self):
        conexion = self.abrirConexion()

        # conexion.execute('''CREATE TABLE productos
        #         (id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         nombre_producto TEXT NOT NULL,
        #         descripcion TEXT NOT NULL,
        #         precio FLOAT NOT NULL,
        #         stock INTEGER NOT NULL
        #         );''')
        
        conexion.execute('''CREATE TABLE IF NOT EXISTS clientes
                (clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                correo_electronico TEXT NOT NULL,
                telefono TEXT NOT NULL
                );''')

        conexion.execute('''CREATE TABLE IF NOT EXISTS menu
                (clave TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                precio FLOAT NOT NULL
                );''')

        conexion.execute('''CREATE TABLE IF NOT EXISTS pedido
                (pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                producto TEXT NOT NULL,
                precio FLOAT NOT NULL,
                FOREIGN KEY (cliente) REFERENCES clientes(clave),
                FOREIGN KEY (producto) REFERENCES menu(clave)
                );''')
        
        conexion.close()
    
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))