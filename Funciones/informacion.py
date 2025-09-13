nombre_paciente=[]
edad_paciente=[]

def agregar_nombre(nombre,apellido):
    nombre_paciente.append(nombre+" "+apellido)

def agregar_edad(año_nacimiento):
    edad_actual=calcular_edad(año_nacimiento)
    edad_paciente.append(edad_actual)
    
def calcular_edad(año):
    actual=2025-año
    return actual

def calcular_mayor_menor():
    paciente_menor=min(edad_paciente)
    paciente_mayor=max(edad_paciente)
    indice_mayor=edad_paciente.index(paciente_mayor)
    indice_menor=edad_paciente.index(paciente_menor)
    nombre_mayor=nombre_paciente[indice_mayor]
    nombre_menor=nombre_paciente[indice_menor]
    print(nombre_paciente)
    print(edad_paciente)
    print(f"{nombre_mayor} con la edad de {paciente_mayor} años es mayor a los demás pacientes")
    print(f"{nombre_menor} con la edad de {paciente_menor} años es menor a los demás pacientes")