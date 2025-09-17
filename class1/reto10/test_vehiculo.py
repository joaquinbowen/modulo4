from auto import Auto
from moto import Moto


vehiculos=[]

auto1=Auto("Toyota","Ae86","1986",3)
auto2=Auto("Honda","S2000","1998",3)
moto1=Moto("Yamaha","gt",2000,"deportiva")
moto2=Moto("Suzuki","YZ","2020","clasica")


auto1.descripcion()
moto2.descripcion()

print("------------------------------------")

#iteracion lista --- polimorfismo

vehiculos.append(auto1)
vehiculos.append(auto2)
vehiculos.append(moto1)
vehiculos.append(moto2)

for serio in vehiculos:
    serio.descripcion()