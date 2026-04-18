from clases import Producto
from funciones import *
productos = list()


productos.append(Producto(123, "Laptop", "Dell", 300))

productos.append(Producto(124, "PC", "Asus", 400))
productos.append(Producto(125, "Mouse", "Dell", 50))
productos.append(Producto(126, "Laptop", "Lenovo", 250))
productos.append(Producto(127, "Teclado", "Apple", 70))


while True: 
    opcion = menu()

    if opcion == 1:
        #Llamar a funcion para mostrar un registro
        mostrar_producto(productos)
    elif opcion == 2:
        #Llamar a funcion para mostrar todos los registros
        mostrar_productos(productos)
    elif opcion == 3:
        #Llamar a funcion para agregar un nuevo registro
        registrar_productos(productos)
    elif opcion == 4:
        #Llamar a funcion para modificar un registro
        modificar_producto(productos)
    elif opcion == 5:
        #Llamar a funcion para eliminar un registro
        eliminar_producto(productos)
    elif opcion == 6:
        print("Saliendo del programa...")
        break
