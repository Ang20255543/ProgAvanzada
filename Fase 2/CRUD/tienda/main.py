from clases import Producto
from funciones import *
productos = list()


productos.append(Producto(123, "Laptop", "Dell", 300))
productos.append(Producto(124, "PC", "Asus", 400))
productos.append(Producto(125, "Mouse", "Dell", 50))
productos.append(Producto(126, "Laptop", "Lenovo", 250))
productos.append(Producto(127, "Teclado", "Apple", 70))

registrar_productos(productos)
guardar_csv(productos)
guardar_json(productos)
