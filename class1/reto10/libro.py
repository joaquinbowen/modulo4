


class Libro:
    
    contador_libros = 0

    def __init__(self,titulo,autor,paginas):
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        Libro.contador_libros+=1

    def mostrar_info(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Paginas: {self.paginas}")

    @staticmethod
    def es_grande(libro):
        if libro.paginas>300:
            return True
        return False
    
    @classmethod
    def total_libros(cls):
        return cls.contador_libros
    
libro1= Libro("1948","George Orwell",200)
libro2= Libro("La republica","Platon",300)
libro3= Libro("La peste","Albert Camus",400)

libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()

print(f"{libro1.titulo} es grande? >>> {Libro.es_grande(libro1)} ")
print(f"{libro2.titulo} es grande? >>> {Libro.es_grande(libro2)} ")
print(f"{libro3.titulo} es grande? >>> {Libro.es_grande(libro3)} ")

print(f"Total de libros:{Libro.total_libros()}")


    
        