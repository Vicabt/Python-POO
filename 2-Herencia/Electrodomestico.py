# Defino la clase
class Electrodomestico:
    # Método Constructor
    def __init__(self, marca, color, capacidad):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Digite el consumo Electrico en Kwh: "))
        

    # Método publico
    def registrar(self):
        print(f"-----------------------------")
        print(f"ELECTRODOMESTICO REGISTRADO")
        print(f"-----------------------------")
        print(f"Marca:  {self.marca}")
        print(f"Color:  {self.color}")
        print(f"Capacidad:  {self.capacidad}")
        print(f"Consumo en Kwh :   {self.consumo_electrico}")
        print(f"Temperatura :  {self.temperatura}")
        print(f"-----------------------------")

    # Método publico
    def detalles_actualizados(self):
        print(f"-----------------------------")
        print(f"ELECTRODOMESTICO REGISTRADO")
        print(f"-----------------------------")
        print(f"Marca: {self.marca}")
        print(f"Color:  {self.color}")
        print(f"Capacidad:  {self.capacidad}")
        print(f"Consumo en Kwh :   {self.consumo_electrico}")
        print(f"Nueva Temperatura :  {self.nueva_temperatura}")
        print(f"-----------------------------")


class Refrigerador(Electrodomestico): #Subclase
    #Constructor
    def __init__(self, marca, color, capacidad, tipo_de_refrigerador):
        super().__init__(marca, color, capacidad) #Super clase heredada
        self.tipo = int(input("Que tipo de Refrigerador es :? \n1.Frost \n2.No Frost \n"))
        self.temperatura = int(input("Digite la temperatura inicial ?  (en °C) :  "))
        self.nueva_temperatura = int(input("Digite la nueva temperatura: "))

    

#instanciando la subclase Refrigerador
objeto_refrigerador=Refrigerador('Haceb', 'Gris', '250 Litros', '50')
objeto_refrigerador.registrar()#Registrando el electrodomestico
objeto_refrigerador.detalles_actualizados()
