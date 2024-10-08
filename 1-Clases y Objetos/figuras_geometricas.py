# Defino la clase
class FiguraGeometrica:
    # Método Constructor
    def __init__(self, tipo, color, base, altura, lado):
        self.tipo = tipo
        self.color = color
        self.base = base
        self.altura = altura
        self.lado = lado

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la Figura Geométrica")
        print(f"Tipo: {self.tipo}")
        print(f"Color: {self.color}")
        print(f"Base: {self.base} cm")
        print(f"Altura: {self.altura} cm")
        print(f"Lado: {self.lado} cm")
        print("-----------------------------")

    # Método para calcular el área del triángulo
    def calcular_area_triangulo(self):
        if self.tipo == "triángulo":
            area = 0.5 * self.base * self.altura
            print(f"El área del triángulo es {area} cm²")
        else:
            print(f"El tipo de figura {self.tipo} no es un triángulo.")

    # Método para calcular el área del cuadrado
    def calcular_area_cuadrado(self):
        if self.tipo == "cuadrado":
            area = self.lado ** 2
            print(f"El área del cuadrado es {area} cm²")
        else:
            print(f"El tipo de figura {self.tipo} no es un cuadrado.")

# Creamos los objetos a partir de instanciar la clase FiguraGeometrica
figura1 = FiguraGeometrica("triángulo", "rojo", 10, 5, 0)
figura2 = FiguraGeometrica("cuadrado", "azul", 0, 0, 4)

# Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura2.mostrar_detalles()