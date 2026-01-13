from abc import ABC, abstractmethod

# Clase abstracta (virtual)
class Algoritmo(ABC):
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje

    @abstractmethod
    def preprocess_data(self, data=None, y=None):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

# Clase que hereda de Algoritmo
class BaseClassifier(Algoritmo):
    def preprocess_data(self, data=None, y=None):
        print(f"Preprocessing data at {self.nombre}")

    def fit(self):
        print(f"Training at {self.nombre}")

    def predict(self):
        print(f"Evaluating at {self.nombre}")

# Crear una instancia para comprobar funcionalidad
model = BaseClassifier("SVM", "Clasificación", "Supervisado")
model.preprocess_data()
model.fit()
model.predict()

# Verificar jerarquía de clases
print("¿Algoritmo es superclase de BaseClassifier?:", issubclass(BaseClassifier, Algoritmo))
