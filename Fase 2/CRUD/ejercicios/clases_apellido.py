class persona:
    nombre = ""
    P_apellido = ""
    M_apellido = ""
    edad = ""

    def __init__(self, nombre, P_apellido, M_apellido, edad):
        self.nombre = nombre 
        self.P_apellido = P_apellido
        self.M_apellido = M_apellido
        self.edad = edad

    def __str__(self):
        salida = f"""nombre: {self.nombre}
P_apellido = {self.P_apellido}
M_apellido = {self.M_apellido}
edad = {self.edad}"""
        return salida
    
