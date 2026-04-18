class Producto:
    clave = ""
    nombre = ""
    marca = ""
    precio = ""
    existencia = 0

    def __init__(self, clave: int, nombre: str, marca: str, precio: float, existencia: int = 0):
        self.clave = clave
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.existencia = existencia

    def __str__(self):
        salida =  f"""Clave: {self.clave}
Nombre: {self.nombre}
Marca: {self.marca}
Precio: {self.precio}
Existencia: {self.existencia}"""
        return salida