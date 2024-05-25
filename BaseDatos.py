import sqlite3 
import os

class BaseDatos:
    """Clase para gestionar la base de datos
    """
    
    def __init__(self, nombreBaseDatos):
        """Se inicializa la clase Base de Datos

        Args:
            nombreBaseDatos (string): nombre de la base de datos.
        """
        self.nombreBaseDatos = nombreBaseDatos
    
    def crearBaseDatos(self):
        """Se  crea la base de datos
        """
        try:
            conn = sqlite3.connect(self.nombreBaseDatos) 
        except Exception as e:
            print('Error al crear la Base de datos: {}'.format(e))
            
    def verificarBaseDatosExiste(self):
        """Verifica la existencia de la base de datos

        Returns:
            bool: retorna verdadero si la base de datos existe, de lo contrario regresa false
        """
        if os.path.isfile(self.nombreBaseDatos):
            return True
        else:
            return False
    
    def crearTablas(self):
        """Crea las tablas necesarias en la base de datos
        
        Clientes: Contendrá informacion de los clientes
        Menu: Contendrá información de los productos del menú.
        Pedido: Contendrá información sobre los pedidos/ventas realizadas.
        """
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
        """Abre la conexion de la base de datos, con sqlite3. Si la conexion se establece correctamente, devuelve el objeto de la conexion,
        de otra forma, devuelve el mensaje de error al conectar con la BD
        """
        try:
            conexion = sqlite3.connect(self.nombreBaseDatos) 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))