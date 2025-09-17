from empleado import Empleado

class Empleado_tiempo_completo(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)
    
    def calcular_salario(self):
        super().calcular_salario()
        salario_final=self.salario_base*120/100
        return f"El salario final de {self.nombre} es: {salario_final}"