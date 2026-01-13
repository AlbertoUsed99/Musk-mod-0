import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from staff import Staff  # importar desde staff.py

class Profesor(Staff):
    def __init__(self, role, dept, salary, nombre, edad):
        super().__init__(role, dept, salary)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return (f"Nombre: {self.nombre}, Edad: {self.edad}, "
                f"Rol: {self.role}, Departamento: {self.dept}, Salario: {self.salary}")