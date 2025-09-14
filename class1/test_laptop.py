from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

laptop_pepito =Laptop("Lenovo","i7",32)
laptop_maria =Laptop("Lenovo","i7",32,600)
laptop_juanito= Laptop_Gaming("MSI","i7",4,"RTX 8GB",900,20)
laptop_gerente=Laptop_Business("ASUS","Dual Core",16,"2TB","12h","800","15")

#asus_laptop=Laptop.asus_laptop()

# for numero in range(1,1001):
#     asus_laptop=Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


#print(Laptop.comparar_costo(laptop_pepito,laptop_maria))
#print(laptop_juanito.realizar_diagnostico_sistema())
print(laptop_gerente.realizar_diagnostico_sistema())