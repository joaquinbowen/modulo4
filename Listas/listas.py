#Listas

planetas=["Mercurio","Venus", "Tierra","Marte", "Jupiter","Saturno","Urano","Neptuno"]

# print(planetas[-1])

# print(planetas[2:])

# print(len(planetas))

#Trabajar con una lista de numeros

gravedad_en_planetas=[0.378,0.907,1,0.377,2.36,0.916,0.889,1.12]
peso_bus=124054


print(f"En la tierra un autobus de dos pisos pesa {peso_bus}")
print(f"En mercurio , un autobus de dos pisos pesa {peso_bus*gravedad_en_planetas[0]} N")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus*min(gravedad_en_planetas)}")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus*max(gravedad_en_planetas)}")