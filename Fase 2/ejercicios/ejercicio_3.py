from datetime import date, timedelta
import locale

locale.setlocale(locale.LC_ALL, "es_MX")

hoy= date.today()
dias = int(input("Ingrese el número de días: "))
fecha = hoy + timedelta(days = dias)

for i in range(dias):
    print(f"En {i+1} día(s) será: {date.strftime(hoy + timedelta(days = i+1), '%A %d de %B de %Y')}")