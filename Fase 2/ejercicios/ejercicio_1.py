from datetime import datetime as dt 
import locale 

locale.setlocale(locale.LC_ALL, "es_MX")

fecha_str = input ("Ingrsa una fecha en formato (aaaa-mm-dd): ")

try:
    fecha = dt.strptime(fecha_str, "%Y-%m-%d")
    fecha_lg = fecha.strftime("%A, %d de %B de %Y")
    print (f"La fecha ingresada es: {fecha_lg.capitalize()}")
except ValueError:
    print ("La fecha ingresada no es válida. Por favor, ingresa una fecha en el formato correcto (aaaa-mm-dd).")
