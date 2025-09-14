

class Auto:
    def __init__(self,marca,modelo,año,kilometraje=0):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.kilometraje=kilometraje
    def mostrar_informacion(self):
        print(f"Informacion \n Marca:{self.marca} \n Modelo:{self.modelo} \n Año:{self.año} \n Kilometraje:{self.kilometraje}")
    def actualizar_kilometraje(self,nuevo_kilometraje):
        if nuevo_kilometraje<self.kilometraje:
            print("No se puede reducir el kilometraje")
        else:
            self.kilometraje=nuevo_kilometraje
    def realizar_viaje(self,kilometraje_viaje):
        if kilometraje_viaje>0:
            self.kilometraje+=kilometraje_viaje
        else:
            print("no se puede reducir ewl kilometraje")
    def estado_auto(self):
        if self.kilometraje<20000:
            print("Estoy como nuevo")
        elif self.kilometraje >=20000 and self.kilometraje<100000:
            print("Ya estoy usado")
        else:
            print("Ya déjame descansar por favor!!")

    @classmethod
    def auto_toyota(cls):
        marca="Toyota"
        modelo="Corolla"
        año="2025"
        return cls(marca,modelo,año)
    @classmethod
    def auto_honda(cls):
        marca="Honda"
        modelo="Civic"
        año="2000"
        kilometraje=200000
        return cls(marca,modelo,año,kilometraje)
    @staticmethod
    def comparar_kilometraje(auto1,auto2):
        if auto1.kilometraje==auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        return "No Tienen el mismo kilometraje"
    @staticmethod
    def comparar_año(auto1,auto2):
        if int(auto1.año)>int(auto2.año):
            return f"El {auto1.marca + auto1.modelo } es mas nuevo que el {auto2.marca + auto2.modelo } "
        elif int(auto2.año)>int(auto1.año):
            return f"El {auto2.marca + auto2.modelo } es mas nuevo que el {auto1.marca + auto1.modelo } "
        return "Los dos autos son del mismo año"