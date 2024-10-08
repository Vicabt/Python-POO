# Defino la clase
class Carro:
    # Método Constructor
    def __init__(self, marca, modelo, año, color, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Carro")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print("-----------------------------")

    # Método para arrancar el carro
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")

# Creamos los objetos a partir de instanciar la clase Carro
carro1 = Carro("Toyota", "Corolla", 2020, "Rojo", "Sedán")
carro2 = Carro("Ford", "Mustang", 2022, "Azul", "Deportivo")
carro3 = Carro("Tesla", "Model 3", 2021, "Blanco", "Eléctrico")

# Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro2.mostrar_detalles()
carro3.mostrar_detalles()