def encontrar_palabra(frase):
    if "feliz" in frase:
        print(f"El emoji que te representa es: \U0001F600")
    elif "triste" in frase:
        print(f"El emoji que te representa es: \U0001F614")


lista=[]

def agregar_frase(frase):
    lista.append(frase)
    print(f"La frase fue guardada correctamente {lista}")