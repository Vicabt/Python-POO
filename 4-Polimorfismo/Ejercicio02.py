'''Ejercicio 2: Clases de  Vehículos con Polimorfismo
Crea tres clases: Carro, Moto y Bicicleta, cada una con un método descripcion() que describa el tipo de vehículo.'''

# Clase base Vehiculo
class Vehiculo:
    def descripcion(self):
        pass

# Clase Carro
class Carro(Vehiculo):
    def __init__(self):
        self.nombre = "Carro"
        self.descripcion_vehiculo = "Vehículo de 4 ruedas."

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"Descripción: {self.descripcion_vehiculo}")

# Clase Moto
class Moto(Vehiculo):
    def __init__(self):
        self.nombre = "Moto"
        self.descripcion_vehiculo = "Vehículo de 2 ruedas."

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"Descripción: {self.descripcion_vehiculo}")

# Clase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self):
        self.nombre = "Bicicleta"
        self.descripcion_vehiculo = "Vehículo movido por el esfuerzo humano."

    def mostrar_info(self):
        print(f"Tipo: {self.nombre}")
        print(f"Descripción: {self.descripcion_vehiculo}")

# Función polimórfica para mostrar información
def mostrar_informacion(vehiculo):
    vehiculo.mostrar_info()

# Crear objetos
carro = Carro()
moto = Moto()
bicicleta = Bicicleta()

# Mostrar la información de cada vehículo
mostrar_informacion(carro)
mostrar_informacion(moto)
mostrar_informacion(bicicleta)
