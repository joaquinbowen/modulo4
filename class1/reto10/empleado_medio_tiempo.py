from empleado import Empleado


class Empleado_medio_tiempo(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre, salario_base)

    def calcular_salario(self):
       super().calcular_salario()
       salario_final=self.salario_base*110/100
       return f"El salario final de {self.nombre} es: {salario_final}"