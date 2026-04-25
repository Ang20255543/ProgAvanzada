from operator import attrgetter
from clases_apellido import persona     

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




def menu() -> int:
    while True:
        texto = """Como desea ordenar?
    [1] Por apellido
    [2] Por edad
    [3] Salir del programa"""

        print (texto)

        num = get_int("Seleccione una opcion: ")

        if 0 < num < 4:
            return num
    
print("Opcion no valida.")



def ordenar_apellido(persona:list):
    sorted(persona.objects, key = lambda persona: (persona.P_appelido, persona.nombre))


def ordenar_edad(persona:list):
    sorted(persona.objects, key= lambda persona: persona.edad)


def agregar_persona(persona:list) -> None:
    nom = input("Ingrese el nombre de la persona.")
    apellido_P = input("Ingresar el apellido paterno de la persona.")
    apellido_M = input("Ingrese el apellido materno de la persona.")
    age = input("Ingrese la edad de la persona.")
    
    persona.append(persona(nom, apellido_P, apellido_M, age))
    return

def mostrar_personas(persona:list) -> None:
    print(persona)



