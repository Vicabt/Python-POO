# Defino la clase
class Celular:
    # Método Constructor
    def __init__(self, marca, modelo, almacenamiento, ram, camara):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.camara = camara

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Celular")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Almacenamiento: " + self.almacenamiento)
        print("Tamaño de la Ram: " + self.ram)
        print("Cámara Frontal: " + self.camara)
        print("-----------------------------")

    # Método para encender el Celular
    def encender(self):
        # Defino el atributo privado energia solo para el método encender
        self.energia = int(input("Digite el valor de la carga: "))
        # Evaluamos si tiene carga el celular
        if self.energia > 0:
            print(f"El celular {self.modelo} se puede encender")
            print(f"|||||||||| {self.energia} % de carga")
            print("-----------------------------")
        else:
            print(f"El celular {self.modelo} no se puede encender")

# Creamos los objetos a partir de instanciar la clase Celular
celular1 = Celular("Xiaomi", "Redmi Note 13", "256 GB", "8 GB", "108mpx")
celular2 = Celular("Apple", "iPhone 8 Plus", "256 GB", "3 GB", "12mpx")
celular3 = Celular("Apple", "iPhone X", "64 GB", "3 GB", "12mpx")

# Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender()  # Método que evalúa el encendido del celular
celular2.mostrar_detalles()
celular3.mostrar_detalles()