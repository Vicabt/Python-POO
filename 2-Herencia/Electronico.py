# Defino la clase
class Electronico:
    # Método Constructor
    def __init__(self, marca, modelo, tipo_de_procesador):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_procesador = tipo_de_procesador
        self.ram = int(input("Digite la cantidad de RAM del equipo :  "))
        

    # Método publico
    def registrar(self):
        print(f"-----------------------------")
        print(f"DISPOSITIVO REGISTRADO")
        print(f"-----------------------------")
        print(f"Marca :  {self.marca}")
        print(f"Modelo :  {self.modelo}")
        print(f"Tipo de Procesador :  {self.tipo_de_procesador}")
        print(f"RAM :  {self.ram} Gigas ")
        print(f"-----------------------------")


    def encender(self):

        encender = int(input("Desea encender la Laptop ? \n1.Si \n2.No \n"))
        if encender == 1:
            print(f"-----------------------------")
            print(f"DISPOSITIVO REGISTRADO")
            print(f"-----------------------------")
            print(f"Marca :  {self.marca}")
            print(f"Modelo :  {self.modelo}")
            print(f"Tipo de Procesador :  {self.tipo_de_procesador}")
            print(f"RAM :  {self.ram} Gigas ")
            print(f"Tipo de Disco Duro :  {self.tipo_de_disco_duro}")
            print(f"Duracion de la Bateria :  {self.duracion_bateria} Horas")
            print(f"-----------------------------")
        else:
            print("No se encendera la Laptop")
    

class Laptop(Electronico): #Subclase
    #Constructor
    def __init__(self, marca, modelo, tipo_de_procesador, tipo_de_disco_duro):
        super().__init__(marca, modelo, tipo_de_procesador) #Super clase heredada
        self.tipo_de_disco_duro = tipo_de_disco_duro
        self.duracion_bateria = input("Digite la duracion de la bateria en horas:  ")

    
#instanciando la subclase 
objeto_laptop=Laptop('HP', 'Laptop', 'Ryzen 9000', 'SSD')
objeto_laptop.registrar()#Registrando el dispositivo
objeto_laptop.encender()#Solicita encender el dispositivo