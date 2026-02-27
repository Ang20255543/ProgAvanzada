from clases import *
from funciones import *

codigo = validar_codigo()
marca = input("Marca: ").upper()
modelo = get_int("Modelo: ")

camion = Transporte(codigo, marca, modelo, 0)

print(f"Codigo: {camion.codigo}")
print(f"Marca: {camion.marca}")
print(f"Modelo: {camion.modelo}")
print(f"Km: {camion.km}")

print(camion)