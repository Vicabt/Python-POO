from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

# Clase para Empleado a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return f"El salario mensual de {self.nombre} es: {self.salario_mensual} USD."

# Clase para Empleado por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, pago_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        salario = self.horas_trabajadas * self.pago_por_hora
        return f"El salario de {self.nombre} por {self.horas_trabajadas} horas trabajadas es: {salario} USD."

# Uso de las clases
empleado_tc = EmpleadoTiempoCompleto('Carlos Pérez', 2000)
empleado_ph = EmpleadoPorHoras('Ana Gómez', 120, 15)

print(empleado_tc.calcular_salario())
print(empleado_ph.calcular_salario())
