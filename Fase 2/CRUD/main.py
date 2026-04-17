from clases import Producto
from funciones import *
productos = list()

productos.append(Producto(123, "Laptop", "Dell", 300))
productos.append(Producto(124, "PC", "Asus", 400))
productos.append(Producto(125, "Mouse", "Dell", 50))
productos.append(Producto(126, "Laptop", "Lenovo", 250))
productos.append(Producto(127, "Teclado", "Apple", 70))


indice = buscar_producto(productos, 123)
print(productos[indice])


"""
while True: 
    opcion = menu()

    if opcion == 1:
        #Llamar a funcion para un registro
        pass
    elif opcion == 2:
        #Llamar a funcion para mostrar todos los registros
        pass
    elif opcion == 3:
        #Llamar a funcion para agregar un nuevo registro
        pass
    elif opcion == 4:
        #Llamar a funcion para modificar un registro
        pass
    elif opcion == 5:
        #Llamar a funcion para eliminar un registro
        pass
    elif opcion == 6:
        print("Saliendo del programa...")
        break """