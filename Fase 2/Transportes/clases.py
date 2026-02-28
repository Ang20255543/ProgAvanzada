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

    def __str__(self):
        salida = f"Codigo: {self.codigo}\nMarca: {self.marca}\nModelo: {self.modelo}\nKm: {self.km}"
        return salida