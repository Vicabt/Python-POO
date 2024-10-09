from abc import ABC, abstractmethod

# Clase abstracta TareaEmpleado
class TareaEmpleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase Ingeniero
class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def realizar_tarea(self):
        return f"Soy el Ingeniero {self.nombre}, y estoy trabajando en un proyecto de {self.especialidad}."

# Clase Doctor
class Doctor(TareaEmpleado):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre)
        self.especialidad = especialidad

    def realizar_tarea(self):
        return f"Soy el Doctor {self.nombre}, y estoy atendiendo a pacientes en la especialidad de {self.especialidad}."

# Uso de las clases
ingeniero = Ingeniero('Luis Morales', 'software')
doctor = Doctor('María Rivera', 'cardiología')

print(ingeniero.realizar_tarea())
print(doctor.realizar_tarea())
