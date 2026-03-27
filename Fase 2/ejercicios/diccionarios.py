# Ejercicio 1: Crear un diccionario para almacenar información personal
#datos = dict()

#datos["nombre"] = input("Ingrese su nombre: ")
#datos["edad"] = input("Ingrese su edad: ")
#datos["direccion"] = input("Ingrese su dirección: ")
#datos["telefono"] = input("Ingrese su teléfono: ")

#print(f"{datos['nombre']} tiene {datos['edad']} años, vive en {datos['direccion']} y su teléfono es {datos['telefono']}.")


# lista de preecios
precios = {"Leche": 23.0, "Aceite": 40.0, "Arroz":28.0, "Huevos": 54.0}

producto = input("Ingrese el nombre del producto: ")

if producto in precios:
    cantidad = int(input("Ingrese la cantidad: "))
    importe = precios[producto] * cantidad
    print(f"El importe a pagar por {cantidad} unidades de {producto} es: {importe}")
else:
    print("El producto no se encuentra en la lista de precios.")

