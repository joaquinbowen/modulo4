from auto import Auto


# auto1=Auto("Toyota","Celica","1992",20000)
# auto1.mostrar_informacion()
# auto1.estado_auto()
# auto1.actualizar_kilometraje(15000)
# auto1.realizar_viaje(200)
# auto1.mostrar_informacion()

auto_toyota=Auto.auto_toyota()
print(auto_toyota.__dict__)
auto_honda=Auto.auto_honda()
print(auto_honda.__dict__)
print(Auto.comparar_año(auto_toyota,auto_honda))
print(Auto.comparar_kilometraje(auto_honda,auto_toyota))



