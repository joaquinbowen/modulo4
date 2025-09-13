print("Viaja con krakedev")

destino=input("Escoge tu destino \n Digite 1 para Ecuador \n Digite 2 para Colombia \n Digite 3 para Peru \n ")

if destino == "1":
    limite=int(input("¿A que velocidad estaria correcto ir en zona urbana en Ecuador"))
    if limite >50:
        print("Está excediendo el limite de velocidad")
    elif limite < 10:
        print("Su velocidad es muy baja")
    else:
        print("Su velocidad es correcta")
elif destino == "2":
    limite=int(input("¿A que velocidad estaria correcto ir en zona perimetral en Colombia"))
    if limite >100:
        print("Está excediendo el limite de velocidad")
    elif limite < 81:
        print("Su velocidad es muy baja")
    else:
        print("Su velocidad es correcta")
elif destino == "3":
    limite=int(input("¿A que velocidad estaria correcto ir en zona rural en Peru"))
    if limite >60:
        print("Está excediendo el limite de velocidad")
    elif limite < 41:
        print("Su velocidad es muy baja")
    else:
        print("Su velocidad es correcta")