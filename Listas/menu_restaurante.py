platos=["Salchipapa","Papi Pollo", "Dorilocos", ""]

print("Segunda es todo")
mensaje=("Escoja una opcion del menu  \n 1. Añadir plato al menú. \n 2. Buscar en el menú. " \
        "\n 3. Eliminar plato del menú. \n 4. Mostrar platos del menú. \n Opción: ")


opcion=int(input(mensaje))

if opcion==1:
    plato_nuevo=input("Ingrese un plato nuevo al menu:")
    platos.append(plato_nuevo)
    print("Plato agregado con exito")
elif opcion==2:
    plato_a_buscar=input("Ingrese el plato que desea buscar:")
    encontrado=platos.count(plato_a_buscar)
    if encontrado != 0:
        print("El plato ingresado se encuentra en el menu.")
    else:
        print("El plato ingresado no ha sido encontrado.")
elif opcion == 3:
    print(platos)
    plato_a_eliminar=input("Ingrese el plato a eliminar:")
    if platos.count(plato_a_eliminar) != 0:
        platos.remove(plato_a_eliminar)
        print("Plato eliminado con éxito")
    else:
        print("No existe el plato que quiere eliminar")
elif opcion == 4:
    print(platos)
else:
    print("La opcion Ingresada es incorrecta.")




