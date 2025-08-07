class Doctor:
    def __init__(self, id_doctor, nombre, especialidad, telefono, email):
        """
        Inicializa un nuevo doctor
        
        Args:
            id_doctor (int): Identificador único del doctor
            nombre (str): Nombre completo del doctor
            especialidad (str): Especialidad médica
            telefono (str): Número de teléfono
            email (str): Correo electrónico
        """
        self.id_doctor = id_doctor
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.email = email
        self.pacientes_atendidos = []
    
    def agregar_paciente(self, id_paciente):
        """
        Agrega un paciente a la lista de atendidos
        
        Args:
            id_paciente (int): ID del paciente
        """
        if id_paciente not in self.pacientes_atendidos:
            self.pacientes_atendidos.append(id_paciente)
            print(f"Paciente {id_paciente} agregado a la lista del Dr. {self.nombre}")
        else:
            print(f"El paciente {id_paciente} ya está en la lista del Dr. {self.nombre}")
    
    def mostrar_doctor(self):
        """Muestra la información del doctor"""
        print(f"\n--- INFORMACIÓN DEL DOCTOR ---")
        print(f"ID: {self.id_doctor}")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Pacientes atendidos: {len(self.pacientes_atendidos)}")
    
    def listar_pacientes(self):
        """Lista todos los pacientes atendidos"""
        if self.pacientes_atendidos:
            print(f"\nPacientes del Dr. {self.nombre}:")
            for i, paciente_id in enumerate(self.pacientes_atendidos, 1):
                print(f"  {i}. Paciente ID: {paciente_id}")
        else:
            print(f"El Dr. {self.nombre} no ha atendido pacientes aún")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un doctor
    doctor1 = Doctor(456, "Dr. María González", "Medicina General", "555-0123", "mgonzalez@farmacia.com")
    
    # Mostrar información
    doctor1.mostrar_doctor()
    
    # Agregar pacientes
    doctor1.agregar_paciente(789)
    doctor1.agregar_paciente(790)
    
    # Listar pacientes
    doctor1.listar_pacientes()
