while True:
    num = input("Ingrese un número entero: ")

    try:
        num = int(num)
        break
    except ValueError:
        print("Número inválido. Por favor, ingrese un número entero.")

print("Número ingresado:", num)