import re

cp = input("Ingrese el código postal: ")

if re.match("^\d{5}$", cp):
    print("Gracias")
else:
    print("Código postal no válido")