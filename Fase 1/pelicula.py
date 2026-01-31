edad = int(input("Ingrese su edad: "))

if edad <= 10 and edad >= 0:
    print("Dirigase a la sala A, no olvides tus palomitas! ")
elif edad >= 11 and edad <= 15:
    print("Dirigase a la sala B, no olvides tus palomitas! ")
elif edad >= 16 and edad >= 18:
    print("Dirigase a la sala C, no olvides tus palomitas! ")
else:
    print("Edad no valida") 