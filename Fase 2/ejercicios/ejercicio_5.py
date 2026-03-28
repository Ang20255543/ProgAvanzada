##TICKET DE COMPRA  
productos = dict()

while True:
    producto = input("Ingrese el nombre del producto: ").lower()

    if producto == "x":
        break
    precio = float(input("Ingrese el precio del producto: "))

    productos [producto] = precio 
for prod, prec in zip(productos.keys(), productos.values()):
    print (f"El producto ingresado fue {prod} y el precio es {prec}")

total = sum(productos.values())
print(f"El total de la compra es: {total}")