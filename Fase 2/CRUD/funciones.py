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
    1. Mostrar un registro
    2. Mostrar todos los registros
    3. Agregar un nuevo registro
    4. Modificar un registro
    5. Eliminar un registro
    6. Salir"""
        print (texto)

        opcion = get_int("Seleccione una opcion: ")

        if 0 < opcion < 7:
            return opcion 
        print("Opcion no valida, intente de nuevo")



def buscar_producto(productos:list, clave:int) -> int:
    for i in range (len(productos)):
        if productos[i].clave == clave:
            return i
    return -1