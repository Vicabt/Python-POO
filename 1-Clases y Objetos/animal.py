# Defino la clase
class Animal:
    # Método Constructor
    def __init__(self, especie, edad, color, nombre, habitat):
        self.especie = especie
        self.edad = edad
        self.color = color
        self.nombre = nombre
        self.habitat = habitat

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Animal")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")
        print(f"Nombre: {self.nombre}")
        print(f"Hábitat: {self.habitat}")
        print("-----------------------------")

    # Método para simular que el animal está comiendo
    def comer(self):
        print(f"{self.nombre} está comiendo.")

# Creamos los objetos a partir de instanciar la clase Animal
animal1 = Animal("Perro", 5, "Marrón", "Max", "Casa")
animal2 = Animal("Gato", 3, "Blanco", "Nieve", "Departamento")
animal3 = Animal("León", 8, "Dorado", "Simba", "Sabana")

# Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal2.mostrar_detalles()
animal3.mostrar_detalles()
