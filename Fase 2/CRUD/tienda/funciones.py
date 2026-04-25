from clases import Producto

## Funciones para validar entradas de datos para ingresar numeros enteros
def get_int(s:str) -> int:
    while True:
        num = input(f"{s}")
        try:
            num = int(num)
            return num
        except ValueError:
            print("Valor no valido, ingrese un numero entero")


## Funciones para validar entradas de datos para ingresar numeros decimales
def get_float(s:str) -> float:
    while True:
        num = input(f"{s}")
        try:
            num = float(num)
            return num
        except ValueError:
            print("Valor no valido, ingrese un numero decimal")


## Funciones para mostrar el menu de opciones
def menu() -> int:
    while True:
        texto = """Seleccione una opcion:
    1. Mostrar un producto
    2. Mostrar todos los productos
    3. Agregar un nuevo producto
    4. Modificar un producto
    5. Eliminar un producto
    6. Salir"""
        print (texto)

        num = get_int("Seleccione una opcion:")

        if 0 < num < 7:
            return num 
print("Opcion no valida, intente de nuevo")


##Funciones para realizar las operaciones CRUD  
##Funcion para buscar un producto por su clave, regresa el indice del producto en la lista o -1 si no lo encuentra
def buscar_producto(productos:list, clave:int) -> int:
    for i in range (len(productos)):
        if productos[i].clave == clave:
            return i
    return -1


##Funcion para mostrar un producto por su clave
def mostrar_producto(productos:list) -> None:
    clave = get_int("Ingrese la clave del producto a mostrar: ")
    indice = buscar_producto(productos, clave)

    if indice == -1:
        print("Producto no encontrado")
        return

    print(productos[indice])


##Funcion para mostrar todos los productos
def mostrar_productos(productos:Producto) -> None:
    print(f"{'CLAVE': <10} {'NOMBRE': <20} {'MARCA': <15}  {'PRECIO': >11}  {'EXISTENCIA': >12}")
    for p in list(productos):
        precio= f"${p.precio: >10.2f}"
        print(f"{p.clave: <10} {p.nombre: <20} {p.marca: <15}  {precio}  {p.existencia: >12}")

    print(productos)


##Funcion para registrar un nuevo producto, valida que la clave no exista antes de agregarlo a la lista
def registrar_productos(productos:list) -> None:
    while True:
        clave = get_int("Ingrese la clave del producto: ")
        if buscar_producto(productos, clave) > -1:
            print("La clave ya existe, ingrese una clave diferente")
        else:
         nombre = input("Ingrese el nombre del producto: ")
         marca = input("Ingrese la marca del producto: ")
         precio = get_float("Ingrese el precio del producto: ")
         existencia = get_int("Ingrese la existencia del producto: ")

         productos.append(Producto(clave, nombre, marca, precio, existencia))
         return


##Funcion para modificar un producto, valida que la clave exista antes de modificarlo
def modificar_producto(productos:list) -> None:
    clave = get_int("Ingrese la clave del producto a modificar: ")
    indice = buscar_producto(productos, clave)

    if indice == -1:
        print("Producto no encontrado")
        return

    nombre = input("Ingrese el nuevo nombre del producto: ")
    marca = input("Ingrese la nueva marca del producto: ")
    precio = get_float("Ingrese el nuevo precio del producto: ")
    existencia = get_int("Ingrese la nueva existencia del producto: ")

    productos[indice].nombre = nombre
    productos[indice].marca = marca
    productos[indice].precio = precio
    productos[indice].existencia = existencia


##Funcion para eliminar un producto, valida que la clave exista antes de eliminarlo
def eliminar_producto(productos:list) -> None:
    clave = get_int("Ingrese la clave del producto a eliminar: ")
    indice = buscar_producto(productos, clave)

    if indice == -1:
        print("Producto no encontrado")
        return

    productos.pop(indice)