# CALIFICACIONES
materias = dict()

while True:
    materia = input("Ingrese el nombre de la materia: ").lower()

    if materia == "x":
        break
    calif = int(input("Ingrese la calificacion: "))

    materias [materia] = calif

for mat, cali in zip(materias.keys(), materias.values()):
    print (f"La materia ingresada fue {mat} y la calificacion es {cali}")

promedio = sum(materias.values()) / len(materias)
print(f"El promedio de las calificaciones es: {promedio}")