class Transporte:
    codigo = ""
    marca = ""
    modelo = ""
    km = 0

    def __init__(self, codigo, marca, modelo, km=0):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.km = km

    def flete(self, distancia: int) -> None:
        self.km += distancia

    def __str__(self):
        salida = f"Codigo: {self.codigo}\nMarca: {self.marca}\nModelo: {self.modelo}\nKm: {self.km}"
        return salida
    

class empleado:
    ID = ""
    nombre = ""
    apellido = ""
    fecha_nacimiento= ""

    def __init__(self,ID, nombre, apellido, fecha_nacimiento):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        salida = f"ID: {self.ID}\nNombre: {self.nombre}\nApellidos: {self.apellido}\nFecha de nacimiento: {self.fecha_nacimiento}"
        return salida