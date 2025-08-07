# pacientes.py

class Paciente:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}"

    def es_mayor_de_edad(self):
        return self.edad >= 18



if __name__ == "__main__":
    paciente1 = Paciente("Juan Pérez", 30, "Masculino")
    print(paciente1.mostrar_info())

    if paciente1.es_mayor_de_edad():
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
