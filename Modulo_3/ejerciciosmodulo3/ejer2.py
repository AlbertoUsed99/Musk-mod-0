# script.py
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from jet import Jet  # Importamos la clase Jet desde el archivo jet.py

# Crear instancias de la clase Jet
su33 = Jet("SU33", "Russia")
ajs37 = Jet("AJS37", "Sweden")
mirage2000 = Jet("Mirage2000", "France")
f14 = Jet("F14", "USA")
mig29 = Jet("Mig29", "USSR")
a10 = Jet("A10", "USA")

# Imprimir los nombres y orígenes de los jets
jets = [su33, ajs37, mirage2000, f14, mig29, a10]

for jet in jets:
    print(f"Nombre: {jet.name}, Origen: {jet.origin}")