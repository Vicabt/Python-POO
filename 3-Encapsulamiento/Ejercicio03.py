# Clase Libro con atributos privados y públicos
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo  # privado
        self.__autor = autor  # privado
        self.__isbn = isbn  # privado
        self.editorial = editorial  # público

    # Métodos getter
    def obtener_titulo(self):
        return self.__titulo

    def obtener_autor(self):
        return self.__autor
    
    def obtener_isbn(self):
        return self.__isbn

    # Métodos setter
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # Método para mostrar detalles del producto
    def mostrar_detalles(self):
        print(f"\nTitulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# Crear objeto Libro
libro = Libro("La Maria", "Jorge Isacc", 12345, "Planeta")

# Imprimir detalles del producto
libro.mostrar_detalles()

print("----------------------")

# Modificar atributos privados mediante setter y mostrar los cambios
libro.establecer_titulo("La Silvina") #setter
print(f"Titulo: { libro.obtener_titulo() }") #getter
libro.establecer_autor("Juanchito") #setter
print(f"Autor: { libro.obtener_autor() }") #getter
print(f"ISBN: { libro.obtener_isbn() }") #getter
print(f"Editorial: { libro.editorial }") #publico
