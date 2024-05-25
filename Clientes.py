
from BaseDatos import BaseDatos
import sqlite3

class Clientes:
    
    baseDatos = None
    
    def __init__(self):
        """Configuracion de la base de datos del inventario. Si la base de datos
        ya existe, abre la conexión existente. Si no existe, crea una nueva base de datos y las tablas
        necesarias.
        """
        self.baseDatos = BaseDatos('inventario.db')
        
        if self.baseDatos.verificarBaseDatosExiste():
            self.baseDatos.abrirConexion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablas()
            
    def abrirConexion(self):
        """Abre la conexion de la base de datos, con sqlite3. Si la conexion se establece correctamente, devuelve el objeto de la conexion,
        de otra forma, devuelve el mensaje de error al conectar con la BD
        """
        try:
            conexion = sqlite3.connect(self.baseDatos)
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))
            return None
    
    def agregar_cliente(self,  clave, nombre, direccion, correo, telefono):
        """Metodo para agregar la información de un nuevo cliente a la base de datos

        Args:
            clave (string): id del cliente
            nombre (string): nombre del cliente
            direccion (string): direccion del cliente
            correo (string): correo del cliente
            telefono (string): telefono del cliente
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                conexion.execute('''
                    INSERT INTO clientes (clave, nombre, direccion, correo_electronico, telefono)
                    VALUES (?, ?, ?, ?, ?)
                ''', (clave, nombre, direccion, correo, telefono))
                conexion.commit()
                print("Producto agregado exitosamente:")
                print(f"Clave: {clave}")
                print(f"Nombre: {nombre}")
                print(f"Dirección: {direccion}")
                print(f"Correo electrónico: {correo}")
                print(f"Teléfono: {telefono}")
            except Exception as e:
                print(f"Error al agregar cliente: {e}")
            finally:
                conexion.close()
        
    def eliminar_cliente(self, clave):
        """Metodo para eliminar un cliente de la base de datos

        Args:
            clave (string): id del cliente
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('''
                    DELETE FROM clientes WHERE clave = ?
                ''', (clave,))
                if cursor.rowcount > 0:
                    print("Cliente eliminado exitosamente.")
                else:
                    print("El cliente no existe.")
                conexion.commit()
            except Exception as e:
                print(f"Error al eliminar el cliente: {e}")
            finally:
                conexion.close()
            
    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo=None, telefono=None):
        """Metodo para actualizar la información de un cliente existente en la base de datos.

        Args:
            clave (string): id del cliente
            nombre (string, optional): nombre del cliente. Defaults to None.
            direccion (string, optional): direccion del cliente. Defaults to None.
            correo (string, optional): correo del cliente. Defaults to None.
            telefono (string, optional): telefono del cliente. Defaults to None.
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                if nombre:
                    conexion.execute('''
                        UPDATE clientes SET nombre = ? WHERE clave = ?
                    ''', (nombre, clave))
                if direccion:
                    conexion.execute('''
                        UPDATE clientes SET direccion = ? WHERE clave = ?
                    ''', (direccion, clave))
                if correo:
                    conexion.execute('''
                        UPDATE clientes SET correo_electronico = ? WHERE clave = ?
                    ''', (correo, clave))
                if telefono:
                    conexion.execute('''
                        UPDATE clientes SET telefono = ? WHERE clave = ?
                    ''', (telefono, clave))
                conexion.commit()
                print("Cliente actualizado exitosamente.")
                print(f"Clave: {clave}")
                if nombre:
                    print(f"Nombre: {nombre}")
                if direccion:
                    print(f"Direccion: {direccion}")
                if correo:
                    print(f"Correo: {correo}")
                if telefono:
                    print(f"Telefono: {telefono}")
            except Exception as e:
                print(f"Error al actualizar Cliente: {e}")
            finally:
                conexion.close()
    
    def mostrar_clientes(self):
        """Metodo para mostrar los clientes registrados en la base de datos
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('SELECT clave, nombre, direccion, correo_electronico, telefono FROM clientes')
                clientes = cursor.fetchall()
                if clientes:
                    print("Listado de Clientes:")
                    for cliente in clientes:
                        print(f"Clave: {cliente[0]}, Nombre: {cliente[1]}, Direccion: {cliente[2]}, Correo: {cliente[3]}, , Telefono: {cliente[4]}")
                else:
                    print("No hay clientes para mostrar.")
            except Exception as e:
                print(f"Error al mostrar clientes: {e}")
            finally:
                conexion.close()