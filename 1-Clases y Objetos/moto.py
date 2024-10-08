# Defino la clase
class Moto:
    # Método Constructor
    def __init__(self, marca, modelo, cilindrada, tipo, color):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.tipo = tipo
        self.color = color

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información de la Moto")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindrada: {self.cilindrada} cc")
        print(f"Tipo: {self.tipo}")
        print(f"Color: {self.color}")
        print("-----------------------------")

    # Método para arrancar la moto
    def arrancar(self):
        print(f"La moto {self.marca} {self.modelo} está arrancando.")

# Creamos los objetos a partir de instanciar la clase Moto
moto1 = Moto("Yamaha", "MT-07", 689, "Naked", "Negro")
moto2 = Moto("Honda", "CB500F", 471, "Naked", "Rojo")
moto3 = Moto("Kawasaki", "Ninja 400", 399, "Deportiva", "Verde")

# Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto2.mostrar_detalles()
moto3.mostrar_detalles()