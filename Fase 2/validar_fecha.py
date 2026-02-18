import re

fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
patron = "^\d{2}/\d{2}/\d{4}$"

if re.match(patron, fecha):
    print("Gracias")
else:
    print("Fecha no válida")