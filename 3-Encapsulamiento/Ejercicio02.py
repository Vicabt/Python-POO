# Clase Producto con atributos privados y públicos
class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre  # privado
        self.__precio = precio  # privado
        self.cantidad = cantidad  # público
        self.categoria = categoria  # público

    # Métodos getter
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    # Métodos setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Método para mostrar detalles del producto
    def mostrar_detalles(self):
        print(f"\nNombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Crear objeto Producto
producto = Producto("Laptop", 1000, 5, "Tecnología")

# Imprimir detalles del producto
producto.mostrar_detalles()

print("----------------------")

# Modificar atributos privados mediante setter y mostrar los cambios
producto.establecer_nombre("PC Gamer") #setter
print(f"Nombre: { producto.obtener_nombre() }") #getter
producto.establecer_precio("5.000.000") #setter
print(f"Precio: { producto.obtener_precio() }") #getter
print(f"Cantidad: { producto.cantidad }") #publico
print(f"Categoria: { producto.categoria }") #público
