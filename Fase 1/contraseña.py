contraseña = input("Cree una contraseña: ")
cantidad = len(contraseña)


while cantidad >= 8 or cantidad >= 16:
   if cantidad >= 8 or cantidad >= 16:
    usuario = input("Ingrese su contraseña para verificar: ")
    if contraseña == usuario:
     print("Contraseña correcta")
    else:
     print("Contraseña incorrecta")
    break

if cantidad < 8 and cantidad < 16:
    print("La contraseña debe tener al menos 8 caracteres y máximo 16 caracteres")
    contraseña = input("Cree una contraseña: ")
    cantidad = len(contraseña) 
   
    



    