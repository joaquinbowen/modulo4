import informacion

print("Voluntarios Cruz Roja")

num_datos=int(input("Ingrese la cantidad de datos a ingresar:"))

for i in range(num_datos):
    print(f"Paciente {i+1}")
    nombre=input("Ingrese nombre:")
    apellido=input("Ingrese apellido:")
    año_nacimiento=int(input("Ingrese año de nacimiento:"))

    informacion.agregar_nombre(nombre,apellido)
    informacion.agregar_edad(año_nacimiento)

informacion.calcular_mayor_menor()