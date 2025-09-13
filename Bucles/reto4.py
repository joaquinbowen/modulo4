num=int(input("¿Cuantos datos desea ingresar?"))
datos=[]

for i in range(num):
    valor = (input(f"Ingrese el dato {i+1}:")).replace(",",".")

    if valor.isdigit() :
        datos.append(int(valor))
    
    elif valor.replace(".","",1).isdigit() and valor.count("."):
        datos.append(float(valor))
    else:
        datos.append(valor)

print(f"Su lista es {datos}")
