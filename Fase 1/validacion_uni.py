##nombre, carrera (LTI, CP; LA), semestre

nombre = input("Ingrese su nombre: ")
carrera = input("Ingrese su carrera: ") 
semestre = input("Ingrese su semestre: ")

carrera_valida = carrera.lower() in ["lti", "cp","la"]
semestre_valido = semestre.isdigit() and 1 <= int(semestre) <= 9

print("Validando datos...")
print("Datos válidos " 
      "Usted está en una carrera válida y semestre válido" if carrera_valida and semestre_valido else "Datos inválidos")
