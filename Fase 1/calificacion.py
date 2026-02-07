suma = 0
cant = 0

while True:
    cal = input("Ingrese una calificación")

    if cal < 0 or cal > 10:
        break

    suma += cal
    cant += 1

promedio = suma / cant

print("El promedio de las calificaciones es:", promedio)