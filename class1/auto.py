

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


auto1=Auto("Toyota","Celica","1992",20000)
auto1.mostrar_informacion()
auto1.estado_auto()
auto1.actualizar_kilometraje(15000)
auto1.realizar_viaje(200)
auto1.mostrar_informacion()