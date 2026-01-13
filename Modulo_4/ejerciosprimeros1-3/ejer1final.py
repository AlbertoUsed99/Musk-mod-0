import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from profesor import Profesor

prof = Profesor("Titular", "Historia", 4700, "Carlos Ramos", 45)
print(prof)
