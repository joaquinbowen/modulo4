from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año,num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas=num_puertas

    def descripcion(self):
        super().descripcion()
        print(f"Numero de puertas: {self.num_puertas}")
    
    pass