class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 16, "10° grado")

# Imprimir los atributos del estudiante
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Grado: {estudiante1.grado}")
