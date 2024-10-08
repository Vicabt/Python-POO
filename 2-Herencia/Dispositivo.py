# Defino la clase
class Dispositivo:
    # Método Constructor
    def __init__(self, marca, modelo, año):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Digite la capacidad de la bateria en Mah :  "))
        

    # Método publico
    def registrar(self):
        print(f"-----------------------------")
        print(f"DISPOSITIVO REGISTRADO")
        print(f"-----------------------------")
        print(f"Marca:  {self.marca}")
        print(f"Modelo:  {self.modelo}")
        print(f"Año:  {self.año}")
        print(f"Capacidad de la Bateria:  {self.capacidad_bateria} Mah")
        print(f"Sistema Operativo:  {self.sistema_operativo}")
        print(f"Tipo de Red:  {getattr(self, 'conectividad', 'No Definido') }")
        print(f"-----------------------------")

    

class Smartphone(Dispositivo): #Subclase
    #Constructor
    def __init__(self, marca, modelo, año, capacidad_bateria, sistema_operativo):
        super().__init__(marca, modelo, año) #Super clase heredada
        self.sistema_operativo = sistema_operativo
        self.conectividad = int(input("Digite la Red en la que se conectara (1 para 4G,  2 para 5G \n)  "))

    def registrar(self):
        super().registrar()
        if self.conectividad == 1:
            red = "4G"
        elif self.conectividad == 2:
            red = "5G"
        else:
            red = "Desconocida"
        print(f"Red: {red}")
        

    def encender(self):
        respuesta = input("Desea encender el Dispositivo ? (s/n): ")
        if respuesta == 's':
            print("El dispositivo esta encendido \n")
        else:
            print("El Dispositivo no se encendera. \n")

#instanciando la subclase Refrigerador
objeto_smartphone=Smartphone('Iphone', 'XS', '2024','2000 Mah', 'IOS')
objeto_smartphone.registrar()#Registrando el dispositivo
objeto_smartphone.encender()#Solicita encender el dispositivo

