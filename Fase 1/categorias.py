edad = int(input("Ingrese su edad: "))

if edad >= 9 and edad <= 11:
    print("Su categoria es junior. ")
elif edad >= 11 and edad <= 15:
    print("Su categoría es secundaria. ")
elif edad >= 16 and edad <= 18:
    print("Su categoría es bachillerato. ")
elif edad >= 19 and edad <=23:
    print("Su categoria es universitario. ")
else:    
    print("Edad no valida")     