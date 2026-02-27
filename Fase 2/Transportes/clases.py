class Transporte:
    codigo = ""
    marca = ""
    modelo = ""
    km = 0

    def __init__(self, codigo, marca, modelo):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        salida = f"Codigo: {self.codigo}\nMarca: {self.marca}\nModelo: {self.modelo}\nKm: {self.km}"
        return salida