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

camiones = []
camiones.append(Transporte("aa-00", "VOLVO", 2010))
camiones.append(Transporte("aa-01", "DODGE", 2023))
camiones.append(Transporte("aa-02", "MERCEDES", 2025))
camiones.append(Transporte("aa-03", "VOLVO", 2024))
camiones.append(Transporte("aa-04", "FORD", 2015))
camiones.append(Transporte("aa-05", "TOYOTA", 2021))

#regisrar(camiones)

numero = input("Ingrese el numero del camion a mostrar: ")
encontrado = buscar(numero, camiones)

if encontrado >= 0:
    print(camiones[encontrado])
    km = get_int("Ingrese los km a agregar: ")
    camiones[encontrado].flete(km)
    print(camiones[encontrado])
else:    
    print("Camion no encontrado")



