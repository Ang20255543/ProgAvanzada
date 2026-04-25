from clases_apellido import persona
from funciones_apellido import *

persona = list()

persona.append(persona("Angel", "Hernandez", "Delgado", "17"))
persona.append(persona("Ingrid", "Delgado", "Abrego", "17"))
persona.append(persona("Amaniel", "Sanchez", "De Leon", "18"))


while True:
    opcion = menu()

    if opcion == 1:
        ordenar_apellido(persona)
    elif opcion == 2:
        ordenar_edad(persona)
    elif opcion == 3:
        print ("Saliendo del programa...")
        break



