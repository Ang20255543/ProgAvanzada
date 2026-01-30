cantidad= int(input("Ingrese la cantidad de productos"))
costo =int(input("Ingrese el costo del producto"))

Total = cantidad * costo

if Total>1000:
    descuento = Total * .05
    totalcdes = Total - descuento
    print(f"Tu total es de: {totalcdes}")
else:
    print(f"Tu total es de: {Total}")