'''Ejercicio 5: Clases de Profesiones con Polimorfismo
Crea tres clases: Médico, Ingeniero, y Docente, cada una con un método trabajar() que describa la información técnica del profesional.'''

# Clase base Profesiones
class Profesion:
    def __init__(self, nombre, especialidad, experiencia):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia
    
    def trabajar(self):
        pass

# Clase Medico
class Medico(Profesion):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
        
    
    def trabajar(self):
        return f"Soy {self.nombre}, un médico especializado en {self.especialidad} con {self.experiencia} años de experiencia."


# Clase Ingeniero
class Ingeniero(Profesion):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
        
    
    def trabajar(self):
        return f"Soy {self.nombre}, un Ingeniero especializado en {self.especialidad} con {self.experiencia} años de experiencia."

# Clase Docente
class Docente(Profesion):
    def __init__(self, nombre, especialidad, experiencia):
        super().__init__(nombre, especialidad, experiencia)
        
    
    def trabajar(self):
        return f"Soy {self.nombre}, un Docente especializado en {self.especialidad} con {self.experiencia} años de experiencia."

# Función polimórfica para mostrar información
def describir_trabajo(profesion):
    print(profesion.trabajar())

# Crear objetos
objeto_medico = Medico('Javier Ortiz', 'Internista', 15)
objeto_ingeniero = Ingeniero('Victor Cabas', 'Sistemas', 5)
objeto_docente = Docente('Vanessa Cabas', 'Idiomas', 2)

# Mostrar la información de cada instrumento
describir_trabajo(objeto_medico)
describir_trabajo(objeto_ingeniero)
describir_trabajo(objeto_docente)