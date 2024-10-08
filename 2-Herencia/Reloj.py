# Defino la clase
class Reloj:
    # Método Constructor
    def __init__(self, marca, tipo_reloj, material):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo = tipo_reloj
        self.material = material
        self.precio = int(input("Digite el precio del Reloj : "))
        
        

    # Método publico
    def registrar(self):
        print(f"-----------------------------")
        print(f"RELOJ REGISTRADO")
        print(f"-----------------------------")
        print(f"Marca :  {self.marca}")
        print(f"Modelo :  {self.modelo}")
        print(f"Material :  {self.material}")
        print(f"Precio :  ${self.precio} ")
        print(f"-----------------------------")


    def encender(self):

        self.encender = int(input("Desea encender el Reloj ? \n1.Si \n2.No \n"))
        if self.encender == 1:
            print(f"-----------------------------")
            print(f"RELOJ REGISTRADO")
            print(f"-----------------------------")
            print(f"Marca :  {self.marca}")
            print(f"Modelo :  {self.modelo}")
            print(f"Material :  {self.material}")
            print(f"Precio :  ${self.precio}")
            print(f"Tipo de Pantalla :  {self.tipo_de_pantalla}")
            print(f"Sistema Operativo :  {self.sistema_operativo}")
            print(f"-----------------------------")
        else:
            print("No se encendera el Reloj")
    

class RelojInteligente(Reloj): #Subclase
    #Constructor
    def __init__(self, marca, tipo_reloj, material, tipo_de_pantalla):
        super().__init__(marca, tipo_reloj, material) #Super clase heredada
        self.tipo_de_pantalla = tipo_de_pantalla
        sistema_op = int(input("¿Cuál es el Sistema Operativo? \n1. Apple \n2. Android \n"))
        self.sistema_operativo = "Apple" if sistema_op == 1 else "Android"
        
        

    
#instanciando la subclase 
objeto_relojInteligente=RelojInteligente('Apple', 'Wacht', 'Titanio', 'Amoled')
objeto_relojInteligente.registrar()#Registrando el dispositivo
objeto_relojInteligente.encender()#Solicita encender el dispositivo