class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def __str__(self):
        return f"Rol: {self.role}, Departamento: {self.dept}, Salario: {self.salary}"
