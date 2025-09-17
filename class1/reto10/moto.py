from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, año,tipo):
        super().__init__(marca, modelo, año)
        self.tipo=tipo

    def descripcion(self):
        super().descripcion()
        print(f"Tipo: {self.tipo}")
    
    
    pass