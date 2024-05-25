

from BaseDatos import BaseDatos
import sqlite3

class Pedido:
    
    baseDatos = None
    
    def __init__(self):
        self.baseDatos = BaseDatos('inventario.db')
        
        if self.baseDatos.verificarBaseDatosExiste():
            self.baseDatos.abrirConexion()
        else:
            self.baseDatos.crearBaseDatos()
            self.baseDatos.crearTablas()
            
    def abrirConexion(self):
        try:
            conexion = sqlite3.connect(self.baseDatos)
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))
            return None
    
    def crear_pedido(self, clave_cliente, clave_producto, cantidad):
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                # Obtener información del producto
                cursor_producto = conexion.execute('''
                    SELECT nombre, precio FROM menu WHERE clave = ?
                ''', (clave_producto,))
                producto_info = cursor_producto.fetchone()

                # Obtener información del cliente
                cursor_cliente = conexion.execute('''
                    SELECT nombre FROM clientes WHERE clave = ?
                ''', (clave_cliente,))
                cliente_info = cursor_cliente.fetchone()

                if producto_info and cliente_info:
                    nombre_producto, precio_unitario = producto_info
                    nombre_cliente = cliente_info[0]
                    precio_total = precio_unitario * cantidad

                    conexion.execute('''
                        INSERT INTO pedido (cliente, producto, precio)
                        VALUES (?, ?, ?)
                    ''', (nombre_cliente, nombre_producto, precio_total))
                    conexion.commit()

                    print("Pedido creado exitosamente:")
                    print(f"Cliente: {nombre_cliente}")
                    print(f"Producto: {nombre_producto}")
                    print(f"Cantidad: {cantidad}")
                    print(f"Precio unitario: {precio_unitario}")
                    print(f"Precio total: {precio_total}")

                    self.imprimir_ticket(nombre_cliente, nombre_producto, cantidad, precio_unitario, precio_total)
                else:
                    if not producto_info:
                        print("El producto no existe.")
                    if not cliente_info:
                        print("El cliente no existe.")
            except Exception as e:
                print(f"Error al crear pedido: {e}")
            finally:
                conexion.close()

    def cancelar_pedido(self, clave):
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('''
                    DELETE FROM pedido WHERE id = ?
                ''', (clave,))
                if cursor.rowcount > 0:
                    print("Pedido cancelado exitosamente.")
                else:
                    print("El pedido no existe.")
                conexion.commit()
            except Exception as e:
                print(f"Error al cancelar pedido: {e}")
            finally:
                conexion.close()
                
    def mostrar_pedidos(self):
        conexion = self.baseDatos.abrirConexion()
        if conexion:
            try:
                cursor = conexion.execute('''
                    SELECT p.id, c.nombre AS cliente, m.nombre AS producto, m.precio, p.precio AS precio_total
                    FROM pedido p
                    INNER JOIN clientes c ON p.cliente = c.nombre
                    INNER JOIN menu m ON p.producto = m.nombre
                ''')
                pedidos = cursor.fetchall()

                if pedidos:
                    print("\n--- Lista de Pedidos ---")
                    for pedido in pedidos:
                        pedido_id, cliente, producto, precio_unitario, precio_total = pedido
                        print(f"ID del Pedido: {pedido_id}")
                        print(f"Cliente: {cliente}")
                        print(f"Producto: {producto}")
                        print(f"Precio unitario: {precio_unitario}")
                        print(f"Precio total: {precio_total}")
                        print("-----------------------")
                else:
                    print("No hay pedidos registrados.")
            except Exception as e:
                print(f"Error al mostrar pedidos: {e}")
            finally:
                conexion.close()

    def imprimir_ticket(self, cliente, producto, cantidad, precio_unitario, precio_total):
        ticket = (
            "\n--- Ticket de Venta ---\n"
            f"Cliente: {cliente}\n"
            f"Producto: {producto}\n"
            f"Cantidad: {cantidad}\n"
            f"Precio unitario: {precio_unitario}\n"
            f"Precio total: {precio_total}\n"
            "-----------------------\n"
        )
        
        print(ticket)
        """Generar el archivo de texto del ticket
        """
        try:
            with open('ticket.txt', 'w') as file:
                file.write(ticket)
            print("El ticket ha sido guardado en 'ticket.txt'.")
        except Exception as e:
            print(f"Error al guardar el ticket: {e}")