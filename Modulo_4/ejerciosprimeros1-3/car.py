import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from vehicle import Vehicle

class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 200')

    def change_gear(self):
        print('Car change 5 gear')


# Instancias y pruebas
v1 = Vehicle("Moto", "Rojo", 5000)
v2 = Vehicle("Bicicleta", "Azul", 1000)

c1 = Car("BMW", "Negro", 30000)
c2 = Car("Toyota", "Blanco", 25000)

# Mostrar detalles
v1.show()
v2.show()
c1.show()
c2.show()

# Probar métodos sobrescritos
v1.max_speed()
v1.change_gear()

c1.max_speed()
c1.change_gear()
