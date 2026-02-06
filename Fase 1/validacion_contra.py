password = 20255543

password_input = input("Ingrese la contraseña: ")

if password_input.isdigit() and int(password_input) == password:
    print("Contraseña correcta. Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")