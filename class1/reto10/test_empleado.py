from empleado_medio_tiempo import Empleado_medio_tiempo
from empleado_tiempo_completo import Empleado_tiempo_completo

empleados=[]

juan=Empleado_tiempo_completo("Juan Perez",1200)
pepe=Empleado_tiempo_completo("Pepe Mejia",1000)
Sebastian=Empleado_medio_tiempo("Sebastian Almeida",400)
Angel=Empleado_medio_tiempo("Angel Londoño",100)

print(juan.calcular_salario())
print(Sebastian.calcular_salario())

print("---------------------------------------------")

empleados.append(juan)
empleados.append(pepe)
empleados.append(Sebastian)
empleados.append(Angel)

for i in empleados:
    print(i.calcular_salario())