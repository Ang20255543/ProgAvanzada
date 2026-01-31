log = int(input("Ingrese la calificación de lógica: "))
kar = int(input("Ingrese la calificación de Karel: "))
c = int(input("Ingrese la calificación de C: "))

if log >= kar and log >= c:
    print("La mejor calificación: ", log)
elif kar >= log and kar >= c:
    print("La mejor calificación: ", kar)
elif c >= log and c >= kar:
    print("La mejor calificación: ", c)