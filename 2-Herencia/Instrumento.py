# Defino la clase
class Instrumento:
    # Método Constructor
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion):
        # Defino los atributos de instancia de la clase
        self.tipo_de_instrumento = tipo_de_instrumento
        self.marca = marca
        self.material_de_fabricacion = material_de_fabricacion
        self.precio = int(input("Digite el precio del instrumento :  "))
        

    # Método publico
    def registrar(self):
        print(f"-----------------------------")
        print(f"INSTRUMENTO REGISTRADO")
        print(f"-----------------------------")
        print(f"Tipo de Instrumento:  {self.tipo_de_instrumento}")
        print(f"Marca:  {self.marca}")
        print(f"Material de Fabricacion:  {self.material_de_fabricacion}")
        print(f"Precio :  ${self.precio} ")
        print(f"-----------------------------")


    def tocar(self):

        tocar = int(input("Desea probar la Guitarra con los acordes proporcionados ? \n1.Si \n2.No \n"))
        if tocar == 1:
            print(f"-----------------------------")
            print(f"INSTRUMENTO REGISTRADO")
            print(f"-----------------------------")
            print(f"Tipo de Instrumento:  {self.tipo_de_instrumento}")
            print(f"Marca:  {self.marca}")
            print(f"Material de Fabricacion:  {self.material_de_fabricacion}")
            print(f"Numero de Cuerdas:  {self.numero_de_cuerdas}")
            print(f"Precio :  ${self.precio} ")
            print(f"Acordes:  {self.acordes}")
            print(f"-----------------------------")
        else:
            print("No se probara el instrumento")
    

class Guitarra(Instrumento): #Subclase
    #Constructor
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion, numero_de_cuerdas):
        super().__init__(tipo_de_instrumento, marca, material_de_fabricacion) #Super clase heredada
        self.numero_de_cuerdas = numero_de_cuerdas
        self.acordes = input("Digite unos acordes para probar la guitarra : ")

    
#instanciando la subclase 
objeto_guitarra=Guitarra('Cuerda', 'Tamaha', 'Madera', int(input("Digite la cantidad de cuerdas: ")))
objeto_guitarra.registrar()#Registrando el dispositivo
objeto_guitarra.tocar()#Solicita encender el dispositivo

