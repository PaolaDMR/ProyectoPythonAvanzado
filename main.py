#PROYECTO DE PYTHON AVANZADO

#Clase Lunes - Miercoles 7:00pm
#Nombre: Paola Denisse Martinez Ramos
#Profesora: Suei Chong

from Clientes import Clientes
from Menu import Menu
from Pedido import Pedido
from BaseDatos import BaseDatos
import sqlite3

class Aplicacion:
    
    def __init__(self):
        
        """Se inicializan la instancia de la clase Aplicacion que incluyen las instancias de Clientes, Menu y Pedido
        """
        
        self.clientes = Clientes()
        self.menu = Menu()
        self.pedido = Pedido()
        self.iniciarAplicacion()
        
    
    def iniciarAplicacion(self):
        
        """Se inicia la aplicacion, muestra el menú principal para seleccionar una de las siguientes opciones: Pedidos, 
        Clientes y Menu. Cada una de ellas despliega un submenu que realiza sus propias funciones.
        """
        
        print("------------------------------------")
        print("Bienvenido al sistema de HappyBurger")
        print("------------------------------------")
        salir_programa = False
        while not salir_programa:
            print("Menú Principal")
            print(""" 
                1.- Pedidos
                2.- Clientes
                3.- Menu
                4.- Salir
                """)
            try:
                opcion = int(input("Indica una opción del menú: "))
                if opcion == 1:
                    self.menu_pedidos()
                elif opcion == 2:
                    self.menu_clientes()
                elif opcion == 3:
                    self.menu_productos()
                elif opcion == 4:
                    print("Salida del programa, hasta luego ")
                    salir_programa = True    
                else:
                    print("Opción no válida, por favor intenta de nuevo.")
                
            except ValueError:
                print("Entrada no válida, por favor ingresa un número.")
                
                
    def calcular_costo_producto(self):
        """
        Solicita el nombre del producto, el precio y las unidades,
        y calcula el costo total.
        """
        producto = input("Ingresa el nombre del producto: ")
        try:
            precio = float(input(f"Ingrese el precio de {producto}: "))
            unidades = int(input(f"Ingrese la cantidad de unidades de {producto}: "))
            total = precio * unidades
            print(f"El costo total para {unidades} unidades de {producto} a {precio:.2f} cada una es {total:.2f}.")
        except ValueError:
            print("Entrada no válida. Asegúrate de ingresar números para el precio y las unidades.")
            
            
            
    def menu_clientes(self):
        """
        Muestra el menu de clientes el cual, indica las opciones que se pueden realizar tanto para agregar, eliminar, actualizar y 
        mostrar los clientes.
        """
        print("Menú de Clientes")
        print(""" 
            1.- Agregar cliente
            2.- Eliminar cliente
            3.- Actualizar cliente
            4.- Mostrar clientes
            5.- Volver al menú principal
            """)
        try:
            opcion = int(input("Indica una opción del menú de clientes: "))
            if opcion == 1:
                self.agregar_cliente()
            elif opcion == 2:
                self.eliminar_cliente()
            elif opcion == 3:
                self.actualizar_cliente()
            elif opcion == 4:
                self.clientes.mostrar_clientes()
            elif opcion == 4:
                print("Volver al menú principal")
            else:
                print("Opción no válida, por favor intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")
            
            
    def agregar_cliente(self):
        """Metodo para solicitar los datos del cliente al usuario, que a su vez mandará los datos al metodo de agregar cliente de
        la instancia de clientes para agregarlo a la base de datos
        """
        clave = input("Ingrese la clave del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        direccion = input("Ingrese la dirección del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        self.clientes.agregar_cliente(clave, nombre, direccion, correo, telefono)

    def eliminar_cliente(self):
        """Metodo para solicitar la clave del cliente que se quiere eliminar que a su vez mandará la clave a la instancia de clientes para
        eliminarlo de la base de datos.
        """
        clave = input("Ingrese la clave del cliente a eliminar: ")
        self.clientes.eliminar_cliente(clave)

    def actualizar_cliente(self):
        """Metodo para solicitar los nuevos datos del cliente que se desea actualizar para que a su vez sea mandado a la funcion de 
        actualizar cliente para editarlo en la base de datos.
        """
        clave = input("Ingrese la clave del cliente a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del cliente (o presione Enter para dejarlo sin cambios): ")
        direccion = input("Ingrese la nueva dirección del cliente (o presione Enter para dejarlo sin cambios): ")
        correo = input("Ingrese el nuevo correo electrónico del cliente (o presione Enter para dejarlo sin cambios): ")
        telefono = input("Ingrese el nuevo teléfono del cliente (o presione Enter para dejarlo sin cambios): ")
        self.clientes.actualizar_cliente(clave, nombre, direccion, correo, telefono)



    def menu_productos(self):
        """
        Muestra el menu de productos el cual, indica las opciones que se pueden realizar tanto para agregar, eliminar, actualizar y 
        mostrar los productos.
        """
        print("Menú de Productos")
        print(""" 
            1.- Agregar Producto
            2.- Eliminar Producto
            3.- Actualizar Producto
            4.- Mostrar productos
            5.- Volver al menú principal
            """)
        try:
            opcion = int(input("Indica una opción del menú: "))
            if opcion == 1:
                self.agregar_producto()
            elif opcion == 2:
                self.eliminar_producto()
            elif opcion == 3:
                self.actualizar_producto()
            elif opcion == 4:
                self.menu.mostrar_productos()
            elif opcion == 5:
                print("Volver al menú principal")
            else:
                print("Opción no válida, por favor intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")
            
            
    def agregar_producto(self):
        """Metodo para solicitar los datos del producto al usuario, que a su vez mandará los datos al metodo de agregar producto de
        la instancia de productos para agregarlo a la base de datos
        """
        clave = input("Ingrese la clave del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = input("Ingrese el precio del producto: ")
        self.menu.agregar_producto(clave, nombre, precio)

    def eliminar_producto(self):
        """Metodo para solicitar la clave del producto que se quiere eliminar que a su vez mandará la clave 
        a la instancia de productos para eliminarlo de la base de datos.
        """
        clave = input("Ingrese la clave del producto a eliminar: ")
        self.menu.eliminar_producto(clave)

    def actualizar_producto(self):
        """Metodo para solicitar los nuevos datos del producto que se desea actualizar para que a su vez sea mandado a la funcion de 
        actualizar producto para editarlo en la base de datos.
        """
        clave = input("Ingrese la clave del producto a actualizar: ")
        nombre = input("Ingrese el nuevo nombre del producto (o presione Enter para dejarlo sin cambios): ")
        precio = input("Ingrese el precio nuevo del producto (o presione Enter para dejarlo sin cambios): ")
        self.menu.actualizar_producto(clave, nombre, precio)
        
        
        
        
        
    def menu_pedidos(self):
        """
        Muestra el menu de pedidos el cual, indica las opciones que se pueden realizar tanto para crear y 
        cancelar los pedidos.
        """
        print("Menú de Pedidos")
        print(""" 
            1.- Crear Pedido
            2.- Cancelar Pedido
            3.- Mostrar Pedidos
            4.- Volver al menú principal
            """)
        try:
            opcion = int(input("Indica una opción del menú: "))
            if opcion == 1:
                self.crear_pedido()
            elif opcion == 2:
                self.cancelar_pedido()
            elif opcion == 3:
                self.pedido.mostrar_pedidos()
            elif opcion == 4:
                print("Volver al menú principal")
            else:
                print("Opción no válida, por favor intenta de nuevo.")
        except ValueError:
            print("Entrada no válida, por favor ingresa un número.")
            
    def crear_pedido(self):
        """Metodo para solicitar la clave del cliente, la clave del producto y cantidad al usuario, 
        que a su vez mandará los datos al metodo de crear pedido de
        la instancia de pedidos para agregarlo a la base de datos
        """
        clave_cliente = input("Ingrese la clave del cliente: ")
        clave_producto = input("Ingrese la clave del producto: ")
        cantidad = int(input("Ingrese la cantidad: "))
        self.pedido.crear_pedido(clave_cliente, clave_producto, cantidad)

    def cancelar_pedido(self):
        """Metodo para ingresar la clave del pedido que se desea cancelar.
        """
        clave = input("Ingrese la clave del pedido a cancelar: ")
        self.pedido.cancelar_pedido(clave)

if __name__ == "__main__":
    sistema_inventario = Aplicacion()
