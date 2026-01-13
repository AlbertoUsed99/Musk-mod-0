import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from parent1 import Parent1
from parent2 import Parent2

class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z

    def display(self):
        print(f"In display method of Child z={self.z}")
        Parent1.display(self)
        Parent2.display(self)
