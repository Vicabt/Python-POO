'''Ejercicio 3: Animales con Polimorfismo
Crea tres clases: Perro, Gato, y Pájaro, cada una con un método sonido() que haga el sonido correspondiente.'''

# Clase base Animal
class Animal:
    def descripcion(self):
        pass

# Clase Perro
class Perro(Animal):
    def __init__(self):
        self.nombre = "Perro"
        self.sonido = "Guau"

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"El Perro ladra: {self.sonido}")

# Clase Gato
class Gato(Animal):
    def __init__(self):
        self.nombre = "Gato"
        self.sonido = "Miau"

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"El Gato Maulla: {self.sonido}")

# Clase Pajaro
class Pajaro(Animal):
    def __init__(self):
        self.nombre = "Pajaro"
        self.sonido = "Pio Pio Pio"

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"El Pajaro esta pillando: {self.sonido}")

# Función polimórfica para mostrar información
def mostrar_informacion(animal):
    animal.mostrar_info()

# Crear objetos
perro = Perro()
gato = Gato()
pajaro = Pajaro()

# Mostrar la información de cada objeto
mostrar_informacion(perro)
mostrar_informacion(gato)
mostrar_informacion(pajaro)
