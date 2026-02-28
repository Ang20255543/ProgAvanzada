from clases import *
from funciones import *

#Clase transporte

codigo = validar_codigo()
marca = input("Marca: ").upper()
modelo = get_int("Modelo: ")
camion = Transporte(codigo, marca, modelo, 0)

#print(f"Codigo: {camion.codigo}")
#print(f"Marca: {camion.marca}")
#print(f"Modelo: {camion.modelo}")
#print(f"Km: {camion.km}")

print(camion)
camion.flete(350)
camion.flete(200)
camion.flete(420)
print(camion)

#Clase empleado

id = validar_ID("ID: ")
nombre = validar_nombre("Nombre: ")
apellido = validar_apellido("Apellido: ")
fecha_nacimiento = validar_fecha("Fecha de nacimiento: ")

empleado1= empleado(id, nombre, apellido, fecha_nacimiento)

print(empleado1)
