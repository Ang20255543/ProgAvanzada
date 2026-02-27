from clases import *
import re

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