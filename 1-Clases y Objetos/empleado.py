# Defino la clase
class Empleado:
    # Método Constructor
    def __init__(self, nombre, edad, cargo, salario, años_experiencia):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
        self.años_experiencia = años_experiencia

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Empleado")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: ${self.salario}")
        print(f"Años de Experiencia: {self.años_experiencia} años")
        print("-----------------------------")

    # Método para calcular el aumento de salario
    def calcular_aumento(self, porcentaje_aumento):
        aumento = self.salario * (porcentaje_aumento / 100)
        self.salario += aumento
        print(f"{self.nombre} ha recibido un aumento de {porcentaje_aumento}%. Nuevo salario: ${self.salario}")

# Creamos los objetos a partir de instanciar la clase Empleado
empleado1 = Empleado("Carlos", 35, "Ingeniero de Software", 50000, 10)
empleado2 = Empleado("Ana", 29, "Gerente de Ventas", 45000, 6)
empleado3 = Empleado("Luis", 42, "Director de Proyectos", 70000, 15)

# Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()