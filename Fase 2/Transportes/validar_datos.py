import re, locale
from datetime import date

def leer_fecha(s: str) -> date:
    while True:
        fecha = input(f"Ingrese {s} en formato DD-MM-AAAA: ")
        try:
            fecha = date.strptime(fecha, "%d-%d-%Y")
            return fecha
        except ValueError as e:
            print("Fecha no válida. Intente nuevamente, ERROR: ", e)

fecha = leer_fecha("Fecha de vencimiento")
print(fecha)