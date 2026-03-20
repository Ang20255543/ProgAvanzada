from clases import *
import re, locale
from datetime import date

locale.setlocale(locale.LC_ALL, "es_MX")

# Validar que el codigo tenga el formato XX-00, donde X es una letra mayuscula y 0 es un numero (esto es de la clase de transporte)

def validar_codigo() -> str:
    while True:
        codigo = input("Codigo:").upper()
        if re.match("^[A-Z]{2}-\d{2}$", codigo):
            return codigo
        print("Codigo no valido, debe tener el formato: XX-00")


def get_int(s:str) -> int:
    while True:
        num = input(f"{s}")
        try:
            num = int(num)
            return num
        except ValueError:
            print("Valor no valido, ingrese un numero entero")


# Validar que el nombre solo contenga letras y un espacio opcional entre dos palabras (esto es de la calse de empleados)

def validar_ID(s:str) -> str:
    while True:
        ID = input(f"{s}").upper()
        if re.match("^[A-Z]{2}\d{4}$", ID):
            return ID
        print("Valor no valido, ingrese un ID con el formato: XX0000")


def validar_nombre(s:str) -> str:
    while True:
        nombre = input(f"{s}")
        if re.match("^[a-zA-Z]{2,20}( [a-zA-Z]{2,20})?$", nombre):
            return nombre
        print("Valor no valido, ingrese solo letras")


def validar_apellido(s:str) -> str:
    while True:
        apellido = input(f"{s}")
        if re.match("^[a-zA-Z]{2,20}( [a-zA-Z]{2,20})?$", apellido):
            return apellido
        print("Valor no valido, ingrese solo letras")


def validar_fecha(s:str) -> str:
    while True:
        fecha = input(f"{s}")
        if re.match("^\d{2}/\d{2}/\d{4}$", fecha):
            return fecha
        print("Valor no valido, ingrese una fecha con el formato: dd/mm/yyyy")


#Funciones para listas
def regisrar(c: list) -> None:
    codigo = validar_codigo()
    marca = input("Marca: ").upper()
    modelo = get_int("Modelo: ")
    c.append(Transporte(codigo, marca, modelo, 0))

def buscar(valor, lista) -> int:
    for idx in range(len(lista)):
        if lista[idx].codigo == valor:
            return idx
    return -1


#Funcion para menu 
def menu() -> int:
    while True:
        print("1. Registrar camion")
        print("2. Flete del camion")
        print("3. Eliminar un camion")
        print("4. Salir")
        opcion = get_int("Ingrese una opcion: ")

        if opcion in [1, 2, 3, 4]:
            return opcion
        print("Opcion no valida, ingrese una opcion del 1 al 4")

def leer_fecha(s: str) -> date:
    while True:
        fecha = input(f"Ingrese {s} en formato DD-MM-AAAA: ")
        try:
            fecha = date.strptime(fecha, "%d-%m-%Y")
            return fecha
        except ValueError as e:
            print("Fecha no válida. Intente nuevamente, ERROR: ", e)

fecha = leer_fecha("Fecha de vencimiento")
print(fecha.strftime("%A %d de %B de %Y.").capitalize())