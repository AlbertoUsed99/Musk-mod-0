from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def preprocess_data(self, data=None, y=None):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass
