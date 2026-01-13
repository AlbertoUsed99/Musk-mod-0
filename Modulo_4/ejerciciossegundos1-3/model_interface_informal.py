class Model:
    def preprocess_data(self, data=None, y=None):
        raise NotImplementedError("Must override preprocess_data")

    def fit(self):
        raise NotImplementedError("Must override fit")

    def predict(self):
        raise NotImplementedError("Must override predict")
