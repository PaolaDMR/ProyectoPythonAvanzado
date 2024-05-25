from BaseDatos import BaseDatos
import sqlite3

class Menu:
    
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
        
    def agregar_producto(self, clave, nombre, precio):
        """Metodo para agregar la información del producto a la base de datos.

        Args:
            clave (string): id del producto
            nombre (string): nombre del producto
            precio (float): precio unitario del producto
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                conexion.execute('''
                    INSERT INTO menu (clave, nombre, precio)
                    VALUES (?, ?, ?)
                ''', (clave, nombre, precio))
                conexion.commit()
                print("Producto agregado exitosamente:")
                print(f"Clave: {clave}")
                print(f"Nombre: {nombre}")
                print(f"Precio: {precio}")
            except Exception as e:
                print(f"Error al agregar producto: {e}")
            finally:
                conexion.close()

    def eliminar_producto(self, clave):
        """Metodo para eliminar un producto de la base de datos.

        Args:
            clave (string): id del producto
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('''
                    DELETE FROM menu WHERE clave = ?
                ''', (clave,))
                if cursor.rowcount > 0:
                    print("Producto eliminado exitosamente.")
                else:
                    print("El producto no existe.")
                conexion.commit()
            except Exception as e:
                print(f"Error al eliminar producto: {e}")
            finally:
                conexion.close()

    def actualizar_producto(self, clave, nombre=None, precio=None):
        """Metodo para editar la información de un producto en la base de datos.

        Args:
            clave (string): id del producto
            nombre (string, optional): nombre del producto. Defaults to None.
            precio (float, optional): precio del producto. Defaults to None.
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                if nombre:
                    conexion.execute('''
                        UPDATE menu SET nombre = ? WHERE clave = ?
                    ''', (nombre, clave))
                if precio:
                    conexion.execute('''
                        UPDATE menu SET precio = ? WHERE clave = ?
                    ''', (precio, clave))
                conexion.commit()
                print("Producto actualizado exitosamente.")
                print(f"Clave: {clave}")
                if nombre:
                    print(f"Nombre: {nombre}")
                if precio:
                    print(f"Precio: {precio}")
            except Exception as e:
                print(f"Error al actualizar producto: {e}")
            finally:
                conexion.close()
                
    
    def mostrar_productos(self):
        """Metodo para mostrar el listado de los productos existentes en la base de datos.
        """
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('SELECT clave, nombre, precio FROM menu')
                productos = cursor.fetchall()
                if productos:
                    print("Productos en el menú:")
                    for producto in productos:
                        print(f"Clave: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
                else:
                    print("No hay productos en el menú.")
            except Exception as e:
                print(f"Error al mostrar productos: {e}")
            finally:
                conexion.close()