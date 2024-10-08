'''Ejercicio 4: Instrumentos Musicales con Polimorfismo
Crea clases: Guitarra, Piano, y Trompeta, cada una con un método tocar() que describa la información técnica del instrumento.'''

# Clase base Instrumento
class Instrumento:
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion):
        # Defino los atributos de instancia de la clase
        self.tipo_de_instrumento = tipo_de_instrumento
        self.marca = marca
        self.material_de_fabricacion = material_de_fabricacion
    
    def tocar(self):
        pass

# Clase Guitarra
class Guitarra(Instrumento):
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion):
        super().__init__(tipo_de_instrumento, marca, material_de_fabricacion)
        self.nombre = "Guitarra"
    
    def tocar(self):
        return "La Guitarra suena asi: Do, Do#, Re, Re#, Mi, Fa, Fa#, Sol, Sol#, La, La#, Si."

    def mostrar_info(self):
        print(f"-----------------------------")
        print(f"INSTRUMENTO REGISTRADO: {self.nombre}")
        print(f"-----------------------------")
        print(f"Tipo de Instrumento:  {self.tipo_de_instrumento}")
        print(f"Marca:  {self.marca}")
        print(f"Material de Fabricacion:  {self.material_de_fabricacion}")
        print(f"-----------------------------")

# Clase Piano
class Piano(Instrumento):
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion):
        super().__init__(tipo_de_instrumento, marca, material_de_fabricacion)
        self.nombre = "Piano"
    
    def tocar(self):
        return "El Piano suena asi: Do, Do#, Re, Re#, Mi, Fa, Fa#, Sol, Sol#, La, La#, Si."

    def mostrar_info(self):
        print(f"-----------------------------")
        print(f"INSTRUMENTO REGISTRADO: {self.nombre}")
        print(f"-----------------------------")
        print(f"Tipo de Instrumento:  {self.tipo_de_instrumento}")
        print(f"Marca:  {self.marca}")
        print(f"Material de Fabricacion:  {self.material_de_fabricacion}")
        print(f"-----------------------------")

# Clase Trompeta
class Trompeta(Instrumento):
    def __init__(self, tipo_de_instrumento, marca, material_de_fabricacion):
        super().__init__(tipo_de_instrumento, marca, material_de_fabricacion)
        self.nombre = "Trompeta"
    
    def tocar(self):
        return "La Trompeta suena asi: Do, Do#, Re, Re#, Mi, Fa, Fa#, Sol, Sol#, La, La#, Si."

    def mostrar_info(self):
        print(f"-----------------------------")
        print(f"INSTRUMENTO REGISTRADO: {self.nombre}")
        print(f"-----------------------------")
        print(f"Tipo de Instrumento:  {self.tipo_de_instrumento}")
        print(f"Marca:  {self.marca}")
        print(f"Material de Fabricacion:  {self.material_de_fabricacion}")
        print(f"-----------------------------")

# Función polimórfica para mostrar información
def mostrar_informacion(instrumento):
    instrumento.mostrar_info()

# Crear objetos
objeto_guitarra = Guitarra('Cuerda', 'Yamaha', 'Madera')
objeto_piano = Piano('Teclas', 'Yamaha', 'Madera')
objeto_trompeta = Trompeta('Viento', 'Mirage', 'Metal')

# Mostrar la información de cada instrumento
mostrar_informacion(objeto_guitarra)
mostrar_informacion(objeto_piano)
mostrar_informacion(objeto_trompeta)
