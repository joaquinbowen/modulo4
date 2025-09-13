

class Laptop:
    def __init__(self,marca,procesador,memoria,costo=500,impuesto=10):
        self.marca =marca
        self.procesador=procesador
        self.memoria=memoria
        self.costo=costo
        self.impuesto=impuesto

    def valor_final(self):
        return self.costo+self.impuesto
    
    def valor_descuento(self,descuento):
        return (self.costo*descuento)/100


laptop_pepito =Laptop("Lenovo","i7",32)

print(laptop_pepito.__dict__)
print(laptop_pepito.valor_final())
print(f"El valor de descuento: {laptop_pepito.valor_descuento(10)}")