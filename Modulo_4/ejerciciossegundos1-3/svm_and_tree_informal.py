import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from model_interface_informal import Model

class SVM(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at SVM")

    def fit(self):
        print("Training at SVM")

    def predict(self):
        print("Evaluating at SVM")


class DecisionTree(Model):
    def preprocess_data(self, data=None, y=None):
        print("Preprocessing data at DecisionTree")

    def fit(self):
        print("Training at DecisionTree")

    def predict(self):
        print("Evaluating at DecisionTree")


# Prueba de funcionamiento
svm = SVM()
svm.preprocess_data()
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data()
dt.fit()
dt.predict()
