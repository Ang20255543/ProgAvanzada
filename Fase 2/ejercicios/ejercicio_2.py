from datetime import date, timedelta
import locale

locale.setlocale(locale.LC_ALL, "es_MX")

dias = int(input("Ingrese el número de días: "))
hoy = date.today()
fecha = hoy - timedelta(days = dias)

print(f"Hace {dias} días fue: {date.strftime(fecha, '%A %d de %B de %Y')}")