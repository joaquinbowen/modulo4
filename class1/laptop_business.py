from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria,almacenamiento,duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento=almacenamiento
        self.duracion_bateria=duracion_bateria
    
    def verificar_conectividad(self):
        resultados={
            "DISPONIBILIDAD_WIFI": "DISPONIBLE" if random.choice([True,False]) else "NO DISPONIBLE",
            "ACCESO_A_SERVIDORES_EMPRESARIALES":  " PERMITIDO" if random.choice([True,False]) else "DENEGADO",
            "LATENCIA_RED" : f"{random.randint(1,1000)} ms"
        }
        return resultados

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico_base=super().realizar_diagnostico_sistema()
        resultados_red=self.verificar_conectividad()
        resultado_diagnostico_base["Resultado de red"]=resultados_red
        return resultado_diagnostico_base
    
    def __str__(self):
        return f"\n Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Almacenamiento: {self.almacenamiento}\n Duracion Bateria: {self.duracion_bateria} \n Costo: {self.costo} \n Impuesto: {self.impuesto}"
    
    pass