from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

def imprimir_informe(laptop):
    informe=laptop.realizar_informe_uso()
    for clave,valor in informe.items():
        print(f"{clave}  :  {valor}")
    print("\n")








laptop_pepito =Laptop("Lenovo","i7",32)
laptop_maria =Laptop("Lenovo","i7",32,600)
laptop_juanito= Laptop_Gaming("MSI","i7",4,"RTX 8GB",900,20)
# laptop_gerente=Laptop_Business("ASUS","Dual Core",16,"2TB","12h","800","15")

#asus_laptop=Laptop.asus_laptop()

# for numero in range(1,1001):
#     asus_laptop=Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


#print(Laptop.comparar_costo(laptop_pepito,laptop_maria))
#print(laptop_juanito.realizar_diagnostico_sistema())
#print(laptop_gerente.realizar_diagnostico_sistema())
print("Pepito")
imprimir_informe(laptop_pepito)
print("Juanito")
imprimir_informe(laptop_juanito)
