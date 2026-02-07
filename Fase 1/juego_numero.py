import random

numero = random.randint(1, 100)
contador = 0

numero_usuario = int(input("Adivina el número entre 1 y 100: "))
while numero_usuario != numero:
    if numero_usuario < numero:
        print("El número es mayor")
        contador += 1
    else:
        print("El número es menor")
        contador += 1
    numero_usuario = int(input("Intenta de nuevo: "))

print("¡Felicidades! Has adivinado el número.")
print("Número de intentos:", contador)